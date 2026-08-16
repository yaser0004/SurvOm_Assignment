#!/usr/bin/env python3
"""Plot the screening outcome of the whole candidate pool from reports/summary.csv.

Every count comes from the CSV. Nothing is typed in here, so the figure cannot
drift from the screening results it claims to show. The run aborts if the
decisions in the file are not exactly the four the classifier emits, or if they
do not partition every row, which is the 11 + 8 + 131 + 50 = 200 check.

Needs the optional `plots` extra:  pip install -e ".[plots]"
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # no display in the environments this runs in
# Fixed salt for the SVG element ids, which are otherwise random per run. With
# the creation date suppressed below, a rerun on unchanged input then produces a
# byte-identical file and shows up as no change at all in git.
matplotlib.rcParams["svg.hashsalt"] = "geo-screen"
import matplotlib.pyplot as plt  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent

# Classifier precedence order, matching reports/screening_report.md.
DECISION_ORDER = ["STRONG_CANDIDATE", "CANDIDATE", "MANUAL_REVIEW", "REJECT"]

SURFACE = "#fcfcfb"
BAR = "#2a78d6"
TEXT_PRIMARY = "#0b0b0b"
TEXT_SECONDARY = "#52514e"
GRID = "#dedcd5"


def read_decisions(summary_csv: Path) -> dict[str, str]:
    with summary_csv.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise SystemExit(f"{summary_csv} has no rows")
    for column in ("accession", "decision"):
        if column not in rows[0]:
            raise SystemExit(f"{summary_csv} has no '{column}' column")
    decisions = {row["accession"]: row["decision"] for row in rows}
    if len(decisions) != len(rows):
        raise SystemExit(f"{summary_csv} has duplicate accessions")
    return decisions


def read_counts(summary_csv: Path) -> tuple[Counter, int]:
    rows = read_decisions(summary_csv)
    counts = Counter(rows.values())
    total = len(rows)

    unexpected = sorted(set(counts) - set(DECISION_ORDER))
    if unexpected:
        raise SystemExit(f"unexpected decision values in {summary_csv}: {unexpected}")
    missing = [d for d in DECISION_ORDER if d not in counts]
    if missing:
        raise SystemExit(f"no rows for {missing} in {summary_csv}")
    if sum(counts.values()) != total:
        raise SystemExit(f"decisions cover {sum(counts.values())} of {total} rows")

    return counts, total


def selection_breakdown(selected_txt: Path, decisions: dict[str, str]) -> tuple[Counter, dict[str, str]]:
    """Which screening tier each finally selected dataset came from.

    The nine selected datasets are a subset of the tiers in the figure, not a
    fifth outcome, so this is reported as text rather than plotted. Deriving it
    here keeps the figure caption in the READMEs checkable against the data.
    """
    accessions = []
    for line in selected_txt.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            accessions.append(line.split()[0])  # selected.txt puts a reason after the GSE

    unscreened = [a for a in accessions if a not in decisions]
    if unscreened:
        raise SystemExit(f"selected but absent from the screening record: {unscreened}")

    by_tier = Counter(decisions[a] for a in accessions)
    non_strong = {a: decisions[a] for a in accessions if decisions[a] != "STRONG_CANDIDATE"}
    return by_tier, non_strong


def draw(counts: Counter, total: int, out_base: Path) -> list[Path]:
    labels = DECISION_ORDER
    values = [counts[d] for d in labels]

    fig, ax = plt.subplots(figsize=(8, 3.6))
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)

    positions = range(len(labels))
    bars = ax.barh(positions, values, height=0.62, color=BAR)
    ax.invert_yaxis()  # STRONG_CANDIDATE at the top

    ax.set_yticks(list(positions))
    ax.set_yticklabels(labels)  # verbatim, so a label can be grepped in summary.csv
    ax.set_xlabel("Datasets", color=TEXT_SECONDARY)
    ax.set_ylabel("Screening decision", color=TEXT_SECONDARY)
    ax.set_title(
        f"Screening outcome of {total} GEO candidates",
        color=TEXT_PRIMARY,
        fontsize=13,
        loc="left",
        pad=12,
    )

    ax.set_xlim(0, max(values) * 1.12)
    ax.xaxis.grid(True, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.tick_params(colors=TEXT_SECONDARY, length=0)
    for label in ax.get_yticklabels():
        label.set_color(TEXT_PRIMARY)

    for bar, value in zip(bars, values):
        ax.text(
            bar.get_width() + max(values) * 0.015,
            bar.get_y() + bar.get_height() / 2,
            str(value),
            va="center",
            ha="left",
            color=TEXT_PRIMARY,
            fontsize=11,
        )

    fig.tight_layout()
    out_base.parent.mkdir(parents=True, exist_ok=True)
    written = []
    for suffix in (".png", ".svg"):
        path = out_base.with_suffix(suffix)
        # Drop the SVG creation date so a rerun on unchanged input is byte-identical.
        metadata = {"Date": None} if suffix == ".svg" else None
        fig.savefig(path, dpi=200, facecolor=SURFACE, metadata=metadata)
        written.append(path)
    plt.close(fig)
    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--summary",
        type=Path,
        default=REPO_ROOT / "survom_nafld" / "reports" / "summary.csv",
        help="screening summary CSV to read (default: survom_nafld/reports/summary.csv)",
    )
    parser.add_argument(
        "--out-base",
        type=Path,
        default=REPO_ROOT / "assets" / "screening_overview",
        help="output path without extension; .png and .svg are written",
    )
    parser.add_argument(
        "--selected",
        type=Path,
        default=REPO_ROOT / "survom_nafld" / "selected.txt",
        help="selected accessions, for the final-selection breakdown; skipped if absent",
    )
    args = parser.parse_args(argv)

    decisions = read_decisions(args.summary)
    counts, total = read_counts(args.summary)
    written = draw(counts, total, args.out_base)

    print(f"{args.summary}: {total} screened")
    for decision in DECISION_ORDER:
        print(f"  {decision:<18} {counts[decision]}")
    print(f"  {'sum':<18} {sum(counts.values())}")

    if args.selected.exists():
        by_tier, non_strong = selection_breakdown(args.selected, decisions)
        named = ", ".join(f"{a} ({d})" for a, d in sorted(non_strong.items()))
        print(f"{args.selected}: {sum(by_tier.values())} finally selected")
        for decision in DECISION_ORDER:
            if by_tier[decision]:
                print(f"  {decision:<18} {by_tier[decision]}")
        if named:
            print(f"  outside STRONG_CANDIDATE: {named}")

    for path in written:
        print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
