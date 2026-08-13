"""Parse GEO `*_family.soft` text into a SoftFamily.

Pure function, no I/O. The SOFT format is line-oriented:

    ^SERIES = GSE135251
    !Series_title = ...
    ^SAMPLE = GSM3998167
    !Sample_organism_ch1 = Homo sapiens
    !Sample_characteristics_ch1 = nas score: 4
    !Sample_characteristics_ch1 = fibrosis stage: 2
    ...
    !series_matrix_table_begin
    ...data rows, not metadata...
    !series_matrix_table_end

`^` lines switch which record subsequent `!` lines belong to. `!` field
names repeat legitimately (multiple characteristics, multiple pubmed ids),
so every value is appended to a list rather than overwriting.
"""

from __future__ import annotations

from geo_screen.models import SoftFamily

_ENTITY_TARGETS = {"SERIES", "SAMPLE", "PLATFORM"}


def parse_soft(text: str) -> SoftFamily:
    series: dict[str, list[str]] = {}
    samples: dict[str, dict[str, list[str]]] = {}
    platforms: dict[str, dict[str, list[str]]] = {}
    discard: dict[str, list[str]] = {}

    current_kind = ""
    current: dict[str, list[str]] = discard
    in_table = False

    for raw_line in text.splitlines():
        line = raw_line.rstrip("\r\n")
        if not line:
            continue

        if line.startswith("!") and line.split(" ", 1)[0].endswith(
            ("_table_begin",)
        ):
            in_table = True
            continue
        if line.startswith("!") and line.split(" ", 1)[0].endswith(("_table_end",)):
            in_table = False
            continue
        if in_table:
            continue

        if line.startswith("^"):
            entity, _, rest = line[1:].partition("=")
            entity = entity.strip()
            record_id = rest.strip()
            if entity == "SERIES":
                current_kind, current = "SERIES", series
            elif entity == "SAMPLE":
                current = samples.setdefault(record_id, {})
                current_kind = "SAMPLE"
            elif entity == "PLATFORM":
                current = platforms.setdefault(record_id, {})
                current_kind = "PLATFORM"
            else:
                current_kind, current = "", discard
            continue

        if line.startswith("!"):
            field, sep, value = line[1:].partition("=")
            field = field.strip()
            value = value.strip() if sep else ""
            current.setdefault(field, []).append(value)
            continue

        # comments (#...) and anything else outside a table are ignored

    return SoftFamily(series=series, samples=samples, platforms=platforms)
