import csv
import hashlib
import json
from pathlib import Path

from geo_screen.checks import run_checks
from geo_screen.classify import classify
from geo_screen.fetch import Fetched
from geo_screen.models import FileInventory
from geo_screen.normalize import sample_rows
from geo_screen.report import render_criteria_markdown, write_dataset, write_screening_report, write_summary
from geo_screen.soft import parse_soft

FIX = Path(__file__).parent / "fixtures"


def screen_fixture(accession):
    text = (FIX / f"{accession}_family.soft").read_text()
    fam = parse_soft(text)
    rows = sample_rows(fam)
    files = FileInventory()
    checks = run_checks(fam, rows, files)
    verdict = classify(checks)
    fetched = Fetched(
        url=f"https://ftp.ncbi.nlm.nih.gov/geo/series/GSE135nnn/{accession}/soft/{accession}_family.soft.gz",
        path=FIX / f"{accession}_family.soft",
        sha256=hashlib.sha256(text.encode()).hexdigest(),
        size_bytes=len(text.encode()),
        retrieved_at="2026-08-13T00:00:00Z",
        from_cache=False,
    )
    return fam, rows, checks, verdict, files, [fetched]


def test_dataset_writes_all_four_mandated_files(tmp_path):
    d = write_dataset(tmp_path, *screen_fixture("GSE135251"))
    for name in ("series_metadata.json", "sample_metadata.csv", "validation_report.md", "source_manifest.json"):
        assert (d / name).is_file()


def test_sample_csv_row_count_matches_gsm_count(tmp_path):
    d = write_dataset(tmp_path, *screen_fixture("GSE135251"))
    rows = list(csv.DictReader((d / "sample_metadata.csv").open()))
    assert len(rows) == 24 and rows[0]["gsm"] == "GSM3998167"


def test_computed_sections_use_parsed_counts_not_prior_notes(tmp_path):
    """The 24-sample fixture must never report 216 in a COMPUTED field. The quoted
    Series_summary legitimately contains '216 snap frozen liver biopsies', so scope
    the assertion to check observations, not the whole document."""
    md = (write_dataset(tmp_path, *screen_fixture("GSE135251")) / "validation_report.md").read_text()
    computed = md.split("<!-- computed -->")[1].split("<!-- /computed -->")[0]
    assert "216" not in computed
    assert "24/24" in computed


def test_manifest_records_checksum_and_timestamp(tmp_path):
    m = json.loads((write_dataset(tmp_path, *screen_fixture("GSE135251")) / "source_manifest.json").read_text())
    assert len(m["sources"][0]["sha256"]) == 64
    assert m["sources"][0]["retrieved_at"].endswith("Z")


def test_series_title_not_hidden_inside_computed_block(tmp_path):
    """The title (quoted GEO prose) sits outside the computed markers, distinct
    from the tool-derived counts and check table."""
    md = (write_dataset(tmp_path, *screen_fixture("GSE135251")) / "validation_report.md").read_text()
    before_computed = md.split("<!-- computed -->")[0]
    assert "TRANSCRIPTOMIC PROFILING" in before_computed


def test_summary_and_screening_report_cover_every_record(tmp_path):
    fam, rows, checks, verdict, files, _ = screen_fixture("GSE135251")
    record = _summary_record(fam, rows, checks, verdict)
    summary_path = write_summary(tmp_path, [record])
    report_path = write_screening_report(tmp_path, [record])
    assert summary_path.is_file() and report_path.is_file()
    csv_rows = list(csv.DictReader(summary_path.open()))
    assert csv_rows[0]["accession"] == "GSE135251"
    assert "STRONG_CANDIDATE" in report_path.read_text()


def _summary_record(fam, rows, checks, verdict):
    from geo_screen.models import SummaryRecord

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


def test_render_criteria_markdown_reflects_actual_thresholds():
    text = render_criteria_markdown()
    assert "20" in text  # STRONG_MIN_SAMPLES
    assert "single_cell_or_spatial" in text
    assert "STRONG_CANDIDATE" in text
