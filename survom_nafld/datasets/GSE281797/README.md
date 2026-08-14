# GSE281797

**Title:** Transcriptomic profiles of liver biopsies in obese patients with metabolic dysfunction-associated steatotic liver disease
**Accession:** GSE281797
**GEO URL:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE281797
**Organism:** Homo sapiens
**Tissue:** liver biopsy
**Disease/condition:** MASLD in obesity: no pathology (30) / MASL (53) / MASH (11)
**Sample count:** 94
**Platform(s):** GPL24676
**PubMed:** 41870035
**Screening decision:** STRONG_CANDIDATE

## What this dataset is

94 liver biopsy transcriptomes deposited in GSE281797, from obese patients spanning no liver
pathology through early MASLD and MASH; bulk RNA-seq on Illumina NovaSeq 6000. The associated study
recruited a larger clinical cohort and combined transcriptomics with metabolomics — 94 is the number
of liver transcriptomes deposited here, not the size of the recruited cohort.

## Bulk vs. single-cell determination

`single_cell_or_spatial` = **PASS** — no single-cell or spatial signal in any sample record.

## Why it is in the collection

The rest of the collection samples established disease and its severity gradient. This one sits at
the no-pathology-to-early-disease end in an obese population, with diagnosis, steatosis
grade, fibrosis stage, NAS, age, BMI and sex all recorded per sample. It is the collection's
coverage of the at-risk and early-disease end of the spectrum.

## Sample metadata at a glance

- **age**: 38 distinct values, range 20-72
- **bmi**: reported for 94/94, range 29.8-56.2
- **diagnosis**: MASH (11), MASL (53), No Pathology (30)
- **fibrosis_stage**: 0 (42), 1 (26), 2 (20), 3 (6)
- **nas_score**: 0 (27), 1 (16), 2 (24), 3 (11), 4 (11), 5 (2), 6 (2), 7 (1)
- **sex**: Female (70), Male (24)
- **steatosis_grade**: 0 (30), 1 (36), 2 (22), 3 (6)
- **tissue**: Liver (94)

Fibrosis staging is recorded under the raw key `fibrosis grade`; the tool maps that to
`fibrosis_stage`, and both the raw and canonical forms are visible in `sample_metadata.csv`.

## Files in this folder

- `expression/GSE281797_tpm.txt.gz`
- `metadata/GSE281797_series_matrix.txt.gz`

## Full checks and provenance

All 14 check results with their observed values: `validation_report.md`. Fetch provenance:
`source_manifest.json`. File sizes and sha256 digests: `download_manifest.json`. GEO submission date:
Nov 13 2024.
