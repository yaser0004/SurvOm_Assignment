# Validation report: GSE186329

Activation of GPR3-b-Arrestin2-PKM2 by DPI enhanced glycolysis in kupffer cells

<!-- computed -->
Sample count: 19

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 19 samples (below 20) |
| organism_consistency | WARN | mixed organisms: Homo sapiens 10/19, Mus musculus 9/19 |
| source_tissue | PASS | liver-pattern source 19/19 |
| library_strategy | PASS | RNA-Seq 19/19 |
| library_source | PASS | transcriptomic 19/19 |
| library_selection | PASS | cDNA 19/19 |
| instrument_model | WARN | mixed instruments: Illumina HiSeq 2000 9/19, Illumina NovaSeq 6000 10/19 |
| metadata_completeness | WARN | patchy fields: diagnosis 6/19, treatment 13/19. reported consistently: tissue; not reported anywhere: age, bmi, disease, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (3 sample(s)) |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: 10x, Cell Ranger, Single-cell suspension (6 sample(s)) |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX12724896, https://www.ncbi.nlm.nih.gov/sra?term=SRX12724897, https://www.ncbi.nlm.nih.gov/sra?term=SRX12724898, https://www.ncbi.nlm.nih.gov/sra?term=SRX12724899, https://www.ncbi.nlm.nih.gov/sra?term=SRX12724900, and 14 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE186329-GPL13112_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX12724896, https://www.ncbi.nlm.nih.gov/sra?term=SRX12724897, https://www.ncbi.nlm.nih.gov/sra?term=SRX12724898, https://www.ncbi.nlm.nih.gov/sra?term=SRX12724899, https://www.ncbi.nlm.nih.gov/sra?term=SRX12724900, and 14 more (see sample_metadata.csv) |

## Canonical field distributions

- **diagnosis**: NAFLD (3), healthy (3)
- **tissue**: liver (19)
- **treatment**: DMSO (2), DPI (6), n/a (2), vehicle (3)

## Field presence

- cell type: 19/19
- diagnosis: 6/19 (canon: diagnosis)
- diet: 9/19
- donor: 4/19
- tissue: 19/19 (canon: tissue)
- treatment: 13/19 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### organism_consistency (WARN)
### instrument_model (WARN)
### metadata_completeness (WARN)
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