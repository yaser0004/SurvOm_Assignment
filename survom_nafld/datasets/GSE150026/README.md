# GSE150026

**Title:** Effects of Tesamorelin on Hepatic Transcriptomic Signatures in HIV-Associated NAFLD
**Accession:** GSE150026
**GEO URL:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE150026
**Organism:** Homo sapiens
**Tissue:** liver
**Disease/condition:** HIV-associated NAFLD (all 78 samples); randomized placebo vs. Tesamorelin arms
**Sample count:** 78
**Platform(s):** GPL24676
**PubMed:** 32701508, 34006921
**Screening decision:** STRONG_CANDIDATE

## Experimental design

Randomized placebo-controlled trial of Tesamorelin in HIV-associated NAFLD, 78 liver samples (42 placebo, 36 Tesamorelin); bulk RNA-seq.

## Bulk vs. single-cell determination

`single_cell_or_spatial` = **PASS** — no single-cell/spatial signal detected

## Technical checks

| check | status | observed |
|---|---|---|
| sample_count | PASS | 78 samples |
| organism_consistency | PASS | Homo sapiens 78/78 |
| source_tissue | PASS | liver-pattern source 78/78 |
| library_strategy | PASS | RNA-Seq 78/78 |
| library_source | PASS | transcriptomic 78/78 |
| library_selection | PASS | cDNA 78/78 |
| instrument_model | PASS | Illumina NovaSeq 6000 78/78 |
| metadata_completeness | PASS | reported consistently: diagnosis, tissue, treatment; not reported anywhere: age, bmi, disease, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (78 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE150026_normalizedReadCounts.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE150026_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX8286842, https://www.ncbi.nlm.nih.gov/sra?term=SRX8286843, https://www.ncbi.nlm.nih.gov/sra?term=SRX8286844, https://www.ncbi.nlm.nih.gov/sra?term=SRX8286845, https://www.ncbi.nlm.nih.gov/sra?term=SRX8286846, and 73 more (see sample_metadata.csv) |

## Metadata summary (canonical field distributions)

- **diagnosis**: HIV with NAFLD (78)
- **tissue**: liver (78)
- **treatment**: PLACEBO (42), TESAMORELIN (36)

## Expression data files

| file | tier | bytes | sha256 |
|---|---|---|---|
| GSE150026_normalizedReadCounts.txt.gz | expression | 14876744 | `5b39ecdf6bc7dfb6...` |
| GSE150026_series_matrix.txt.gz | metadata | 6794 | `c32f07c35d810fab...` |

## Selection rationale

The only interventional trial design in the collection and the only dataset focused on a specific comorbid population (HIV-associated NAFLD, a clinically distinct and more aggressive disease course per the study's own summary). Every other selected dataset is an observational cross-sectional cohort; this adds a treatment-response angle and a population not represented elsewhere in the collection.

## Provenance

Screened and downloaded via `geo_screen`. Full source manifest: `source_manifest.json`. Full download manifest: `download_manifest.json`. Submission date: May 07 2020.
