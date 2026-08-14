# Validation report: GSE185051

Hepatic Transcriptome Profiling of A Multiethnic Cohort of Pediatric Non-Alcoholic Fatty Liver Disease Patients Reveals Novel Genes and Pathways Associated With Disease Stages

<!-- computed -->
Sample count: 57

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 57 samples |
| organism_consistency | PASS | Homo sapiens 57/57 |
| source_tissue | PASS | liver-pattern source 57/57 |
| library_strategy | PASS | RNA-Seq 57/57 |
| library_source | PASS | transcriptomic 57/57 |
| library_selection | PASS | cDNA 57/57 |
| instrument_model | PASS | Illumina NovaSeq 6000 57/57 |
| metadata_completeness | PASS | reported consistently: age, disease, fibrosis_stage, nas_score, sex; not reported anywhere: bmi, diagnosis, ethnicity, group, stage, steatosis_grade, tissue, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (57 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX12411586, https://www.ncbi.nlm.nih.gov/sra?term=SRX12411587, https://www.ncbi.nlm.nih.gov/sra?term=SRX12411588, https://www.ncbi.nlm.nih.gov/sra?term=SRX12411589, https://www.ncbi.nlm.nih.gov/sra?term=SRX12411590, and 52 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE185051_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX12411586, https://www.ncbi.nlm.nih.gov/sra?term=SRX12411587, https://www.ncbi.nlm.nih.gov/sra?term=SRX12411588, https://www.ncbi.nlm.nih.gov/sra?term=SRX12411589, https://www.ncbi.nlm.nih.gov/sra?term=SRX12411590, and 52 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 10 (3), 11 (8), 12 (3), 13 (6), 14 (6), 15 (6), 16 (4), 17 (8), 18 (1), 19 (1), 20 (1), 36 (1), 37 (1), 41 (1), 55 (1), 68 (1), 9 (5)
- **disease**: NAFLD disease (52), Normal (5)
- **fibrosis_stage**: 0 (11), 1 (37), 2 (4), 3 (5)
- **nas_score**: 0 (7), 1 (2), 2 (1), 3 (10), 4 (19), 5 (12), 6 (5), 7 (1)
- **sex**: F (25), M (32)

## Field presence

- age: 57/57 (canon: age)
- disease: 57/57 (canon: disease)
- fibrosis_stage: 57/57 (canon: fibrosis_stage)
- gender: 57/57 (canon: sex)
- nas: 57/57 (canon: nas_score)
- nash_status: 57/57

Decision: CANDIDATE

Unmet STRONG_CANDIDATE conditions:
- expression_data_availability not PASS
<!-- /computed -->