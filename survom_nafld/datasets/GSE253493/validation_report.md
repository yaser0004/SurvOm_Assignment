# Validation report: GSE253493

RNA-Seq experiment of primary hepatic stellate cells (HSCs) and LX-2 cell line treated with TGFb

<!-- computed -->
Sample count: 12

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 12 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 12/12 |
| source_tissue | WARN | liver-pattern source 6/12 |
| library_strategy | PASS | RNA-Seq 12/12 |
| library_source | PASS | transcriptomic 12/12 |
| library_selection | PASS | cDNA 12/12 |
| instrument_model | PASS | Illumina HiSeq 3000 12/12 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: LX-2, cell line (6/12 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX23265334, https://www.ncbi.nlm.nih.gov/sra?term=SRX23265335, https://www.ncbi.nlm.nih.gov/sra?term=SRX23265336, https://www.ncbi.nlm.nih.gov/sra?term=SRX23265337, https://www.ncbi.nlm.nih.gov/sra?term=SRX23265338, and 7 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE253493_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX23265334, https://www.ncbi.nlm.nih.gov/sra?term=SRX23265335, https://www.ncbi.nlm.nih.gov/sra?term=SRX23265336, https://www.ncbi.nlm.nih.gov/sra?term=SRX23265337, https://www.ncbi.nlm.nih.gov/sra?term=SRX23265338, and 7 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Priamry Hepatic Stellate Cells (6)
- **treatment**: Solvent (6), TGFBeta (6)

## Field presence

- cell line: 6/12
- tissue: 6/12 (canon: tissue)
- treatment: 12/12 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE253493 / Series_summary: matched `steatohepatitis` in "Liver fibrosis stands as the most prominent predictor of overall mortality in non-alcoholic steatohepatitis (NASH). The fibrotic liver features excessive deposition of extracellular matrix (ECM), prim"
### material_type (WARN)
- GSM8021671 / Sample_source_name_ch1: matched `LX-2` in "LX-2 Cell Line"
- GSM8021672 / Sample_source_name_ch1: matched `LX-2` in "LX-2 Cell Line"
- GSM8021673 / Sample_source_name_ch1: matched `LX-2` in "LX-2 Cell Line"
- GSM8021674 / Sample_source_name_ch1: matched `LX-2` in "LX-2 Cell Line"
- GSM8021675 / Sample_source_name_ch1: matched `LX-2` in "LX-2 Cell Line"
- GSM8021676 / Sample_source_name_ch1: matched `LX-2` in "LX-2 Cell Line"
- GSM8021671 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2Cell Line"
- GSM8021672 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2Cell Line"
- GSM8021673 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2Cell Line"
- GSM8021674 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2Cell Line"
- GSM8021675 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2Cell Line"
- GSM8021676 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2Cell Line"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 12 samples (below 20)
- source_tissue: liver-pattern source 6/12
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: LX-2, cell line (6/12 samples)
<!-- /computed -->