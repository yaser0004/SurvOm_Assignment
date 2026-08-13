"""HTTP fetch layer: on-disk cache, provenance, and GEO-specific endpoints.

Every network call in the tool goes through GeoClient so caching, rate
limiting, and provenance capture happen in exactly one place. Screening
never downloads bulk expression data through this client — it only fetches
SOFT family text and small directory listings; download.py is the only
caller that pulls large files.
"""

from __future__ import annotations

import gzip
import hashlib
import logging
import os
import re
import time
from dataclasses import dataclass, replace
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logger = logging.getLogger(__name__)

_ACCESSION_RE = re.compile(r"^GSE\d+$")

FTP_BASE = "https://ftp.ncbi.nlm.nih.gov/geo/series"
ACC_CGI = "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi"


class FileTooLargeError(Exception):
    """Raised when a fetch would exceed the client's max_file_size."""


def validate_accession(value: str) -> str:
    """The only accession validator in the codebase. Raises ValueError on anything
    that is not exactly `GSE` followed by digits — untrusted input (argv, file
    lines, search results) must pass through here before it reaches a URL."""
    candidate = value.strip()
    if not _ACCESSION_RE.match(candidate):
        raise ValueError(f"invalid GEO series accession: {value!r}")
    return candidate


def _series_bucket(gse: str) -> str:
    digits = gse[3:]
    prefix = digits[:-3] if len(digits) > 3 else ""
    return f"GSE{prefix}nnn"


def ftp_series_url(gse: str, sub: str, name: str = "") -> str:
    gse = validate_accession(gse)
    bucket = _series_bucket(gse)
    url = f"{FTP_BASE}/{bucket}/{gse}/{sub}/"
    if name:
        url += name
    return url


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


@dataclass(frozen=True)
class Fetched:
    url: str
    path: Path
    sha256: str
    size_bytes: int
    retrieved_at: str
    from_cache: bool


_SIZE_SUFFIX = {"K": 1024, "M": 1024**2, "G": 1024**3}


def _parse_listing_size(token: str) -> int:
    token = token.strip()
    if not token or token == "-":
        return 0
    match = re.match(r"^([\d.]+)\s*([KMG]?)$", token, re.IGNORECASE)
    if not match:
        return 0
    value, suffix = match.groups()
    try:
        number = float(value)
    except ValueError:
        return 0
    return int(number * _SIZE_SUFFIX.get(suffix.upper(), 1))


_ANCHOR_RE = re.compile(
    r'<a href="([^"?][^"]*)"[^>]*>.*?</a>\s*[\d\-]{2}[\-A-Za-z]*[\d\-]*\s+[\d:]*\s*([\d.]*[KMG]?)\s*$',
    re.IGNORECASE,
)


