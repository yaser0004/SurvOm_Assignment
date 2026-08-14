# Validation report: GSE210140

Gene expression profiling of stress-induced senescence and paracrine senecence in human hepatocytes

<!-- computed -->
Sample count: 20

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 20 samples |
| organism_consistency | PASS | Homo sapiens 20/20 |
| source_tissue | PASS | liver-pattern source 20/20 |
| library_strategy | PASS | RNA-Seq 20/20 |
| library_source | PASS | transcriptomic 20/20 |
| library_selection | PASS | cDNA 20/20 |
| instrument_model | PASS | Illumina NovaSeq 6000 20/20 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (20/20 samples) |
| expression_data_availability | PASS | processed series-level file: GSE210140_UJ3100_exp_gene_level_tpm.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE210140_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX16743606, https://www.ncbi.nlm.nih.gov/sra?term=SRX16743607, https://www.ncbi.nlm.nih.gov/sra?term=SRX16743608, https://www.ncbi.nlm.nih.gov/sra?term=SRX16743609, https://www.ncbi.nlm.nih.gov/sra?term=SRX16743610, and 15 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: liver (20)
- **treatment**: Conditioned medium (Ctrl) (5), Conditioned medium (DOX-treated IHH) (5), Control (5), DOX (2uM) (5)

## Field presence

- cell line: 20/20
- cell type: 20/20
- genotype: 20/20
- tissue: 20/20 (canon: tissue)
- treatment: 20/20 (canon: treatment)

## Evidence for WARN/FAIL checks

### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE210140 / Series_summary: matched `NAFLD` in "Hepatocytes undergo senescence during development and progression of NAFLD. In order to better understand the phenotype of these senescent cells we generated an in vitro model of stress-induced senesc"
### material_type (WARN)
- GSM6422725 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6422726 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6422727 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6422728 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6422729 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6422730 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6422731 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6422732 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6422733 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6422734 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6422735 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6422736 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6422737 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6422738 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6422739 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6422740 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6422741 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6422742 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6422743 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"
- GSM6422744 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human hepatocytes (IHH)"

Decision: MANUAL_REVIEW

Reasons:
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (20/20 samples)
<!-- /computed -->