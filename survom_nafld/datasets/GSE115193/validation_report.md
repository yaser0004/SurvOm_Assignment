# Validation report: GSE115193

Evaluating pre-clinical models for studying NASH driven HCC.

<!-- computed -->
Sample count: 9

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 9 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 9/9 |
| source_tissue | PASS | liver-pattern source 9/9 |
| library_strategy | PASS | RNA-Seq 9/9 |
| library_source | PASS | transcriptomic 9/9 |
| library_selection | PASS | cDNA 9/9 |
| instrument_model | PASS | Illumina HiSeq 2500 9/9 |
| metadata_completeness | PASS | reported consistently: age, bmi, group, sex; not reported anywhere: diagnosis, disease, ethnicity, fibrosis_stage, nas_score, stage, steatosis_grade, tissue, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (6 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX4150293, https://www.ncbi.nlm.nih.gov/sra?term=SRX4150294, https://www.ncbi.nlm.nih.gov/sra?term=SRX4150295, https://www.ncbi.nlm.nih.gov/sra?term=SRX4150296, https://www.ncbi.nlm.nih.gov/sra?term=SRX4150297, and 4 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE115193_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX4150293, https://www.ncbi.nlm.nih.gov/sra?term=SRX4150294, https://www.ncbi.nlm.nih.gov/sra?term=SRX4150295, https://www.ncbi.nlm.nih.gov/sra?term=SRX4150296, https://www.ncbi.nlm.nih.gov/sra?term=SRX4150297, and 4 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 30 (1), 33 (1), 45 (1), 47 (2), 52 (1), 59 (1), 61 (1), 67 (1)
- **bmi**: 34.5 (1), 39.9 (1), 40.5 (1), 45.5 (1), 47.4 (1), 48.5 (1), 49.6 (1), 51.9 (1), 79.6 (1)
- **group**: NAFLD (3), NASH (3), heathy (3)
- **sex**: M (9)

## Field presence

- age: 9/9 (canon: age)
- bmi: 9/9 (canon: bmi)
- gender: 9/9 (canon: sex)
- group: 9/9 (canon: group)

## Evidence for WARN/FAIL checks

### sample_count (WARN)

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 9 samples (below 20)
<!-- /computed -->