# Validation report: GSE150026

Effects of Tesamorelin on Hepatic Transcriptomic Signatures in HIV-Associated NAFLD

<!-- computed -->
Sample count: 78

## Checks

| id | status | observed |
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

## Canonical field distributions

- **diagnosis**: HIV with NAFLD (78)
- **tissue**: liver (78)
- **treatment**: PLACEBO (42), TESAMORELIN (36)

## Field presence

- participant: 78/78
- patient diagnosis: 78/78 (canon: diagnosis)
- timepoint: 78/78
- tissue: 78/78 (canon: tissue)
- treatment: 78/78 (canon: treatment)

Decision: STRONG_CANDIDATE
<!-- /computed -->