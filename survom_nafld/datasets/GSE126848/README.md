# GSE126848

**Title:** HEPATIC TRANSCRIPTOME SIGNATURES IN PATIENTS WITH VARYING DEGREES OF NON-ALCOHOLIC FATTY LIVER DISEASE COMPARED TO HEALTHY NORMAL-WEIGHT INDIVIDUALS
**Accession:** GSE126848
**GEO URL:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE126848
**Organism:** Homo sapiens
**Tissue:** Liver (biopsy)
**Disease/condition:** healthy normal-weight / obese / NAFL / NASH (four arms)
**Sample count:** 57
**Platform(s):** GPL18573
**PubMed:** 30653341
**Screening decision:** STRONG_CANDIDATE

## What this dataset is

Liver-biopsy RNA-seq across four groups — healthy normal-weight (14), obese without NAFLD (12), NAFL
(15) and NASH (16) — on Illumina NextSeq 500, with quantitative histomorphometry of liver fat,
inflammation and fibrosis performed alongside sequencing.

## Bulk vs. single-cell determination

`single_cell_or_spatial` = **PASS** — no single-cell or spatial signal in any sample record.

## Why it is in the collection

The only dataset here that reports a healthy normal-weight control arm and an obese-without-NAFLD
control arm as separate groups. Every other selected dataset compares severity within a
NAFLD-spectrum cohort, so this is the collection's only way to separate the effect of obesity itself
from the effect of NAFLD/NASH — the comparison the assignment brief gives as its own first example.
The study's finding is that normal-weight and obese controls have comparable liver transcriptomes,
both distinct from NAFL and NASH.

It carries no fibrosis or NAS staging: its contribution is the control-arm design, not depth of
severity annotation.

## Sample metadata at a glance

- **disease**: NAFLD (15), NASH (16), healthy (14), obese (12)
- **sex**: Female (10), Male (47)
- **tissue**: Liver (57)

## Files in this folder

- `expression/GSE126848_Gene_counts_raw.txt.gz`
- `metadata/GSE126848_series_matrix.txt.gz`

## Full checks and provenance

All 14 check results with their observed values: `validation_report.md`. Fetch provenance:
`source_manifest.json`. File sizes and sha256 digests: `download_manifest.json`. GEO submission date:
Feb 21 2019.
