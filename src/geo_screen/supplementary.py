"""Parse the supplementary-file table off a GEO Series record page.

GEO's esummary `suppfile` field is a series-level roll-up of file types, not a
per-file type: GSE135251 ships one file, `GSE135251_RAW.tar`, and esummary
reports `TXT` because the tar's members are text. The Series record page is the
only GEO surface that states a type per file, in a table whose columns are
`Supplementary file | Size | Download | File type/resource`, where that same
file reads `TAR (of TXT)`.

This module reads that table and nothing else. Type strings are carried through
verbatim; no type is derived from a filename, an extension or a title. Rows
below the file rows (`SRA Run Selector`, `Raw data are available in SRA`) are
relations and status, not files, and come back separately so the two never get
conflated.

Pure functions over a string, so the tests run offline against saved pages.
"""

from __future__ import annotations

import html
import re
from dataclasses import dataclass

HEADER_CELLS = ("Supplementary file", "Size", "Download", "File type/resource")

# Set when GEO lists a file but leaves its type cell empty.
TYPE_UNSPECIFIED = "Not specified by GEO"

_TABLE_OPEN = "<table"
_TABLE_CLOSE = "</table>"
_ROW_RE = re.compile(r"<tr[^>]*>(.*?)</tr>", re.IGNORECASE | re.DOTALL)
# Captures the cell's attributes as well as its content: GEO puts the exact
# byte count in the size cell's title attribute, alongside the rounded text.
_CELL_RE = re.compile(r"<td([^>]*)>(.*?)</td>", re.IGNORECASE | re.DOTALL)
_TAG_RE = re.compile(r"<[^>]+>")
_TITLE_RE = re.compile(r'\btitle="(\d+)"', re.IGNORECASE)
_HREF_RE = re.compile(r'href="([^"]+)"', re.IGNORECASE)


@dataclass(frozen=True)
class SupplementaryFile:
    """One row of the GEO table, as GEO states it."""

    filename: str
    file_type: str
    size: str
    size_bytes: str
    download_url: str


def _text(cell_html: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(_TAG_RE.sub("", cell_html))).strip()


def _table_containing(page: str, needle: str) -> str | None:
    index = page.find(needle)
    if index < 0:
        return None
    start = page.rfind(_TABLE_OPEN, 0, index)
    end = page.find(_TABLE_CLOSE, index)
    if start < 0 or end < 0:
        return None
    return page[start : end + len(_TABLE_CLOSE)]


def _download_url(cell_html: str) -> str:
    """Prefer the FTP href GEO gives per file; fall back to its download path.

    A `_RAW.tar` row carries only the /geo/download/ link, so there is no FTP
    URL to take. Relative paths are made absolute against the GEO host rather
    than rewritten.
    """
    hrefs = [html.unescape(h) for h in _HREF_RE.findall(cell_html)]
    for href in hrefs:
        if href.startswith("ftp://"):
            return href
    for href in hrefs:
        if href.startswith("/"):
            return f"https://www.ncbi.nlm.nih.gov{href}"
        if href.startswith("http"):
            return href
    return ""


def parse_series_page(page: str) -> tuple[list[SupplementaryFile], list[str]]:
    """Return (supplementary files, raw-data status notes) for a Series page.

    Both lists are empty when the page carries no supplementary-file table,
    which is how GEO represents a series with no supplementary files.
    """
    table = _table_containing(page, f"<strong>{HEADER_CELLS[0]}</strong>")
    if table is None:
        return [], []

    files: list[SupplementaryFile] = []
    notes: list[str] = []
    for row_html in _ROW_RE.findall(table):
        parsed = _CELL_RE.findall(row_html)
        cells = [_text(inner) for _, inner in parsed]
        if not any(cells):
            continue
        if len(cells) != len(HEADER_CELLS):
            notes.append(" ".join(c for c in cells if c))
            continue
        if tuple(cells) == HEADER_CELLS:
            continue  # the header itself

        size_attrs, _ = parsed[1]
        size_bytes = _TITLE_RE.search(size_attrs)
        files.append(
            SupplementaryFile(
                filename=cells[0],
                file_type=cells[3] or TYPE_UNSPECIFIED,
                size=cells[1],
                size_bytes=size_bytes.group(1) if size_bytes else "",
                download_url=_download_url(parsed[2][1]),
            )
        )
    return files, notes


def format_files(files: list[SupplementaryFile]) -> str:
    """`name [GEO type]; name [GEO type]`, page order preserved."""
    return "; ".join(f"{f.filename} [{f.file_type}]" for f in files)
