"""Characteristics parsing and metadata normalisation.

GEO characteristics arrive as free-text "key: value" strings with no fixed
schema and inconsistent casing between series (`disease: NAFLD` next to
`Stage: early`). This module splits them into (key, value) pairs, discovers
which fields a given series actually reports, and maps known synonyms onto
a small set of canonical columns — without ever discarding the original
raw key, so a report always shows exactly what GEO said.
"""

from __future__ import annotations

import re

from geo_screen.models import SoftFamily
from geo_screen.rules import CANONICAL_FIELDS


def _normalize_key(raw_key: str) -> str:
    lowered = raw_key.strip().lower()
    collapsed = re.sub(r"[^a-z0-9]+", " ", lowered)
    return collapsed.strip()


_SYNONYM_TO_CANONICAL: dict[str, str] = {
    _normalize_key(synonym): canonical
    for canonical, synonyms in CANONICAL_FIELDS.items()
    for synonym in synonyms
}


def canonical_key(raw_key: str) -> str | None:
    return _SYNONYM_TO_CANONICAL.get(_normalize_key(raw_key))


def parse_characteristics(values: list[str]) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    for index, raw in enumerate(values, start=1):
        key, sep, value = raw.partition(":")
        if sep:
            pairs.append((key.strip(), value.strip()))
        else:
            pairs.append((f"characteristics_{index}", raw.strip()))
    return pairs


def _sample_characteristics(fam: SoftFamily, gsm: str) -> list[tuple[str, str]]:
    values = fam.samples[gsm].get("Sample_characteristics_ch1", [])
    return parse_characteristics(values)


def discover_fields(fam: SoftFamily) -> dict[str, int]:
    """Raw characteristic key -> number of samples that report it."""
    counts: dict[str, int] = {}
    for gsm in fam.samples:
        seen_this_sample = {key for key, _ in _sample_characteristics(fam, gsm)}
        for key in seen_this_sample:
            counts[key] = counts.get(key, 0) + 1
    return counts


def field_report(fam: SoftFamily) -> dict[str, dict[str, object]]:
    """Raw characteristic key -> presence count, total samples, canonical mapping."""
    total = len(fam.samples)
    counts = discover_fields(fam)
    return {
        raw_key: {
            "present": present,
            "total": total,
            "canonical": canonical_key(raw_key),
        }
        for raw_key, present in counts.items()
    }


_ROW_SAMPLE_FIELDS = {
    "title": "Sample_title",
    "organism": "Sample_organism_ch1",
    "source_name": "Sample_source_name_ch1",
    "molecule": "Sample_molecule_ch1",
    "library_strategy": "Sample_library_strategy",
    "library_source": "Sample_library_source",
    "library_selection": "Sample_library_selection",
    "instrument_model": "Sample_instrument_model",
    "platform_id": "Sample_platform_id",
    "sample_type": "Sample_type",
}


def _join(values: list[str]) -> str:
    return " | ".join(v for v in values if v)


def _supplementary_files(sample_fields: dict[str, list[str]]) -> str:
    names = [
        value
        for key, values in sample_fields.items()
        if key.startswith("Sample_supplementary_file")
        for value in values
        if value and value != "NONE"
    ]
    return _join(names)


def _sra_relation(sample_fields: dict[str, list[str]]) -> str:
    relations = sample_fields.get("Sample_relation", [])
    sra = [r.split(":", 1)[1].strip() for r in relations if r.lower().startswith("sra:")]
    return _join(sra)


def sample_rows(fam: SoftFamily) -> list[dict[str, str]]:
    all_raw_keys: set[str] = set()
    all_canonical_keys: set[str] = set()
    for gsm in fam.samples:
        for key, _ in _sample_characteristics(fam, gsm):
            all_raw_keys.add(key)
            canon = canonical_key(key)
            if canon:
                all_canonical_keys.add(canon)

    rows: list[dict[str, str]] = []
    for gsm, sample_fields in fam.samples.items():
        row: dict[str, str] = {"gsm": gsm}
        for column, soft_field in _ROW_SAMPLE_FIELDS.items():
            row[column] = _join(sample_fields.get(soft_field, []))
        row["supplementary_files"] = _supplementary_files(sample_fields)
        row["sra_relation"] = _sra_relation(sample_fields)

        pairs = _sample_characteristics(fam, gsm)
        by_raw_key: dict[str, list[str]] = {}
        for key, value in pairs:
            by_raw_key.setdefault(key, []).append(value)

        canon_values: dict[str, list[str]] = {}
        for key, values in by_raw_key.items():
            canon = canonical_key(key)
            if canon:
                canon_values.setdefault(canon, []).extend(values)

        for canon in sorted(all_canonical_keys):
            row[f"canon__{canon}"] = _join(canon_values.get(canon, []))
        for raw_key in sorted(all_raw_keys):
            row[f"raw__{raw_key}"] = _join(by_raw_key.get(raw_key, []))

        rows.append(row)

    return rows
