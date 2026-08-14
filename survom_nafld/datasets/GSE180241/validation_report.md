# Validation report: GSE180241

Endothelial-immune crosstalk contributes to vascular injury in non-alcoholic fatty liver disease

<!-- computed -->
Sample count: 6

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 6 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 6/6 |
| source_tissue | WARN | liver-pattern source 0/6 |
| library_strategy | PASS | RNA-Seq 6/6 |
| library_source | PASS | transcriptomic 6/6 |
| library_selection | PASS | cDNA 6/6 |
| instrument_model | PASS | Illumina HiSeq 2000 6/6 |
| metadata_completeness | PASS | reported consistently: disease; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade, tissue, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (3 sample(s)) |
| single_cell_or_spatial | WARN | series prose mentions single-cell; sample metadata does not corroborate |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX11482564, https://www.ncbi.nlm.nih.gov/sra?term=SRX11482565, https://www.ncbi.nlm.nih.gov/sra?term=SRX11482566, https://www.ncbi.nlm.nih.gov/sra?term=SRX11482568, https://www.ncbi.nlm.nih.gov/sra?term=SRX11482569, and 1 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE180241_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX11482564, https://www.ncbi.nlm.nih.gov/sra?term=SRX11482565, https://www.ncbi.nlm.nih.gov/sra?term=SRX11482566, https://www.ncbi.nlm.nih.gov/sra?term=SRX11482568, https://www.ncbi.nlm.nih.gov/sra?term=SRX11482569, and 1 more (see sample_metadata.csv) |

## Canonical field distributions

- **disease**: NAFLD (3), heathly (3)

## Field presence

- cell: 6/6
- disease state: 6/6 (canon: disease)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
### single_cell_or_spatial (WARN)
- GSE180241 / Series_summary: matched `single-cell` in "Cardiovascular complications are major causes of death in non-alcoholic fatty liver disease (NAFLD) but the underlying endothelial pathophysiology remains understudied. Here, we cultivated blood outgr"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 6 samples (below 20)
- source_tissue: liver-pattern source 0/6
- single_cell_or_spatial: series prose mentions single-cell; sample metadata does not corroborate
<!-- /computed -->