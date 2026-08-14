# Validation report: GSE223652

Hepatocyte mARC1 Promotes Fatty Liver Disease

<!-- computed -->
Sample count: 60

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 60 samples |
| organism_consistency | PASS | Homo sapiens 60/60 |
| source_tissue | PASS | liver-pattern source 60/60 |
| library_strategy | PASS | RNA-Seq 60/60 |
| library_source | PASS | transcriptomic 60/60 |
| library_selection | PASS | cDNA 60/60 |
| instrument_model | PASS | Illumina NextSeq 500 60/60 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (60/60 samples) |
| expression_data_availability | PASS | processed series-level file: GSE223652_counts_matrix_for_GEO_final.csv.gz |
| series_matrix | INFO | present, metadata-only (GSE223652_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX19162112, https://www.ncbi.nlm.nih.gov/sra?term=SRX19162113, https://www.ncbi.nlm.nih.gov/sra?term=SRX19162114, https://www.ncbi.nlm.nih.gov/sra?term=SRX19162115, https://www.ncbi.nlm.nih.gov/sra?term=SRX19162116, and 55 more (see sample_metadata.csv) |

## Field presence

- cell line: 60/60
- cell type: 60/60
- donor id: 60/60
- genotype: 60/60
- perturbation: 60/60
- sirna: 60/60

## Evidence for WARN/FAIL checks

### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE223652 / Series_title: matched `Fatty Liver` in "Hepatocyte mARC1 Promotes Fatty Liver Disease"
- GSE223652 / Series_summary: matched `Non-alcoholic fatty liver` in "Non-alcoholic fatty liver disease (NAFLD) has a prevalence of ~25% worldwide, with significant public health consequences yet has few effective treatments. Human genetics can help elucidate novel biol"
- GSE223652 / Series_summary: matched `NASH` in "Analyses including multi-trait colocalization and Mendelian randomization were used to assess the genetic associations of MTARC1. In addition, we established an in vitro long-term primary human hepato"
- GSE223652 / Series_summary: matched `NAFLD` in "Collectively, our findings from human genetics, and in vitro and in vivo hepatocyte-specific mARC1 knockdown support the potential efficacy of hepatocyte-specific targeting of mARC1 for treatment of N"
### material_type (WARN)
- GSM6970005 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970006 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970007 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970008 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970009 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970010 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970011 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970012 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970013 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970014 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970015 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970016 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970017 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970018 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970019 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970020 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970021 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970022 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970023 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970024 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970025 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970026 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970027 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970028 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970029 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970030 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970031 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970032 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970033 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970034 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970035 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970036 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970037 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970038 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970039 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970040 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970041 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970042 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970043 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970044 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970045 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970046 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970047 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970048 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970049 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970050 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970051 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970052 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970053 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970054 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970055 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970056 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970057 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970058 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970059 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970060 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970061 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970062 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970063 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM6970064 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"

Decision: MANUAL_REVIEW

Reasons:
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (60/60 samples)
<!-- /computed -->