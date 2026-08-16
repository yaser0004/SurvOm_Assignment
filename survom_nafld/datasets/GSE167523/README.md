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
**Experimental design:** Snap-frozen liver tissue from 98 patients with biopsy-proven NAFLD, with no control arm in the sample records. The cohort splits into NAFL (51) and NASH (47), and fibrosis stage is not reported.

## What this dataset is

98 biopsy-proven NAFLD liver samples, bulk RNA-seq on Illumina HiSeq 3000. A separate
sample-phenotype spreadsheet ships with the series, linking each sample to its clinical record; it
is included here under `metadata/`.

## Bulk vs. single-cell determination

`single_cell_or_spatial` = **PASS** — no single-cell or spatial signal in any sample record.

## Why it is in the collection

An independent NAFLD cohort whose metadata has a different shape from the staged cohorts: disease
status, age, sex and tissue are reported per sample, while fibrosis stage and NAS are not reported
at all. It is a Japanese cohort — GEO gives the submitter's country as Japan, and the linked
publication (PMID 34105780) states that the 98 patients sequenced here were biopsied at Sendai Kousei
Hospital — making it the second Japanese cohort in the collection alongside GSE174478. It was selected on that basis: it provides an independent unstaged cohort for comparison
with the staged datasets, rather than another staged cohort.

## Sample metadata at a glance

- **age**: 43 distinct values, range 18-81
- **disease**: NAFLD (98)
- **sex**: F (34), M (64)
- **tissue**: liver biopsy (98)

## Known data quirk: duplicate feature labels

The matrix has 26,364 data rows but 26,362 distinct feature labels — `1-Mar` and `2-Mar` each
appear twice, on rows carrying different values (the two `1-Mar` rows sum to 95,770 and 10,762
across the 98 samples). Both are feature labels represented in a date-like form; what each
originally denoted is not recoverable from this file. Because the paired rows differ, collapsing
them by label would lose data. The file is shipped exactly as GEO serves it; downstream work needs
a deliberate policy for these two labels rather than letting a lookup hit whichever row comes
first.

## Files in this folder

- `expression/GSE167523_Raw_gene_counts_matrix.txt.gz`
- `metadata/GSE167523_Sample_phenotype_correspondence.xlsx` — the study's own sample-to-phenotype map
- `metadata/GSE167523_series_matrix.txt.gz`

## Full checks and provenance

All 14 check results with their observed values: `validation_report.md`. Fetch provenance:
`source_manifest.json`. File sizes and sha256 digests: `download_manifest.json`. GEO submission date:
Feb 25 2021.
