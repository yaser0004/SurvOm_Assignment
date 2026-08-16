#!/usr/bin/env python3
"""Build reports/experimental_design.csv for the selected datasets.

The study-structure summaries in survom_nafld/design_notes.csv are written by
hand from the GEO record. This script does not generate them; it pulls the GEO
fields they were written from, puts them in the same row so a reader can check
the summary against its source, and refuses to emit a row whose summary it
cannot tie back to that source.

The tie-back is numeric: every integer in a summary must also appear in that
accession's Series_overall_design, Series_summary, sample count, or observed
sample-group distribution. A count that appears nowhere in the record is a hard
failure, which is what keeps an invented number out of the table.

Reads only files already in the tree. No network, no GEO refetch.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Field names design_source may cite, mapped to the series_metadata.json key
# that has to be non-empty for the citation to hold.
CITABLE_FIELDS = {
    "Series_overall_design": "overall_design",
    "Series_summary": "summary",
}

# A metadata column is treated as group structure when it has at most this many
# distinct values. Anything wider (age, BMI) is a per-sample measurement.
MAX_GROUP_VALUES = 12

OUTPUT_FIELDS = [
    "accession",
    "sample_count",
    "design_source",
    "experimental_design_summary",
    "series_overall_design",
    "series_summary",
    "series_relations",
    "sample_group_distribution",
    "geo_url",
]


def read_selected(path: Path) -> list[str]:
    """Accessions from selected.txt, which puts a free-text reason after the GSE."""
    accessions = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        accessions.append(line.split()[0])
    return accessions


def read_notes(path: Path) -> dict[str, dict[str, str]]:
    with path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    notes = {}
    for row in rows:
        accession = row["accession"].strip()
        if accession in notes:
            raise SystemExit(f"{path}: duplicate row for {accession}")
        notes[accession] = row
    return notes


def group_distribution(sample_csv: Path) -> str:
    """Observed value counts for every low-cardinality metadata column.

    raw__ columns are dropped where a canon__ column already carries the same
    distribution, so the string shows the canonical view plus whatever the raw
    GEO fields add on top of it.
    """
    with sample_csv.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        return ""

    per_column: dict[str, Counter] = {}
    for column in rows[0]:
        if not column.startswith(("canon__", "raw__")):
            continue
        counts = Counter(row[column] for row in rows if row.get(column))
        if 0 < len(counts) <= MAX_GROUP_VALUES:
            per_column[column] = counts

    canonical = [c for c in per_column if c.startswith("canon__")]
    parts = []
    for column in sorted(per_column):
        if column.startswith("raw__") and any(
            per_column[column] == per_column[c] for c in canonical
        ):
            continue
        counts = per_column[column]
        values = "; ".join(f"{value} ({count})" for value, count in sorted(counts.items()))
        parts.append(f"{column}={values}")
    return " | ".join(parts)


def check_sources_present(accession: str, design_source: str, series: dict) -> None:
    for field, key in CITABLE_FIELDS.items():
        if field in design_source and not series.get(key):
            raise SystemExit(f"{accession}: design_source cites {field}, which is empty in series_metadata.json")


def check_numbers_traceable(accession: str, summary: str, provenance: str) -> None:
    claimed = set(re.findall(r"\d+", summary))
    supported = set(re.findall(r"\d+", provenance))
    unsupported = sorted(claimed - supported, key=int)
    if unsupported:
        raise SystemExit(
            f"{accession}: {unsupported} in the summary appear nowhere in the GEO record "
            f"or the sample-group distribution"
        )


def build_row(accession: str, note: dict[str, str], datasets_dir: Path) -> dict[str, str]:
    dataset_dir = datasets_dir / accession
    series_path = dataset_dir / "series_metadata.json"
    sample_path = dataset_dir / "sample_metadata.csv"
    for path in (series_path, sample_path):
        if not path.exists():
            raise SystemExit(f"{accession}: {path} is missing")

    series = json.loads(series_path.read_text())
    overall_design = series.get("overall_design", "")
    series_summary = " ".join(series.get("summary", []))
    distribution = group_distribution(sample_path)
    sample_count = series["sample_count"]

    summary = note["experimental_design_summary"].strip()
    design_source = note["design_source"].strip()
    if not summary or not design_source:
        raise SystemExit(f"{accession}: design_notes.csv row is incomplete")

    check_sources_present(accession, design_source, series)
    check_numbers_traceable(
        accession,
        summary,
        " ".join([overall_design, series_summary, str(sample_count), distribution]),
    )

    return {
        "accession": accession,
        "sample_count": sample_count,
        "design_source": design_source,
        "experimental_design_summary": summary,
        "series_overall_design": overall_design,
        "series_summary": series_summary,
        "series_relations": " | ".join(series.get("relations", [])),
        "sample_group_distribution": distribution,
        "geo_url": series.get("geo_url", ""),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out-dir", type=Path, default=REPO_ROOT / "survom_nafld")
    args = parser.parse_args(argv)

    out_dir = args.out_dir
    selected = read_selected(out_dir / "selected.txt")
    notes = read_notes(out_dir / "design_notes.csv")

    missing = [a for a in selected if a not in notes]
    if missing:
        raise SystemExit(f"design_notes.csv has no row for {missing}")
    extra = sorted(set(notes) - set(selected))
    if extra:
        raise SystemExit(f"design_notes.csv describes datasets that are not selected: {extra}")

    datasets_dir = out_dir / "datasets"
    rows = [build_row(accession, notes[accession], datasets_dir) for accession in selected]

    path = out_dir / "reports" / "experimental_design.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    for row in rows:
        print(f"{row['accession']}  n={row['sample_count']:<4} source={row['design_source']}")
    print(f"wrote {path} ({len(rows)} rows)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
