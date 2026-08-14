# Validation report: GSE193080

Transcriptome profile of liver biopsy tissues from patients with non-alcoholic fatty liver disease (tissue validation set 2).

<!-- computed -->
Sample count: 59

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 59 samples |
| organism_consistency | PASS | Homo sapiens 59/59 |
| source_tissue | PASS | liver-pattern source 59/59 |
| library_strategy | PASS | RNA-Seq 59/59 |
| library_source | PASS | transcriptomic 59/59 |
| library_selection | PASS | cDNA 59/59 |
| instrument_model | PASS | Illumina NextSeq 500 59/59 |
| metadata_completeness | PASS | reported consistently: age, fibrosis_stage, nas_score, sex, tissue; not reported anywhere: bmi, diagnosis, disease, ethnicity, group, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (59 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX13615945, https://www.ncbi.nlm.nih.gov/sra?term=SRX13615946, https://www.ncbi.nlm.nih.gov/sra?term=SRX13615947, https://www.ncbi.nlm.nih.gov/sra?term=SRX13615948, https://www.ncbi.nlm.nih.gov/sra?term=SRX13615949, and 54 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE193080_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX13615945, https://www.ncbi.nlm.nih.gov/sra?term=SRX13615946, https://www.ncbi.nlm.nih.gov/sra?term=SRX13615947, https://www.ncbi.nlm.nih.gov/sra?term=SRX13615948, https://www.ncbi.nlm.nih.gov/sra?term=SRX13615949, and 54 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 36 (1), 44 (1), 49 (1), 56 (1), 57 (2), 58 (1), 59 (2), 60 (1), 61 (1), 63 (3), 64 (1), 65 (3), 67 (1), 68 (3), 69 (4), 70 (1), 71 (1), 72 (4), 73 (1), 74 (3), 75 (3), 76 (2), 77 (5), 78 (2), 79 (5), 80 (1), 81 (1), 82 (3), 84 (1)
- **fibrosis_stage**: 0 (5), 1 (20), 2 (10), 3 (14), 4 (10)
- **nas_score**: 0 (28), 1 (9), 2 (8), 3 (8), 4 (2), 5 (3), 6 (1)
- **sex**: female (15), male (44)
- **tissue**: Liver (59)

## Field presence

- Sex: 59/59 (canon: sex)
- age: 59/59 (canon: age)
- fibrosis stage: 59/59 (canon: fibrosis_stage)
- nafld activity score: 59/59 (canon: nas_score)
- pls-nafld-based risk prediction: 59/59
- tissue: 59/59 (canon: tissue)

Decision: CANDIDATE

Unmet STRONG_CANDIDATE conditions:
- expression_data_availability not PASS
<!-- /computed -->