from pathlib import Path

from geo_screen.checks import (
    disease_relevance_check,
    material_type_check,
    run_checks,
    single_cell_check,
)
from geo_screen.models import FileInventory, Status
from geo_screen.normalize import sample_rows
from geo_screen.soft import parse_soft

FIX = Path(__file__).parent / "fixtures"
EMPTY_FILES = FileInventory()


def checks_for_family(fam):
    return run_checks(fam, sample_rows(fam), EMPTY_FILES)


def checks_for(accession):
    fam = parse_soft((FIX / f"{accession}_family.soft").read_text())
    return checks_for_family(fam)


def drop_field(accession, raw_key, from_samples):
    fam = parse_soft((FIX / f"{accession}_family.soft").read_text())
    gsms = list(fam.samples.keys())
    for i in from_samples:
        gsm = gsms[i]
        chars = fam.samples[gsm].get("Sample_characteristics_ch1", [])
        fam.samples[gsm]["Sample_characteristics_ch1"] = [
            c for c in chars if not c.lower().startswith(raw_key.lower() + ":")
        ]
    return fam


_SRA_SOFT_TEXT = """^SERIES = GSE900001
!Series_geo_accession = GSE900001
!Series_title = Fake SRA-only series for testing
^SAMPLE = GSM1
!Sample_geo_accession = GSM1
!Sample_type = SRA
!Sample_organism_ch1 = Homo sapiens
!Sample_source_name_ch1 = liver biopsy
!Sample_characteristics_ch1 = disease: NAFLD
!Sample_library_strategy = RNA-Seq
!Sample_library_source = transcriptomic
!Sample_supplementary_file_1 = NONE
!Sample_data_row_count = 0
^SAMPLE = GSM2
!Sample_geo_accession = GSM2
!Sample_type = SRA
!Sample_organism_ch1 = Homo sapiens
!Sample_source_name_ch1 = liver biopsy
!Sample_characteristics_ch1 = disease: NAFLD
!Sample_library_strategy = RNA-Seq
!Sample_library_source = transcriptomic
!Sample_supplementary_file_1 = NONE
!Sample_data_row_count = 0
"""
sra_family = parse_soft(_SRA_SOFT_TEXT)
sra_rows = sample_rows(sra_family)


def test_bulk_liver_series_passes_core_checks():
    by_id = {c.id: c for c in checks_for("GSE135251")}
    assert by_id["library_strategy"].status is Status.PASS
    assert by_id["organism_consistency"].observed.startswith("Homo sapiens 24/24")
    assert by_id["source_tissue"].status is Status.PASS
    assert by_id["single_cell_or_spatial"].status is Status.PASS
    assert by_id["disease_relevance"].status is Status.PASS


def test_single_cell_detected_from_sample_protocol_not_series_text():
    c = {x.id: x for x in checks_for("GSE159262")}["single_cell_or_spatial"]
    assert c.status is Status.FAIL
    fields = {e.field for e in c.evidence}
    assert "Sample_extract_protocol_ch1" in fields or "Sample_data_processing" in fields
    assert all(not f.startswith("Series_") for f in fields)


def test_series_background_mention_of_single_cell_only_warns():
    fam = parse_soft("^SERIES = GSE1\n!Series_geo_accession = GSE1\n!Series_summary = Unlike single-cell studies, we used bulk RNA-seq.\n")
    assert single_cell_check(fam, [], EMPTY_FILES).status is Status.WARN


def test_cell_line_named_in_sample_metadata_warns_not_rejects():
    by_id = {c.id: c for c in checks_for("GSE270357")}
    assert by_id["material_type"].status is Status.WARN
    assert "HepG2" in by_id["material_type"].observed
    assert any(e.field.startswith("Sample_") for e in by_id["material_type"].evidence)


def test_in_vitro_only_in_series_prose_is_info_not_warn():
    """A real liver-biopsy cohort whose abstract says 'provides an in-vitro model for...'
    must not be dragged into MANUAL_REVIEW by its own discussion section."""
    fam = parse_soft((FIX / "GSE135251_family.soft").read_text())
    fam.series["Series_summary"].append("These findings provide an in vitro model for drug testing.")
    c = material_type_check(fam, sample_rows(fam), EMPTY_FILES)
    assert c.status is Status.INFO
    assert "does not corroborate" in c.observed


def test_absent_fields_do_not_warn_but_patchy_fields_do():
    by_id = {c.id: c for c in checks_for("GSE135251")}
    # fixture reports disease/nas/fibrosis/group/Stage in every sample; sex/age/bmi nowhere
    assert by_id["metadata_completeness"].status is Status.PASS
    assert "sex" in by_id["metadata_completeness"].observed  # listed as not reported
    patchy = checks_for_family(drop_field("GSE135251", "disease", from_samples=[0]))
    assert {c.id: c for c in patchy}["metadata_completeness"].status is Status.WARN


def test_raw_tar_of_processed_counts_is_expression_availability_pass():
    """GEO's _RAW.tar is 'archive of per-sample files', not 'raw FASTQ'. GSE135251's
    contains GSM*_*.counts.txt.gz - WARNing here would make STRONG unreachable."""
    c = {x.id: x for x in checks_for("GSE135251")}["expression_data_availability"]
    assert c.status is Status.PASS
    assert "counts" in c.observed.lower()


def test_sra_only_series_is_info_not_pass_and_not_fail():
    files = FileInventory(
        series_supplementary=(), sample_supplementary=("NONE",), series_matrix=(), sra_links=("SRP217231",)
    )
    c = {x.id: x for x in run_checks(sra_family, sra_rows, files)}["expression_data_availability"]
    assert c.status is Status.INFO and "raw sequencing only" in c.observed


def test_long_sra_link_list_is_truncated_not_dumped_inline():
    """A 368-sample series has 368 SRA links - joining them all inline makes
    validation_report.md and the per-dataset README unreadable."""
    files = FileInventory(series_supplementary=(), sample_supplementary=(), series_matrix=(), sra_links=tuple(f"SRX{i}" for i in range(50)))
    c = {x.id: x for x in run_checks(sra_family, sra_rows, files)}["raw_sra_availability"]
    assert "and 45 more" in c.observed
    assert c.observed.count("SRX") == 5


def test_series_matrix_without_table_is_not_expression_availability():
    files = FileInventory(
        series_supplementary=(),
        sample_supplementary=(),
        series_matrix=(("GSE900001_series_matrix.txt.gz", 4000),),
        sra_links=(),
    )
    res = {c.id: c for c in run_checks(sra_family, sra_rows, files)}
    assert res["series_matrix"].status is Status.INFO
    assert "metadata-only" in res["series_matrix"].observed
    assert res["expression_data_availability"].status is Status.FAIL


def test_disease_term_only_in_series_prose_warns_not_passes():
    fam = parse_soft(
        "^SERIES = GSE1\n!Series_geo_accession = GSE1\n"
        "!Series_summary = We studied NAFLD progression.\n"
        "^SAMPLE = GSM1\n!Sample_geo_accession = GSM1\n!Sample_source_name_ch1 = liver\n"
    )
    c = disease_relevance_check(fam, sample_rows(fam), EMPTY_FILES)
    assert c.status is Status.WARN
