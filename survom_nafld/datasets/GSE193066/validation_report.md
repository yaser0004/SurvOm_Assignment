# Validation report: GSE193066

Transcriptome profile of liver biopsy tissues from patients with non-alcoholic fatty liver disease (tissue validation set 1).

<!-- computed -->
Sample count: 164

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 164 samples |
| organism_consistency | PASS | Homo sapiens 164/164 |
| source_tissue | PASS | liver-pattern source 164/164 |
| library_strategy | PASS | RNA-Seq 164/164 |
| library_source | PASS | transcriptomic 164/164 |
| library_selection | PASS | cDNA 164/164 |
| instrument_model | PASS | Illumina NextSeq 500 164/164 |
| metadata_completeness | PASS | reported consistently: age, fibrosis_stage, nas_score, sex, tissue; not reported anywhere: bmi, diagnosis, disease, ethnicity, group, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (164 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX13614022, https://www.ncbi.nlm.nih.gov/sra?term=SRX13614023, https://www.ncbi.nlm.nih.gov/sra?term=SRX13614024, https://www.ncbi.nlm.nih.gov/sra?term=SRX13614025, https://www.ncbi.nlm.nih.gov/sra?term=SRX13614026, and 159 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE193066_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX13614022, https://www.ncbi.nlm.nih.gov/sra?term=SRX13614023, https://www.ncbi.nlm.nih.gov/sra?term=SRX13614024, https://www.ncbi.nlm.nih.gov/sra?term=SRX13614025, https://www.ncbi.nlm.nih.gov/sra?term=SRX13614026, and 159 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 20 (2), 23 (1), 31 (5), 32 (2), 33 (4), 34 (1), 35 (2), 36 (2), 37 (5), 38 (3), 39 (3), 40 (2), 41 (3), 42 (3), 43 (3), 44 (3), 45 (2), 46 (6), 47 (3), 48 (6), 49 (2), 50 (5), 51 (6), 52 (1), 53 (4), 54 (4), 55 (6), 57 (6), 58 (3), 59 (6), 60 (5), 61 (5), 62 (9), 63 (7), 64 (5), 65 (3), 66 (2), 68 (1), 69 (3), 71 (5), 73 (4), 74 (3), 75 (4), 76 (1), 77 (1), 79 (1), 83 (1)
- **fibrosis_stage**: 0 (6), 1 (45), 2 (71), 3 (41), 4 (1)
- **nas_score**: 1 (4), 2 (10), 3 (71), 4 (34), 5 (20), 6 (12), 7 (11), 8 (2)
- **sex**: female (69), male (95)
- **tissue**: Liver (164)

## Field presence

- Sex: 164/164 (canon: sex)
- age: 164/164 (canon: age)
- biopsy: 164/164
- fibrosis stage: 164/164 (canon: fibrosis_stage)
- nafld activity score: 164/164 (canon: nas_score)
- pls-nafld-based risk prediction at 1st biopsy: 164/164
- tissue: 164/164 (canon: tissue)

Decision: CANDIDATE

Unmet STRONG_CANDIDATE conditions:
- expression_data_availability not PASS
<!-- /computed -->