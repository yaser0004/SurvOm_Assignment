import io
import tarfile

import pytest

from geo_screen.download import Plan, download, extract_archive, plan_downloads
from geo_screen.fetch import Fetched
from geo_screen.models import FileInventory


def make_tar(tmp_path, names):
    tar_path = tmp_path / "archive.tar"
    with tarfile.open(tar_path, "w") as tar:
        for name in names:
            data = b"x" * 10
            info = tarfile.TarInfo(name=name)
            info.size = len(data)
            tar.addfile(info, io.BytesIO(data))
    return tar_path


def test_prefers_series_matrix_over_raw_tar():
    p = plan_downloads(
        FileInventory(
            series_supplementary=(
                ("GSE167523_Raw_gene_counts_matrix.txt.gz", 2_652_007),
                ("GSE167523_Sample_phenotype_correspondence.xlsx", 40_000),
                ("GSE167523_RAW.tar", 900_000_000),
            ),
            sample_supplementary=(),
            series_matrix=(),
            sra_links=(),
        ),
        include_raw=False,
        max_file_size=500 * 1024 * 1024,
    )
    assert p.expression == ("GSE167523_Raw_gene_counts_matrix.txt.gz",)
    assert p.metadata == ("GSE167523_Sample_phenotype_correspondence.xlsx",)
    assert p.archives == ()


def test_raw_tar_is_the_fallback_when_no_series_matrix_exists():
    p = plan_downloads(
        FileInventory(
            series_supplementary=(("GSE135251_RAW.tar", 45_854_720),),
            sample_supplementary=(),
            series_matrix=(),
            sra_links=(),
        ),
        include_raw=False,
        max_file_size=500 * 1024 * 1024,
    )
    assert p.archives == ("GSE135251_RAW.tar",)  # otherwise this dataset has no expression data


def test_archive_contents_land_in_expression_not_archives(tmp_path):
    tar = make_tar(tmp_path, ["GSM1_a.counts.txt.gz", "GSM2_b.counts.txt.gz", "readme.pdf"])
    written = extract_archive(tar, tmp_path / "expression")
    assert {p.name for p in written} == {"GSM1_a.counts.txt.gz", "GSM2_b.counts.txt.gz"}


def test_archive_path_traversal_is_refused(tmp_path):
    evil = make_tar(tmp_path, ["../../etc/passwd_counts.txt.gz"])
    with pytest.raises(tarfile.OutsideDestinationError):
        extract_archive(evil, tmp_path / "expression")
    assert not (tmp_path.parent / "etc").exists()


def test_oversized_file_skipped_with_reason():
    p = plan_downloads(
        FileInventory(series_supplementary=(("GSE1_RAW.tar", 10**10),), sample_supplementary=(), series_matrix=(), sra_links=()),
        include_raw=True,
        max_file_size=500 * 1024 * 1024,
    )
    assert p.archives == () and "exceeds max-file-size" in dict(p.skipped)["GSE1_RAW.tar"]


def test_geo_filelist_txt_is_never_mistaken_for_expression_data():
    """NCBI auto-generates filelist.txt in every series' suppl/ directory as a
    directory index. It is not itself data and must not block the RAW.tar
    fallback (GSE135251 has no other candidate expression file)."""
    p = plan_downloads(
        FileInventory(
            series_supplementary=(
                ("filelist.txt", 16384),
                ("GSE135251_RAW.tar", 46_137_344),
            ),
            sample_supplementary=(),
            series_matrix=(),
            sra_links=(),
        ),
        include_raw=False,
        max_file_size=500 * 1024 * 1024,
    )
    assert p.expression == ()
    assert "filelist.txt" not in p.metadata
    assert p.archives == ("GSE135251_RAW.tar",)


def test_plan_downloads_refuses_path_traversal_in_series_supplementary_name():
    """A filename harvested from the FTP directory listing is network input.
    Path.__truediv__ does not sanitize '..' components or absolute paths -
    Path("/a/b") / "../../etc/passwd_counts.txt.gz" escapes the intended
    directory entirely - so plan_downloads must never hand such a name to
    the expression/metadata/archives tiers."""
    p = plan_downloads(
        FileInventory(
            series_supplementary=(("../../etc/passwd_counts.txt.gz", 100),),
            sample_supplementary=(),
            series_matrix=(),
            sra_links=(),
        ),
        include_raw=False,
        max_file_size=500 * 1024 * 1024,
    )
    assert p.expression == ()
    assert p.archives == ()
    assert "unsafe filename" in dict(p.skipped)["../../etc/passwd_counts.txt.gz"]


def test_plan_downloads_refuses_absolute_path_in_series_matrix_name():
    p = plan_downloads(
        FileInventory(
            series_supplementary=(),
            sample_supplementary=(),
            series_matrix=(("/etc/cron.d/evil", 100),),
            sra_links=(),
        ),
        include_raw=False,
        max_file_size=500 * 1024 * 1024,
    )
    assert p.metadata == ()
    assert "unsafe filename" in dict(p.skipped)["/etc/cron.d/evil"]


def test_fetch_named_refuses_unsafe_name_even_if_plan_was_hand_built(tmp_path):
    """The check must hold at the point a name becomes a filesystem path,
    not only inside plan_downloads - a Plan can be constructed directly,
    bypassing that filter."""
    from geo_screen.download import _fetch_named

    class FakeClient:
        max_file_size = 500 * 1024 * 1024

        def get(self, url, dest):
            raise AssertionError("must not reach the network for an unsafe name")

    with pytest.raises(ValueError, match="unsafe"):
        _fetch_named(FakeClient(), "GSE1", "suppl", "../../etc/passwd", tmp_path, "expression")
    assert not any(tmp_path.parent.glob("**/passwd"))


def test_sra_never_planned():
    p = plan_downloads(FileInventory((), (), (), sra_links=("SRP217231",)), True, 10**12)
    assert not any("SRP" in n for n in p.expression + p.archives + p.metadata)


class FakeClient:
    def __init__(self, tmp_path):
        self.max_file_size = 500 * 1024 * 1024
        self.call_count = 0
        self._tmp_path = tmp_path

    def list_dir(self, gse, sub):
        if sub == "suppl":
            return [("GSE1_counts.txt.gz", 1000)], None
        return [], None

    def get(self, url, dest):
        self.call_count += 1
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(b"fake counts data")
        return Fetched(
            url=url, path=dest, sha256="a" * 64, size_bytes=17, retrieved_at="2026-08-13T00:00:00Z", from_cache=False
        )


def test_rerun_is_idempotent(tmp_path):
    fake_client = FakeClient(tmp_path)
    download(fake_client, "GSE1", tmp_path)
    calls_before = fake_client.call_count
    download(fake_client, "GSE1", tmp_path)
    assert fake_client.call_count == calls_before  # checksum match -> no refetch
