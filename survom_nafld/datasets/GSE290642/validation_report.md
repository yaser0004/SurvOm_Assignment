# Validation report: GSE290642

Selective targeting of endothelial and perivascular ROCK2 reverses liver fibrosis in  pigs and human patients

<!-- computed -->
Sample count: 36

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 36 samples |
| organism_consistency | WARN | mixed organisms: Homo sapiens 24/36, Sus scrofa 12/36 |
| source_tissue | PASS | liver-pattern source 36/36 |
| library_strategy | PASS | RNA-Seq 36/36 |
| library_source | WARN | library_source: transcriptomic single cell 36/36 |
| library_selection | PASS | cDNA 36/36 |
| instrument_model | PASS | HiSeq X Ten 36/36 |
| metadata_completeness | WARN | patchy fields: age 24/36, fibrosis_stage 24/36, sex 24/36. reported consistently: tissue; not reported anywhere: bmi, diagnosis, disease, ethnicity, group, nas_score, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (30 sample(s)) |
| single_cell_or_spatial | WARN | series prose mentions single-cell; sample metadata does not corroborate |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX34454623, https://www.ncbi.nlm.nih.gov/sra?term=SRX34454624, https://www.ncbi.nlm.nih.gov/sra?term=SRX34454625, https://www.ncbi.nlm.nih.gov/sra?term=SRX34454626, https://www.ncbi.nlm.nih.gov/sra?term=SRX34454627, and 7 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE290642-GPL20795_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX34454623, https://www.ncbi.nlm.nih.gov/sra?term=SRX34454624, https://www.ncbi.nlm.nih.gov/sra?term=SRX34454625, https://www.ncbi.nlm.nih.gov/sra?term=SRX34454626, https://www.ncbi.nlm.nih.gov/sra?term=SRX34454627, and 7 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 16 (1), 18 (1), 19 (2), 20 (1), 25 (1), 26 (1), 28 (1), 29 (1), 30 (2), 32 (1), 34 (1), 35 (2), 36 (1), 43 (1), 51 (3), 55 (1), 57 (1), 63 (1), 75 (1)
- **fibrosis_stage**: F0 (3), F1 (10), F1-2 (7), F2 (1), F4 (3)
- **sex**: Female (11), Male (13)
- **tissue**: Liver (36)

## Field presence

- age: 24/36 (canon: age)
- cell type: 36/36
- fibrosis stage: 24/36 (canon: fibrosis_stage)
- gender: 24/36 (canon: sex)
- tissue: 36/36 (canon: tissue)

## Evidence for WARN/FAIL checks

### organism_consistency (WARN)
### library_source (WARN)
### metadata_completeness (WARN)
### single_cell_or_spatial (WARN)
- GSE290642 / Series_overall_design: matched `single-cell` in "We performed single-cell RNA sequencing on liver non-parenchymal cells (NPCs) derived from humans and minipigs to evaluate ROCK2 expression and therapeutic effects."

Decision: MANUAL_REVIEW

Reasons:
- organism_consistency: mixed organisms: Homo sapiens 24/36, Sus scrofa 12/36
- library_source: library_source: transcriptomic single cell 36/36
- metadata_completeness: patchy fields: age 24/36, fibrosis_stage 24/36, sex 24/36. reported consistently: tissue; not reported anywhere: bmi, diagnosis, disease, ethnicity, group, nas_score, stage, steatosis_grade, treatment
- single_cell_or_spatial: series prose mentions single-cell; sample metadata does not corroborate
<!-- /computed -->