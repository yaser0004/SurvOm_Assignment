# Validation report: GSE279791

Effect of GCN5 depletion in hepatocytes in NAFLD

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
| instrument_model | PASS | DNBSEQ-T7 6/6 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (6/6 samples) |
| expression_data_availability | PASS | processed series-level file: GSE279791_fpkm.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE279791_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX26423569, https://www.ncbi.nlm.nih.gov/sra?term=SRX26423570, https://www.ncbi.nlm.nih.gov/sra?term=SRX26423571, https://www.ncbi.nlm.nih.gov/sra?term=SRX26423572, https://www.ncbi.nlm.nih.gov/sra?term=SRX26423573, and 1 more (see sample_metadata.csv) |

## Canonical field distributions

- **treatment**: free fatty acid (6)

## Field presence

- cell line: 6/6
- cell type: 6/6
- genotype: 6/6
- treatment: 6/6 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE279791 / Series_title: matched `NAFLD` in "Effect of GCN5 depletion in hepatocytes in NAFLD"
- GSE279791 / Series_summary: matched `Non-alcoholic fatty liver` in "Non-alcoholic fatty liver disease (NAFLD) is a burden of global health, yet the mechanism of the disease is not fully elucidated. General control non-repressed protein 5 (GCN5) is histone acetyltransf"
### material_type (WARN)
- GSM8580360 / Sample_characteristics_ch1: matched `cell line` in "cell line: HL-7702"
- GSM8580361 / Sample_characteristics_ch1: matched `cell line` in "cell line: HL-7702"
- GSM8580362 / Sample_characteristics_ch1: matched `cell line` in "cell line: HL-7702"
- GSM8580363 / Sample_characteristics_ch1: matched `cell line` in "cell line: HL-7702"
- GSM8580364 / Sample_characteristics_ch1: matched `cell line` in "cell line: HL-7702"
- GSM8580365 / Sample_characteristics_ch1: matched `cell line` in "cell line: HL-7702"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 6 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (6/6 samples)
<!-- /computed -->