# Validation report: GSE286572

Hepatocyte reporter cells and integrated metabolomic and transcriptomic analyses reveal insights into hepatocyte changes in offspring of pregnancies with obesity

<!-- computed -->
Sample count: 30

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 30 samples |
| organism_consistency | PASS | Homo sapiens 30/30 |
| source_tissue | WARN | liver-pattern source 30/30; off-target tissue signal detected |
| library_strategy | PASS | RNA-Seq 30/30 |
| library_source | PASS | transcriptomic 30/30 |
| library_selection | PASS | cDNA 30/30 |
| instrument_model | PASS | Illumina NovaSeq 6000 30/30 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: HepaRG, cell line (30/30 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX27340496, https://www.ncbi.nlm.nih.gov/sra?term=SRX27340497, https://www.ncbi.nlm.nih.gov/sra?term=SRX27340498, https://www.ncbi.nlm.nih.gov/sra?term=SRX27340499, https://www.ncbi.nlm.nih.gov/sra?term=SRX27340500, and 25 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE286572_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX27340496, https://www.ncbi.nlm.nih.gov/sra?term=SRX27340497, https://www.ncbi.nlm.nih.gov/sra?term=SRX27340498, https://www.ncbi.nlm.nih.gov/sra?term=SRX27340499, https://www.ncbi.nlm.nih.gov/sra?term=SRX27340500, and 25 more (see sample_metadata.csv) |

## Canonical field distributions

- **treatment**: normal weight cord plasma (15), obese cord plasma (15)

## Field presence

- cell line: 30/30
- cell type: 30/30
- treatment: 30/30 (canon: treatment)

## Evidence for WARN/FAIL checks

### source_tissue (WARN)
- GSM8729563 / Sample_characteristics_ch1: matched `plasma` in "treatment: obese cord plasma"
- GSM8729564 / Sample_characteristics_ch1: matched `plasma` in "treatment: normal weight cord plasma"
- GSM8729565 / Sample_characteristics_ch1: matched `plasma` in "treatment: obese cord plasma"
- GSM8729566 / Sample_characteristics_ch1: matched `plasma` in "treatment: normal weight cord plasma"
- GSM8729567 / Sample_characteristics_ch1: matched `plasma` in "treatment: normal weight cord plasma"
- GSM8729568 / Sample_characteristics_ch1: matched `plasma` in "treatment: obese cord plasma"
- GSM8729569 / Sample_characteristics_ch1: matched `plasma` in "treatment: normal weight cord plasma"
- GSM8729570 / Sample_characteristics_ch1: matched `plasma` in "treatment: normal weight cord plasma"
- GSM8729571 / Sample_characteristics_ch1: matched `plasma` in "treatment: obese cord plasma"
- GSM8729572 / Sample_characteristics_ch1: matched `plasma` in "treatment: normal weight cord plasma"
- GSM8729573 / Sample_characteristics_ch1: matched `plasma` in "treatment: obese cord plasma"
- GSM8729574 / Sample_characteristics_ch1: matched `plasma` in "treatment: obese cord plasma"
- GSM8729575 / Sample_characteristics_ch1: matched `plasma` in "treatment: normal weight cord plasma"
- GSM8729576 / Sample_characteristics_ch1: matched `plasma` in "treatment: normal weight cord plasma"
- GSM8729577 / Sample_characteristics_ch1: matched `plasma` in "treatment: normal weight cord plasma"
- GSM8729578 / Sample_characteristics_ch1: matched `plasma` in "treatment: obese cord plasma"
- GSM8729579 / Sample_characteristics_ch1: matched `plasma` in "treatment: obese cord plasma"
- GSM8729580 / Sample_characteristics_ch1: matched `plasma` in "treatment: obese cord plasma"
- GSM8729581 / Sample_characteristics_ch1: matched `plasma` in "treatment: obese cord plasma"
- GSM8729582 / Sample_characteristics_ch1: matched `plasma` in "treatment: normal weight cord plasma"
- GSM8729583 / Sample_characteristics_ch1: matched `plasma` in "treatment: normal weight cord plasma"
- GSM8729584 / Sample_characteristics_ch1: matched `plasma` in "treatment: normal weight cord plasma"
- GSM8729585 / Sample_characteristics_ch1: matched `plasma` in "treatment: obese cord plasma"
- GSM8729586 / Sample_characteristics_ch1: matched `plasma` in "treatment: obese cord plasma"
- GSM8729587 / Sample_characteristics_ch1: matched `plasma` in "treatment: obese cord plasma"
- GSM8729588 / Sample_characteristics_ch1: matched `plasma` in "treatment: normal weight cord plasma"
- GSM8729589 / Sample_characteristics_ch1: matched `plasma` in "treatment: normal weight cord plasma"
- GSM8729590 / Sample_characteristics_ch1: matched `plasma` in "treatment: obese cord plasma"
- GSM8729591 / Sample_characteristics_ch1: matched `plasma` in "treatment: normal weight cord plasma"
- GSM8729592 / Sample_characteristics_ch1: matched `plasma` in "treatment: obese cord plasma"
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE286572 / Series_summary: matched `non-alcoholic fatty liver` in "Infants born to mothers with obesity have increased risk for later development of non-alcoholic fatty liver disease (NAFLD); however early hepatic changes that occur in these infants remain unclear. W"
### material_type (WARN)
- GSM8729563 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729564 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729565 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729566 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729567 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729568 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729569 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729570 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729571 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729572 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729573 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729574 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729575 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729576 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729577 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729578 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729579 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729580 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729581 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729582 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729583 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729584 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729585 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729586 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729587 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729588 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729589 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729590 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729591 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729592 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG cells"
- GSM8729563 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729564 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729565 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729566 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729567 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729568 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729569 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729570 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729571 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729572 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729573 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729574 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729575 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729576 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729577 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729578 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729579 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729580 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729581 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729582 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729583 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729584 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729585 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729586 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729587 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729588 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729589 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729590 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729591 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"
- GSM8729592 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG cells"

Decision: MANUAL_REVIEW

Reasons:
- source_tissue: liver-pattern source 30/30; off-target tissue signal detected
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: HepaRG, cell line (30/30 samples)
<!-- /computed -->