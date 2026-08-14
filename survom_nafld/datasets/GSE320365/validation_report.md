# Validation report: GSE320365

An Integrated Multi-omic Analysis Reveals Novel Gene-Metabolite Relationships in Human Steatohepatitic Hepatocellular Carcinoma

<!-- computed -->
Sample count: 15

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 15 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 15/15 |
| source_tissue | PASS | liver-pattern source 15/15 |
| library_strategy | PASS | RNA-Seq 15/15 |
| library_source | PASS | transcriptomic 15/15 |
| library_selection | PASS | cDNA 15/15 |
| instrument_model | PASS | Illumina NovaSeq 6000 15/15 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (15/15 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX32263362, https://www.ncbi.nlm.nih.gov/sra?term=SRX32263363, https://www.ncbi.nlm.nih.gov/sra?term=SRX32263364, https://www.ncbi.nlm.nih.gov/sra?term=SRX32263365, https://www.ncbi.nlm.nih.gov/sra?term=SRX32263366, and 10 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE320365_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX32263362, https://www.ncbi.nlm.nih.gov/sra?term=SRX32263363, https://www.ncbi.nlm.nih.gov/sra?term=SRX32263364, https://www.ncbi.nlm.nih.gov/sra?term=SRX32263365, https://www.ncbi.nlm.nih.gov/sra?term=SRX32263366, and 10 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Liver (15)

## Field presence

- cell line: 15/15
- tissue: 15/15 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE320365 / Series_summary: matched `Metabolic dysfunction-associated stea` in "Background Metabolic dysfunction-associated steatotic liver disease (MASLD) is the fastest-growing etiology of hepatocellular carcinoma (HCC). A mechanistic understanding of the metabolic heterogeneit"
### material_type (WARN)
- GSM9541699 / Sample_characteristics_ch1: matched `cell line` in "cell line: Adjacent"
- GSM9541700 / Sample_characteristics_ch1: matched `cell line` in "cell line: Tumor"
- GSM9541701 / Sample_characteristics_ch1: matched `cell line` in "cell line: Adjacent"
- GSM9541702 / Sample_characteristics_ch1: matched `cell line` in "cell line: Tumor"
- GSM9541703 / Sample_characteristics_ch1: matched `cell line` in "cell line: Adjacent"
- GSM9541704 / Sample_characteristics_ch1: matched `cell line` in "cell line: Tumor"
- GSM9541705 / Sample_characteristics_ch1: matched `cell line` in "cell line: Tumor"
- GSM9541706 / Sample_characteristics_ch1: matched `cell line` in "cell line: Tumor"
- GSM9541707 / Sample_characteristics_ch1: matched `cell line` in "cell line: Adjacent"
- GSM9541708 / Sample_characteristics_ch1: matched `cell line` in "cell line: Adjacent"
- GSM9541709 / Sample_characteristics_ch1: matched `cell line` in "cell line: Tumor"
- GSM9541710 / Sample_characteristics_ch1: matched `cell line` in "cell line: Adjacent"
- GSM9541711 / Sample_characteristics_ch1: matched `cell line` in "cell line: Tumor"
- GSM9541712 / Sample_characteristics_ch1: matched `cell line` in "cell line: Adjacent"
- GSM9541713 / Sample_characteristics_ch1: matched `cell line` in "cell line: Tumor"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 15 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (15/15 samples)
<!-- /computed -->