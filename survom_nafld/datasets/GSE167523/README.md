# GSE167523

**Title:** Transcriptome profiling of human non-alcoholic fatty liver disease
**Accession:** GSE167523
**GEO URL:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE167523
**Organism:** Homo sapiens
**Tissue:** liver biopsy
**Disease/condition:** NAFLD
**Sample count:** 98
**Platform(s):** GPL21290
**PubMed:** 34105780
**Screening decision:** STRONG_CANDIDATE

## What this dataset is

98 biopsy-proven NAFLD liver samples, bulk RNA-seq on Illumina HiSeq 3000. A separate
sample-phenotype spreadsheet ships with the series, linking each sample to its clinical record; it
is included here under `metadata/`.

## Bulk vs. single-cell determination

`single_cell_or_spatial` = **PASS** — no single-cell or spatial signal in any sample record.

## Why it is in the collection

An independent NAFLD cohort with a deliberately different metadata shape from the staged cohorts:
disease status, age, sex and tissue are reported per sample, but fibrosis stage and NAS are not.
That makes it useful as a validation cohort against the spectrum datasets rather than another
severity-annotated cohort — and it is honest about what it does not carry.

## Sample metadata at a glance

- **age**: 43 distinct values, range 18-81
- **disease**: NAFLD (98)
- **sex**: F (34), M (64)
- **tissue**: liver biopsy (98)

## Files in this folder

- `expression/GSE167523_Raw_gene_counts_matrix.txt.gz`
- `metadata/GSE167523_Sample_phenotype_correspondence.xlsx` — the study's own sample-to-phenotype map
- `metadata/GSE167523_series_matrix.txt.gz`

## Full checks and provenance

All 14 check results with their observed values: `validation_report.md`. Fetch provenance:
`source_manifest.json`. File sizes and sha256 digests: `download_manifest.json`. GEO submission date:
Feb 25 2021.
