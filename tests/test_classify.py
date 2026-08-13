from pathlib import Path

from geo_screen.checks import run_checks
from geo_screen.classify import classify
from geo_screen.models import CheckResult, Decision, FileInventory, Status
from geo_screen.normalize import sample_rows
from geo_screen.soft import parse_soft

FIX = Path(__file__).parent / "fixtures"
EMPTY_FILES = FileInventory()


def checks_for(accession):
    fam = parse_soft((FIX / f"{accession}_family.soft").read_text())
    return run_checks(fam, sample_rows(fam), EMPTY_FILES)


def perfect_checks(organism="Homo sapiens", overrides=None):
    """A textbook-good 24-sample bulk human liver series: every check PASS
    (series_matrix/raw_sra INFO, which never gate STRONG). `overrides` maps
    a check id to the Status it should carry instead, for testing precedence."""
    overrides = overrides or {}
    base = {
        "sample_count": CheckResult("sample_count", "Sample count", Status.PASS, "24 samples"),
        "organism_consistency": CheckResult(
            "organism_consistency", "Organism consistency", Status.PASS, f"{organism} 24/24"
        ),
        "source_tissue": CheckResult("source_tissue", "Source tissue", Status.PASS, "liver-pattern source 24/24"),
        "library_strategy": CheckResult("library_strategy", "Library strategy", Status.PASS, "RNA-Seq 24/24"),
        "library_source": CheckResult("library_source", "Library source", Status.PASS, "transcriptomic 24/24"),
        "library_selection": CheckResult("library_selection", "Library selection", Status.PASS, "cDNA 24/24"),
        "instrument_model": CheckResult(
            "instrument_model", "Sequencing instrument", Status.PASS, "Illumina NextSeq 500 24/24"
        ),
        "metadata_completeness": CheckResult(
            "metadata_completeness", "Metadata completeness", Status.PASS, "reported consistently: disease"
        ),
        "disease_relevance": CheckResult(
            "disease_relevance",
            "Disease relevance",
            Status.PASS,
            "disease/fibrosis terms found in sample metadata (24 sample(s))",
        ),
        "single_cell_or_spatial": CheckResult(
            "single_cell_or_spatial", "Single-cell/spatial indicators", Status.PASS, "no single-cell/spatial signal detected"
        ),
        "material_type": CheckResult("material_type", "Material type", Status.PASS, "no cell-line/culture signal detected"),
        "expression_data_availability": CheckResult(
            "expression_data_availability",
            "Expression data availability",
            Status.PASS,
            "processed per-sample counts (24/24)",
        ),
        "series_matrix": CheckResult(
            "series_matrix", "Series Matrix availability", Status.INFO, "series matrix not found/listed"
        ),
        "raw_sra_availability": CheckResult(
            "raw_sra_availability", "Raw/SRA availability", Status.INFO, "SRA links recorded"
        ),
    }
    for check_id, status in overrides.items():
        old = base[check_id]
        base[check_id] = CheckResult(old.id, old.label, status, old.observed)
    return list(base.values())


def test_structural_single_cell_rejects_even_when_everything_else_is_perfect():
    v = classify(perfect_checks(overrides={"single_cell_or_spatial": Status.FAIL}))
    assert v.decision is Decision.REJECT
    assert any("cell-resolved" in r for r in v.reasons)


def test_textual_single_cell_warn_downgrades_to_manual_review_not_reject():
    v = classify(perfect_checks(overrides={"single_cell_or_spatial": Status.WARN}))
    assert v.decision is Decision.MANUAL_REVIEW


def test_mouse_is_candidate_never_reject():
    v = classify(perfect_checks(organism="Mus musculus"))
    assert v.decision is Decision.CANDIDATE
    assert any("not equivalent to human NAFLD" in r for r in v.unmet_strong)


def test_hepg2_is_manual_review_not_strong():
    v = classify(perfect_checks(overrides={"material_type": Status.WARN}))
    assert v.decision is Decision.MANUAL_REVIEW


def test_small_cohort_warn_goes_to_manual_review_by_precedence_rule_5():
    v = classify(perfect_checks(overrides={"sample_count": Status.WARN}))
    assert v.decision is Decision.MANUAL_REVIEW  # WARN outranks the STRONG test, deliberately


def test_real_flagship_fixture_actually_reaches_strong_candidate():
    """Guards precedence rule 5: if any check WARNs on a textbook-good dataset,
    the STRONG tier is unreachable and Task 9 has nothing to select from."""
    v = classify(checks_for("GSE135251"))
    assert v.decision is Decision.STRONG_CANDIDATE, v.reasons


def test_real_single_cell_fixture_is_rejected():
    v = classify(checks_for("GSE159262"))
    assert v.decision is Decision.REJECT


def test_every_reason_cites_a_check_id():
    v = classify(perfect_checks(overrides={"material_type": Status.WARN}))
    assert all(any(c.id in r for c in perfect_checks()) for r in v.reasons)
