# Validation report: GSE325645

Transcriptomic profiling of NK cells in CHB and CHB-MASLD

<!-- computed -->
Sample count: 7

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 7 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 7/7 |
| source_tissue | WARN | liver-pattern source 0/7 |
| library_strategy | PASS | RNA-Seq 7/7 |
| library_source | PASS | transcriptomic 7/7 |
| library_selection | PASS | cDNA 7/7 |
| instrument_model | PASS | Illumina NovaSeq 6000 7/7 |
| metadata_completeness | WARN | patchy fields: disease 6/7. reported consistently: tissue; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (3 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (1/7 samples) |
| expression_data_availability | PASS | processed series-level file: GSE325645_gene_expression.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE325645_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX32606313, https://www.ncbi.nlm.nih.gov/sra?term=SRX32606314, https://www.ncbi.nlm.nih.gov/sra?term=SRX32606315, https://www.ncbi.nlm.nih.gov/sra?term=SRX32606316, https://www.ncbi.nlm.nih.gov/sra?term=SRX32606317, and 2 more (see sample_metadata.csv) |

## Canonical field distributions

- **disease**: CHB (3), CHB-MASLD (3)
- **tissue**: peripheral blood (7)

## Field presence

- batch: 6/7
- cell line: 1/7
- cell type: 6/7
- disease state: 6/7 (canon: disease)
- tissue: 7/7 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
### metadata_completeness (WARN)
### material_type (WARN)
- GSM9759946 / Sample_characteristics_ch1: matched `cell line` in "cell line: NK cell"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 7 samples (below 20)
- source_tissue: liver-pattern source 0/7
- metadata_completeness: patchy fields: disease 6/7. reported consistently: tissue; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade, treatment
- material_type: cell/culture terms in sample metadata: cell line (1/7 samples)
<!-- /computed -->