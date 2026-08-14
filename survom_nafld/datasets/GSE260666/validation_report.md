# Validation report: GSE260666

Differential analysis of gene expression in liver tissues of patients with nonalcoholic fatty liver disease and controls.

<!-- computed -->
Sample count: 16

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 16 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 16/16 |
| source_tissue | PASS | liver-pattern source 16/16 |
| library_strategy | PASS | RNA-Seq 16/16 |
| library_source | PASS | transcriptomic 16/16 |
| library_selection | PASS | cDNA 16/16 |
| instrument_model | PASS | Illumina NovaSeq 6000 16/16 |
| metadata_completeness | PASS | reported consistently: disease, tissue, treatment; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (10 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE260666_raw_counts.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE260666_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX23809226, https://www.ncbi.nlm.nih.gov/sra?term=SRX23809227, https://www.ncbi.nlm.nih.gov/sra?term=SRX23809228, https://www.ncbi.nlm.nih.gov/sra?term=SRX23809229, https://www.ncbi.nlm.nih.gov/sra?term=SRX23809230, and 11 more (see sample_metadata.csv) |

## Canonical field distributions

- **disease**: healthy control (6), non-alcoholic fatty liver disease (NAFLD) (6), non-alcoholic steatohepatitis (NASH) (4)
- **tissue**: Liver (16)
- **treatment**: untreated (16)

## Field presence

- cell type: 16/16
- disease state: 16/16 (canon: disease)
- tissue: 16/16 (canon: tissue)
- treatment: 16/16 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 16 samples (below 20)
<!-- /computed -->