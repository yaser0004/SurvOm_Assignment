# Validation report: GSE276114

Integrative proteo-transcriptomic characterization of advanced fibrosis in chronic liver disease across etiologies

<!-- computed -->
Sample count: 177

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 177 samples |
| organism_consistency | PASS | Homo sapiens 177/177 |
| source_tissue | PASS | liver-pattern source 177/177 |
| library_strategy | PASS | RNA-Seq 177/177 |
| library_source | PASS | transcriptomic 177/177 |
| library_selection | PASS | cDNA 177/177 |
| instrument_model | PASS | Illumina NovaSeq 6000 177/177 |
| metadata_completeness | PASS | reported consistently: disease, tissue; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (81 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX25923107, https://www.ncbi.nlm.nih.gov/sra?term=SRX25923108, https://www.ncbi.nlm.nih.gov/sra?term=SRX25923109, https://www.ncbi.nlm.nih.gov/sra?term=SRX25923110, https://www.ncbi.nlm.nih.gov/sra?term=SRX25923111, and 172 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE276114_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX25923107, https://www.ncbi.nlm.nih.gov/sra?term=SRX25923108, https://www.ncbi.nlm.nih.gov/sra?term=SRX25923109, https://www.ncbi.nlm.nih.gov/sra?term=SRX25923110, https://www.ncbi.nlm.nih.gov/sra?term=SRX25923111, and 172 more (see sample_metadata.csv) |

## Canonical field distributions

- **disease**: ARLD (14), CVH (82), MASLD (81)
- **tissue**: liver (177)

## Field presence

- disease: 177/177 (canon: disease)
- disease group: 177/177
- tissue: 177/177 (canon: tissue)

Decision: CANDIDATE

Unmet STRONG_CANDIDATE conditions:
- expression_data_availability not PASS
<!-- /computed -->