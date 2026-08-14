# Validation report: GSE214435

Disseminative Recurrence Signature for hepatocellular carcinoma from non-alcoholic fatty liver disease

<!-- computed -->
Sample count: 104

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 104 samples |
| organism_consistency | PASS | Homo sapiens 104/104 |
| source_tissue | PASS | liver-pattern source 104/104 |
| library_strategy | PASS | RNA-Seq 104/104 |
| library_source | PASS | transcriptomic 104/104 |
| library_selection | PASS | cDNA 104/104 |
| instrument_model | PASS | Illumina NextSeq 500 104/104 |
| metadata_completeness | WARN | patchy fields: fibrosis_stage 59/104, nas_score 59/104. reported consistently: age, sex, tissue; not reported anywhere: bmi, diagnosis, disease, ethnicity, group, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (59 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX13615945, https://www.ncbi.nlm.nih.gov/sra?term=SRX13615946, https://www.ncbi.nlm.nih.gov/sra?term=SRX13615947, https://www.ncbi.nlm.nih.gov/sra?term=SRX13615948, https://www.ncbi.nlm.nih.gov/sra?term=SRX13615949, and 99 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE214435_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX13615945, https://www.ncbi.nlm.nih.gov/sra?term=SRX13615946, https://www.ncbi.nlm.nih.gov/sra?term=SRX13615947, https://www.ncbi.nlm.nih.gov/sra?term=SRX13615948, https://www.ncbi.nlm.nih.gov/sra?term=SRX13615949, and 99 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 36 (1), 44 (1), 49 (1), 56 (1), 57 (4), 58 (2), 59 (4), 60 (1), 61 (1), 63 (5), 64 (2), 65 (7), 67 (2), 68 (5), 69 (7), 70 (2), 71 (1), 72 (6), 73 (1), 74 (4), 75 (6), 76 (4), 77 (11), 78 (3), 79 (10), 80 (2), 81 (2), 82 (6), 84 (2)
- **fibrosis_stage**: 0 (5), 1 (20), 2 (10), 3 (14), 4 (10)
- **nas_score**: 0 (28), 1 (9), 2 (8), 3 (8), 4 (2), 5 (3), 6 (1)
- **sex**: Female (9), Male (36), female (15), male (44)
- **tissue**: Liver (104)

## Field presence

- Sex: 104/104 (canon: sex)
- age: 104/104 (canon: age)
- fibrosis stage: 59/104 (canon: fibrosis_stage)
- nafld activity score: 59/104 (canon: nas_score)
- pls-nafld-based risk prediction: 59/104
- recurrence: 45/104
- tissue: 104/104 (canon: tissue)

## Evidence for WARN/FAIL checks

### metadata_completeness (WARN)

Decision: MANUAL_REVIEW

Reasons:
- metadata_completeness: patchy fields: fibrosis_stage 59/104, nas_score 59/104. reported consistently: age, sex, tissue; not reported anywhere: bmi, diagnosis, disease, ethnicity, group, stage, steatosis_grade, treatment
<!-- /computed -->