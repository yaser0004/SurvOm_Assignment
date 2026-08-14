# Validation report: GSE278593

IGFBP-7 transforms hepatic stellate cells into an HCC-promoting phenotype in MASLD.

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
| material_type | WARN | cell/culture terms in sample metadata: LX-2, cell line (6/6 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX26259537, https://www.ncbi.nlm.nih.gov/sra?term=SRX26259538, https://www.ncbi.nlm.nih.gov/sra?term=SRX26259539, https://www.ncbi.nlm.nih.gov/sra?term=SRX26259540, https://www.ncbi.nlm.nih.gov/sra?term=SRX26259541, and 1 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE278593_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX26259537, https://www.ncbi.nlm.nih.gov/sra?term=SRX26259538, https://www.ncbi.nlm.nih.gov/sra?term=SRX26259539, https://www.ncbi.nlm.nih.gov/sra?term=SRX26259540, https://www.ncbi.nlm.nih.gov/sra?term=SRX26259541, and 1 more (see sample_metadata.csv) |

## Canonical field distributions

- **treatment**: IGFBP-7 (3), PBS (3)

## Field presence

- cell line: 6/6
- cell type: 6/6
- genotype: 6/6
- treatment: 6/6 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE278593 / Series_title: matched `MASLD` in "IGFBP-7 transforms hepatic stellate cells into an HCC-promoting phenotype in MASLD."
- GSE278593 / Series_summary: matched `metabolic dysfunction-associated stea` in "Hepatic fibrosis is the strongest contributor to hepatocarcinogenesis in metabolic dysfunction-associated steatotic liver disease (MASLD); however, the underlying mechanisms have yet to be fully eluci"
### material_type (WARN)
- GSM8550470 / Sample_source_name_ch1: matched `LX-2` in "LX-2"
- GSM8550471 / Sample_source_name_ch1: matched `LX-2` in "LX-2"
- GSM8550472 / Sample_source_name_ch1: matched `LX-2` in "LX-2"
- GSM8550473 / Sample_source_name_ch1: matched `LX-2` in "LX-2"
- GSM8550474 / Sample_source_name_ch1: matched `LX-2` in "LX-2"
- GSM8550475 / Sample_source_name_ch1: matched `LX-2` in "LX-2"
- GSM8550470 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM8550471 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM8550472 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM8550473 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM8550474 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM8550475 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 6 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: LX-2, cell line (6/6 samples)
<!-- /computed -->