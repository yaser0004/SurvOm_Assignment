# Validation report: GSE267032

Bulk White Blood Cells in MAFLD/MASH

<!-- computed -->
Sample count: 35

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 35 samples |
| organism_consistency | PASS | Homo sapiens 35/35 |
| source_tissue | WARN | liver-pattern source 0/35 |
| library_strategy | PASS | RNA-Seq 35/35 |
| library_source | PASS | transcriptomic 35/35 |
| library_selection | PASS | cDNA 35/35 |
| instrument_model | PASS | Illumina NovaSeq 6000 35/35 |
| metadata_completeness | PASS | reported consistently: disease, nas_score, sex, tissue; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (21 sample(s)) |
| single_cell_or_spatial | WARN | series prose mentions single cell; sample metadata does not corroborate |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE267032_counts_RNASeq_WBC_bulk.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE267032_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX24499405, https://www.ncbi.nlm.nih.gov/sra?term=SRX24499406, https://www.ncbi.nlm.nih.gov/sra?term=SRX24499407, https://www.ncbi.nlm.nih.gov/sra?term=SRX24499408, https://www.ncbi.nlm.nih.gov/sra?term=SRX24499409, and 30 more (see sample_metadata.csv) |

## Canonical field distributions

- **disease**: Control | 0_healthy (14), MAFLD/MASH | 1_low (8), MAFLD/MASH | 2_medium (6), MAFLD/MASH | 3_high (7)
- **nas_score**: 0 (2), 1 (4), 2 (2), 3 (3), 4 (3), 5 (2), 6 (4), 8 (1), n/a (14)
- **sex**: female (18), male (17)
- **tissue**: White blood cells (35)

## Field presence

- Sex: 35/35 (canon: sex)
- assaytype: 35/35
- batch: 35/35
- celltype: 35/35
- condition: 35/35 (canon: disease)
- disease: 35/35 (canon: disease)
- id_sample: 35/35
- nas: 35/35 (canon: nas_score)
- tissue: 35/35 (canon: tissue)
- type_patient: 35/35

## Evidence for WARN/FAIL checks

### source_tissue (WARN)
### single_cell_or_spatial (WARN)
- GSE267032 / Series_summary: matched `single cell` in "Background & Aims: Metabolic dysfunction associated steatotic liver disease (MAFLD) progresses to steatohepatitis (MASH) and is a major cause of liver cirrhosis. In the early disease stage, liver infl"

Decision: MANUAL_REVIEW

Reasons:
- source_tissue: liver-pattern source 0/35
- single_cell_or_spatial: series prose mentions single cell; sample metadata does not corroborate
<!-- /computed -->