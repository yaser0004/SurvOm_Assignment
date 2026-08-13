"""GEO candidate discovery via NCBI E-utilities (db=gds).

Two requests per query regardless of hit count (up to 500): one esearch for
UIDs, then esummary in batches of <=200 UIDs (the documented NCBI cap).
Screening reads candidates.csv/accessions.txt written here; it never calls
esearch/esummary itself.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

import csv

from geo_screen import __version__
from geo_screen.fetch import GeoClient

EUTILS_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
_ESUMMARY_BATCH = 200


def search(client: GeoClient, query: str, retmax: int = 500) -> list[dict[str, object]]:
    esearch_url = f"{EUTILS_BASE}/esearch.fcgi?db=gds&retmax={retmax}&retmode=json&term={quote(query)}"
    text, _ = client.get_text(esearch_url)
    uids = json.loads(text).get("esearchresult", {}).get("idlist", [])

    hits: list[dict[str, object]] = []
    for start in range(0, len(uids), _ESUMMARY_BATCH):
        batch = uids[start : start + _ESUMMARY_BATCH]
        esummary_url = f"{EUTILS_BASE}/esummary.fcgi?db=gds&retmode=json&id={','.join(batch)}"
        text, _ = client.get_text(esummary_url)
        result = json.loads(text).get("result", {})
        for uid in result.get("uids", []):
            item = result.get(uid, {})
            if item.get("entrytype") == "GSE":
                item = {**item, "uid": uid}
                hits.append(item)
    return hits


_CANDIDATE_FIELDS = ["accession", "title", "taxon", "gdstype", "n_samples", "suppfile", "pdat", "uid"]


def write_candidates(out: Path, query: str, hits: list[dict[str, object]]) -> Path:
    candidates_dir = Path(out) / "candidates"
    candidates_dir.mkdir(parents=True, exist_ok=True)

    csv_path = candidates_dir / "candidates.csv"
    accessions: list[str] = []
    with csv_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=_CANDIDATE_FIELDS, restval="", extrasaction="ignore")
        writer.writeheader()
        for hit in hits:
            accession = str(hit.get("accession", "")).strip()
            if not accession:
                continue
            accessions.append(accession)
            writer.writerow(hit)

    accessions_text = "\n".join(accessions)
    (candidates_dir / "accessions.txt").write_text(accessions_text + "\n" if accessions else "")

    manifest = {
        "query": query,
        "hit_count": len(hits),
        "accession_count": len(accessions),
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "tool_version": __version__,
    }
    (candidates_dir / "search_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True))

    return csv_path
