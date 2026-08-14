# Validation report: GSE192959

Transcriptome profile of liver biopsy tissues from patients with non-alcoholic fatty liver disease (derivation set).

<!-- computed -->
Sample count: 48

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 48 samples |
| organism_consistency | PASS | Homo sapiens 48/48 |
| source_tissue | PASS | liver-pattern source 48/48 |
| library_strategy | PASS | RNA-Seq 48/48 |
| library_source | PASS | transcriptomic 48/48 |
| library_selection | PASS | cDNA 48/48 |
| instrument_model | PASS | Illumina NextSeq 500 48/48 |
| metadata_completeness | PASS | reported consistently: age, fibrosis_stage, nas_score, sex, tissue; not reported anywhere: bmi, diagnosis, disease, ethnicity, group, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (48 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX13586670, https://www.ncbi.nlm.nih.gov/sra?term=SRX13586671, https://www.ncbi.nlm.nih.gov/sra?term=SRX13586672, https://www.ncbi.nlm.nih.gov/sra?term=SRX13586673, https://www.ncbi.nlm.nih.gov/sra?term=SRX13586674, and 43 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE192959_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX13586670, https://www.ncbi.nlm.nih.gov/sra?term=SRX13586671, https://www.ncbi.nlm.nih.gov/sra?term=SRX13586672, https://www.ncbi.nlm.nih.gov/sra?term=SRX13586673, https://www.ncbi.nlm.nih.gov/sra?term=SRX13586674, and 43 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 56 (1), 61 (1), 62 (1), 63 (3), 64 (2), 65 (1), 66 (3), 67 (2), 68 (2), 69 (1), 70 (2), 71 (3), 72 (2), 73 (3), 74 (7), 75 (2), 76 (3), 77 (3), 78 (2), 79 (1), 80 (2), 84 (1)
- **fibrosis_stage**: 0 (1), 1 (1), 2 (3), 3 (16), 4 (27)
- **nas_score**: 0 (1), 1 (4), 2 (10), 3 (12), 4 (9), 5 (11), 6 (1)
- **sex**: female (32), male (16)
- **tissue**: Liver (48)

## Field presence

- Sex: 48/48 (canon: sex)
- age: 48/48 (canon: age)
- fibrosis stage: 48/48 (canon: fibrosis_stage)
- nafld activity score: 48/48 (canon: nas_score)
- pls-nafld-based risk prediction: 48/48
- tissue: 48/48 (canon: tissue)

Decision: CANDIDATE

Unmet STRONG_CANDIDATE conditions:
- expression_data_availability not PASS
<!-- /computed -->