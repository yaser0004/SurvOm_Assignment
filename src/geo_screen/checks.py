"""Fourteen objective, evidence-producing checks over a screened GSE.

Every check is a pure function of (SoftFamily, sample rows, FileInventory)
returning one CheckResult. No check makes a network call or downloads
anything - by the time run_checks() runs, all evidence is already in hand
from the SOFT family text plus (for series_matrix/raw_sra) a small FTP
directory listing gathered separately.

Sample-level evidence outranks series prose: single_cell_check and
material_type_check both consult a structural (GSM-field) tier before a
textual (series free-text) tier, per rules.SINGLE_CELL_SIGNALS /
rules.NON_TISSUE_SIGNALS.
"""

from __future__ import annotations

import re
from collections.abc import Callable, Iterable

from geo_screen.models import CheckResult, Evidence, FileInventory, SoftFamily, Status
from geo_screen.normalize import CANONICAL_FIELDS, field_report
from geo_screen.rules import (
    DISEASE_ISH_CANONICAL_FIELDS,
    DISEASE_TERMS,
    LIVER_SOURCE_FIELDS,
    LIVER_SOURCE_PATTERN,
    NON_TISSUE_SIGNALS,
    OFF_TARGET_TISSUE_SIGNALS,
    SINGLE_CELL_SIGNALS,
    STRONG_MIN_SAMPLES,
    STRONG_SOURCE_FRACTION,
    BULK_STRATEGIES,
    Signal,
)


def _series_accession(fam: SoftFamily) -> str:
    values = fam.series.get("Series_geo_accession", [])
    return values[0] if values else "unknown"


def _iter_field_values(fam: SoftFamily, field: str) -> Iterable[tuple[str, str, str]]:
    """Yield (accession, actual_soft_key, value) for a Signal field name.

    "Sample_supplementary_file" and "Series_supplementary_file" are treated
    as prefixes covering the numbered !Sample_supplementary_file_N /
    !Series_supplementary_file variants that actually appear in SOFT text.
    """
    if field == "Series_supplementary_file":
        for value in fam.series.get(field, []):
            yield _series_accession(fam), field, value
        return
    if field == "Sample_supplementary_file":
        for gsm, sample in fam.samples.items():
            for key, values in sample.items():
                if key.startswith("Sample_supplementary_file"):
                    for value in values:
                        yield gsm, key, value
        return
    if field.startswith("Series_"):
        for value in fam.series.get(field, []):
            yield _series_accession(fam), field, value
        return
    if field.startswith("Sample_"):
        for gsm, sample in fam.samples.items():
            for value in sample.get(field, []):
                yield gsm, field, value


def _find_signal_hits(signal: Signal, fam: SoftFamily) -> list[Evidence]:
    pattern = re.compile(signal.pattern, re.IGNORECASE)
    hits: list[Evidence] = []
    for field in signal.fields:
        for accession, actual_key, value in _iter_field_values(fam, field):
            match = pattern.search(value)
            if match:
                hits.append(
                    Evidence(
                        accession=accession,
                        field=actual_key,
                        matched=match.group(0),
                        snippet=value[:200],
                    )
                )
    return hits


def sample_count_check(fam: SoftFamily, rows: list[dict[str, str]], files: FileInventory) -> CheckResult:
    n = len(rows)
    if n == 0:
        return CheckResult("sample_count", "Sample count", Status.FAIL, "0 samples")
    if n < STRONG_MIN_SAMPLES:
        return CheckResult(
            "sample_count", "Sample count", Status.WARN, f"{n} samples (below {STRONG_MIN_SAMPLES})"
        )
    return CheckResult("sample_count", "Sample count", Status.PASS, f"{n} samples")


def organism_check(fam: SoftFamily, rows: list[dict[str, str]], files: FileInventory) -> CheckResult:
    n = len(rows)
    organisms = [r["organism"] for r in rows if r.get("organism")]
    distinct = sorted(set(organisms))
    if len(distinct) <= 1:
        organism = distinct[0] if distinct else "unreported"
        return CheckResult(
            "organism_consistency", "Organism consistency", Status.PASS, f"{organism} {len(organisms)}/{n}"
        )
    breakdown = ", ".join(f"{o} {organisms.count(o)}/{n}" for o in distinct)
    return CheckResult(
        "organism_consistency", "Organism consistency", Status.WARN, f"mixed organisms: {breakdown}"
    )


_LIVER_SIGNAL = Signal(
    id="liver_source",
    pattern=LIVER_SOURCE_PATTERN,
    fields=LIVER_SOURCE_FIELDS,
    tier="structural",
    note="sample source names liver/hepatic/biopsy material",
)


