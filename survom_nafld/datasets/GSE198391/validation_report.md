# Validation report: GSE198391

Developmental modeling of hepatogenesis using obese iPSCs-hepatocyte differentiation uncovers pathological features

<!-- computed -->
Sample count: 32

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 32 samples |
| organism_consistency | PASS | Homo sapiens 32/32 |
| source_tissue | PASS | liver-pattern source 32/32 |
| library_strategy | PASS | RNA-Seq 32/32 |
| library_source | PASS | transcriptomic 32/32 |
| library_selection | PASS | cDNA 32/32 |
| instrument_model | PASS | Illumina NextSeq 500 32/32 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: pluripotent stem cell (32/32 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX14433843, https://www.ncbi.nlm.nih.gov/sra?term=SRX14433844, https://www.ncbi.nlm.nih.gov/sra?term=SRX14433845, https://www.ncbi.nlm.nih.gov/sra?term=SRX14433846, https://www.ncbi.nlm.nih.gov/sra?term=SRX14433847, and 27 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE198391_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX14433843, https://www.ncbi.nlm.nih.gov/sra?term=SRX14433844, https://www.ncbi.nlm.nih.gov/sra?term=SRX14433845, https://www.ncbi.nlm.nih.gov/sra?term=SRX14433846, https://www.ncbi.nlm.nih.gov/sra?term=SRX14433847, and 27 more (see sample_metadata.csv) |

## Canonical field distributions

- **treatment**: control (16), palmitate (16)

## Field presence

- cell type: 32/32
- differentiation days: 32/32
- differentiation stage: 32/32
- donor weight: 32/32
- replicate: 32/32
- treatment: 32/32 (canon: treatment)

## Evidence for WARN/FAIL checks

### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE198391 / Series_summary: matched `non-alcoholic fatty liver` in "Obesity is a multigene disorder. However, in addition to genetic factors, environmental determinants also participate in developing obesity and related pathologies. Thus, obesity could be best describ"
### material_type (WARN)
- GSM5946077 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946078 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946079 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946080 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946081 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946082 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946083 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946084 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946085 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946086 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946087 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946088 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946089 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946090 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946091 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946092 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946093 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946094 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946095 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946096 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946097 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946098 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946099 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946100 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946101 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946102 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946103 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946104 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946105 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946106 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946107 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946108 / Sample_source_name_ch1: matched `pluripotent stem cell` in "Induced pluripotent stem cells"
- GSM5946077 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946078 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946079 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946080 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946081 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946082 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946083 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946084 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946085 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946086 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946087 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946088 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946089 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946090 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946091 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946092 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946093 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946094 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946095 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946096 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946097 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946098 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946099 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946100 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946101 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946102 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946103 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946104 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946105 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946106 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946107 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"
- GSM5946108 / Sample_characteristics_ch1: matched `pluripotent stem cell` in "cell type: Induced pluripotent stem cells differentiated into hepatocytes"

Decision: MANUAL_REVIEW

Reasons:
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: pluripotent stem cell (32/32 samples)
<!-- /computed -->