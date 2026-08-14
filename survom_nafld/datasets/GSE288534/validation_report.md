# Validation report: GSE288534

Targeting Senescent Hepatocytes for Treatment of Metabolic Dysfunction-associated Steatotic Liver Disease and Multi-organ Dysfunction

<!-- computed -->
Sample count: 24

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 24 samples |
| organism_consistency | WARN | mixed organisms: Homo sapiens 14/24, Mus musculus 10/24 |
| source_tissue | PASS | liver-pattern source 24/24 |
| library_strategy | PASS | RNA-Seq 24/24 |
| library_source | PASS | transcriptomic 24/24 |
| library_selection | PASS | cDNA 24/24 |
| instrument_model | PASS | Illumina NovaSeq 6000 24/24 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | WARN | series prose mentions Single-nucle; sample metadata does not corroborate |
| material_type | WARN | cell/culture terms in sample metadata: Huh7, cell line (14/24 samples) |
| expression_data_availability | PASS | processed per-sample counts (18/24), packaged in GSE288534_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE288534-GPL24247_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX27536606, https://www.ncbi.nlm.nih.gov/sra?term=SRX27536607, https://www.ncbi.nlm.nih.gov/sra?term=SRX27536608, https://www.ncbi.nlm.nih.gov/sra?term=SRX27536609, https://www.ncbi.nlm.nih.gov/sra?term=SRX27536610, and 19 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Liver (10)
- **treatment**: Ctrl (3), Dp44mT (4), DpC (5), Palbo (3), Vehicle (9)

## Field presence

- batch: 24/24
- cell line: 14/24
- cell type: 14/24
- tissue: 10/24 (canon: tissue)
- treatment: 24/24 (canon: treatment)

## Evidence for WARN/FAIL checks

### organism_consistency (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE288534 / Series_title: matched `Metabolic Dysfunction-associated Stea` in "Targeting Senescent Hepatocytes for Treatment of Metabolic Dysfunction-associated Steatotic Liver Disease and Multi-organ Dysfunction"
- GSE288534 / Series_summary: matched `metabolic dysfunction-associated stea` in "Senescent hepatocytes accumulate in metabolic dysfunction-associated steatotic liver disease (MASLD) and are linked to worse clinical outcomes. However, their heterogeneity and lack of specific marker"
- GSE288534 / Series_overall_design: matched `MASLD` in "To induce hepatocyte senescence, Huh7 cells were treated with the CDK4/6 inhibitor palbociclib (1uM) for 8 days. To test the effects of Dp44mT on senescent Huh7 cells, the cells were treated with Dp44"
### single_cell_or_spatial (WARN)
- GSE288534 / Series_summary: matched `Single-nucle` in "Senescent hepatocytes accumulate in metabolic dysfunction-associated steatotic liver disease (MASLD) and are linked to worse clinical outcomes. However, their heterogeneity and lack of specific marker"
### material_type (WARN)
- GSM8769557 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8769558 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8769559 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8769560 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8769561 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8769562 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8769563 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8769564 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8769565 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8769566 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8769567 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8769568 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8769569 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8769570 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8769557 / Sample_title: matched `Huh7` in "Huh7_Veh_1"
- GSM8769558 / Sample_title: matched `Huh7` in "Huh7_Veh_2"
- GSM8769559 / Sample_title: matched `Huh7` in "Huh7_Veh_3"
- GSM8769560 / Sample_title: matched `Huh7` in "Huh7_Veh_4"
- GSM8769561 / Sample_title: matched `Huh7` in "Huh7_Dp44mT_1"
- GSM8769562 / Sample_title: matched `Huh7` in "Huh7_Dp44mT_2"
- GSM8769563 / Sample_title: matched `Huh7` in "Huh7_Dp44mT_3"
- GSM8769564 / Sample_title: matched `Huh7` in "Huh7_Dp44mT_4"
- GSM8769557 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8769558 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8769559 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8769560 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8769561 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8769562 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8769563 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8769564 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8769565 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8769566 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8769567 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8769568 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8769569 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8769570 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"

Decision: MANUAL_REVIEW

Reasons:
- organism_consistency: mixed organisms: Homo sapiens 14/24, Mus musculus 10/24
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- single_cell_or_spatial: series prose mentions Single-nucle; sample metadata does not corroborate
- material_type: cell/culture terms in sample metadata: Huh7, cell line (14/24 samples)
<!-- /computed -->