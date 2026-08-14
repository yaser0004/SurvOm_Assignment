# GSE162694

**Title:** Molecular Characterization and Cell Type Composition Deconvolution of Fibrosis in NAFLD
**Accession:** GSE162694
**GEO URL:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE162694
**Organism:** Homo sapiens
**Tissue:** liver
**Disease/condition:** NASH, fibrosis staged F0-F4, plus an explicit 'normal liver histology' group
**Sample count:** 143
**Platform(s):** GPL21290
**PubMed:** 34508113
**Screening decision:** STRONG_CANDIDATE

## What this dataset is

A 143-sample cross-sectional NASH cohort profiled by bulk RNA-seq on Illumina HiSeq 3000. The study
deconvolves the bulk signal into estimated cell-type composition across fibrosis stages; the
single-cell data it uses for that are external reference datasets, not part of this series.

## Bulk vs. single-cell determination

`single_cell_or_spatial` = **PASS** — no single-cell or spatial signal in any sample record.

## Why it is in the collection

The third-largest cohort here, after GSE213621 and GSE135251, and the one whose stated purpose is an
analytical angle rather than a case-control contrast: relating fibrosis stage to shifts in cell-type
composition. It also carries an explicit normal-liver-histology group (31 samples) alongside the
staged ones, so a histologically normal comparison is available inside the same cohort.

## Sample metadata at a glance

- **age**: 45 distinct values, range 18-72
- **fibrosis_stage**: 0 (35), 1 (30), 2 (27), 3 (8), 4 (12), normal liver histology (31)
- **nas_score**: 0 (32), 1 (12), 2 (9), 3 (11), 4 (13), 5 (19), 6 (12), 7 (9), NA (26)
- **sex**: Female (103), Male (40)
- **tissue**: Liver (143)

## Files in this folder

- `expression/GSE162694_raw_counts.csv.gz`
- `metadata/GSE162694_series_matrix.txt.gz`

## Full checks and provenance

All 14 check results with their observed values: `validation_report.md`. Fetch provenance:
`source_manifest.json`. File sizes and sha256 digests: `download_manifest.json`. GEO submission date:
Dec 04 2020.
