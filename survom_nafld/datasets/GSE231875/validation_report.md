# Validation report: GSE231875

Effect of overexpression of ZBED3 on gene expression in HHL-5 hepatocytes

<!-- computed -->
Sample count: 6

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 6 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 6/6 |
| source_tissue | PASS | liver-pattern source 6/6 |
| library_strategy | PASS | RNA-Seq 6/6 |
| library_source | PASS | transcriptomic 6/6 |
| library_selection | PASS | cDNA 6/6 |
| instrument_model | PASS | Illumina NovaSeq 6000 6/6 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (6/6 samples) |
| expression_data_availability | PASS | processed series-level file: GSE231875_ExpressionProfile.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE231875_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX20248995, https://www.ncbi.nlm.nih.gov/sra?term=SRX20248996, https://www.ncbi.nlm.nih.gov/sra?term=SRX20248997, https://www.ncbi.nlm.nih.gov/sra?term=SRX20248998, https://www.ncbi.nlm.nih.gov/sra?term=SRX20248999, and 1 more (see sample_metadata.csv) |

## Field presence

- cell line: 6/6
- cell type: 6/6
- genotype: 6/6

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE231875 / Series_summary: matched `NAFLD` in "To investigate the regulatory function of ZBED3 in NAFLD, we established a ZBED3-overexpressing HHL-5 cell line treated with FFAs."
### material_type (WARN)
- GSM7305467 / Sample_characteristics_ch1: matched `cell line` in "cell line: HHL-5"
- GSM7305468 / Sample_characteristics_ch1: matched `cell line` in "cell line: HHL-5"
- GSM7305469 / Sample_characteristics_ch1: matched `cell line` in "cell line: HHL-5"
- GSM7305470 / Sample_characteristics_ch1: matched `cell line` in "cell line: HHL-5"
- GSM7305471 / Sample_characteristics_ch1: matched `cell line` in "cell line: HHL-5"
- GSM7305472 / Sample_characteristics_ch1: matched `cell line` in "cell line: HHL-5"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 6 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (6/6 samples)
<!-- /computed -->