def source_tissue_check(fam: SoftFamily, rows: list[dict[str, str]], files: FileInventory) -> CheckResult:
    n = len(rows)
    liver_evidence = _find_signal_hits(_LIVER_SIGNAL, fam)
    liver_accessions = {e.accession for e in liver_evidence}
    off_target_evidence = _find_signal_hits(OFF_TARGET_TISSUE_SIGNALS[0], fam)
    fraction = len(liver_accessions) / n if n else 0.0

    if fraction >= STRONG_SOURCE_FRACTION and not off_target_evidence:
        return CheckResult(
            "source_tissue", "Source tissue", Status.PASS, f"liver-pattern source {len(liver_accessions)}/{n}"
        )

    note = f"liver-pattern source {len(liver_accessions)}/{n}"
    if off_target_evidence:
        note += "; off-target tissue signal detected"
    return CheckResult(
        "source_tissue", "Source tissue", Status.WARN, note, tuple(off_target_evidence)
    )


def library_strategy_check(fam: SoftFamily, rows: list[dict[str, str]], files: FileInventory) -> CheckResult:
    n = len(rows)
    strategies = [r.get("library_strategy", "") for r in rows]
    distinct = sorted(set(strategies))
    bulk_hits = [s for s in strategies if s in BULK_STRATEGIES]
    if not bulk_hits:
        return CheckResult(
            "library_strategy",
            "Library strategy",
            Status.FAIL,
            f"no expression-profiling strategy found ({', '.join(distinct) or 'none reported'})",
        )
    if len(distinct) == 1:
        return CheckResult("library_strategy", "Library strategy", Status.PASS, f"{distinct[0]} {n}/{n}")
    breakdown = ", ".join(f"{s or 'unreported'} {strategies.count(s)}/{n}" for s in distinct)
    return CheckResult("library_strategy", "Library strategy", Status.WARN, f"mixed strategies: {breakdown}")


def library_source_check(fam: SoftFamily, rows: list[dict[str, str]], files: FileInventory) -> CheckResult:
    n = len(rows)
    sources = [r.get("library_source", "") for r in rows]
    distinct = sorted(set(sources))
    if len(distinct) == 1 and distinct[0].lower() == "transcriptomic":
        return CheckResult("library_source", "Library source", Status.PASS, f"{distinct[0]} {n}/{n}")
    breakdown = ", ".join(f"{s or 'unreported'} {sources.count(s)}/{n}" for s in distinct)
    return CheckResult("library_source", "Library source", Status.WARN, f"library_source: {breakdown}")


def library_selection_check(fam: SoftFamily, rows: list[dict[str, str]], files: FileInventory) -> CheckResult:
    n = len(rows)
    values = [r.get("library_selection", "") for r in rows]
    distinct = sorted(set(values))
    if len(distinct) <= 1:
        value = distinct[0] if distinct else "unreported"
        return CheckResult("library_selection", "Library selection", Status.PASS, f"{value} {n}/{n}")
    breakdown = ", ".join(f"{v or 'unreported'} {values.count(v)}/{n}" for v in distinct)
    return CheckResult(
        "library_selection", "Library selection", Status.WARN, f"mixed library_selection: {breakdown}"
    )


def instrument_check(fam: SoftFamily, rows: list[dict[str, str]], files: FileInventory) -> CheckResult:
    n = len(rows)
    values = [r.get("instrument_model", "") for r in rows if r.get("instrument_model")]
    if not values:
        return CheckResult(
            "instrument_model", "Sequencing instrument", Status.INFO, "instrument model not reported"
        )
    distinct = sorted(set(values))
    if len(distinct) == 1:
        return CheckResult(
            "instrument_model", "Sequencing instrument", Status.PASS, f"{distinct[0]} {len(values)}/{n}"
        )
    breakdown = ", ".join(f"{v} {values.count(v)}/{n}" for v in distinct)
    return CheckResult(
        "instrument_model", "Sequencing instrument", Status.WARN, f"mixed instruments: {breakdown}"
    )


def metadata_completeness_check(
    fam: SoftFamily, rows: list[dict[str, str]], files: FileInventory
) -> CheckResult:
    n = len(rows)
    canon_columns = sorted({k for row in rows for k in row if k.startswith("canon__")})
    reported = {col[len("canon__") :]: sum(1 for row in rows if row.get(col)) for col in canon_columns}

    disease_ish_present = any(reported.get(c, 0) > 0 for c in DISEASE_ISH_CANONICAL_FIELDS)
    if not disease_ish_present:
        return CheckResult(
            "metadata_completeness",
            "Metadata completeness",
            Status.WARN,
            "no disease/diagnosis/group/stage-type canonical field reported anywhere",
        )

    patchy = sorted(c for c, present in reported.items() if 0 < present < n)
    fully_reported = sorted(c for c, present in reported.items() if present == n)
    not_reported = sorted(set(CANONICAL_FIELDS) - set(reported))

    parts = []
    if fully_reported:
        parts.append("reported consistently: " + ", ".join(fully_reported))
    if not_reported:
        parts.append("not reported anywhere: " + ", ".join(not_reported))
    observed = "; ".join(parts)

    if patchy:
        patchy_desc = ", ".join(f"{c} {reported[c]}/{n}" for c in patchy)
        return CheckResult(
            "metadata_completeness",
            "Metadata completeness",
            Status.WARN,
            f"patchy fields: {patchy_desc}. {observed}",
        )
    return CheckResult("metadata_completeness", "Metadata completeness", Status.PASS, observed)


