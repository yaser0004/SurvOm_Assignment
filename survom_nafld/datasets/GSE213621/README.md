# GSE213621

**Title:** Hepatocyte Smoothened Activity Controls Susceptibility to Insulin Resistance and Nonalcoholic Fatty Liver Disease [RNA-Seq]
**Accession:** GSE213621
**GEO URL:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE213621
**Organism:** Homo sapiens
**Tissue:** liver (hepatocyte-containing biopsy/resection material)
**Disease/condition:** NAFLD / insulin resistance, with fibrosis staged per sample (e.g. F2)
**Sample count:** 368
**Platform(s):** GPL16791
**PubMed:** 36535507
**Screening decision:** MANUAL_REVIEW

## Experimental design

368-sample human liver cohort investigating hepatocyte Smoothened signalling in insulin resistance and NAFLD; bulk RNA-seq on Illumina HiSeq 2500.

## Bulk vs. single-cell determination

`single_cell_or_spatial` = **WARN** — series prose mentions single-cell; sample metadata does not corroborate

## Technical checks

| check | status | observed |
|---|---|---|
| sample_count | PASS | 368 samples |
| organism_consistency | PASS | Homo sapiens 368/368 |
| source_tissue | PASS | liver-pattern source 368/368 |
| library_strategy | PASS | RNA-Seq 368/368 |
| library_source | PASS | transcriptomic 368/368 |
| library_selection | PASS | cDNA 368/368 |
| instrument_model | PASS | Illumina HiSeq 2500 368/368 |
| metadata_completeness | PASS | reported consistently: fibrosis_stage; not reported anywhere: age, bmi, diagnosis, disease, ethnicity, group, nas_score, sex, stage, steatosis_grade, tissue, treatment |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | WARN | series prose mentions single-cell; sample metadata does not corroborate |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE213621_FPKMs_allsamples.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE213621_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX17623649, https://www.ncbi.nlm.nih.gov/sra?term=SRX17623650, https://www.ncbi.nlm.nih.gov/sra?term=SRX17623651, https://www.ncbi.nlm.nih.gov/sra?term=SRX17623652, https://www.ncbi.nlm.nih.gov/sra?term=SRX17623653, and 363 more (see sample_metadata.csv) |

## Metadata summary (canonical field distributions)

- **fibrosis_stage**: Control (69), F0F1 (97), F2 (107), F3F4 (95)

## Expression data files

| file | tier | bytes | sha256 |
|---|---|---|---|
| GSE213621_FPKMs_allsamples.txt.gz | expression | 33224068 | `ccd861c61a7f1f2d...` |
| GSE213621_series_matrix.txt.gz | metadata | 11880 | `aa9f7b6771080832...` |

## Selection rationale

The largest cohort in the entire 200-candidate screening pool - larger even than the flagship GSE135251. Initially landed on MANUAL_REVIEW because its samples record disease relevance only through fibrosis staging (raw key 'fibrotic stage', not the more common 'fibrosis stage') and the series title mentions single-cell work in background prose that no sample corroborates. Both were resolved by hand: (1) the 'fibrotic stage' synonym was added to the tool's canonical-field mapping after confirming it appears on all 368 samples (this also reclassified 2 other datasets in the pool - see the top-level README); (2) every sample's own library_strategy is RNA-Seq with no structural single-cell signal anywhere in sample metadata, so the single-cell mention is confirmed to be background prose about other work, not this series' own assay. Included as a human-reviewed addition specifically for its size and fibrosis staging.

## Provenance

Screened and downloaded via `geo_screen`. Full source manifest: `source_manifest.json`. Full download manifest: `download_manifest.json`. Submission date: Sep 19 2022.
