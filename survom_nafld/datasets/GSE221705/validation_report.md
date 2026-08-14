# Validation report: GSE221705

Transcriptomic characterization of control and drug-treated APOB-mutant organoids to study steatosis-resolving drug effects

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
| instrument_model | PASS | NextSeq 2000 12/12 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line, organoid (12/12 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX18840739, https://www.ncbi.nlm.nih.gov/sra?term=SRX18840740, https://www.ncbi.nlm.nih.gov/sra?term=SRX18840741, https://www.ncbi.nlm.nih.gov/sra?term=SRX18840742, https://www.ncbi.nlm.nih.gov/sra?term=SRX18840743, and 7 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE221705_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX18840739, https://www.ncbi.nlm.nih.gov/sra?term=SRX18840740, https://www.ncbi.nlm.nih.gov/sra?term=SRX18840741, https://www.ncbi.nlm.nih.gov/sra?term=SRX18840742, https://www.ncbi.nlm.nih.gov/sra?term=SRX18840743, and 7 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Liver (12)
- **treatment**: ACCi 7 days (2), DGAT2i 7 days (2), FASi 7 days (2), FGF19 7 days (2), FXRa 7 days (2), vehicle 7 days (2)

## Field presence

- cell line: 12/12
- cell type: 12/12
- genotype: 12/12
- individual: 12/12
- tissue: 12/12 (canon: tissue)
- treatment: 12/12 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE221705 / Series_title: matched `steatosis` in "Transcriptomic characterization of control and drug-treated APOB-mutant organoids to study steatosis-resolving drug effects"
- GSE221705 / Series_summary: matched `NAFLD` in "We treated APOB-mutant organoids with different anti-NAFLD drug candidates that were effective at resolving steatosis. To understand the mechanisms of drug action and adverse drug effects we performed"
### material_type (WARN)
- GSM6893374 / Sample_title: matched `organoid` in "ACCi treated APOB-/- organoids from donor 1"
- GSM6893375 / Sample_title: matched `organoid` in "vehicle treated APOB-/- organoids from donor 1"
- GSM6893376 / Sample_title: matched `organoid` in "DGAT2i treated APOB-/- organoids from donor 1"
- GSM6893377 / Sample_title: matched `organoid` in "FASi treated APOB-/- organoids from donor 1"
- GSM6893378 / Sample_title: matched `organoid` in "FGF19 treated APOB-/- organoids from donor 1"
- GSM6893379 / Sample_title: matched `organoid` in "ACCi treated APOB-/- organoids from donor 2"
- GSM6893380 / Sample_title: matched `organoid` in "vehicle treated APOB-/- organoids from donor 2"
- GSM6893381 / Sample_title: matched `organoid` in "DGAT2i treated APOB-/- organoids from donor 2"
- GSM6893382 / Sample_title: matched `organoid` in "FASi treated APOB-/- organoids from donor 2"
- GSM6893383 / Sample_title: matched `organoid` in "FGF19 treated APOB-/- organoids from donor 2"
- GSM6893384 / Sample_title: matched `organoid` in "FXRa treated APOB-/- organoids from donor 1"
- GSM6893385 / Sample_title: matched `organoid` in "FXRa treated APOB-/- organoids from donor 2"
- GSM6893374 / Sample_characteristics_ch1: matched `cell line` in "cell line: Human hepatocyte organoid"
- GSM6893375 / Sample_characteristics_ch1: matched `cell line` in "cell line: Human hepatocyte organoid"
- GSM6893376 / Sample_characteristics_ch1: matched `cell line` in "cell line: Human hepatocyte organoid"
- GSM6893377 / Sample_characteristics_ch1: matched `cell line` in "cell line: Human hepatocyte organoid"
- GSM6893378 / Sample_characteristics_ch1: matched `cell line` in "cell line: Human hepatocyte organoid"
- GSM6893379 / Sample_characteristics_ch1: matched `cell line` in "cell line: Human hepatocyte organoid"
- GSM6893380 / Sample_characteristics_ch1: matched `cell line` in "cell line: Human hepatocyte organoid"
- GSM6893381 / Sample_characteristics_ch1: matched `cell line` in "cell line: Human hepatocyte organoid"
- GSM6893382 / Sample_characteristics_ch1: matched `cell line` in "cell line: Human hepatocyte organoid"
- GSM6893383 / Sample_characteristics_ch1: matched `cell line` in "cell line: Human hepatocyte organoid"
- GSM6893384 / Sample_characteristics_ch1: matched `cell line` in "cell line: Human hepatocyte organoid"
- GSM6893385 / Sample_characteristics_ch1: matched `cell line` in "cell line: Human hepatocyte organoid"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 12 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line, organoid (12/12 samples)
<!-- /computed -->