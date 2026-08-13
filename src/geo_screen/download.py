"""Tiered download phase - a separate, explicit step from screening.

Screening (checks.py, cli.screen_one) never downloads bulk data; it only
lists directories to gather evidence. This module is what actually pulls
files, and only after a human has selected a GSE. SRA/FASTQ is never
downloaded here, only recorded.

A GEO `_RAW.tar` is "the archive of per-sample submitted files", not "raw
FASTQ" - for a series like GSE135251 it is the only way to get the
per-sample processed count files, so it lands in archives/ (as downloaded)
while extract_archive() pulls its processed members into expression/ (as
usable data). See checks.expression_check for the same reasoning applied
to screening evidence.
"""

from __future__ import annotations

import hashlib
import json
import logging
import re
import tarfile
from dataclasses import dataclass
from pathlib import Path

from geo_screen.checks import is_processed_expression_filename
from geo_screen.fetch import GeoClient, ftp_series_url, validate_accession
from geo_screen.models import FileInventory

logger = logging.getLogger(__name__)

_TIER1_PATTERN = re.compile(r"counts|matrix|tpm|fpkm|rpkm|expression|cpm|\.csv$|\.tsv$|\.txt$", re.IGNORECASE)
_TIER1B_PATTERN = re.compile(r"xlsx|phenotype|clinical|sample.*info|metadata", re.IGNORECASE)
_RAW_TAR_SUFFIX = "_raw.tar"
# NCBI auto-generates this directory index in every series' suppl/ folder -
# it lists filenames and sizes, it is never itself expression or metadata.
_GEO_HOUSEKEEPING_FILES = {"filelist.txt"}

DEFAULT_MAX_ARCHIVE_MEMBERS = 2000


@dataclass(frozen=True)
class Plan:
    expression: tuple[str, ...] = ()
    metadata: tuple[str, ...] = ()
    archives: tuple[str, ...] = ()
    skipped: tuple[tuple[str, str], ...] = ()


def _is_raw_tar(name: str) -> bool:
    return name.lower().endswith(_RAW_TAR_SUFFIX)


def _is_safe_filename(name: str) -> bool:
    """Reject anything that isn't a plain, single-component filename.

    `name` values originate from parsing an FTP directory listing (HTML from
    the network) or a `!Sample_supplementary_file_N` SOFT field (free text
    from the network) - both cross a trust boundary before they are ever
    joined onto a local directory path. A path separator or a bare `..`
    component would let a malicious or malformed listing write outside the
    dataset's own directory (e.g. `../../.bashrc` or an absolute path, which
    `Path.__truediv__` does not sanitize - it discards the left side
    entirely for an absolute right-hand operand).
    """
    if not name or name in (".", ".."):
        return False
    return "/" not in name and "\\" not in name and "\x00" not in name


def plan_downloads(files: FileInventory, include_raw: bool, max_file_size: int) -> Plan:
    """Tier 1: series-level processed files (not _RAW.tar). Tier 1b: phenotype/
    clinical/metadata files plus the series matrix. Tier 2 (RAW.tar), only when
    Tier 1 found nothing or the caller explicitly asked for it via include_raw:
    the tar itself goes to archives/ when it fits under max_file_size, or - if
    it doesn't, and nothing else supplies expression data - fall back to
    fetching per-sample supplementary files individually. SRA/FASTQ is never
    planned here; sra_links are informational only.
    """
    expression: list[str] = []
    metadata: list[str] = []
    archives: list[str] = []
    skipped: list[tuple[str, str]] = []

    safe_supplementary = []
    for name, size in files.series_supplementary:
        if _is_safe_filename(name):
            safe_supplementary.append((name, size))
        else:
            skipped.append((name, "unsafe filename (path traversal risk)"))

    tar_entries = [(name, size) for name, size in safe_supplementary if _is_raw_tar(name)]
    other_entries = [(name, size) for name, size in safe_supplementary if not _is_raw_tar(name)]

    for name, size in other_entries:
        if name.lower() in _GEO_HOUSEKEEPING_FILES:
            continue
        if size > max_file_size:
            skipped.append((name, f"exceeds max-file-size ({size} > {max_file_size} bytes)"))
            continue
        if _TIER1_PATTERN.search(name):
            expression.append(name)
        elif _TIER1B_PATTERN.search(name):
            metadata.append(name)

    for name, _size in files.series_matrix:
        if _is_safe_filename(name):
            metadata.append(name)
        else:
            skipped.append((name, "unsafe filename (path traversal risk)"))

    need_tar = not expression or include_raw
    if need_tar and tar_entries:
        name, size = tar_entries[0]
        if size <= max_file_size:
            archives.append(name)
        else:
            skipped.append((name, f"exceeds max-file-size ({size} > {max_file_size} bytes)"))
            if not expression:
                for sample_name in files.sample_supplementary[:500]:
                    if not sample_name or sample_name == "NONE":
                        continue
                    if _is_safe_filename(sample_name):
                        expression.append(sample_name)
                    else:
                        skipped.append((sample_name, "unsafe filename (path traversal risk)"))

    return Plan(
        expression=tuple(expression),
        metadata=tuple(metadata),
        archives=tuple(archives),
        skipped=tuple(skipped),
    )


