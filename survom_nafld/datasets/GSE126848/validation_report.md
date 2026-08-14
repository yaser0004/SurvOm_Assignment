# Validation report: GSE126848

HEPATIC TRANSCRIPTOME SIGNATURES IN PATIENTS WITH VARYING DEGREES OF NON-ALCOHOLIC FATTY LIVER DISEASE COMPARED TO HEALTHY NORMAL-WEIGHT INDIVIDUALS

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
| instrument_model | PASS | Illumina NextSeq 500 57/57 |
| metadata_completeness | PASS | reported consistently: disease, sex, tissue; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (31 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE126848_Gene_counts_raw.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE126848_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX5401534, https://www.ncbi.nlm.nih.gov/sra?term=SRX5401535, https://www.ncbi.nlm.nih.gov/sra?term=SRX5401536, https://www.ncbi.nlm.nih.gov/sra?term=SRX5401537, https://www.ncbi.nlm.nih.gov/sra?term=SRX5401538, and 52 more (see sample_metadata.csv) |

## Canonical field distributions

- **disease**: NAFLD (15), NASH (16), healthy (14), obese (12)
- **sex**: Female (10), Male (47)
- **tissue**: Liver (57)

## Field presence

- disease: 57/57 (canon: disease)
- gender: 57/57 (canon: sex)
- tissue: 57/57 (canon: tissue)

Decision: STRONG_CANDIDATE
<!-- /computed -->