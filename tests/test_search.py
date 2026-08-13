import json
import urllib.parse

from geo_screen.fetch import GeoClient
from geo_screen.search import search, write_candidates


def _esummary_payload_for(batch):
    result = {"uids": batch}
    for uid in batch:
        result[uid] = {"accession": f"GSE{uid}", "entrytype": "GSE", "title": "t"}
    return {"result": result}


def capture_requests(client, total_uids):
    """Monkeypatches client._http_get to serve a fake esearch + esummary
    exchange and records every URL requested, so the caller can assert on
    call count/shape without touching the network."""
    esearch_payload = {"esearchresult": {"idlist": [str(i) for i in range(total_uids)]}}
    calls = []

    def fake_http_get(url):
        calls.append(url)
        if "esearch.fcgi" in url:
            return json.dumps(esearch_payload).encode()
        if "esummary.fcgi" in url:
            qs = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
            batch = qs["id"][0].split(",")
            return json.dumps(_esummary_payload_for(batch)).encode()
        raise AssertionError(f"unexpected url: {url}")

    client._http_get = fake_http_get
    return calls


def test_esummary_batches_uids(tmp_path):
    client = GeoClient(cache_dir=tmp_path)
    calls = capture_requests(client, total_uids=300)
    hits = search(client, "q", retmax=300)
    assert len(calls) == 1 + 2  # 1 esearch + 2 esummary batches of <=200
    assert len(hits) == 300
    assert all(h["entrytype"] == "GSE" for h in hits)


def test_write_candidates_produces_csv_accessions_and_manifest(tmp_path):
    hits = [{"accession": "GSE1", "title": "a", "uid": "1"}, {"accession": "GSE2", "title": "b", "uid": "2"}]
    csv_path = write_candidates(tmp_path, "NAFLD query", hits)
    assert csv_path.is_file()
    assert (tmp_path / "candidates" / "accessions.txt").read_text().splitlines() == ["GSE1", "GSE2"]
    manifest = json.loads((tmp_path / "candidates" / "search_manifest.json").read_text())
    assert manifest["hit_count"] == 2