def extract_archive(
    tar_path: Path,
    dest: Path,
    max_total_size: int = 2 * 1024**3,
    max_members: int = DEFAULT_MAX_ARCHIVE_MEMBERS,
) -> list[Path]:
    """Extract only the processed-expression members of a downloaded tar into
    dest, treating the archive as untrusted input. Python 3.12's "data" filter
    rejects absolute paths, `..` traversal, symlinks, device nodes, and setuid
    bits; total extracted size and member count are additionally capped so a
    hostile or malformed tar cannot fill the disk."""
    dest.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    with tarfile.open(tar_path) as tar:
        members = tar.getmembers()
        if len(members) > max_members:
            raise ValueError(f"{tar_path} has {len(members)} members, exceeds cap of {max_members}")
        total = sum(m.size for m in members if m.isfile())
        if total > max_total_size:
            raise ValueError(f"{tar_path} extracted size {total} exceeds cap of {max_total_size} bytes")

        for member in members:
            if not member.isfile() or not is_processed_expression_filename(member.name):
                continue
            tar.extract(member, path=dest, filter="data")
            written.append(dest / member.name)
    return written


def _fetch_named(client: GeoClient, gse: str, sub: str, name: str, dest_dir: Path, tier: str) -> dict[str, object]:
    """Fetch `name` (a filename harvested from the network - an FTP listing
    or a SOFT field) into dest_dir/name. The safety check happens here,
    at the exact point `name` is turned into a filesystem path, rather than
    only in plan_downloads() - a Plan can be constructed directly by a
    caller, bypassing that earlier filter, so this is the check that
    actually has to hold."""
    if not _is_safe_filename(name):
        raise ValueError(f"refusing to fetch unsafe filename from network listing: {name!r}")
    dest = dest_dir / name
    url = ftp_series_url(gse, sub, name)
    if dest.exists():
        data = dest.read_bytes()
        return {
            "name": name,
            "tier": tier,
            "url": url,
            "sha256": hashlib.sha256(data).hexdigest(),
            "bytes": len(data),
            "from_cache": True,
        }
    fetched = client.get(url, dest)
    return {
        "name": name,
        "tier": tier,
        "url": fetched.url,
        "sha256": fetched.sha256,
        "bytes": fetched.size_bytes,
        "retrieved_at": fetched.retrieved_at,
        "from_cache": fetched.from_cache,
    }


def download(client: GeoClient, gse: str, out: Path, *, include_raw: bool = False) -> Path:
    gse = validate_accession(gse)
    dataset_dir = Path(out) / "datasets" / gse
    expression_dir = dataset_dir / "expression"
    metadata_dir = dataset_dir / "metadata"
    archives_dir = dataset_dir / "archives"

    suppl_entries, _ = client.list_dir(gse, "suppl")
    matrix_entries, _ = client.list_dir(gse, "matrix")
    series_matrix = tuple((name, size) for name, size in matrix_entries if "series_matrix" in name)
    matrix_names = {name for name, _size in series_matrix}
    files = FileInventory(
        series_supplementary=tuple(suppl_entries), sample_supplementary=(), series_matrix=series_matrix, sra_links=()
    )

    plan = plan_downloads(files, include_raw=include_raw, max_file_size=client.max_file_size)

    manifest_entries: list[dict[str, object]] = []
    for name in plan.expression:
        manifest_entries.append(_fetch_named(client, gse, "suppl", name, expression_dir, "expression"))
    for name in plan.metadata:
        sub = "matrix" if name in matrix_names else "suppl"
        manifest_entries.append(_fetch_named(client, gse, sub, name, metadata_dir, "metadata"))
    for name in plan.archives:
        entry = _fetch_named(client, gse, "suppl", name, archives_dir, "archive")
        manifest_entries.append(entry)
        try:
            extracted = extract_archive(archives_dir / name, expression_dir, max_total_size=client.max_file_size)
        except (tarfile.TarError, ValueError) as exc:
            logger.warning("could not extract %s: %s", name, exc)
        else:
            manifest_entries.append(
                {"name": name, "tier": "archive_extracted", "members": [p.name for p in extracted]}
            )

    manifest = {
        "accession": gse,
        "files": manifest_entries,
        "skipped": [{"name": name, "reason": reason} for name, reason in plan.skipped],
        "sra_links": list(files.sra_links),
    }
    dataset_dir.mkdir(parents=True, exist_ok=True)
    (dataset_dir / "download_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True))
    return dataset_dir
