# Validation report: GSE200679

Hepatic senescence is associated with clinical progression of NAFLD/NASH: Role of BMP4 and its antagonist Gremlin1 (Hepatocytes)

<!-- computed -->
Sample count: 8

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 8 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 8/8 |
| source_tissue | WARN | liver-pattern source 8/8; off-target tissue signal detected |
| library_strategy | PASS | RNA-Seq 8/8 |
| library_source | PASS | transcriptomic 8/8 |
| library_selection | PASS | cDNA 8/8 |
| instrument_model | PASS | Illumina NovaSeq 6000 8/8 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (8/8 samples) |
| expression_data_availability | PASS | processed series-level file: GSE200679_Kallisto_TPM_exp_profiles_cellline.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE200679_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX14833631, https://www.ncbi.nlm.nih.gov/sra?term=SRX14833632, https://www.ncbi.nlm.nih.gov/sra?term=SRX14833633, https://www.ncbi.nlm.nih.gov/sra?term=SRX14833634, https://www.ncbi.nlm.nih.gov/sra?term=SRX14833635, and 3 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: liver (8)
- **treatment**: Ctrl (10% serum) (4), rec hGREM1 (10% serum) (4)

## Field presence

- cell line: 8/8
- cell type: 8/8
- genotype: 8/8
- tissue: 8/8 (canon: tissue)
- treatment: 8/8 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
- GSM6041933 / Sample_characteristics_ch1: matched `serum` in "treatment: Ctrl (10% serum)"
- GSM6041934 / Sample_characteristics_ch1: matched `serum` in "treatment: rec hGREM1 (10% serum)"
- GSM6041935 / Sample_characteristics_ch1: matched `serum` in "treatment: Ctrl (10% serum)"
- GSM6041936 / Sample_characteristics_ch1: matched `serum` in "treatment: rec hGREM1 (10% serum)"
- GSM6041937 / Sample_characteristics_ch1: matched `serum` in "treatment: Ctrl (10% serum)"
- GSM6041938 / Sample_characteristics_ch1: matched `serum` in "treatment: rec hGREM1 (10% serum)"
- GSM6041939 / Sample_characteristics_ch1: matched `serum` in "treatment: Ctrl (10% serum)"
- GSM6041940 / Sample_characteristics_ch1: matched `serum` in "treatment: rec hGREM1 (10% serum)"
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE200679 / Series_title: matched `NAFLD` in "Hepatic senescence is associated with clinical progression of NAFLD/NASH: Role of BMP4 and its antagonist Gremlin1 (Hepatocytes)"
### material_type (WARN)
- GSM6041933 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6041934 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6041935 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6041936 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6041937 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6041938 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6041939 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6041940 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 8 samples (below 20)
- source_tissue: liver-pattern source 8/8; off-target tissue signal detected
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (8/8 samples)
<!-- /computed -->