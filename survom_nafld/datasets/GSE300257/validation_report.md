# Validation report: GSE300257

Effect of overexpression of LY6D on gene expression in L02 hepatocytes

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
| expression_data_availability | PASS | processed series-level file: GSE300257_ExpressionProfile.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE300257_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX29266676, https://www.ncbi.nlm.nih.gov/sra?term=SRX29266677, https://www.ncbi.nlm.nih.gov/sra?term=SRX29266678, https://www.ncbi.nlm.nih.gov/sra?term=SRX29266679, https://www.ncbi.nlm.nih.gov/sra?term=SRX29266680, and 1 more (see sample_metadata.csv) |

## Canonical field distributions

- **treatment**: FFAs750μM (6)

## Field presence

- cell line: 6/6
- cell type: 6/6
- genotype: 6/6
- treatment: 6/6 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE300257 / Series_summary: matched `NAFLD` in "To investigate the regulatory function of LY6D in NAFLD, we established a LY6D-overexpressing L02 cell line treated with FFAs."
### material_type (WARN)
- GSM9056550 / Sample_source_name_ch1: matched `L02` in "L02"
- GSM9056551 / Sample_source_name_ch1: matched `L02` in "L02"
- GSM9056552 / Sample_source_name_ch1: matched `L02` in "L02"
- GSM9056553 / Sample_source_name_ch1: matched `L02` in "L02"
- GSM9056554 / Sample_source_name_ch1: matched `L02` in "L02"
- GSM9056555 / Sample_source_name_ch1: matched `L02` in "L02"
- GSM9056550 / Sample_title: matched `L02` in "L02 cells，Control，FFAs750μM，rep1"
- GSM9056551 / Sample_title: matched `L02` in "L02 cells，Control，FFAs750μM，rep2"
- GSM9056552 / Sample_title: matched `L02` in "L02 cells，Control，FFAs750μM，rep3"
- GSM9056553 / Sample_title: matched `L02` in "L02 cells，LY6D-OE，FFAs750μM，rep1"
- GSM9056554 / Sample_title: matched `L02` in "L02 cells，LY6D-OE，FFAs750μM，rep2"
- GSM9056555 / Sample_title: matched `L02` in "L02 cells，LY6D-OE，FFAs750μM，rep3"
- GSM9056550 / Sample_characteristics_ch1: matched `cell line` in "cell line: L02"
- GSM9056551 / Sample_characteristics_ch1: matched `cell line` in "cell line: L02"
- GSM9056552 / Sample_characteristics_ch1: matched `cell line` in "cell line: L02"
- GSM9056553 / Sample_characteristics_ch1: matched `cell line` in "cell line: L02"
- GSM9056554 / Sample_characteristics_ch1: matched `cell line` in "cell line: L02"
- GSM9056555 / Sample_characteristics_ch1: matched `cell line` in "cell line: L02"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 6 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: L02, cell line (6/6 samples)
<!-- /computed -->