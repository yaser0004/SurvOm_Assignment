# Validation report: GSE336962

Advancing probabilistic risk assessment of perfluorooctanoic acid through integration of in vitro data and physiologically based toxicokinetic modeling coupled with population-specific analysis

<!-- computed -->
Sample count: 36

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 36 samples |
| organism_consistency | PASS | Homo sapiens 36/36 |
| source_tissue | WARN | liver-pattern source 0/36 |
| library_strategy | PASS | RNA-Seq 36/36 |
| library_source | PASS | transcriptomic 36/36 |
| library_selection | PASS | cDNA 36/36 |
| instrument_model | PASS | DNBSEQ-G400 36/36 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: EA.hy926, cell line (36/36 samples) |
| expression_data_availability | PASS | processed series-level file: GSE336962_PA_12w_normalized_counts.csv.gz |
| series_matrix | INFO | present, metadata-only (GSE336962_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX34096018, https://www.ncbi.nlm.nih.gov/sra?term=SRX34096019, https://www.ncbi.nlm.nih.gov/sra?term=SRX34096020, https://www.ncbi.nlm.nih.gov/sra?term=SRX34096021, https://www.ncbi.nlm.nih.gov/sra?term=SRX34096022, and 31 more (see sample_metadata.csv) |

## Canonical field distributions

- **treatment**: 1 nM PFOA (6), 1 uM PFOA (3), 10 nM PFOA (6), 10 uM PFOA (3), 100 nM PFOA (6), 100 uM PFOA (3), Control (9)

## Field presence

- cell line: 36/36
- cell type: 36/36
- genotype: 36/36
- time: 36/36
- treatment: 36/36 (canon: treatment)

## Evidence for WARN/FAIL checks

### source_tissue (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE336962 / Series_summary: matched `NAFLD` in "Current human health risk assessment for perfluorooctanoic acid (PFOA) has proven inadequate due to a lack of innovative approaches. Here, we applied benchmark dose-response modeling to derive benchma"
### material_type (WARN)
- GSM9845425 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845426 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845427 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845428 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845429 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845430 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845431 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845432 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845433 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845434 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845435 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845436 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845437 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845438 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845439 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845440 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845441 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845442 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845443 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845444 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845445 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845446 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845447 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845448 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845449 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845450 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845451 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845452 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845453 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845454 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845455 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845456 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845457 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845458 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845459 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845460 / Sample_source_name_ch1: matched `EA.hy926` in "EA.hy926"
- GSM9845425 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA Control, 6 weeks, biological replicate 1"
- GSM9845426 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA Control, 6 weeks, biological replicate 2"
- GSM9845427 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA Control, 6 weeks, biological replicate 3"
- GSM9845428 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 1nM, 6 weeks, biological replicate 1"
- GSM9845429 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 1nM, 6 weeks, biological replicate 2"
- GSM9845430 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 1nM, 6 weeks, biological replicate 3"
- GSM9845431 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 10nM, 6 weeks, biological replicate 1"
- GSM9845432 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 10nM, 6 weeks, biological replicate 2"
- GSM9845433 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 10nM, 6 weeks, biological replicate 3"
- GSM9845434 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 100nM, 6 weeks, biological replicate 1"
- GSM9845435 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 100nM, 6 weeks, biological replicate 2"
- GSM9845436 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 100nM, 6 weeks, biological replicate 3"
- GSM9845437 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA Control, 12 weeks, biological replicate 1"
- GSM9845438 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA Control, 12 weeks, biological replicate 2"
- GSM9845439 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA Control, 12 weeks, biological replicate 3"
- GSM9845440 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 1nM, 12 weeks, biological replicate 1"
- GSM9845441 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 1nM, 12 weeks, biological replicate 2"
- GSM9845442 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 1nM, 12 weeks, biological replicate 3"
- GSM9845443 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 10nM, 12 weeks, biological replicate 1"
- GSM9845444 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 10nM, 12 weeks, biological replicate 2"
- GSM9845445 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 10nM, 12 weeks, biological replicate 3"
- GSM9845446 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 100nM, 12 weeks, biological replicate 1"
- GSM9845447 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 100nM, 12 weeks, biological replicate 2"
- GSM9845448 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 100nM, 12 weeks, biological replicate 3"
- GSM9845449 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA Control, 48h, biological replicate 1"
- GSM9845450 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA Control, 48h, biological replicate 2"
- GSM9845451 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA Control, 48h, biological replicate 3"
- GSM9845452 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 1uM, 48h, biological replicate 1"
- GSM9845453 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 1uM, 48h, biological replicate 2"
- GSM9845454 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 1uM, 48h, biological replicate 3"
- GSM9845455 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 10uM, 48h, biological replicate 1"
- GSM9845456 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 10uM, 48h, biological replicate 2"
- GSM9845457 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 10uM, 48h, biological replicate 3"
- GSM9845458 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 100uM, 48h, biological replicate 1"
- GSM9845459 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 100uM, 48h, biological replicate 2"
- GSM9845460 / Sample_title: matched `EA.hy926` in "EA.hy926 cells, PFOA 100uM, 48h, biological replicate 3"
- GSM9845425 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845426 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845427 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845428 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845429 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845430 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845431 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845432 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845433 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845434 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845435 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845436 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845437 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845438 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845439 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845440 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845441 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845442 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845443 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845444 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845445 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845446 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845447 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845448 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845449 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845450 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845451 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845452 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845453 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845454 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845455 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845456 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845457 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845458 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845459 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"
- GSM9845460 / Sample_characteristics_ch1: matched `cell line` in "cell line: EA.hy926"

Decision: MANUAL_REVIEW

Reasons:
- source_tissue: liver-pattern source 0/36
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: EA.hy926, cell line (36/36 samples)
<!-- /computed -->