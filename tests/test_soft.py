from pathlib import Path

from geo_screen.soft import parse_soft

FIX = Path(__file__).parent / "fixtures"


def test_parses_series_samples_and_repeated_keys():
    fam = parse_soft((FIX / "GSE135251_family.soft").read_text())
    assert fam.accession == "GSE135251"
    assert fam.series["Series_title"][0].startswith("TRANSCRIPTOMIC PROFILING")
    assert len(fam.series["Series_summary"]) == 3  # repeated key -> list
    s = fam.samples["GSM3998167"]
    assert s["Sample_organism_ch1"] == ["Homo sapiens"]
    assert s["Sample_library_strategy"] == ["RNA-Seq"]
    assert "nas score: 4" in s["Sample_characteristics_ch1"]
    assert len(s["Sample_characteristics_ch1"]) == 5


def test_value_containing_equals_is_not_split():
    fam = parse_soft("^SERIES = GSE1\n!Series_overall_design = a = b = c\n")
    assert fam.series["Series_overall_design"] == ["a = b = c"]


def test_data_tables_and_comments_ignored():
    txt = (
        "^SERIES = GSE1\n#ID_REF = x\n!series_matrix_table_begin\n"
        "1\t2\n!series_matrix_table_end\n"
    )
    assert parse_soft(txt).series == {}


def test_platform_and_multiple_samples_are_keyed_by_accession():
    fam = parse_soft((FIX / "GSE159262_family.soft").read_text())
    assert set(fam.samples) == {
        "GSM4824487",
        "GSM4824488",
        "GSM4824489",
        "GSM4824490",
        "GSM4824491",
    }
    assert "GPL20301" in fam.platforms
    assert fam.platforms["GPL20301"]["Platform_geo_accession"] == ["GPL20301"]


def test_field_with_no_equals_sign_gets_empty_value():
    fam = parse_soft("^SERIES = GSE1\n!Series_type\n")
    assert fam.series["Series_type"] == [""]
