# Validation report: GSE210927

Effect of Combinatorial Extracellular Matrix and Substrate Stiffness on Gene Expression of Activated Hepatic Stellate Cells

<!-- computed -->
Sample count: 18

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 18 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 18/18 |
| source_tissue | PASS | liver-pattern source 18/18 |
| library_strategy | PASS | RNA-Seq 18/18 |
| library_source | PASS | transcriptomic 18/18 |
| library_selection | PASS | cDNA 18/18 |
| instrument_model | PASS | Illumina NovaSeq 6000 18/18 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (18/18 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX17023418, https://www.ncbi.nlm.nih.gov/sra?term=SRX17023419, https://www.ncbi.nlm.nih.gov/sra?term=SRX17023420, https://www.ncbi.nlm.nih.gov/sra?term=SRX17023421, https://www.ncbi.nlm.nih.gov/sra?term=SRX17023422, and 13 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE210927_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX17023418, https://www.ncbi.nlm.nih.gov/sra?term=SRX17023419, https://www.ncbi.nlm.nih.gov/sra?term=SRX17023420, https://www.ncbi.nlm.nih.gov/sra?term=SRX17023421, https://www.ncbi.nlm.nih.gov/sra?term=SRX17023422, and 13 more (see sample_metadata.csv) |

## Field presence

- cell line: 18/18
- cell type: 18/18
- ecm compositions: 18/18
- substrate stiffness: 18/18
- time: 18/18

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE210927 / Series_summary: matched `NAFLD` in "Understand mechanisms of NAFLD related liver fibrosis"
### material_type (WARN)
- GSM6442988 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary Human HSCs"
- GSM6442989 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary Human HSCs"
- GSM6442990 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary Human HSCs"
- GSM6442991 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary Human HSCs"
- GSM6442992 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary Human HSCs"
- GSM6442993 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary Human HSCs"
- GSM6442994 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary Human HSCs"
- GSM6442995 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary Human HSCs"
- GSM6442996 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary Human HSCs"
- GSM6442997 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary Human HSCs"
- GSM6442998 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary Human HSCs"
- GSM6442999 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary Human HSCs"
- GSM6443000 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary Human HSCs"
- GSM6443001 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary Human HSCs"
- GSM6443002 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary Human HSCs"
- GSM6443003 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary Human HSCs"
- GSM6443004 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary Human HSCs"
- GSM6443005 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary Human HSCs"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 18 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (18/18 samples)
<!-- /computed -->