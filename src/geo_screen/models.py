"""Shared data types for geo_screen.

Grows one dataclass/enum per task as the pipeline gains stages
(SoftFamily -> checks -> classification -> reports). Kept in one module
so every stage imports from the same place instead of each other.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


@dataclass(frozen=True)
class SoftFamily:
    """Parsed contents of a GEO `*_family.soft` file.

    Keys are the SOFT field names verbatim (e.g. "Series_title",
    "Sample_organism_ch1") so every value in a report traces back to the
    exact line it came from. Values are lists because SOFT fields legitimately
    repeat (multiple Series_summary paragraphs, multiple
    Sample_characteristics_ch1 lines).
    """

    series: dict[str, list[str]]
    samples: dict[str, dict[str, list[str]]]
    platforms: dict[str, dict[str, list[str]]]

    @property
    def accession(self) -> str:
        values = self.series.get("Series_geo_accession", [])
        if not values:
            raise ValueError("SoftFamily has no Series_geo_accession")
        return values[0]


class Status(StrEnum):
    PASS = "PASS"
    WARN = "WARN"
    FAIL = "FAIL"
    INFO = "INFO"


@dataclass(frozen=True)
class Evidence:
    accession: str
    field: str
    matched: str
    snippet: str  # truncated to <= 200 chars


@dataclass(frozen=True)
class CheckResult:
    id: str
    label: str
    status: Status
    observed: str
    evidence: tuple[Evidence, ...] = ()


class Decision(StrEnum):
    STRONG_CANDIDATE = "STRONG_CANDIDATE"
    CANDIDATE = "CANDIDATE"
    MANUAL_REVIEW = "MANUAL_REVIEW"
    REJECT = "REJECT"


@dataclass(frozen=True)
class Verdict:
    decision: Decision
    reasons: tuple[str, ...]
    unmet_strong: tuple[str, ...]


@dataclass(frozen=True)
class SummaryRecord:
    accession: str
    title: str
    organism: str
    n_samples: int
    source_summary: str
    library_strategy: str
    single_cell_flag: str
    material_flag: str
    disease_terms_found: str
    expression_files: str
    decision: str
    top_reason: str


@dataclass(frozen=True)
class FileInventory:
    """Supplementary/matrix files known for a series, gathered from SOFT
    fields and (when available) an FTP directory listing. Consumed by both
    checks.py (screening, no download) and download.py (tiered fetch)."""

    series_supplementary: tuple[tuple[str, int], ...] = ()
    sample_supplementary: tuple[str, ...] = ()
    series_matrix: tuple[tuple[str, int], ...] = ()
    sra_links: tuple[str, ...] = ()
