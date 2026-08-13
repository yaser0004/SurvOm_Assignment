from pathlib import Path

from geo_screen.normalize import (
    canonical_key,
    discover_fields,
    field_report,
    parse_characteristics,
    sample_rows,
)
from geo_screen.soft import parse_soft

FIX = Path(__file__).parent / "fixtures"


def test_characteristics_split_on_first_colon_only():
    out = parse_characteristics(["nas score: 4", "note: see ref: 12", "no_colon_value"])
    assert out[0] == ("nas score", "4")
    assert out[1] == ("note", "see ref: 12")
    assert out[2] == ("characteristics_3", "no_colon_value")


def test_canonical_mapping_is_case_and_punctuation_insensitive():
    assert canonical_key("Fibrosis Stage") == "fibrosis_stage"
    assert canonical_key("fibrosis_stage") == "fibrosis_stage"
    assert canonical_key("group in paper") == "group"
    assert canonical_key("Stage") == "stage"  # NOT fibrosis_stage
    assert canonical_key("random unknown field") is None


def test_fibrotic_stage_synonym_maps_to_fibrosis_stage():
    """GSE213621 (368 samples) reports 'fibrotic stage: F2' - a real GEO series
    that uses this adjective form instead of 'fibrosis stage'. Missing this
    synonym silently drops a large dataset's disease-relevant metadata."""
    assert canonical_key("fibrotic stage") == "fibrosis_stage"
    assert canonical_key("fibrosisscore") == "fibrosis_stage"
    assert canonical_key("patient diagnosis") == "diagnosis"


def test_field_discovery_counts_presence_not_assumption():
    fam = parse_soft((FIX / "GSE135251_family.soft").read_text())
    fields = discover_fields(fam)
    assert fields["disease"] == 24  # 24 samples in the trimmed fixture
    assert "made_up_clinical_field" not in fields


def test_field_report_carries_canonical_mapping_and_totals():
    fam = parse_soft((FIX / "GSE135251_family.soft").read_text())
    report = field_report(fam)
    assert report["fibrosis stage"] == {
        "present": 24,
        "total": 24,
        "canonical": "fibrosis_stage",
    }


def test_rows_carry_canonical_and_raw_columns():
    rows = sample_rows(parse_soft((FIX / "GSE135251_family.soft").read_text()))
    assert len(rows) == 24
    r = rows[0]
    assert r["gsm"] == "GSM3998167"
    assert r["organism"] == "Homo sapiens"
    assert r["library_strategy"] == "RNA-Seq"
    assert r["instrument_model"] == "Illumina NextSeq 500"
    assert r["canon__fibrosis_stage"] == "2"
    assert r["raw__group in paper"] == "NASH_F2"  # original key preserved verbatim


def test_rows_never_invent_a_column_for_a_field_the_series_never_reports():
    rows = sample_rows(parse_soft((FIX / "GSE135251_family.soft").read_text()))
    # GSE135251 never reports sex/age/bmi for any sample - no canon__ column
    # should be fabricated for them ("discover fields actually present").
    assert "canon__sex" not in rows[0]
    assert "canon__bmi" not in rows[0]