_DISEASE_PATTERN = re.compile("|".join(re.escape(term) for term in DISEASE_TERMS), re.IGNORECASE)
_DISEASE_SAMPLE_FIELDS = ("Sample_title", "Sample_source_name_ch1", "Sample_characteristics_ch1")
_DISEASE_SERIES_FIELDS = ("Series_title", "Series_summary", "Series_overall_design")


def disease_relevance_check(fam: SoftFamily, rows: list[dict[str, str]], files: FileInventory) -> CheckResult:
    sample_hits: list[Evidence] = []
    for field in _DISEASE_SAMPLE_FIELDS:
        for accession, key, value in _iter_field_values(fam, field):
            match = _DISEASE_PATTERN.search(value)
            if match:
                sample_hits.append(Evidence(accession, key, match.group(0), value[:200]))

    if sample_hits:
        n_hit = len({e.accession for e in sample_hits})
        return CheckResult(
            "disease_relevance",
            "Disease relevance",
            Status.PASS,
            f"disease/fibrosis terms found in sample metadata ({n_hit} sample(s))",
            tuple(sample_hits),
        )

    series_hits: list[Evidence] = []
    for field in _DISEASE_SERIES_FIELDS:
        for accession, key, value in _iter_field_values(fam, field):
            match = _DISEASE_PATTERN.search(value)
            if match:
                series_hits.append(Evidence(accession, key, match.group(0), value[:200]))

    if series_hits:
        return CheckResult(
            "disease_relevance",
            "Disease relevance",
            Status.WARN,
            "disease term found only in series-level text, not corroborated by sample metadata",
            tuple(series_hits),
        )

    return CheckResult(
        "disease_relevance", "Disease relevance", Status.FAIL, "no NAFLD-spectrum term found in series or sample metadata"
    )


def single_cell_check(fam: SoftFamily, rows: list[dict[str, str]], files: FileInventory) -> CheckResult:
    structural_signals = [s for s in SINGLE_CELL_SIGNALS if s.tier == "structural"]
    textual_signals = [s for s in SINGLE_CELL_SIGNALS if s.tier == "textual"]
    structural_hits = [e for sig in structural_signals for e in _find_signal_hits(sig, fam)]
    textual_hits = [e for sig in textual_signals for e in _find_signal_hits(sig, fam)]

    if structural_hits:
        terms = sorted({e.matched for e in structural_hits})
        n_hit = len({e.accession for e in structural_hits})
        return CheckResult(
            "single_cell_or_spatial",
            "Single-cell/spatial indicators",
            Status.FAIL,
            f"cell-resolved signal in sample metadata: {', '.join(terms)} ({n_hit} sample(s))",
            tuple(structural_hits),
        )
    if textual_hits:
        terms = sorted({e.matched for e in textual_hits})
        return CheckResult(
            "single_cell_or_spatial",
            "Single-cell/spatial indicators",
            Status.WARN,
            f"series prose mentions {', '.join(terms)}; sample metadata does not corroborate",
            tuple(textual_hits),
        )
    return CheckResult(
        "single_cell_or_spatial", "Single-cell/spatial indicators", Status.PASS, "no single-cell/spatial signal detected"
    )


def material_type_check(fam: SoftFamily, rows: list[dict[str, str]], files: FileInventory) -> CheckResult:
    structural = next(s for s in NON_TISSUE_SIGNALS if s.tier == "structural")
    textual = next(s for s in NON_TISSUE_SIGNALS if s.tier == "textual")
    structural_hits = _find_signal_hits(structural, fam)
    textual_hits = _find_signal_hits(textual, fam)

    if structural_hits:
        terms = sorted({e.matched for e in structural_hits})
        n_hit = len({e.accession for e in structural_hits})
        return CheckResult(
            "material_type",
            "Material type",
            Status.WARN,
            f"cell/culture terms in sample metadata: {', '.join(terms)} ({n_hit}/{len(rows)} samples)",
            tuple(structural_hits),
        )
    if textual_hits:
        terms = sorted({e.matched for e in textual_hits})
        return CheckResult(
            "material_type",
            "Material type",
            Status.INFO,
            f"series prose mentions {', '.join(terms)}; sample metadata does not corroborate",
            tuple(textual_hits),
        )
    return CheckResult("material_type", "Material type", Status.PASS, "no cell-line/culture signal detected")


