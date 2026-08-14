# Validation report: GSE247467

Transcriptomic characterization of circulating neutrophils isolated from patients with metabolic dysfunction-associated steatohepatitis (MASH), formerly known as nonalcoholic steatohepatitis (NASH).

<!-- computed -->
Sample count: 12

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 12 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 12/12 |
| source_tissue | WARN | liver-pattern source 0/12 |
| library_strategy | PASS | RNA-Seq 12/12 |
| library_source | PASS | transcriptomic 12/12 |
| library_selection | PASS | cDNA 12/12 |
| instrument_model | PASS | Illumina NextSeq 500 12/12 |
| metadata_completeness | PASS | reported consistently: disease, tissue; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (8 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (12/12), packaged in GSE247467_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE247467_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX22482408, https://www.ncbi.nlm.nih.gov/sra?term=SRX22482409, https://www.ncbi.nlm.nih.gov/sra?term=SRX22482410, https://www.ncbi.nlm.nih.gov/sra?term=SRX22482411, https://www.ncbi.nlm.nih.gov/sra?term=SRX22482412, and 7 more (see sample_metadata.csv) |

## Canonical field distributions

- **disease**: MASH (8), healthy (4)
- **tissue**: Peripheral blood (12)

## Field presence

- cell type: 12/12
- disease state: 12/12 (canon: disease)
- tissue: 12/12 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 12 samples (below 20)
- source_tissue: liver-pattern source 0/12
<!-- /computed -->