class GeoClient:
    def __init__(
        self,
        cache_dir: Path,
        offline: bool = False,
        api_key: str | None = None,
        timeout: float = 60.0,
        max_file_size: int = 500 * 1024 * 1024,
    ) -> None:
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.offline = offline
        self.api_key = api_key
        self.timeout = timeout
        self.max_file_size = max_file_size
        self._session = self._build_session()
        self._last_request_at = 0.0

    def _build_session(self) -> requests.Session:
        session = requests.Session()
        retry = Retry(
            total=4,
            backoff_factor=1.5,
            status_forcelist=[429, 500, 502, 503, 504],
            respect_retry_after_header=True,
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        session.headers["User-Agent"] = (
            "geo-screen/0.1 (NAFLD transcriptomics screening tool; "
            "auditable research CLI, not a bot scraper)"
        )
        return session

    def _rate_limit(self) -> None:
        min_interval = 1 / 10 if self.api_key else 1 / 3
        elapsed = time.monotonic() - self._last_request_at
        if elapsed < min_interval:
            time.sleep(min_interval - elapsed)
        self._last_request_at = time.monotonic()

    def _http_get(self, url: str) -> bytes:
        params = {"api_key": self.api_key} if self.api_key and "eutils" in url else None
        # HTTPAdapter's Retry only covers status codes / connection setup; a
        # connection reset mid-body-read (large FTP files in particular)
        # surfaces as ChunkedEncodingError *after* a 200 response, so it needs
        # its own bounded retry here rather than relying on the adapter.
        last_error: Exception | None = None
        for attempt in range(3):
            self._rate_limit()
            try:
                response = self._session.get(url, timeout=self.timeout, params=params)
                response.raise_for_status()
                return response.content
            except requests.exceptions.ChunkedEncodingError as exc:
                last_error = exc
                logger.warning("body read failed for %s (attempt %d/3): %s", url, attempt + 1, exc)
                time.sleep(1.5 * (attempt + 1))
        raise last_error  # type: ignore[misc]

    def _cache_path(self, url: str) -> Path:
        digest = hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]
        basename = Path(urlparse(url).path.rstrip("/")).name or "index"
        return self.cache_dir / f"{digest}_{basename}"

    def _fetch_bytes(self, url: str) -> tuple[bytes, Fetched]:
        cache_path = self._cache_path(url)
        if cache_path.exists():
            data = cache_path.read_bytes()
            from_cache = True
        elif self.offline:
            raise FileNotFoundError(f"offline mode: not cached: {url}")
        else:
            data = self._http_get(url)
            if len(data) > self.max_file_size:
                raise FileTooLargeError(
                    f"{url} exceeds max-file-size ({len(data)} > {self.max_file_size} bytes)"
                )
            part = cache_path.with_name(cache_path.name + ".part")
            part.write_bytes(data)
            os.replace(part, cache_path)
            from_cache = False

        fetched = Fetched(
            url=url,
            path=cache_path,
            sha256=hashlib.sha256(data).hexdigest(),
            size_bytes=len(data),
            retrieved_at=_utc_now_iso(),
            from_cache=from_cache,
        )
        return data, fetched

    def get(self, url: str, dest: Path) -> Fetched:
        data, fetched = self._fetch_bytes(url)
        dest = Path(dest)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        return replace(fetched, path=dest)

    def get_text(self, url: str) -> tuple[str, Fetched]:
        data, fetched = self._fetch_bytes(url)
        return data.decode("utf-8", errors="replace"), fetched

    def soft_family(self, gse: str) -> tuple[str, Fetched]:
        gse = validate_accession(gse)
        url = ftp_series_url(gse, "soft", f"{gse}_family.soft.gz")
        try:
            data, fetched = self._fetch_bytes(url)
            return gzip.decompress(data).decode("utf-8", errors="replace"), fetched
        except requests.HTTPError as exc:
            if exc.response is not None and exc.response.status_code == 404:
                logger.warning("FTP family SOFT missing for %s, falling back to acc.cgi", gse)
                return self._soft_family_via_acc_cgi(gse)
            raise

    def _soft_family_via_acc_cgi(self, gse: str) -> tuple[str, Fetched]:
        series_url = f"{ACC_CGI}?acc={gse}&targ=self&form=text&view=brief"
        samples_url = f"{ACC_CGI}?acc={gse}&targ=gsm&form=text&view=brief"
        series_text, series_fetched = self.get_text(series_url)
        samples_text, _ = self.get_text(samples_url)
        combined = series_text + "\n" + samples_text
        return combined, series_fetched

    def list_dir(self, gse: str, sub: str) -> tuple[list[tuple[str, int]], Fetched]:
        gse = validate_accession(gse)
        url = ftp_series_url(gse, sub)
        try:
            html, fetched = self.get_text(url)
        except (requests.RequestException, FileNotFoundError, FileTooLargeError) as exc:
            logger.warning("could not list %s for %s: %s", sub, gse, exc)
            empty = Fetched(
                url=url, path=self.cache_dir, sha256="", size_bytes=0,
                retrieved_at=_utc_now_iso(), from_cache=False,
            )
            return [], empty

        entries: list[tuple[str, int]] = []
        for line in html.splitlines():
            match = _ANCHOR_RE.search(line)
            if not match:
                continue
            name, size_token = match.groups()
            if name in ("../", "/"):
                continue
            entries.append((name, _parse_listing_size(size_token)))
        return entries, fetched
