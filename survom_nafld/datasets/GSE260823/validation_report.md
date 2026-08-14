# Validation report: GSE260823

Transcriptomic analysis of co-culture generated lipid-associated macrophages (LAMs)

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
| instrument_model | PASS | Illumina NovaSeq 6000 6/6 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: THP-1, cell line (6/6 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX23831353, https://www.ncbi.nlm.nih.gov/sra?term=SRX23831354, https://www.ncbi.nlm.nih.gov/sra?term=SRX23831355, https://www.ncbi.nlm.nih.gov/sra?term=SRX23831356, https://www.ncbi.nlm.nih.gov/sra?term=SRX23831357, and 1 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE260823_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX23831353, https://www.ncbi.nlm.nih.gov/sra?term=SRX23831354, https://www.ncbi.nlm.nih.gov/sra?term=SRX23831355, https://www.ncbi.nlm.nih.gov/sra?term=SRX23831356, https://www.ncbi.nlm.nih.gov/sra?term=SRX23831357, and 1 more (see sample_metadata.csv) |

## Field presence

- cell line: 6/6

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE260823 / Series_summary: matched `Metabolic dysfunction-associated stea` in "Metabolic dysfunction-associated steatotic liver disease (MASLD) is characterized by profound remodeling of hepatic macrophages, including the emergence of lipid-associated macrophages (LAMs). However"
### material_type (WARN)
- GSM8125060 / Sample_source_name_ch1: matched `THP-1` in "THP-1"
- GSM8125061 / Sample_source_name_ch1: matched `THP-1` in "THP-1"
- GSM8125062 / Sample_source_name_ch1: matched `THP-1` in "THP-1"
- GSM8125063 / Sample_source_name_ch1: matched `THP-1` in "THP-1"
- GSM8125064 / Sample_source_name_ch1: matched `THP-1` in "THP-1"
- GSM8125065 / Sample_source_name_ch1: matched `THP-1` in "THP-1"
- GSM8125060 / Sample_title: matched `THP-1` in "THP-1, Control, rep1"
- GSM8125061 / Sample_title: matched `THP-1` in "THP-1, Control, rep2"
- GSM8125062 / Sample_title: matched `THP-1` in "THP-1, Control, rep3"
- GSM8125063 / Sample_title: matched `THP-1` in "THP-1, LAMs, rep1"
- GSM8125064 / Sample_title: matched `THP-1` in "THP-1, LAMs, rep2"
- GSM8125065 / Sample_title: matched `THP-1` in "THP-1, LMAs, rep3"
- GSM8125060 / Sample_characteristics_ch1: matched `cell line` in "cell line: THP-1"
- GSM8125061 / Sample_characteristics_ch1: matched `cell line` in "cell line: THP-1"
- GSM8125062 / Sample_characteristics_ch1: matched `cell line` in "cell line: THP-1"
- GSM8125063 / Sample_characteristics_ch1: matched `cell line` in "cell line: THP-1"
- GSM8125064 / Sample_characteristics_ch1: matched `cell line` in "cell line: THP-1"
- GSM8125065 / Sample_characteristics_ch1: matched `cell line` in "cell line: THP-1"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 6 samples (below 20)
- source_tissue: liver-pattern source 0/6
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: THP-1, cell line (6/6 samples)
<!-- /computed -->