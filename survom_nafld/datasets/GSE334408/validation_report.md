# Validation report: GSE334408

Resmetirom ameliorates fibrogenesis in hepatic stellate cells via thyroid hormone receptor alpha-fatty-acid amide hydrolase 1 signaling pathway

<!-- computed -->
Sample count: 8

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 8 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 8/8 |
| source_tissue | PASS | liver-pattern source 8/8 |
| library_strategy | PASS | RNA-Seq 8/8 |
| library_source | PASS | transcriptomic 8/8 |
| library_selection | PASS | cDNA 8/8 |
| instrument_model | PASS | DNBSEQ-G400 8/8 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (8/8 samples) |
| expression_data_availability | PASS | processed per-sample counts (8/8), packaged in GSE334408_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE334408_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX33758426, https://www.ncbi.nlm.nih.gov/sra?term=SRX33758427, https://www.ncbi.nlm.nih.gov/sra?term=SRX33758428, https://www.ncbi.nlm.nih.gov/sra?term=SRX33758429, https://www.ncbi.nlm.nih.gov/sra?term=SRX33758430, and 3 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Liver (8)
- **treatment**: TGF-beta1 36h (8 ng/mL) (4), TGF-beta1 36h (8 ng/mL) + Resmetirom (300 uM) 24h (4)

## Field presence

- cell line: 8/8
- cell type: 8/8
- tissue: 8/8 (canon: tissue)
- treatment: 8/8 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE334408 / Series_summary: matched `steatohepatitis` in "Resmetirom is a liver-directed, thyroid hormone receptor β (THRβ)-selective agonist approved for treating metabolic-associated steatohepatitis (MASH). While Resmetirom hepatocyte-specific effects are "
### material_type (WARN)
- GSM9788195 / Sample_characteristics_ch1: matched `cell line` in "cell line: CyHum19007-SC-P2-Z"
- GSM9788196 / Sample_characteristics_ch1: matched `cell line` in "cell line: CyHum19007-SC-P2-Z"
- GSM9788197 / Sample_characteristics_ch1: matched `cell line` in "cell line: CyHum19007-SC-P2-Z"
- GSM9788198 / Sample_characteristics_ch1: matched `cell line` in "cell line: CyHum19007-SC-P2-Z"
- GSM9788199 / Sample_characteristics_ch1: matched `cell line` in "cell line: CyHum19007-SC-P2-Z"
- GSM9788200 / Sample_characteristics_ch1: matched `cell line` in "cell line: CyHum19007-SC-P2-Z"
- GSM9788201 / Sample_characteristics_ch1: matched `cell line` in "cell line: CyHum19007-SC-P2-Z"
- GSM9788202 / Sample_characteristics_ch1: matched `cell line` in "cell line: CyHum19007-SC-P2-Z"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 8 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (8/8 samples)
<!-- /computed -->