# Validation report: GSE266460

Protein tyrosine phosphatase delta is a STAT3-phosphatase and suppressor of metabolic liver disease (HepaRG cells).

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
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX24437046, https://www.ncbi.nlm.nih.gov/sra?term=SRX24437047, https://www.ncbi.nlm.nih.gov/sra?term=SRX24437048, https://www.ncbi.nlm.nih.gov/sra?term=SRX24437049, https://www.ncbi.nlm.nih.gov/sra?term=SRX24437050, and 1 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE266460_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX24437046, https://www.ncbi.nlm.nih.gov/sra?term=SRX24437047, https://www.ncbi.nlm.nih.gov/sra?term=SRX24437048, https://www.ncbi.nlm.nih.gov/sra?term=SRX24437049, https://www.ncbi.nlm.nih.gov/sra?term=SRX24437050, and 1 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Liver (6)
- **treatment**: PTPF (3), STATF (3)

## Field presence

- cell line: 6/6
- cell type: 6/6
- tissue: 6/6 (canon: tissue)
- treatment: 6/6 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE266460 / Series_summary: matched `metabolic dysfunction-associated stea` in "Background & Aims: Protein tyrosine phosphatase delta (PTPRD) is suppressed in several diseases including HCV infection. To identify hepatic pathways responsive to PTPRD function and their role in non"
### material_type (WARN)
- GSM8247442 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG"
- GSM8247443 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG"
- GSM8247444 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG"
- GSM8247445 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG"
- GSM8247446 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG"
- GSM8247447 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 6 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (6/6 samples)
<!-- /computed -->