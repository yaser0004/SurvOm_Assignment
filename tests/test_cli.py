import csv

from geo_screen import cli
from geo_screen.cli import main, read_accessions
from geo_screen.models import SummaryRecord


def fake_record(accession: str) -> SummaryRecord:
    return SummaryRecord(
        accession=accession,
        title="fake title",
        organism="Homo sapiens 1/1",
        n_samples=1,
        source_summary="liver-pattern source 1/1",
        library_strategy="RNA-Seq 1/1",
        single_cell_flag="PASS",
        material_flag="PASS",
        disease_terms_found="disease/fibrosis terms found in sample metadata (1 sample(s))",
        expression_files="processed per-sample counts (1/1)",
        decision="STRONG_CANDIDATE",
        top_reason="",
    )


def test_bare_accession_dispatches_to_screen(monkeypatch, tmp_path):
    seen = []
    monkeypatch.setattr(cli, "screen_accessions", lambda accs, **kw: seen.extend(accs))
    assert main(["GSE135251", "--out", str(tmp_path), "--offline"]) == 0
    assert seen == ["GSE135251"]


def test_file_input_tolerates_comments_blanks_dupes_and_trailing_reasons(tmp_path):
    f = tmp_path / "c.txt"
    f.write_text("GSE1\n# comment\n\nGSE2  largest fibrosis-spectrum cohort\nGSE1\n")
    assert read_accessions(f) == ["GSE1", "GSE2"]


def test_invalid_accession_is_rejected_not_fetched(tmp_path, caplog):
    assert main(["GSE1; rm -rf /", "--out", str(tmp_path), "--offline"]) == 1
    assert "invalid accession" in caplog.text.lower()


def test_search_dedupes_hits_across_overlapping_queries(monkeypatch, tmp_path):
    query_file = tmp_path / "queries.txt"
    query_file.write_text("query one\nquery two\n")

    def fake_search(client, query, retmax=500):
        # GSE1 shows up under both queries; a naive concat would list it twice.
        return [{"accession": "GSE1", "title": "t"}, {"accession": "GSE2", "title": "t2"}]

    captured = {}

    def fake_write_candidates(out, query, hits):
        captured["hits"] = hits
        return tmp_path / "candidates.csv"

    monkeypatch.setattr("geo_screen.search.search", fake_search)
    monkeypatch.setattr("geo_screen.search.write_candidates", fake_write_candidates)

    assert main(["search", "--query-file", str(query_file), "--out", str(tmp_path), "--offline"]) == 0
    assert [h["accession"] for h in captured["hits"]] == ["GSE1", "GSE2"]


def test_one_failing_gse_does_not_abort_the_batch(monkeypatch, tmp_path, caplog):
    def fake_screen_one(acc, **kw):
        if acc == "GSE1":
            raise RuntimeError("boom")
        return fake_record(acc)

    monkeypatch.setattr(cli, "screen_one", fake_screen_one)
    assert main(["GSE1", "GSE2", "--out", str(tmp_path)]) == 0
    rows = list(csv.DictReader((tmp_path / "reports" / "summary.csv").open()))
    assert [r["accession"] for r in rows] == ["GSE2"]
    assert "GSE1" in caplog.text and "boom" in caplog.text
