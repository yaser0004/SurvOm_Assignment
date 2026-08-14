# Validation report: GSE205179

3D bioprinting of human liver models with biliary branching morphogenesis for hepatotoxicity, regeneration and NASH

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
| instrument_model | PASS | Illumina NovaSeq 6000 12/12 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (12/12 samples) |
| expression_data_availability | PASS | processed series-level file: GSE205179_gene_fpkm.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE205179_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX15505887, https://www.ncbi.nlm.nih.gov/sra?term=SRX15505888, https://www.ncbi.nlm.nih.gov/sra?term=SRX15505889, https://www.ncbi.nlm.nih.gov/sra?term=SRX15505890, https://www.ncbi.nlm.nih.gov/sra?term=SRX15505891, and 7 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: liver (12)
- **treatment**: 3D bio-printed and differentiation (6), planar cell culture (3), planar cell differentiation (3)

## Field presence

- cell line: 12/12
- cell type: 12/12
- genotype: 12/12
- tissue: 12/12 (canon: tissue)
- treatment: 12/12 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE205179 / Series_title: matched `NASH` in "3D bioprinting of human liver models with biliary branching morphogenesis for hepatotoxicity, regeneration and NASH"
### material_type (WARN)
- GSM6206872 / Sample_characteristics_ch1: matched `cell line` in "cell line: hepaRG"
- GSM6206873 / Sample_characteristics_ch1: matched `cell line` in "cell line: hepaRG"
- GSM6206874 / Sample_characteristics_ch1: matched `cell line` in "cell line: hepaRG"
- GSM6206875 / Sample_characteristics_ch1: matched `cell line` in "cell line: hepaRG"
- GSM6206876 / Sample_characteristics_ch1: matched `cell line` in "cell line: hepaRG"
- GSM6206877 / Sample_characteristics_ch1: matched `cell line` in "cell line: hepaRG"
- GSM6206878 / Sample_characteristics_ch1: matched `cell line` in "cell line: hepaRG"
- GSM6206879 / Sample_characteristics_ch1: matched `cell line` in "cell line: hepaRG"
- GSM6206880 / Sample_characteristics_ch1: matched `cell line` in "cell line: hepaRG"
- GSM6206881 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary human hepatocyte"
- GSM6206882 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary human hepatocyte"
- GSM6206883 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary human hepatocyte"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 12 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (12/12 samples)
<!-- /computed -->