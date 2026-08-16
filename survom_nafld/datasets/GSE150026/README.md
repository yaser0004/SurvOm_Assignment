# GSE150026

**Title:** Effects of Tesamorelin on Hepatic Transcriptomic Signatures in HIV-Associated NAFLD
**Accession:** GSE150026
**GEO URL:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE150026
**Organism:** Homo sapiens
**Tissue:** liver
**Disease/condition:** HIV-associated NAFLD; randomized placebo vs. tesamorelin
**Sample count:** 78 biopsy samples from 39 participants
**Platform(s):** GPL24676
**PubMed:** 32701508, 34006921
**Screening decision:** STRONG_CANDIDATE
**Experimental design:** Randomized placebo-controlled trial with paired liver biopsies at baseline and 12 months, tesamorelin (n=18) against placebo (n=21). The 78 samples come from 39 participants contributing two timepoints each.

## What this dataset is

A randomized placebo-controlled trial of tesamorelin in HIV-associated NAFLD, with paired liver
biopsies taken at baseline and at 12 months. Bulk RNA-seq on Illumina NovaSeq 6000.

**78 samples is not 78 participants.** `sample_metadata.csv` carries `raw__participant` and
`raw__timepoint` for every sample: 39 distinct participants, each contributing two timepoints — 21
in the placebo arm (42 samples) and 18 in the tesamorelin arm (36 samples). Any per-subject analysis
has to group by `raw__participant` rather than treating the rows as independent.

## Bulk vs. single-cell determination

`single_cell_or_spatial` = **PASS** — no single-cell or spatial signal in any sample record.

## Why it is in the collection

The only interventional design here, and the only distinct comorbid population — HIV-associated
NAFLD, which the study describes as following a more aggressive course. Every other selected dataset
is a cross-sectional observational cohort, so this is the only one carrying a treatment arm and
paired within-subject sampling over time.

## Sample metadata at a glance

- **diagnosis**: HIV with NAFLD (78)
- **tissue**: liver (78)
- **treatment**: PLACEBO (42 samples / 21 participants), TESAMORELIN (36 samples / 18 participants)
- **participant / timepoint** (raw fields): 39 participants x 2 timepoints

Fibrosis stage, NAS, age, sex and BMI are not reported in this series' GEO metadata.

## Files in this folder

- `expression/GSE150026_normalizedReadCounts.txt.gz`
- `metadata/GSE150026_series_matrix.txt.gz`

## Full checks and provenance

All 14 check results with their observed values: `validation_report.md`. Fetch provenance:
`source_manifest.json`. File sizes and sha256 digests: `download_manifest.json`. GEO submission date:
May 07 2020.
