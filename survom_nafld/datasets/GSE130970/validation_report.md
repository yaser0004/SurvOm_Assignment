# Validation report: GSE130970

Gene expression predicts histological severity and reveals distinct molecular profiles of nonalcoholic fatty liver disease

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
| instrument_model | PASS | Illumina HiSeq 2500 78/78 |
| metadata_completeness | PASS | reported consistently: age, fibrosis_stage, nas_score, sex, steatosis_grade, tissue; not reported anywhere: bmi, diagnosis, disease, ethnicity, group, stage, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (78 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE130970_all_sample_salmon_tximport_TPM_entrez_gene_ID.csv.gz |
| series_matrix | INFO | present, metadata-only (GSE130970_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX5813455, https://www.ncbi.nlm.nih.gov/sra?term=SRX5813456, https://www.ncbi.nlm.nih.gov/sra?term=SRX5813457, https://www.ncbi.nlm.nih.gov/sra?term=SRX5813458, https://www.ncbi.nlm.nih.gov/sra?term=SRX5813459, and 73 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 19 (1), 21 (1), 26 (1), 31 (2), 32 (1), 34 (2), 35 (1), 36 (1), 37 (1), 38 (2), 39 (1), 40 (1), 41 (5), 43 (3), 44 (2), 45 (2), 46 (2), 47 (1), 48 (2), 49 (2), 50 (1), 51 (1), 52 (3), 53 (6), 54 (1), 55 (4), 56 (3), 57 (3), 59 (3), 60 (3), 61 (2), 62 (1), 64 (5), 65 (3), 68 (1), 69 (1), 70 (1), 77 (1), 80 (1)
- **fibrosis_stage**: 0 (25), 1 (28), 2 (9), 3 (14), 4 (2)
- **nas_score**: 0 (4), 1 (5), 2 (9), 3 (18), 4 (16), 5 (18), 6 (8)
- **sex**: F (48), M (30)
- **steatosis_grade**: 0 (8), 1 (29), 2 (27), 3 (14)
- **tissue**: liver biopsy (78)

## Field presence

- Sex: 78/78 (canon: sex)
- age at biopsy: 78/78 (canon: age)
- cytological ballooning grade: 78/78
- fibrosis stage: 78/78 (canon: fibrosis_stage)
- lobular inflammation grade: 78/78
- nafld activity score: 78/78 (canon: nas_score)
- steatosis grade: 78/78 (canon: steatosis_grade)
- tissue: 78/78 (canon: tissue)

Decision: STRONG_CANDIDATE
<!-- /computed -->