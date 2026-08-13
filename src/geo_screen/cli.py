"""Command-line entry point.

    python -m geo_screen GSE135251                 # bare accessions -> screen
    python -m geo_screen --file candidates.txt
    python -m geo_screen screen --file candidates.txt --out survom_nafld
    python -m geo_screen search --query-file queries.txt --out survom_nafld
    python -m geo_screen download GSE135251 --out survom_nafld

A leading token that is not a known subcommand is treated as an implicit
`screen` invocation, so bare accessions work without typing the word
"screen". Screening never downloads bulk data; that only happens under the
explicit `download` subcommand (Task 8).
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from geo_screen.checks import run_checks
from geo_screen.classify import classify
from geo_screen.fetch import GeoClient, validate_accession
from geo_screen.models import FileInventory, SummaryRecord
from geo_screen.normalize import sample_rows
from geo_screen.report import write_dataset, write_screening_report, write_summary
from geo_screen.soft import parse_soft

logger = logging.getLogger(__name__)

KNOWN_SUBCOMMANDS = {"screen", "search", "download"}


def read_accessions(path: Path) -> list[str]:
    """Blank lines and #-comments are skipped; only the first whitespace-delimited
    token per line is kept, so a trailing reason ("GSE2  largest cohort") is fine.
    Order-preserving, deduplicated."""
    seen: set[str] = set()
    ordered: list[str] = []
    for raw_line in Path(path).read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        token = line.split()[0]
        if token not in seen:
            seen.add(token)
            ordered.append(token)
    return ordered


def _dedupe(values: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            ordered.append(value)
    return ordered


def _gather_file_inventory(client: GeoClient, accession: str) -> FileInventory:
    suppl_entries, _ = client.list_dir(accession, "suppl")
    matrix_entries, _ = client.list_dir(accession, "matrix")
    series_matrix = tuple((name, size) for name, size in matrix_entries if "series_matrix" in name)
    return FileInventory(
        series_supplementary=tuple(suppl_entries),
        sample_supplementary=(),
        series_matrix=series_matrix,
        sra_links=(),
    )


def _build_summary_record(fam, rows, checks, verdict) -> SummaryRecord:
    by_id = {c.id: c for c in checks}
    return SummaryRecord(
        accession=fam.accession,
        title=fam.series.get("Series_title", [""])[0],
        organism=by_id["organism_consistency"].observed,
        n_samples=len(rows),
        source_summary=by_id["source_tissue"].observed,
        library_strategy=by_id["library_strategy"].observed,
        single_cell_flag=by_id["single_cell_or_spatial"].status.value,
        material_flag=by_id["material_type"].status.value,
        disease_terms_found=by_id["disease_relevance"].observed,
        expression_files=by_id["expression_data_availability"].observed,
        decision=verdict.decision.value,
        top_reason=verdict.reasons[0] if verdict.reasons else "",
    )


def screen_one(accession: str, *, out: Path, client: GeoClient) -> SummaryRecord:
    """Fetch, parse, check, classify, and write the four mandated report files
    for exactly one GSE. Raises on a hard failure (network, malformed SOFT)."""
    text, series_fetched = client.soft_family(accession)
    fam = parse_soft(text)
    rows = sample_rows(fam)
    files = _gather_file_inventory(client, accession)
    checks = run_checks(fam, rows, files)
    verdict = classify(checks)
    write_dataset(out, fam, rows, checks, verdict, files, [series_fetched])
    logger.info("%s -> %s", accession, verdict.decision.value)
    return _build_summary_record(fam, rows, checks, verdict)


def screen_accessions(accessions: list[str], *, out: Path, client: GeoClient) -> int:
    """Screen every accession, logging and skipping failures rather than
    aborting the batch. Returns the number of accessions that failed."""
    records: list[SummaryRecord] = []
    failures = 0
    for accession in accessions:
        try:
            records.append(screen_one(accession, out=out, client=client))
        except Exception:
            logger.exception("failed to screen %s", accession)
            failures += 1
    write_summary(out, records)
    write_screening_report(out, records)
    return failures


def _configure_logging(out: Path | None, verbose: bool) -> None:
    root = logging.getLogger()
    root.setLevel(logging.DEBUG if verbose else logging.INFO)

    has_console = any(
        isinstance(h, logging.StreamHandler) and not isinstance(h, logging.FileHandler) for h in root.handlers
    )
    if not has_console:
        console = logging.StreamHandler()
        console.setFormatter(logging.Formatter("%(levelname)s %(name)s: %(message)s"))
        root.addHandler(console)

    if out is None:
        return
    log_path = (Path(out) / "logs" / "geo_screen.log").resolve()
    log_path.parent.mkdir(parents=True, exist_ok=True)
    already = any(
        isinstance(h, logging.FileHandler) and Path(h.baseFilename) == log_path for h in root.handlers
    )
    if not already:
        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s"))
        root.addHandler(file_handler)


def _build_parser() -> argparse.ArgumentParser:
    global_parser = argparse.ArgumentParser(add_help=False)
    global_parser.add_argument("--out", type=Path, default=Path("survom_nafld"))
    global_parser.add_argument("--cache-dir", type=Path, default=None)
    global_parser.add_argument("--offline", action="store_true")
    global_parser.add_argument("--max-file-size", type=int, default=500 * 1024 * 1024)
    global_parser.add_argument("-v", "--verbose", action="store_true")

    parser = argparse.ArgumentParser(prog="geo-screen")
    subparsers = parser.add_subparsers(dest="command", required=True)

    screen_parser = subparsers.add_parser("screen", parents=[global_parser])
    screen_parser.add_argument("accessions", nargs="*")
    screen_parser.add_argument("--file", type=Path, default=None)

    search_parser = subparsers.add_parser("search", parents=[global_parser])
    search_parser.add_argument("--query-file", type=Path, default=Path("queries.txt"))
    search_parser.add_argument("--retmax", type=int, default=500)

    download_parser = subparsers.add_parser("download", parents=[global_parser])
    download_parser.add_argument("accessions", nargs="*")
    download_parser.add_argument("--file", type=Path, default=None)
    download_parser.add_argument("--include-raw", action="store_true")
    download_parser.add_argument("--max-samples", type=int, default=500)

    return parser


def _make_client(args: argparse.Namespace) -> GeoClient:
    cache_dir = args.cache_dir or (Path(args.out).parent / ".geo_cache")
    return GeoClient(cache_dir=cache_dir, offline=args.offline, max_file_size=args.max_file_size)


def _validated_accessions(raw: list[str]) -> list[str] | None:
    """Returns the validated, deduplicated accessions, or None if any is invalid
    (already logged) - the caller should exit 1 without touching the network."""
    validated = []
    for accession in _dedupe(raw):
        try:
            validated.append(validate_accession(accession))
        except ValueError:
            logger.error("invalid accession: %r", accession)
            return None
    return validated


def _run_screen(args: argparse.Namespace) -> int:
    accessions = list(args.accessions)
    if args.file:
        accessions.extend(read_accessions(args.file))

    validated = _validated_accessions(accessions)
    if validated is None:
        return 1
    if not validated:
        logger.error("no accessions given (pass accessions, or --file)")
        return 1

    client = _make_client(args)
    screen_accessions(validated, out=args.out, client=client)
    return 0


def _run_search(args: argparse.Namespace) -> int:
    from geo_screen.search import search, write_candidates

    if not args.query_file.is_file():
        logger.error("query file not found: %s", args.query_file)
        return 1

    client = _make_client(args)
    queries = [line.strip() for line in args.query_file.read_text().splitlines() if line.strip()]
    seen_accessions: set[str] = set()
    all_hits: list[dict] = []
    for query in queries:
        hits = search(client, query, retmax=args.retmax)
        logger.info("query %r -> %d GSE hits", query, len(hits))
        for hit in hits:
            accession = hit.get("accession")
            if accession and accession not in seen_accessions:
                seen_accessions.add(accession)
                all_hits.append(hit)

    write_candidates(args.out, "\n".join(queries), all_hits)
    return 0


def _run_download(args: argparse.Namespace) -> int:
    from geo_screen.download import download

    accessions = list(args.accessions)
    if args.file:
        accessions.extend(read_accessions(args.file))

    validated = _validated_accessions(accessions)
    if validated is None:
        return 1
    if not validated:
        logger.error("no accessions given (pass accessions, or --file)")
        return 1

    client = _make_client(args)
    failures = 0
    for accession in validated:
        try:
            download(client, accession, args.out, include_raw=args.include_raw)
        except Exception:
            logger.exception("failed to download %s", accession)
            failures += 1
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] not in KNOWN_SUBCOMMANDS:
        argv = ["screen", *argv]

    parser = _build_parser()
    args = parser.parse_args(argv)
    _configure_logging(getattr(args, "out", None), args.verbose)

    if args.command == "screen":
        return _run_screen(args)
    if args.command == "search":
        return _run_search(args)
    if args.command == "download":
        return _run_download(args)
    parser.error(f"unknown command: {args.command}")
    return 2
