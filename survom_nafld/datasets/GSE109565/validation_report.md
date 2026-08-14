# Validation report: GSE109565

Identification of transcriptome and metabolome signatures of fatty liver disease in HepaRG cells exposed to PCB 126 and glyphosate

<!-- computed -->
Sample count: 40

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 40 samples |
| organism_consistency | PASS | Homo sapiens 40/40 |
| source_tissue | PASS | liver-pattern source 40/40 |
| library_strategy | PASS | RNA-Seq 40/40 |
| library_source | PASS | transcriptomic 40/40 |
| library_selection | PASS | cDNA 40/40 |
| instrument_model | PASS | Illumina NextSeq 500 40/40 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: HepaRG, cell line (40/40 samples) |
| expression_data_availability | PASS | processed series-level file: GSE109565_Mesnage_et_al._Glyphosate_HepaRG_FPKM_Data.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE109565_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX3595402, https://www.ncbi.nlm.nih.gov/sra?term=SRX3595403, https://www.ncbi.nlm.nih.gov/sra?term=SRX3595404, https://www.ncbi.nlm.nih.gov/sra?term=SRX3595405, https://www.ncbi.nlm.nih.gov/sra?term=SRX3595406, and 35 more (see sample_metadata.csv) |

## Canonical field distributions

- **treatment**: Control | PCB 126 (5), Glyphosate_0.1g/L | glyphosate (5), Glyphosate_10ug/L | glyphosate (5), Glyphosate_1mg/L | glyphosate (5), PCB_100pM | PCB 126 (5), PCB_10nM | PCB 126 (5), PCB_1uM | PCB 126 (5), Roundup_10ug/L | Roundup (5)

## Field presence

- agent: 40/40 (canon: treatment)
- cell line: 40/40
- cell type: 40/40
- treatment: 40/40 (canon: treatment)

## Evidence for WARN/FAIL checks

### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE109565 / Series_title: matched `fatty liver` in "Identification of transcriptome and metabolome signatures of fatty liver disease in HepaRG cells exposed to PCB 126 and glyphosate"
- GSE109565 / Series_summary: matched `steatosis` in "We provide here the alterations in gene expression profiles of HepaRG cells, a validated model for cellular steatosis, exposed to three concentration of the polychlorinated biphenyl (PCB) 126, one of "
### material_type (WARN)
- GSM2946622 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946623 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946624 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946625 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946626 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946627 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946628 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946629 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946630 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946631 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946632 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946633 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946634 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946635 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946636 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946637 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946638 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946639 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946640 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946641 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946642 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946643 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946644 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946645 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946646 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946647 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946648 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946649 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946650 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946651 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946652 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946653 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946654 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946655 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946656 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946657 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946658 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946659 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946660 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946661 / Sample_source_name_ch1: matched `HepaRG` in "HepaRGTM cells (HPR 116)"
- GSM2946622 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946623 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946624 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946625 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946626 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946627 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946628 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946629 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946630 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946631 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946632 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946633 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946634 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946635 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946636 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946637 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946638 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946639 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946640 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946641 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946642 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946643 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946644 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946645 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946646 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946647 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946648 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946649 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946650 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946651 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946652 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946653 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946654 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946655 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946656 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946657 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946658 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946659 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946660 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"
- GSM2946661 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRGTM cells (HPR 116)"

Decision: MANUAL_REVIEW

Reasons:
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: HepaRG, cell line (40/40 samples)
<!-- /computed -->