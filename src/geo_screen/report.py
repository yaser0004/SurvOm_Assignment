"""Per-dataset and aggregate report generation.

write_dataset produces the four spec-mandated files verbatim
(series_metadata.json, sample_metadata.csv, validation_report.md,
source_manifest.json) under <out>/datasets/<GSE>/. The tool-computed
sections of validation_report.md are wrapped in <!-- computed -->
markers so downstream checks (and this repo's own tests) can verify that
every number in that block came from parsed SOFT, not from a hand-copied
note - a quoted GEO abstract elsewhere on the page is free to say whatever
the authors wrote.
"""

from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from dataclasses import asdict
from pathlib import Path

from geo_screen import __version__
from geo_screen.classify import REJECT_PRECEDENCE, STRONG_CHECK_IDS
from geo_screen.fetch import Fetched
from geo_screen.models import CheckResult, FileInventory, SoftFamily, Status, SummaryRecord, Verdict
from geo_screen.normalize import field_report


def _first(fields: dict[str, list[str]], key: str) -> str:
    values = fields.get(key, [])
    return values[0] if values else ""


def _geo_url(accession: str) -> str:
    return f"https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={accession}"


def _write_series_metadata(dataset_dir: Path, fam: SoftFamily) -> None:
    data = {
        "accession": fam.accession,
        "title": _first(fam.series, "Series_title"),
        "summary": fam.series.get("Series_summary", []),
        "overall_design": _first(fam.series, "Series_overall_design"),
        "type": fam.series.get("Series_type", []),
        "organisms": sorted({o for s in fam.samples.values() for o in s.get("Sample_organism_ch1", [])}),
        "sample_count": len(fam.samples),
        "platform_ids": sorted(fam.platforms.keys()),
        "pubmed_ids": fam.series.get("Series_pubmed_id", []),
        "submission_date": _first(fam.series, "Series_submission_date"),
        "last_update_date": _first(fam.series, "Series_last_update_date"),
        "geo_url": _geo_url(fam.accession),
        "relations": fam.series.get("Series_relation", []),
    }
    (dataset_dir / "series_metadata.json").write_text(json.dumps(data, indent=2, sort_keys=True))


def _write_sample_metadata(dataset_dir: Path, rows: list[dict[str, str]]) -> None:
    fieldnames = sorted({key for row in rows for key in row})
    if "gsm" in fieldnames:
        fieldnames.remove("gsm")
        fieldnames = ["gsm", *fieldnames]
    with (dataset_dir / "sample_metadata.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, restval="", extrasaction="raise")
        writer.writeheader()
        writer.writerows(rows)


def _write_validation_report(
    dataset_dir: Path,
    fam: SoftFamily,
    rows: list[dict[str, str]],
    checks: list[CheckResult],
    verdict: Verdict,
) -> None:
    lines: list[str] = [f"# Validation report: {fam.accession}", "", _first(fam.series, "Series_title"), ""]
    lines.append("<!-- computed -->")
    lines.append(f"Sample count: {len(rows)}")
    lines.append("")
    lines.append("## Checks")
    lines.append("")
    lines.append("| id | status | observed |")
    lines.append("|---|---|---|")
    for check in checks:
        lines.append(f"| {check.id} | {check.status.value} | {check.observed} |")
    lines.append("")

    canon_columns = sorted({key for row in rows for key in row if key.startswith("canon__")})
    if canon_columns:
        lines.append("## Canonical field distributions")
        lines.append("")
        for column in canon_columns:
            name = column[len("canon__") :]
            counts = Counter(row[column] for row in rows if row.get(column))
            distribution = ", ".join(f"{value} ({count})" for value, count in sorted(counts.items()))
            lines.append(f"- **{name}**: {distribution}")
        lines.append("")

    presence = field_report(fam)
    if presence:
        lines.append("## Field presence")
        lines.append("")
        for raw_key, info in sorted(presence.items()):
            canon = f" (canon: {info['canonical']})" if info["canonical"] else ""
            lines.append(f"- {raw_key}: {info['present']}/{info['total']}{canon}")
        lines.append("")

    flagged = [c for c in checks if c.status in (Status.WARN, Status.FAIL)]
    if flagged:
        lines.append("## Evidence for WARN/FAIL checks")
        lines.append("")
        for check in flagged:
            lines.append(f"### {check.id} ({check.status.value})")
            for ev in check.evidence:
                lines.append(f"- {ev.accession} / {ev.field}: matched `{ev.matched}` in \"{ev.snippet}\"")
        lines.append("")

    lines.append(f"Decision: {verdict.decision.value}")
    if verdict.reasons:
        lines.append("")
        lines.append("Reasons:")
        lines.extend(f"- {r}" for r in verdict.reasons)
    if verdict.unmet_strong:
        lines.append("")
        lines.append("Unmet STRONG_CANDIDATE conditions:")
        lines.extend(f"- {u}" for u in verdict.unmet_strong)
    lines.append("<!-- /computed -->")

    (dataset_dir / "validation_report.md").write_text("\n".join(lines))


def _write_source_manifest(
    dataset_dir: Path,
    fam: SoftFamily,
    rows: list[dict[str, str]],
    provenance: list[Fetched],
) -> None:
    data = {
        "accession": fam.accession,
        "gsm_accessions": sorted(fam.samples.keys()),
        "geo_url": _geo_url(fam.accession),
        "platform_accessions": sorted(fam.platforms.keys()),
        "sources": [
            {
                "url": p.url,
                "sha256": p.sha256,
                "bytes": p.size_bytes,
                "retrieved_at": p.retrieved_at,
                "from_cache": p.from_cache,
            }
            for p in provenance
        ],
        "supplementary_filenames": sorted(
            {name for row in rows for name in row.get("supplementary_files", "").split(" | ") if name}
        ),
        "tool_version": __version__,
        "argv": sys.argv[1:],
    }
    (dataset_dir / "source_manifest.json").write_text(json.dumps(data, indent=2, sort_keys=True))


def write_dataset(
    out: Path,
    fam: SoftFamily,
    rows: list[dict[str, str]],
    checks: list[CheckResult],
    verdict: Verdict,
    files: FileInventory,
    provenance: list[Fetched],
) -> Path:
    dataset_dir = Path(out) / "datasets" / fam.accession
    dataset_dir.mkdir(parents=True, exist_ok=True)

    _write_series_metadata(dataset_dir, fam)
    _write_sample_metadata(dataset_dir, rows)
    _write_validation_report(dataset_dir, fam, rows, checks, verdict)
    _write_source_manifest(dataset_dir, fam, rows, provenance)

    return dataset_dir


_SUMMARY_FIELDS = [
    "accession",
    "title",
    "organism",
    "n_samples",
    "source_summary",
    "library_strategy",
    "single_cell_flag",
    "material_flag",
    "disease_terms_found",
    "expression_files",
    "decision",
    "top_reason",
]


def write_summary(out: Path, records: list[SummaryRecord]) -> Path:
    reports_dir = Path(out) / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    path = reports_dir / "summary.csv"
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=_SUMMARY_FIELDS)
        writer.writeheader()
        for record in records:
            writer.writerow(asdict(record))
    return path


