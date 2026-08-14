# Validation report: GSE143319

Inhibition of Grb14, a negative modulator of insulin signaling,  improves glucose homeostasis without causing cardiac dysfunction

<!-- computed -->
Sample count: 50

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 50 samples |
| organism_consistency | PASS | Homo sapiens 50/50 |
| source_tissue | WARN | liver-pattern source 0/50; off-target tissue signal detected |
| library_strategy | PASS | RNA-Seq 50/50 |
| library_source | PASS | transcriptomic 50/50 |
| library_selection | PASS | cDNA 50/50 |
| instrument_model | PASS | Illumina HiSeq 4000 50/50 |
| metadata_completeness | PASS | reported consistently: disease; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade, tissue, treatment |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE143319_MHOvsMUO_FPKM.xlsx |
| series_matrix | INFO | present, metadata-only (GSE143319_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX7523613, https://www.ncbi.nlm.nih.gov/sra?term=SRX7523614, https://www.ncbi.nlm.nih.gov/sra?term=SRX7523615, https://www.ncbi.nlm.nih.gov/sra?term=SRX7523616, https://www.ncbi.nlm.nih.gov/sra?term=SRX7523617, and 45 more (see sample_metadata.csv) |

## Canonical field distributions

- **disease**: MHO (15), MUO (15), Post (10), Pre (10)

## Field presence

- condition: 50/50 (canon: disease)

## Evidence for WARN/FAIL checks

### source_tissue (WARN)
- GSM4257063 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257064 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257065 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257066 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257067 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257068 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257069 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257070 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257071 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257072 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257073 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257074 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257075 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257076 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257077 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257078 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257079 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257080 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257081 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257082 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257083 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257084 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257085 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257086 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257087 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257088 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257089 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257090 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257091 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257092 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257093 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257094 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257095 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257096 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257097 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257098 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257099 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257100 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257101 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257102 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257103 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257104 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257105 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257106 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257107 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257108 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257109 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257110 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257111 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4257112 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
### disease_relevance (WARN)
- GSE143319 / Series_summary: matched `steatohepatitis` in "Insulin resistance increases patient’s risk of developing type 2 diabetes (T2D), nonalcoholic  steatohepatitis (NASH) and a host of other comorbidities including  cardiovascular disease and cancer. At"

Decision: MANUAL_REVIEW

Reasons:
- source_tissue: liver-pattern source 0/50; off-target tissue signal detected
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
<!-- /computed -->