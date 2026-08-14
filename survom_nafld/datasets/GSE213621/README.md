# GSE213621

**Title:** Hepatocyte Smoothened Activity Controls Susceptibility to Insulin Resistance and Nonalcoholic Fatty Liver Disease [RNA-Seq]
**Accession:** GSE213621
**GEO URL:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE213621
**Organism:** Homo sapiens
**Tissue:** liver (hepatocyte-containing biopsy/resection material)
**Disease/condition:** NAFLD / insulin resistance, fibrosis staged per sample
**Sample count:** 368
**Platform(s):** GPL16791
**PubMed:** 36535507
**Screening decision:** MANUAL_REVIEW (included after manual resolution, see below)

## What this dataset is

368 human liver samples from controls and NAFLD patients, bulk RNA-seq on Illumina HiSeq 2500,
examining how hepatocyte Smoothened signalling relates to insulin resistance, inflammation and
fibrosis.

**This is the human SubSeries of a mixed-species study.** `series_metadata.json` records
`relations: "SubSeries of: GSE213623"`. The parent SuperSeries also covers mouse work, including
mouse single-cell RNA-seq; none of that material is in GSE213621, whose 368 samples are all
`Homo sapiens` and all `library_strategy = RNA-Seq`.

## Bulk vs. single-cell determination

`single_cell_or_spatial` = **WARN** — the series-level prose mentions single-cell work, but no
individual sample record corroborates it. That prose describes the SuperSeries' mouse component;
every one of the 368 sample records here is bulk RNA-seq with no single-cell platform, tool or file
format anywhere in its metadata.

## Why it is in the collection

The largest cohort in the collection at 368 samples, with fibrosis staged across four levels
including a control group. (One larger series in the screened pool, `GSE267145` at 508 samples, is a
human/mouse mixed-organism series left unresolved — see the top-level README.)

It reaches the collection through a manual decision rather than an automatic promotion. Two checks
flagged it: `metadata_completeness`, because the series records staging under the raw key
`fibrotic stage` rather than the more common `fibrosis stage`; and `disease_relevance`, because the
sample records carry staging and `liver cells` without naming NAFLD, which the series title does.
The first is a naming variant covering all 368 samples, the second is exactly the sample-level
versus series-level distinction `MANUAL_REVIEW` exists to surface. Neither undermines the data, so
the dataset was included on its size and its genuine per-sample fibrosis staging.

## Sample metadata at a glance

- **fibrosis_stage**: Control (69), F0F1 (97), F2 (107), F3F4 (95)

Note that age, sex, BMI, NAS and diagnosis are not reported for this series — the fibrosis stage is
the phenotype it carries.

## Files in this folder

- `expression/GSE213621_FPKMs_allsamples.txt.gz` — FPKM matrix, 368 sample columns
- `metadata/GSE213621_series_matrix.txt.gz`

## Full checks and provenance

All 14 check results with their observed values: `validation_report.md`. Fetch provenance:
`source_manifest.json`. File sizes and sha256 digests: `download_manifest.json`. GEO submission date:
Sep 19 2022.
