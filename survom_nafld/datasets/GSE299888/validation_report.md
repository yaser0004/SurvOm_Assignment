# Validation report: GSE299888

Liver-specific LXR inverse agonist restores lipid homeostasis in animal models and humans

<!-- computed -->
Sample count: 12

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 12 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 12/12 |
| source_tissue | PASS | liver-pattern source 12/12 |
| library_strategy | PASS | RNA-Seq 12/12 |
| library_source | PASS | transcriptomic 12/12 |
| library_selection | PASS | cDNA 12/12 |
| instrument_model | PASS | BGISEQ-500 12/12 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: organoid (12/12 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX29191293, https://www.ncbi.nlm.nih.gov/sra?term=SRX29191294, https://www.ncbi.nlm.nih.gov/sra?term=SRX29191295, https://www.ncbi.nlm.nih.gov/sra?term=SRX29191296, https://www.ncbi.nlm.nih.gov/sra?term=SRX29191297, and 7 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE299888_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX29191293, https://www.ncbi.nlm.nih.gov/sra?term=SRX29191294, https://www.ncbi.nlm.nih.gov/sra?term=SRX29191295, https://www.ncbi.nlm.nih.gov/sra?term=SRX29191296, https://www.ncbi.nlm.nih.gov/sra?term=SRX29191297, and 7 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Human liver organoids (12)
- **treatment**: DMSO (6), TLC-2716 (6)

## Field presence

- genotype: 12/12
- tissue: 12/12 (canon: tissue)
- treatment: 12/12 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE299888 / Series_summary: matched `steatohepatitis` in "Despite advances in lipid-lowering treatment, atherosclerotic cardiovascular disease (ASCVD) remains the leading cause of mortality, underscoring the need for treatments that address residual risk. Ta"
- GSE299888 / Series_overall_design: matched `MASH` in "The effect of TLC-2716 on lipid accumulation was also evaluated in an induced pluripotent stem cell (iPSC)-derived human liver organoid (HLO) model established from human donors with different genetic"
### material_type (WARN)
- GSM9049399 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM9049400 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM9049401 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM9049402 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM9049403 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM9049404 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM9049405 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM9049406 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM9049407 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM9049408 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM9049409 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM9049410 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM9049399 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM9049400 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM9049401 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM9049402 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM9049403 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM9049404 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM9049405 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM9049406 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM9049407 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM9049408 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM9049409 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM9049410 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 12 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: organoid (12/12 samples)
<!-- /computed -->