_MAX_LISTED_LINKS = 5


def _summarize_links(links: list[str]) -> str:
    """A series can have hundreds of SRA links; joining every one inline makes
    a report unreadable. Show the first few and a count of the rest - the
    full list is still in sample_metadata.csv's sra_relation column."""
    if len(links) <= _MAX_LISTED_LINKS:
        return ", ".join(links)
    shown = ", ".join(links[:_MAX_LISTED_LINKS])
    return f"{shown}, and {len(links) - _MAX_LISTED_LINKS} more (see sample_metadata.csv)"


_EXPRESSION_PATTERN = re.compile(
    r"counts|matrix|tpm|fpkm|rpkm|cpm|expression|abundance|quant", re.IGNORECASE
)
_NON_EXPRESSION_PATTERN = re.compile(r"\.fastq|\.bam|\.sra|\.bw|\.bed", re.IGNORECASE)


def is_processed_expression_filename(name: str) -> bool:
    return bool(_EXPRESSION_PATTERN.search(name)) and not _NON_EXPRESSION_PATTERN.search(name)


def expression_check(fam: SoftFamily, rows: list[dict[str, str]], files: FileInventory) -> CheckResult:
    n = len(rows)
    sample_hit_count = 0
    for row in rows:
        names = [name for name in row.get("supplementary_files", "").split(" | ") if name]
        if any(is_processed_expression_filename(name) for name in names):
            sample_hit_count += 1

    series_names = [name for name, _size in files.series_supplementary]
    series_names += fam.series.get("Series_supplementary_file", [])
    series_hit = next((name for name in series_names if is_processed_expression_filename(name)), None)

    if sample_hit_count:
        raw_tar = next(
            (name for name, _size in files.series_supplementary if name.lower().endswith("_raw.tar")), None
        )
        packaging = f", packaged in {raw_tar}" if raw_tar else ""
        return CheckResult(
            "expression_data_availability",
            "Expression data availability",
            Status.PASS,
            f"processed per-sample counts ({sample_hit_count}/{n}){packaging}",
        )

    if series_hit:
        return CheckResult(
            "expression_data_availability",
            "Expression data availability",
            Status.PASS,
            f"processed series-level file: {series_hit}",
        )

    sra_links = list(files.sra_links) or sorted({row["sra_relation"] for row in rows if row.get("sra_relation")})
    if sra_links:
        return CheckResult(
            "expression_data_availability",
            "Expression data availability",
            Status.INFO,
            f"raw sequencing only ({_summarize_links(sra_links)})",
        )

    return CheckResult(
        "expression_data_availability",
        "Expression data availability",
        Status.FAIL,
        "no downloadable expression data or sequencing reads found",
    )


def series_matrix_check(fam: SoftFamily, rows: list[dict[str, str]], files: FileInventory) -> CheckResult:
    if not files.series_matrix:
        return CheckResult("series_matrix", "Series Matrix availability", Status.INFO, "series matrix not found/listed")

    name, _size = files.series_matrix[0]
    sample_types = {row.get("sample_type", "") for row in rows}
    row_counts = [v for sample in fam.samples.values() for v in sample.get("Sample_data_row_count", [])]
    metadata_only = sample_types == {"SRA"} or (row_counts and all(v == "0" for v in row_counts))

    if metadata_only:
        return CheckResult(
            "series_matrix",
            "Series Matrix availability",
            Status.INFO,
            f"present, metadata-only ({name}); samples are SRA-type with zero data rows",
        )
    return CheckResult("series_matrix", "Series Matrix availability", Status.PASS, f"present with expression data: {name}")


def raw_sra_check(fam: SoftFamily, rows: list[dict[str, str]], files: FileInventory) -> CheckResult:
    links = list(files.sra_links) or sorted({row["sra_relation"] for row in rows if row.get("sra_relation")})
    if links:
        return CheckResult(
            "raw_sra_availability",
            "Raw/SRA availability",
            Status.INFO,
            f"SRA/BioProject links recorded, not downloaded: {_summarize_links(links)}",
        )
    return CheckResult("raw_sra_availability", "Raw/SRA availability", Status.INFO, "no SRA/raw sequencing links found")


CHECKS: tuple[Callable[[SoftFamily, list[dict[str, str]], FileInventory], CheckResult], ...] = (
    sample_count_check,
    organism_check,
    source_tissue_check,
    library_strategy_check,
    library_source_check,
    library_selection_check,
    instrument_check,
    metadata_completeness_check,
    disease_relevance_check,
    single_cell_check,
    material_type_check,
    expression_check,
    series_matrix_check,
    raw_sra_check,
)


def run_checks(fam: SoftFamily, rows: list[dict[str, str]], files: FileInventory) -> list[CheckResult]:
    return [check(fam, rows, files) for check in CHECKS]
