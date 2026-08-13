import pytest

from geo_screen.fetch import GeoClient, ftp_series_url


def test_ftp_url_nnn_bucketing():
    assert ftp_series_url("GSE135251", "soft", "GSE135251_family.soft.gz").endswith(
        "/geo/series/GSE135nnn/GSE135251/soft/GSE135251_family.soft.gz"
    )
    assert "/GSE1nnn/GSE1234/" in ftp_series_url("GSE1234", "suppl")
    assert "/GSEnnn/GSE123/" in ftp_series_url("GSE123", "suppl")


def test_cache_hit_serves_offline_and_keeps_checksum(tmp_path, monkeypatch):
    client = GeoClient(cache_dir=tmp_path, offline=False)
    monkeypatch.setattr(client, "_http_get", lambda url: b"payload")
    first = client.get_text("https://example/x")[1]
    offline = GeoClient(cache_dir=tmp_path, offline=True)
    second = offline.get_text("https://example/x")[1]
    assert second.from_cache and second.sha256 == first.sha256


def test_offline_miss_raises_not_silently_empty(tmp_path):
    with pytest.raises(FileNotFoundError):
        GeoClient(cache_dir=tmp_path, offline=True).get_text("https://example/missing")


def test_bad_accession_rejected():
    for bad in ["GDS1234", "GSE", "gse135251; rm -rf /", "../etc"]:
        with pytest.raises(ValueError):
            ftp_series_url(bad, "soft")


def test_chunked_encoding_error_mid_body_is_retried(tmp_path, monkeypatch):
    """A connection reset mid-download (large FTP files) surfaces as
    ChunkedEncodingError *after* headers already returned 200 - the
    status-code-based Retry adapter never sees it, so _http_get needs its
    own retry."""
    import requests

    client = GeoClient(cache_dir=tmp_path)
    attempts = []

    class FakeResponse:
        def raise_for_status(self):
            pass

        @property
        def content(self):
            attempts.append(1)
            if len(attempts) < 2:
                raise requests.exceptions.ChunkedEncodingError("boom")
            return b"full payload"

    monkeypatch.setattr(client._session, "get", lambda *a, **k: FakeResponse())
    text, fetched = client.get_text("https://example/big-file")
    assert text == "full payload"
    assert len(attempts) == 2


def test_oversized_fetch_refused_before_writing_to_cache(tmp_path, monkeypatch):
    client = GeoClient(cache_dir=tmp_path, offline=False, max_file_size=10)
    monkeypatch.setattr(client, "_http_get", lambda url: b"x" * 100)
    from geo_screen.fetch import FileTooLargeError

    with pytest.raises(FileTooLargeError):
        client.get_text("https://example/big")
    assert list(tmp_path.iterdir()) == []
