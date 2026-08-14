# Validation report: GSE281797

Transcriptomic profiles of liver biopsies in obese patients with metabolic dysfunction-associated steatotic liver disease

<!-- computed -->
Sample count: 94

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 94 samples |
| organism_consistency | PASS | Homo sapiens 94/94 |
| source_tissue | PASS | liver-pattern source 94/94 |
| library_strategy | PASS | RNA-Seq 94/94 |
| library_source | PASS | transcriptomic 94/94 |
| library_selection | PASS | cDNA 94/94 |
| instrument_model | PASS | Illumina NovaSeq 6000 94/94 |
| metadata_completeness | PASS | reported consistently: age, bmi, diagnosis, nas_score, sex, steatosis_grade, tissue; not reported anywhere: disease, ethnicity, fibrosis_stage, group, stage, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (94 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE281797_tpm.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE281797_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX26701090, https://www.ncbi.nlm.nih.gov/sra?term=SRX26701091, https://www.ncbi.nlm.nih.gov/sra?term=SRX26701092, https://www.ncbi.nlm.nih.gov/sra?term=SRX26701093, https://www.ncbi.nlm.nih.gov/sra?term=SRX26701094, and 89 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 20 (1), 22 (1), 24 (3), 25 (1), 26 (1), 27 (1), 28 (2), 29 (2), 31 (4), 32 (4), 33 (2), 34 (4), 35 (6), 36 (8), 37 (1), 38 (2), 39 (2), 40 (3), 41 (1), 43 (4), 44 (5), 45 (6), 46 (3), 47 (1), 48 (2), 49 (2), 50 (1), 51 (4), 52 (2), 53 (3), 54 (1), 55 (2), 56 (2), 58 (1), 59 (1), 60 (2), 64 (2), 72 (1)
- **bmi**: 29.764 (1), 29.965 (1), 30.883 (1), 32.347 (1), 33.609 (1), 34.335 (1), 34.987 (1), 35.003 (1), 35.275 (1), 35.398 (1), 35.432 (1), 35.538 (1), 35.802 (1), 35.894 (1), 35.927 (1), 36.068 (1), 36.357 (1), 36.365 (1), 36.504 (1), 36.767 (1), 36.984 (1), 37.290 (1), 37.322 (1), 37.537 (1), 37.855 (1), 37.920 (1), 37.959 (1), 38.028 (1), 38.368 (1), 38.431 (1), 38.582 (1), 38.710 (1), 39.247 (1), 39.476 (1), 39.560 (1), 39.654 (1), 39.728 (1), 39.792 (1), 39.919 (1), 40.414 (1), 41.840 (1), 41.881 (1), 41.907 (1), 42.133 (1), 42.278 (1), 42.608 (1), 42.786 (1), 42.813 (1), 42.988 (1), 43.150 (1), 43.333 (1), 43.362 (1), 43.984 (1), 44.023 (1), 44.291 (1), 44.444 (1), 44.522 (1), 44.658 (1), 44.713 (1), 44.845 (1), 44.914 (1), 45.648 (2), 46.702 (1), 46.709 (1), 46.777 (1), 46.812 (1), 47.057 (1), 47.266 (1), 47.345 (1), 47.452 (1), 47.700 (1), 48.048 (1), 48.227 (1), 48.469 (1), 48.619 (1), 48.753 (1), 49.062 (1), 49.354 (1), 50.131 (1), 50.666 (1), 51.172 (1), 51.495 (1), 51.563 (1), 51.717 (1), 52.243 (1), 52.507 (1), 53.778 (1), 54.039 (1), 54.381 (1), 54.643 (1), 54.860 (1), 54.979 (1), 56.248 (1)
- **diagnosis**: MASH (11), MASL (53), No Pathology (30)
- **nas_score**: 0 (27), 1 (16), 2 (24), 3 (11), 4 (11), 5 (2), 6 (2), 7 (1)
- **sex**: Female (70), Male (24)
- **steatosis_grade**: 0 (30), 1 (36), 2 (22), 3 (6)
- **tissue**: Liver (94)

## Field presence

- age at_biopsy: 94/94 (canon: age)
- ballooning grade: 94/94
- body mass_index: 94/94 (canon: bmi)
- diabetes: 94/94
- diagnosis: 94/94 (canon: diagnosis)
- fibrosis grade: 94/94
- gender: 94/94 (canon: sex)
- inflammation grade: 94/94
- nafld activity_score: 94/94 (canon: nas_score)
- steatosis grade: 94/94 (canon: steatosis_grade)
- tissue: 94/94 (canon: tissue)

Decision: STRONG_CANDIDATE
<!-- /computed -->