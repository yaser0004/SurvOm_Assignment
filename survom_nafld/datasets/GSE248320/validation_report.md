# Validation report: GSE248320

Lysine tRNA fragments and miR-194-5p co-regulate hepatic steatosis via β-Klotho and Perilipin 2 (RNA)

<!-- computed -->
Sample count: 4

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 4 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 4/4 |
| source_tissue | WARN | liver-pattern source 0/4 |
| library_strategy | PASS | RNA-Seq 4/4 |
| library_source | PASS | transcriptomic 4/4 |
| library_selection | PASS | cDNA 4/4 |
| instrument_model | PASS | NextSeq 2000 4/4 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (4/4 samples) |
| expression_data_availability | PASS | processed series-level file: GSE248320_raw_counts_cells_longRNA.csv.gz |
| series_matrix | INFO | present, metadata-only (GSE248320_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX22588784, https://www.ncbi.nlm.nih.gov/sra?term=SRX22588785, https://www.ncbi.nlm.nih.gov/sra?term=SRX22588786, https://www.ncbi.nlm.nih.gov/sra?term=SRX22588787 |

## Field presence

- cell line: 4/4

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE248320 / Series_title: matched `steatosis` in "Lysine tRNA fragments and miR-194-5p co-regulate hepatic steatosis via β-Klotho and Perilipin 2 (RNA)"
- GSE248320 / Series_summary: matched `Non-alcoholic fatty liver` in "Non-alcoholic fatty liver disease (NAFLD) involves hepatic accumulation of intracellular lipid droplets via incompletely understood processes. Here, we report distinct and cooperative NAFLD roles of L"
### material_type (WARN)
- GSM7911529 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep G2"
- GSM7911530 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep G2"
- GSM7911531 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep G2"
- GSM7911532 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep G2"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 4 samples (below 20)
- source_tissue: liver-pattern source 0/4
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (4/4 samples)
<!-- /computed -->