def write_screening_report(out: Path, records: list[SummaryRecord]) -> Path:
    reports_dir = Path(out) / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    path = reports_dir / "screening_report.md"

    counts = Counter(r.decision for r in records)
    lines = ["# Screening report", "", "## Counts by decision", ""]
    for decision in ("STRONG_CANDIDATE", "CANDIDATE", "MANUAL_REVIEW", "REJECT"):
        lines.append(f"- {decision}: {counts.get(decision, 0)}")

    lines += [
        "",
        "## All screened datasets",
        "",
        "| accession | title | organism | n_samples | decision | top reason |",
        "|---|---|---|---|---|---|",
    ]
    for record in records:
        lines.append(
            f"| {record.accession} | {record.title} | {record.organism} | {record.n_samples} | "
            f"{record.decision} | {record.top_reason} |"
        )

    rejected = [r for r in records if r.decision == "REJECT"]
    if rejected:
        lines += ["", "## Rejected datasets and reasons", ""]
        lines.extend(f"- {r.accession}: {r.top_reason}" for r in rejected)

    path.write_text("\n".join(lines))
    return path


def render_criteria_markdown() -> str:
    """Render rules.py + classify.py's precedence into the README criteria
    section, so the documented criteria cannot drift from what the code does."""
    from geo_screen.rules import (
        DISEASE_TERMS,
        NON_TISSUE_SIGNALS,
        SINGLE_CELL_SIGNALS,
        STRONG_MIN_SAMPLES,
        STRONG_SOURCE_FRACTION,
    )

    lines = [
        "## Screening criteria",
        "",
        f"- Strong-candidate minimum sample count: {STRONG_MIN_SAMPLES}",
        f"- Strong-candidate liver-source fraction: {STRONG_SOURCE_FRACTION:.0%}",
        "",
        "### Disease terms recognised",
        "",
        ", ".join(DISEASE_TERMS),
        "",
        "### Single-cell/spatial signals",
        "",
    ]
    for sig in SINGLE_CELL_SIGNALS:
        lines.append(f"- [{sig.tier}] `{sig.pattern}` over {', '.join(sig.fields)} — {sig.note}")
    lines += ["", "### Non-tissue / cell-line signals", ""]
    for sig in NON_TISSUE_SIGNALS:
        lines.append(f"- [{sig.tier}] `{sig.pattern}` over {', '.join(sig.fields)} — {sig.note}")

    lines += ["", "### Classification precedence (first match wins)", ""]
    for i, (check_id, reason) in enumerate(REJECT_PRECEDENCE, start=1):
        lines.append(f"{i}. `{check_id}` = FAIL → REJECT — {reason}")
    lines.append(f"{len(REJECT_PRECEDENCE) + 1}. any check = WARN → MANUAL_REVIEW")
    lines.append(
        f"{len(REJECT_PRECEDENCE) + 2}. organism == Homo sapiens and all of "
        f"{', '.join(STRONG_CHECK_IDS)} = PASS → STRONG_CANDIDATE"
    )
    lines.append(f"{len(REJECT_PRECEDENCE) + 3}. otherwise → CANDIDATE, with unmet conditions listed")

    return "\n".join(lines)
