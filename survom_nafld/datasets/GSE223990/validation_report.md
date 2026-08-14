# Validation report: GSE223990

Network Pharmacology-based analysis of Resinacein S against non-alcoholic fatty liver disease by modulating lipid metabolism

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
| material_type | WARN | cell/culture terms in sample metadata: L02, cell line (6/6 samples) |
| expression_data_availability | PASS | processed series-level file: GSE223990_All.counts.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE223990_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX19210969, https://www.ncbi.nlm.nih.gov/sra?term=SRX19210970, https://www.ncbi.nlm.nih.gov/sra?term=SRX19210971, https://www.ncbi.nlm.nih.gov/sra?term=SRX19210972, https://www.ncbi.nlm.nih.gov/sra?term=SRX19210973, and 1 more (see sample_metadata.csv) |

## Canonical field distributions

- **treatment**: DMSO (3), Resinacein S (3)

## Field presence

- cell line: 6/6
- cell type: 6/6
- genotype: 6/6
- treatment: 6/6 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE223990 / Series_title: matched `non-alcoholic fatty liver` in "Network Pharmacology-based analysis of Resinacein S against non-alcoholic fatty liver disease by modulating lipid metabolism"
- GSE223990 / Series_summary: matched `NAFLD` in "In order to investigate the hub regulated genes of Resinacein S against NAFLD in human liver cells, we treated the normal human hepatic cell line L02 with Resinacein S and detected the gene expression"
### material_type (WARN)
- GSM7009321 / Sample_source_name_ch1: matched `L02` in "L02"
- GSM7009322 / Sample_source_name_ch1: matched `L02` in "L02"
- GSM7009323 / Sample_source_name_ch1: matched `L02` in "L02"
- GSM7009324 / Sample_source_name_ch1: matched `L02` in "L02"
- GSM7009325 / Sample_source_name_ch1: matched `L02` in "L02"
- GSM7009326 / Sample_source_name_ch1: matched `L02` in "L02"
- GSM7009321 / Sample_characteristics_ch1: matched `cell line` in "cell line: L02"
- GSM7009322 / Sample_characteristics_ch1: matched `cell line` in "cell line: L02"
- GSM7009323 / Sample_characteristics_ch1: matched `cell line` in "cell line: L02"
- GSM7009324 / Sample_characteristics_ch1: matched `cell line` in "cell line: L02"
- GSM7009325 / Sample_characteristics_ch1: matched `cell line` in "cell line: L02"
- GSM7009326 / Sample_characteristics_ch1: matched `cell line` in "cell line: L02"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 6 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: L02, cell line (6/6 samples)
<!-- /computed -->