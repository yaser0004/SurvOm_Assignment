# Validation report: GSE213653

The loss of paraoxonase-2 activity aggravates lipid accumulation, mitochondrial dysfunction, and oxidative stress through the impaired autophagy pathway in in vitro fatty liver model

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
| expression_data_availability | PASS | processed series-level file: GSE213653_FPKMs_allsamples.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE213653_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX17626466, https://www.ncbi.nlm.nih.gov/sra?term=SRX17626467, https://www.ncbi.nlm.nih.gov/sra?term=SRX17626468, https://www.ncbi.nlm.nih.gov/sra?term=SRX17626469, https://www.ncbi.nlm.nih.gov/sra?term=SRX17626470, and 1 more (see sample_metadata.csv) |

## Field presence

- cell line: 6/6
- cell type: 6/6
- genotype: 6/6

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE213653 / Series_title: matched `fatty liver` in "The loss of paraoxonase-2 activity aggravates lipid accumulation, mitochondrial dysfunction, and oxidative stress through the impaired autophagy pathway in in vitro fatty liver model"
- GSE213653 / Series_summary: matched `Non-alcoholic fatty liver` in "Non-alcoholic fatty liver disease (NAFLD) is an increasingly prevalent immunometabolic disease that can progress to hepatic cirrhosis and cancer. NAFLD pathogenesis is extremely complex and is associa"
### material_type (WARN)
- GSM6591574 / Sample_characteristics_ch1: matched `cell line` in "cell line: LO2"
- GSM6591575 / Sample_characteristics_ch1: matched `cell line` in "cell line: LO2"
- GSM6591576 / Sample_characteristics_ch1: matched `cell line` in "cell line: LO2"
- GSM6591577 / Sample_characteristics_ch1: matched `cell line` in "cell line: LO2"
- GSM6591578 / Sample_characteristics_ch1: matched `cell line` in "cell line: LO2"
- GSM6591579 / Sample_characteristics_ch1: matched `cell line` in "cell line: LO2"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 6 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (6/6 samples)
<!-- /computed -->