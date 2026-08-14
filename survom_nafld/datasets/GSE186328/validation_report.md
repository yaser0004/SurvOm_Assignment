# Validation report: GSE186328

Activation of GPR3-b-Arrestin2-PKM2 by DPI enhanced glycolysis in kupffer cells [single-cell RNA-seq]

<!-- computed -->
Sample count: 6

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 6 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 6/6 |
| source_tissue | PASS | liver-pattern source 6/6 |
| library_strategy | PASS | RNA-Seq 6/6 |
| library_source | PASS | transcriptomic 6/6 |
| library_selection | PASS | cDNA 6/6 |
| instrument_model | PASS | Illumina NovaSeq 6000 6/6 |
| metadata_completeness | PASS | reported consistently: diagnosis, tissue; not reported anywhere: age, bmi, disease, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (3 sample(s)) |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: 10x, Cell Ranger, Single-cell suspension (6 sample(s)) |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE186328_raw_counts.csv.gz |
| series_matrix | INFO | present, metadata-only (GSE186328_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX12727804, https://www.ncbi.nlm.nih.gov/sra?term=SRX12727805, https://www.ncbi.nlm.nih.gov/sra?term=SRX12727806, https://www.ncbi.nlm.nih.gov/sra?term=SRX12727807, https://www.ncbi.nlm.nih.gov/sra?term=SRX12727808, and 1 more (see sample_metadata.csv) |

## Canonical field distributions

- **diagnosis**: NAFLD (3), healthy (3)
- **tissue**: liver (6)

## Field presence

- cell type: 6/6
- diagnosis: 6/6 (canon: diagnosis)
- tissue: 6/6 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### single_cell_or_spatial (FAIL)
- GSM5643817 / Sample_extract_protocol_ch1: matched `Single-cell suspension` in "Single-cell suspensions of FACS-sorted CD45+ liver cells were resuspended and washed in 0.05% RNase-free BSA in PBS for single-cell library preparation."
- GSM5643817 / Sample_extract_protocol_ch1: matched `10x` in "10x Chromium Next GEM Single Cell 3' Kit."
- GSM5643818 / Sample_extract_protocol_ch1: matched `Single-cell suspension` in "Single-cell suspensions of FACS-sorted CD45+ liver cells were resuspended and washed in 0.05% RNase-free BSA in PBS for single-cell library preparation."
- GSM5643818 / Sample_extract_protocol_ch1: matched `10x` in "10x Chromium Next GEM Single Cell 3' Kit."
- GSM5643819 / Sample_extract_protocol_ch1: matched `Single-cell suspension` in "Single-cell suspensions of FACS-sorted CD45+ liver cells were resuspended and washed in 0.05% RNase-free BSA in PBS for single-cell library preparation."
- GSM5643819 / Sample_extract_protocol_ch1: matched `10x` in "10x Chromium Next GEM Single Cell 3' Kit."
- GSM5643820 / Sample_extract_protocol_ch1: matched `Single-cell suspension` in "Single-cell suspensions of FACS-sorted CD45+ liver cells were resuspended and washed in 0.05% RNase-free BSA in PBS for single-cell library preparation."
- GSM5643820 / Sample_extract_protocol_ch1: matched `10x` in "10x Chromium Next GEM Single Cell 3' Kit."
- GSM5643821 / Sample_extract_protocol_ch1: matched `Single-cell suspension` in "Single-cell suspensions of FACS-sorted CD45+ liver cells were resuspended and washed in 0.05% RNase-free BSA in PBS for single-cell library preparation."
- GSM5643821 / Sample_extract_protocol_ch1: matched `10x` in "10x Chromium Next GEM Single Cell 3' Kit."
- GSM5643822 / Sample_extract_protocol_ch1: matched `Single-cell suspension` in "Single-cell suspensions of FACS-sorted CD45+ liver cells were resuspended and washed in 0.05% RNase-free BSA in PBS for single-cell library preparation."
- GSM5643822 / Sample_extract_protocol_ch1: matched `10x` in "10x Chromium Next GEM Single Cell 3' Kit."
- GSM5643817 / Sample_data_processing: matched `Cell Ranger` in "Raw sequences were demultiplexed, aligned, filtered, barcode counting, unique molecular identifier (UMI) counting with Cell Ranger software v3.1 (10XGenomics) to digitalize the expression of each gene"
- GSM5643818 / Sample_data_processing: matched `Cell Ranger` in "Raw sequences were demultiplexed, aligned, filtered, barcode counting, unique molecular identifier (UMI) counting with Cell Ranger software v3.1 (10XGenomics) to digitalize the expression of each gene"
- GSM5643819 / Sample_data_processing: matched `Cell Ranger` in "Raw sequences were demultiplexed, aligned, filtered, barcode counting, unique molecular identifier (UMI) counting with Cell Ranger software v3.1 (10XGenomics) to digitalize the expression of each gene"
- GSM5643820 / Sample_data_processing: matched `Cell Ranger` in "Raw sequences were demultiplexed, aligned, filtered, barcode counting, unique molecular identifier (UMI) counting with Cell Ranger software v3.1 (10XGenomics) to digitalize the expression of each gene"
- GSM5643821 / Sample_data_processing: matched `Cell Ranger` in "Raw sequences were demultiplexed, aligned, filtered, barcode counting, unique molecular identifier (UMI) counting with Cell Ranger software v3.1 (10XGenomics) to digitalize the expression of each gene"
- GSM5643822 / Sample_data_processing: matched `Cell Ranger` in "Raw sequences were demultiplexed, aligned, filtered, barcode counting, unique molecular identifier (UMI) counting with Cell Ranger software v3.1 (10XGenomics) to digitalize the expression of each gene"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: 10x, Cell Ranger, Single-cell suspension (6 sample(s)))
<!-- /computed -->