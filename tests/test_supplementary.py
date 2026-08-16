"""Parser tests against saved GEO Series pages. No network."""

from pathlib import Path

import pytest

from geo_screen.supplementary import (
    TYPE_UNSPECIFIED,
    format_files,
    parse_series_page,
)

FIXTURES = Path(__file__).parent / "fixtures"


def page(name: str) -> str:
    return (FIXTURES / name).read_text()


def test_single_tar_keeps_geos_compound_type_verbatim():
    """The reason this parser exists: esummary reports TXT for this series,
    because it looks through the tar. GEO's own per-file type does not."""
    files, _ = parse_series_page(page("GSE135251_acc.html"))

    assert [f.filename for f in files] == ["GSE135251_RAW.tar"]
    assert files[0].file_type == "TAR (of TXT)"
    assert files[0].size_bytes == "45854720"


def test_multiple_files_keep_page_order_and_their_own_types():
    files, _ = parse_series_page(page("GSE167523_acc.html"))

    assert [(f.filename, f.file_type) for f in files] == [
        ("GSE167523_RAW.tar", "TAR (of TXT)"),
        ("GSE167523_Raw_gene_counts_matrix.txt.gz", "TXT"),
        ("GSE167523_Sample_phenotype_correspondence.xlsx", "XLSX"),
    ]


def test_header_row_is_not_reported_as_a_file():
    files, notes = parse_series_page(page("GSE167523_acc.html"))

    assert "Supplementary file" not in [f.filename for f in files]
    assert "Supplementary file" not in " ".join(notes)


def test_sra_and_status_rows_are_notes_not_files():
    """A linked SRA resource is not a supplementary file and must not be
    counted as one."""
    files, notes = parse_series_page(page("GSE167523_acc.html"))

    assert not any("SRA" in f.filename for f in files)
    assert "SRA Run Selector" in notes
    assert "Raw data are available in SRA" in notes


def test_ftp_url_preferred_but_tar_falls_back_to_the_download_path():
    files, _ = parse_series_page(page("GSE167523_acc.html"))
    tar, matrix = files[0], files[1]

    assert tar.download_url.startswith("https://www.ncbi.nlm.nih.gov/geo/download/")
    assert matrix.download_url.startswith("ftp://ftp.ncbi.nlm.nih.gov/geo/series/")


def test_series_with_no_supplementary_table_yields_no_files():
    files, _ = parse_series_page(page("GSE193084_acc.html"))

    assert files == []


def test_empty_type_cell_is_marked_unspecified_not_guessed():
    """The filename ends .txt.gz, which is exactly the kind of guess this
    parser must not make when GEO leaves the cell blank."""
    files, _ = parse_series_page(page("empty_type_acc.html"))
    blank = [f for f in files if f.filename.endswith("_Raw_gene_counts_matrix.txt.gz")]

    assert len(blank) == 1
    assert blank[0].file_type == TYPE_UNSPECIFIED


def test_page_without_the_table_markup_does_not_raise():
    assert parse_series_page("<html><body><p>nothing here</p></body></html>") == ([], [])


@pytest.mark.parametrize("fixture", ["GSE135251_acc.html", "GSE167523_acc.html"])
def test_formatted_column_pairs_every_name_with_its_type(fixture):
    files, _ = parse_series_page(page(fixture))
    formatted = format_files(files)

    assert formatted.count(";") == len(files) - 1
    for supp in files:
        assert f"{supp.filename} [{supp.file_type}]" in formatted
