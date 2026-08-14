# Validation report: GSE116185

A NAFLD Model Created By Endoplasmic Reticulum Stress Response-Associated Steatosis in Human Induced Pluripotent Stem Cell-Derived Hepatocytes

<!-- computed -->
Sample count: 4

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 4 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 4/4 |
| source_tissue | PASS | liver-pattern source 4/4 |
| library_strategy | PASS | RNA-Seq 4/4 |
| library_source | PASS | transcriptomic 4/4 |
| library_selection | PASS | cDNA 4/4 |
| instrument_model | PASS | Illumina HiSeq 1500 4/4 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line, hiPSC, iPSC, pluripotent stem cell (4/4 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX4286160, https://www.ncbi.nlm.nih.gov/sra?term=SRX4286161, https://www.ncbi.nlm.nih.gov/sra?term=SRX4286162, https://www.ncbi.nlm.nih.gov/sra?term=SRX4286163) |
| series_matrix | INFO | present, metadata-only (GSE116185_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX4286160, https://www.ncbi.nlm.nih.gov/sra?term=SRX4286161, https://www.ncbi.nlm.nih.gov/sra?term=SRX4286162, https://www.ncbi.nlm.nih.gov/sra?term=SRX4286163 |

## Field presence

- cell type: 4/4
- genotype: 4/4
- treatmnet: 4/4

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE116185 / Series_title: matched `NAFLD` in "A NAFLD Model Created By Endoplasmic Reticulum Stress Response-Associated Steatosis in Human Induced Pluripotent Stem Cell-Derived Hepatocytes"
- GSE116185 / Series_summary: matched `steatosis` in "Our study reports a phenotypic approach to model hepatic steatosis in induced pluripotent stem cell-derived hepatocytes"
- GSE116185 / Series_overall_design: matched `steatosis` in "hiPSCs, differentiated into functional hepatocytes that exhibited classic hepatocyte-associated bio-functions, were subjected to lipid overload and challenged with acute induced-ER stress developed a "
### material_type (WARN)
- GSM3212769 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Human induced pluripotent stem cells (hiPSC)"
- GSM3212770 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Human induced pluripotent stem cells (hiPSC)"
- GSM3212771 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Human induced pluripotent stem cells (hiPSC)"
- GSM3212772 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Human induced pluripotent stem cells (hiPSC)"
- GSM3212769 / Sample_title: matched `iPSC` in "iPSC-Hep_RNAseq 1"
- GSM3212770 / Sample_title: matched `iPSC` in "iPSC-Hep_RNAseq 2"
- GSM3212771 / Sample_title: matched `iPSC` in "iPSC-Hep_RNAseq 3"
- GSM3212772 / Sample_title: matched `iPSC` in "iPSC-Hep_RNAseq 4"
- GSM3212769 / Sample_characteristics_ch1: matched `hiPSC` in "cell type: Cryopreserved hiPSC-derived Hepatocytes"
- GSM3212769 / Sample_characteristics_ch1: matched `cell line` in "genotype: Wild type ( cell line)"
- GSM3212770 / Sample_characteristics_ch1: matched `hiPSC` in "cell type: Cryopreserved hiPSC-derived Hepatocytes"
- GSM3212770 / Sample_characteristics_ch1: matched `cell line` in "genotype: Wild type ( cell line)"
- GSM3212771 / Sample_characteristics_ch1: matched `hiPSC` in "cell type: Cryopreserved hiPSC-derived Hepatocytes"
- GSM3212771 / Sample_characteristics_ch1: matched `cell line` in "genotype: Wild type ( cell line)"
- GSM3212772 / Sample_characteristics_ch1: matched `hiPSC` in "cell type: Cryopreserved hiPSC-derived Hepatocytes"
- GSM3212772 / Sample_characteristics_ch1: matched `hiPSC` in "treatmnet: Pretreatment of hiPSC-Hep with OCA and lipid loading plus thapsigargin for 18 hrs"
- GSM3212772 / Sample_characteristics_ch1: matched `cell line` in "genotype: Wild type ( cell line)"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 4 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line, hiPSC, iPSC, pluripotent stem cell (4/4 samples)
<!-- /computed -->