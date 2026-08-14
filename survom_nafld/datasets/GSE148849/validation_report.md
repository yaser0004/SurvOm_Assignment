# Validation report: GSE148849

Gene Expression Analysis of the response to ACC inhibition

<!-- computed -->
Sample count: 74

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 74 samples |
| organism_consistency | WARN | mixed organisms: Homo sapiens 36/74, Mus musculus 38/74 |
| source_tissue | WARN | liver-pattern source 74/74; off-target tissue signal detected |
| library_strategy | PASS | RNA-Seq 74/74 |
| library_source | PASS | transcriptomic 74/74 |
| library_selection | PASS | cDNA 74/74 |
| instrument_model | WARN | mixed instruments: Illumina HiSeq 2500 38/74, Ion Torrent S5 XL 36/74 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (74/74), packaged in GSE148849_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE148849-GPL17021_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX8131154, https://www.ncbi.nlm.nih.gov/sra?term=SRX8131155, https://www.ncbi.nlm.nih.gov/sra?term=SRX8131156, https://www.ncbi.nlm.nih.gov/sra?term=SRX8131157, https://www.ncbi.nlm.nih.gov/sra?term=SRX8131158, and 69 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: liver (38)
- **treatment**: ACCi 300nM (6), ACCi_1mpk (10), ACCi_5mpk (10), DMSO (6), NA (8), TGFb 5ng/ml (6), TGFb 5ng/ml + ACCi 300nM (6), TGFb 5ng/ml + TGFi 5uM (6), TGFi 5uM (6), Vehicle (10)

## Field presence

- cell type: 36/74
- culture condition: 36/74
- diet: 38/74
- donor: 36/74
- strain: 38/74
- tissue: 38/74 (canon: tissue)
- treatment: 74/74 (canon: treatment)
- treatment time: 66/74

## Evidence for WARN/FAIL checks

### organism_consistency (WARN)
### source_tissue (WARN)
- GSM4483954 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483955 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483956 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483957 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483958 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483959 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483960 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483961 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483962 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483963 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483964 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483965 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483966 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483967 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483968 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483969 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483970 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483971 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483972 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483973 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483974 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483975 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483976 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483977 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483978 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483979 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483980 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483981 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483982 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483983 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483984 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483985 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483986 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483987 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483988 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
- GSM4483989 / Sample_characteristics_ch1: matched `serum` in "culture condition: serum free media"
### instrument_model (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE148849 / Series_summary: matched `steatohepatitis` in "BACKGROUND & AIMS: Nonalcoholic steatohepatitis (NASH) is a chronic liver disease characterized by hepatic lipid accumulation, inflammation, and progressive fibrosis. Acetyl-CoA carboxylase (ACC) cata"

Decision: MANUAL_REVIEW

Reasons:
- organism_consistency: mixed organisms: Homo sapiens 36/74, Mus musculus 38/74
- source_tissue: liver-pattern source 74/74; off-target tissue signal detected
- instrument_model: mixed instruments: Illumina HiSeq 2500 38/74, Ion Torrent S5 XL 36/74
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
<!-- /computed -->