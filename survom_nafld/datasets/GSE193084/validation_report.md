# Validation report: GSE193084

Transcriptome profile of liver biopsy tissues from patients with non-alcoholic fatty liver disease

<!-- computed -->
Sample count: 271

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 271 samples |
| organism_consistency | PASS | Homo sapiens 271/271 |
| source_tissue | PASS | liver-pattern source 271/271 |
| library_strategy | PASS | RNA-Seq 271/271 |
| library_source | PASS | transcriptomic 271/271 |
| library_selection | PASS | cDNA 271/271 |
| instrument_model | PASS | Illumina NextSeq 500 271/271 |
| metadata_completeness | PASS | reported consistently: age, fibrosis_stage, nas_score, sex, tissue; not reported anywhere: bmi, diagnosis, disease, ethnicity, group, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (271 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX13586670, https://www.ncbi.nlm.nih.gov/sra?term=SRX13586671, https://www.ncbi.nlm.nih.gov/sra?term=SRX13586672, https://www.ncbi.nlm.nih.gov/sra?term=SRX13586673, https://www.ncbi.nlm.nih.gov/sra?term=SRX13586674, and 266 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE193084_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX13586670, https://www.ncbi.nlm.nih.gov/sra?term=SRX13586671, https://www.ncbi.nlm.nih.gov/sra?term=SRX13586672, https://www.ncbi.nlm.nih.gov/sra?term=SRX13586673, https://www.ncbi.nlm.nih.gov/sra?term=SRX13586674, and 266 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 20 (2), 23 (1), 31 (5), 32 (2), 33 (4), 34 (1), 35 (2), 36 (3), 37 (5), 38 (3), 39 (3), 40 (2), 41 (3), 42 (3), 43 (3), 44 (4), 45 (2), 46 (6), 47 (3), 48 (6), 49 (3), 50 (5), 51 (6), 52 (1), 53 (4), 54 (4), 55 (6), 56 (2), 57 (8), 58 (4), 59 (8), 60 (6), 61 (7), 62 (10), 63 (13), 64 (8), 65 (7), 66 (5), 67 (3), 68 (6), 69 (8), 70 (3), 71 (9), 72 (6), 73 (8), 74 (13), 75 (9), 76 (6), 77 (9), 78 (4), 79 (7), 80 (3), 81 (1), 82 (3), 83 (1), 84 (2)
- **fibrosis_stage**: 0 (12), 1 (66), 2 (84), 3 (71), 4 (38)
- **nas_score**: 0 (29), 1 (17), 2 (28), 3 (91), 4 (45), 5 (34), 6 (14), 7 (11), 8 (2)
- **sex**: female (116), male (155)
- **tissue**: Liver (271)

## Field presence

- Sex: 271/271 (canon: sex)
- age: 271/271 (canon: age)
- biopsy: 164/271
- fibrosis stage: 271/271 (canon: fibrosis_stage)
- nafld activity score: 271/271 (canon: nas_score)
- pls-nafld-based risk prediction: 107/271
- pls-nafld-based risk prediction at 1st biopsy: 164/271
- tissue: 271/271 (canon: tissue)

Decision: CANDIDATE

Unmet STRONG_CANDIDATE conditions:
- expression_data_availability not PASS
<!-- /computed -->