# Validation report: GSE296996

Gene expression profiling of tunicamycin-induced ER stress in HepG2 hepatoma cells

<!-- computed -->
Sample count: 10

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 10 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 10/10 |
| source_tissue | WARN | liver-pattern source 0/10 |
| library_strategy | PASS | RNA-Seq 10/10 |
| library_source | PASS | transcriptomic 10/10 |
| library_selection | PASS | cDNA 10/10 |
| instrument_model | PASS | Illumina NextSeq 500 10/10 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: HepG2, cell line (10/10 samples) |
| expression_data_availability | PASS | processed series-level file: GSE296996_count_matrix.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE296996_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX28775049, https://www.ncbi.nlm.nih.gov/sra?term=SRX28775050, https://www.ncbi.nlm.nih.gov/sra?term=SRX28775051, https://www.ncbi.nlm.nih.gov/sra?term=SRX28775052, https://www.ncbi.nlm.nih.gov/sra?term=SRX28775053, and 5 more (see sample_metadata.csv) |

## Canonical field distributions

- **treatment**: Control (5), Tunicamycin (5)

## Field presence

- cell line: 10/10
- replicate: 10/10
- treatment: 10/10 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE296996 / Series_summary: matched `metabolic dysfunction-associated stea` in "Endoplasmic reticulum (ER) stress, a disruption of ER homeostasis, is involved in the pathophysiology of several human diseases, including metabolic dysfunction-associated steatotic liver disease (MAS"
### material_type (WARN)
- GSM8981325 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8981326 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8981327 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8981328 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8981329 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8981330 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8981331 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8981332 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8981333 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8981334 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8981325 / Sample_title: matched `HepG2` in "HepG2, Control, rep1"
- GSM8981326 / Sample_title: matched `HepG2` in "HepG2, Control, rep2"
- GSM8981327 / Sample_title: matched `HepG2` in "HepG2, Control, rep3"
- GSM8981328 / Sample_title: matched `HepG2` in "HepG2, Control, rep4"
- GSM8981329 / Sample_title: matched `HepG2` in "HepG2, Control, rep5"
- GSM8981330 / Sample_title: matched `HepG2` in "HepG2, Tunicamycin, rep1"
- GSM8981331 / Sample_title: matched `HepG2` in "HepG2, Tunicamycin, rep2"
- GSM8981332 / Sample_title: matched `HepG2` in "HepG2, Tunicamycin, rep3"
- GSM8981333 / Sample_title: matched `HepG2` in "HepG2, Tunicamycin, rep4"
- GSM8981334 / Sample_title: matched `HepG2` in "HepG2, Tunicamycin, rep5"
- GSM8981325 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8981326 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8981327 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8981328 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8981329 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8981330 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8981331 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8981332 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8981333 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8981334 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 10 samples (below 20)
- source_tissue: liver-pattern source 0/10
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: HepG2, cell line (10/10 samples)
<!-- /computed -->