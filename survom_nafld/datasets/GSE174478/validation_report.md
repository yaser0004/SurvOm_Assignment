# Validation report: GSE174478

Whole transcriptome profiling of Japanese  nonalcoholic fatty liver disease cohort.

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
| metadata_completeness | PASS | reported consistently: age, disease, fibrosis_stage, nas_score, sex, tissue; not reported anywhere: bmi, diagnosis, ethnicity, group, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (94 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE174478_raw_gene_counts_matrix.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE174478_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX10894433, https://www.ncbi.nlm.nih.gov/sra?term=SRX10894434, https://www.ncbi.nlm.nih.gov/sra?term=SRX10894435, https://www.ncbi.nlm.nih.gov/sra?term=SRX10894436, https://www.ncbi.nlm.nih.gov/sra?term=SRX10894437, and 89 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 19 (1), 25 (2), 27 (2), 31 (1), 32 (1), 33 (1), 34 (2), 35 (4), 36 (1), 37 (1), 38 (1), 40 (1), 42 (3), 44 (4), 45 (1), 46 (1), 47 (2), 48 (2), 49 (2), 50 (2), 51 (6), 52 (1), 53 (3), 54 (3), 56 (1), 57 (2), 58 (3), 59 (2), 60 (2), 61 (2), 63 (1), 64 (1), 65 (1), 66 (4), 67 (2), 68 (8), 69 (1), 70 (2), 71 (1), 72 (1), 73 (1), 74 (1), 75 (2), 76 (2), 77 (1), 83 (2), 85 (1), 87 (1), 92 (1)
- **disease**: NAFLD (94)
- **fibrosis_stage**: 0 (7), 1 (29), 2 (23), 3 (24), 4 (11)
- **nas_score**: 1 (1), 2 (11), 3 (9), 4 (17), 5 (36), 6 (17), 7 (3)
- **sex**: F (45), M (49)
- **tissue**: liver (94)

## Field presence

- Sex: 94/94 (canon: sex)
- age: 94/94 (canon: age)
- disease state: 94/94 (canon: disease)
- fibrosis stage: 94/94 (canon: fibrosis_stage)
- nafld activity score: 94/94 (canon: nas_score)
- tissue: 94/94 (canon: tissue)

Decision: STRONG_CANDIDATE
<!-- /computed -->