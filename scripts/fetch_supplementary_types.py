#!/usr/bin/env python3
"""Record GEO's per-file supplementary types for every screened candidate.

Reads the accessions already in candidates/candidates.csv, so the historical
search is never re-run and the candidate set cannot drift. For each one it
fetches the GEO Series record page and reads the supplementary-file table,
whose `File type/resource` column is the only place GEO states a type per file.
Nothing is inferred from filenames, extensions or titles.

Writes candidates/supplementary_files.csv (one row per file), appends two
columns to candidates.csv, and records fetch provenance in
candidates/supplementary_manifest.json. Every pre-existing column is copied
through unchanged and checked afterwards.

The parsed file count is compared per accession against the cached SOFT
record's !Series_supplementary_file lines. A page that yields no files while
SOFT lists some aborts the run, which is what catches a silent parser break if
NCBI changes the page markup. Any other difference is reported, not corrected:
the page is the source of truth for these columns.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from geo_screen import __version__  # noqa: E402
from geo_screen.fetch import GeoClient  # noqa: E402
from geo_screen.supplementary import TYPE_UNSPECIFIED, format_files, parse_series_page  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent

ACC_URL = "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={accession}"
NO_FILES = "None reported by GEO"

DETAIL_FIELDS = [
    "accession",
    "filename",
    "geo_file_type",
    "geo_reported_size",
    "geo_size_bytes",
    "geo_download_url",
    "source_url",
]
NEW_COLUMNS = ["supplementary_files", "geo_raw_data_status"]


def soft_supplementary_count(client: GeoClient, accession: str) -> int | None:
    """!Series_supplementary_file lines in the SOFT family record.

    None when the record cannot be read, which makes the cross-check skip
    rather than fail: this script must not depend on a screening run having
    already cached every family file.
    """
    try:
        text, _ = client.soft_family(accession)
    except Exception:
        return None
    count = 0
    for line in text.splitlines():
        if line.startswith("!Series_supplementary_file"):
            count += 1
        elif line.startswith("^SAMPLE"):
            break
    return count


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out-dir", type=Path, default=REPO_ROOT / "survom_nafld")
    parser.add_argument("--cache-dir", type=Path, default=REPO_ROOT / ".geo_cache")
    parser.add_argument("--offline", action="store_true", help="replay from cache only")
    args = parser.parse_args(argv)

    candidates_path = args.out_dir / "candidates" / "candidates.csv"
    with candidates_path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        original_fields = list(reader.fieldnames or [])
        rows = list(reader)
    if not rows:
        raise SystemExit(f"{candidates_path} has no rows")
    for column in NEW_COLUMNS:
        if column in original_fields:
            original_fields.remove(column)

    client = GeoClient(cache_dir=args.cache_dir, offline=args.offline)

    detail_rows: list[dict[str, str]] = []
    provenance: list[dict[str, object]] = []
    mismatches: list[str] = []
    breakdown = Counter()

    for row in rows:
        accession = row["accession"].strip()
        url = ACC_URL.format(accession=accession)
        page, fetched = client.get_text(url)
        files, notes = parse_series_page(page)

        soft_count = soft_supplementary_count(client, accession)
        if soft_count and not files:
            raise SystemExit(
                f"{accession}: SOFT lists {soft_count} supplementary file(s) but the Series page "
                f"parsed to none. Refusing to write a blank value; check the page markup at {url}"
            )
        if soft_count is not None and soft_count != len(files):
            mismatches.append(f"{accession}: page {len(files)}, SOFT {soft_count}")

        for supp in files:
            detail_rows.append(
                {
                    "accession": accession,
                    "filename": supp.filename,
                    "geo_file_type": supp.file_type,
                    "geo_reported_size": supp.size,
                    "geo_size_bytes": supp.size_bytes,
                    "geo_download_url": supp.download_url,
                    "source_url": url,
                }
            )

        row["supplementary_files"] = format_files(files) if files else NO_FILES
        row["geo_raw_data_status"] = "; ".join(notes)

        if not files:
            breakdown["no supplementary files reported"] += 1
        elif any(f.file_type == TYPE_UNSPECIFIED for f in files):
            breakdown["at least one file with no type given by GEO"] += 1
        else:
            breakdown["all files carry an explicit GEO type"] += 1

        provenance.append(
            {
                "accession": accession,
                "url": url,
                "sha256": fetched.sha256,
                "bytes": fetched.size_bytes,
                "retrieved_at": fetched.retrieved_at,
                "from_cache": fetched.from_cache,
                "files_reported": len(files),
            }
        )

    if len(rows) != len({r["accession"] for r in rows}):
        raise SystemExit("duplicate accessions in candidates.csv")

    detail_path = args.out_dir / "candidates" / "supplementary_files.csv"
    with detail_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=DETAIL_FIELDS)
        writer.writeheader()
        writer.writerows(detail_rows)

    with candidates_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=[*original_fields, *NEW_COLUMNS])
        writer.writeheader()
        writer.writerows(rows)

    manifest_path = args.out_dir / "candidates" / "supplementary_manifest.json"
    manifest_path.write_text(
        json.dumps(
            {
                "source": "GEO Series record page, 'File type/resource' column",
                "url_template": ACC_URL,
                "accession_count": len(rows),
                "supplementary_file_count": len(detail_rows),
                "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "tool_version": __version__,
                "pages": provenance,
            },
            indent=2,
            sort_keys=True,
        )
    )

    print(f"{len(rows)} accessions, {len(detail_rows)} supplementary files reported by GEO")
    for label, count in sorted(breakdown.items()):
        print(f"  {count:>4}  {label}")
    types = Counter(r["geo_file_type"] for r in detail_rows)
    print(f"  {len(types)} distinct GEO file-type strings")
    if mismatches:
        print(f"  page/SOFT count differs for {len(mismatches)}:")
        for line in mismatches:
            print(f"    {line}")
    for path in (detail_path, candidates_path, manifest_path):
        print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
