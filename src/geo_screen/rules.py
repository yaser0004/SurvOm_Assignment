"""Rule table for geo_screen — DATA ONLY, no logic.

Every regex pattern, field list, and threshold that drives screening lives
here so the generated README's criteria section (render_criteria_markdown
in report.py) can be built straight from this module instead of drifting
from whatever checks.py actually does.

Sample-level evidence outranks series prose everywhere: both
SINGLE_CELL_SIGNALS and NON_TISSUE_SIGNALS are split into a "structural"
tier (GSM fields — what was actually sequenced) and a "textual" tier
(Series_title/summary/overall_design — background prose, often about other
people's methods or the paper's own discussion). A structural hit is
high-confidence; a textual-only hit is not.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class Signal:
    id: str
    pattern: str
    fields: tuple[str, ...]
    tier: Literal["structural", "textual"]
    note: str


SINGLE_CELL_SIGNALS: tuple[Signal, ...] = (
    Signal(
        id="single_cell_protocol",
        pattern=(
            r"10x|10X Genomics|Chromium|cellranger|cell ?ranger|STARsolo|"
            r"Seurat|Scanpy|alevin|Drop-?seq|Smart-?seq|single cells were|"
            r"single[- ]cell (suspension|capture|controller|library)|"
            r"single[- ]nucle(us|i)|nuclei (were )?isolat|snRNA|scRNA|"
            r"CITE-seq|Visium|GeoMx|MERFISH|spatial transcriptom"
        ),
        fields=(
            "Sample_extract_protocol_ch1",
            "Sample_data_processing",
            "Sample_library_strategy",
            "Sample_title",
            "Sample_source_name_ch1",
        ),
        tier="structural",
        note="cell-resolved protocol or processing tool named in sample metadata",
    ),
    Signal(
        id="single_cell_supplementary_filename",
        pattern=(
            r"matrix\.mtx|barcodes\.tsv|features\.tsv|genes\.tsv|"
            r"filtered_feature_bc_matrix|\.h5ad|\.loom|tissue_positions"
        ),
        fields=("Sample_supplementary_file", "Series_supplementary_file"),
        tier="structural",
        note="single-cell/spatial file format in a supplementary filename",
    ),
    Signal(
        id="single_cell_series_prose",
        pattern=r"single[- ]cell|single[- ]nucle|spatial transcriptom",
        fields=("Series_summary", "Series_overall_design", "Series_title"),
        tier="textual",
        note=(
            "series free text mentions single-cell/spatial work; bulk papers "
            "routinely discuss it in background without using it themselves"
        ),
    ),
)

NON_TISSUE_SIGNALS: tuple[Signal, ...] = (
    Signal(
        id="non_tissue_sample_metadata",
        pattern=(
            r"HepG2|Huh-?7|HuH-?7|Hep3B|HepaRG|\bL02\b|LX-2|AML12|THP-1|"
            r"EA\.?hy926|cell line|organoid|spheroid|iPSC|hiPSC|"
            r"pluripotent stem cell|in vitro|cultured (primary )?hepatocyte"
        ),
        fields=(
            "Sample_source_name_ch1",
            "Sample_title",
            "Sample_characteristics_ch1",
        ),
        tier="structural",
        note="sample metadata itself names a cell line, culture, or in vitro model",
    ),
    Signal(
        id="non_tissue_series_prose",
        pattern=(
            r"HepG2|Huh-?7|HuH-?7|Hep3B|HepaRG|\bL02\b|LX-2|AML12|THP-1|"
            r"EA\.?hy926|cell line|organoid|spheroid|iPSC|hiPSC|"
            r"pluripotent stem cell|in vitro|cultured (primary )?hepatocyte"
        ),
        fields=("Series_title", "Series_summary", "Series_overall_design"),
        tier="textual",
        note="series prose mentions a cell/culture term; sample metadata does not corroborate",
    ),
)

LIVER_SOURCE_PATTERN = r"liver|hepatic|biopsy|hepatocyte"
LIVER_SOURCE_FIELDS = ("Sample_source_name_ch1", "Sample_characteristics_ch1")

OFF_TARGET_TISSUE_SIGNALS: tuple[Signal, ...] = (
    Signal(
        id="off_target_tissue",
        pattern=(
            r"adipose|visceral fat|subcutaneous fat|skeletal muscle|\bPBMC\b|"
            r"whole blood|serum|plasma|intestin|colon|kidney|pancrea|"
            r"tumou?r adjacent normal"
        ),
        fields=("Sample_source_name_ch1", "Sample_characteristics_ch1"),
        tier="structural",
        note="sample source names tissue outside the liver-disease target",
    ),
)

DISEASE_TERMS: tuple[str, ...] = (
    "NAFLD",
    "MASLD",
    "NASH",
    "MASH",
    "non-alcoholic fatty liver",
    "nonalcoholic fatty liver",
    "metabolic dysfunction-associated stea",
    "steatohepatitis",
    "steatosis",
    "fatty liver",
    "fibrosis stage",
    "NAS score",
    "NAFLD activity score",
    "Kleiner",
)

# canonical -> synonyms (matched case-insensitively after stripping non-alphanumerics)
CANONICAL_FIELDS: dict[str, tuple[str, ...]] = {
    "diagnosis": ("diagnosis", "histological diagnosis", "patient diagnosis"),
    "disease": (
        "disease",
        "disease state",
        "condition",
        "phenotype",
        "dx",
        "non-alcoholic fatty_liver_disease_(nafld)",
    ),
    "group": ("group", "group in paper", "cohort", "study group", "comparison group"),
    "stage": ("stage", "disease stage", "severity"),
    "fibrosis_stage": (
        "fibrosis stage",
        "fibrosis",
        "kleiner fibrosis",
        "fibrosis score",
        "f stage",
        "fibrotic stage",
        "fibrosisscore",
        "fibrosis grade",
    ),
    "steatosis_grade": ("steatosis", "steatosis grade", "steatosis score"),
    "nas_score": ("nas", "nas score", "nafld activity score", "activity score"),
    "treatment": ("treatment", "drug", "agent", "intervention"),
    "tissue": ("tissue", "tissue type", "organ", "source", "sample type"),
    "sex": ("sex", "gender"),
    "age": ("age", "age at biopsy", "age years"),
    "bmi": ("bmi", "body mass index"),
    "ethnicity": ("ethnicity", "race"),
}

# canonical fields whose presence indicates the series reports a disease/diagnosis axis
DISEASE_ISH_CANONICAL_FIELDS = frozenset(
    {"disease", "diagnosis", "group", "stage", "fibrosis_stage", "nas_score", "steatosis_grade"}
)

BULK_STRATEGIES: frozenset[str] = frozenset({"RNA-Seq"})

STRONG_MIN_SAMPLES = 20
STRONG_SOURCE_FRACTION = 0.95
