# Validation report: GSE330266

Hepatocyte Hedgehog Signaling Controls Ferroptosis to Alleviate Aging-related Organ Dysfunction

<!-- computed -->
Sample count: 10

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 10 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 10/10 |
| source_tissue | PASS | liver-pattern source 10/10 |
| library_strategy | PASS | RNA-Seq 10/10 |
| library_source | WARN | library_source: transcriptomic single cell 10/10 |
| library_selection | PASS | cDNA 10/10 |
| instrument_model | PASS | Illumina NovaSeq 6000 10/10 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (4 sample(s)) |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: 10x, Single-nucleus, single-nucleus (10 sample(s)) |
| material_type | WARN | cell/culture terms in sample metadata: cell line (10/10 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX33257231, https://www.ncbi.nlm.nih.gov/sra?term=SRX33257232, https://www.ncbi.nlm.nih.gov/sra?term=SRX33257233, https://www.ncbi.nlm.nih.gov/sra?term=SRX33257234, https://www.ncbi.nlm.nih.gov/sra?term=SRX33257235, and 5 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE330266_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX33257231, https://www.ncbi.nlm.nih.gov/sra?term=SRX33257232, https://www.ncbi.nlm.nih.gov/sra?term=SRX33257233, https://www.ncbi.nlm.nih.gov/sra?term=SRX33257234, https://www.ncbi.nlm.nih.gov/sra?term=SRX33257235, and 5 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Liver (10)

## Field presence

- cell line: 10/10
- cell type: 10/10
- tissue: 10/10 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### library_source (WARN)
### metadata_completeness (WARN)
### single_cell_or_spatial (FAIL)
- GSM9722699 / Sample_extract_protocol_ch1: matched `single-nucleus` in "Flash-frozen liver tissue was processed for single-nucleus RNA extraction under cold conditions. Tissue was minced and homogenized in ice-cold nuclei isolation buffer containing detergent and RNase in"
- GSM9722699 / Sample_extract_protocol_ch1: matched `Single-nucleus` in "Single-nucleus RNA-seq libraries were constructed using the 10x Genomics Chromium platform according to the manufacturer’s instructions. Briefly, isolated nuclei were loaded onto a Chromium chip for G"
- GSM9722700 / Sample_extract_protocol_ch1: matched `single-nucleus` in "Flash-frozen liver tissue was processed for single-nucleus RNA extraction under cold conditions. Tissue was minced and homogenized in ice-cold nuclei isolation buffer containing detergent and RNase in"
- GSM9722700 / Sample_extract_protocol_ch1: matched `Single-nucleus` in "Single-nucleus RNA-seq libraries were constructed using the 10x Genomics Chromium platform according to the manufacturer’s instructions. Briefly, isolated nuclei were loaded onto a Chromium chip for G"
- GSM9722701 / Sample_extract_protocol_ch1: matched `single-nucleus` in "Flash-frozen liver tissue was processed for single-nucleus RNA extraction under cold conditions. Tissue was minced and homogenized in ice-cold nuclei isolation buffer containing detergent and RNase in"
- GSM9722701 / Sample_extract_protocol_ch1: matched `Single-nucleus` in "Single-nucleus RNA-seq libraries were constructed using the 10x Genomics Chromium platform according to the manufacturer’s instructions. Briefly, isolated nuclei were loaded onto a Chromium chip for G"
- GSM9722702 / Sample_extract_protocol_ch1: matched `single-nucleus` in "Flash-frozen liver tissue was processed for single-nucleus RNA extraction under cold conditions. Tissue was minced and homogenized in ice-cold nuclei isolation buffer containing detergent and RNase in"
- GSM9722702 / Sample_extract_protocol_ch1: matched `Single-nucleus` in "Single-nucleus RNA-seq libraries were constructed using the 10x Genomics Chromium platform according to the manufacturer’s instructions. Briefly, isolated nuclei were loaded onto a Chromium chip for G"
- GSM9722703 / Sample_extract_protocol_ch1: matched `single-nucleus` in "Flash-frozen liver tissue was processed for single-nucleus RNA extraction under cold conditions. Tissue was minced and homogenized in ice-cold nuclei isolation buffer containing detergent and RNase in"
- GSM9722703 / Sample_extract_protocol_ch1: matched `Single-nucleus` in "Single-nucleus RNA-seq libraries were constructed using the 10x Genomics Chromium platform according to the manufacturer’s instructions. Briefly, isolated nuclei were loaded onto a Chromium chip for G"
- GSM9722704 / Sample_extract_protocol_ch1: matched `single-nucleus` in "Flash-frozen liver tissue was processed for single-nucleus RNA extraction under cold conditions. Tissue was minced and homogenized in ice-cold nuclei isolation buffer containing detergent and RNase in"
- GSM9722704 / Sample_extract_protocol_ch1: matched `Single-nucleus` in "Single-nucleus RNA-seq libraries were constructed using the 10x Genomics Chromium platform according to the manufacturer’s instructions. Briefly, isolated nuclei were loaded onto a Chromium chip for G"
- GSM9722705 / Sample_extract_protocol_ch1: matched `single-nucleus` in "Flash-frozen liver tissue was processed for single-nucleus RNA extraction under cold conditions. Tissue was minced and homogenized in ice-cold nuclei isolation buffer containing detergent and RNase in"
- GSM9722705 / Sample_extract_protocol_ch1: matched `Single-nucleus` in "Single-nucleus RNA-seq libraries were constructed using the 10x Genomics Chromium platform according to the manufacturer’s instructions. Briefly, isolated nuclei were loaded onto a Chromium chip for G"
- GSM9722706 / Sample_extract_protocol_ch1: matched `single-nucleus` in "Flash-frozen liver tissue was processed for single-nucleus RNA extraction under cold conditions. Tissue was minced and homogenized in ice-cold nuclei isolation buffer containing detergent and RNase in"
- GSM9722706 / Sample_extract_protocol_ch1: matched `Single-nucleus` in "Single-nucleus RNA-seq libraries were constructed using the 10x Genomics Chromium platform according to the manufacturer’s instructions. Briefly, isolated nuclei were loaded onto a Chromium chip for G"
- GSM9722707 / Sample_extract_protocol_ch1: matched `single-nucleus` in "Flash-frozen liver tissue was processed for single-nucleus RNA extraction under cold conditions. Tissue was minced and homogenized in ice-cold nuclei isolation buffer containing detergent and RNase in"
- GSM9722707 / Sample_extract_protocol_ch1: matched `Single-nucleus` in "Single-nucleus RNA-seq libraries were constructed using the 10x Genomics Chromium platform according to the manufacturer’s instructions. Briefly, isolated nuclei were loaded onto a Chromium chip for G"
- GSM9722708 / Sample_extract_protocol_ch1: matched `single-nucleus` in "Flash-frozen liver tissue was processed for single-nucleus RNA extraction under cold conditions. Tissue was minced and homogenized in ice-cold nuclei isolation buffer containing detergent and RNase in"
- GSM9722708 / Sample_extract_protocol_ch1: matched `Single-nucleus` in "Single-nucleus RNA-seq libraries were constructed using the 10x Genomics Chromium platform according to the manufacturer’s instructions. Briefly, isolated nuclei were loaded onto a Chromium chip for G"
- GSM9722699 / Sample_data_processing: matched `10x` in "Raw sequencing data were processed using the 10x Genomics Cell Ranger pipeline."
- GSM9722700 / Sample_data_processing: matched `10x` in "Raw sequencing data were processed using the 10x Genomics Cell Ranger pipeline."
- GSM9722701 / Sample_data_processing: matched `10x` in "Raw sequencing data were processed using the 10x Genomics Cell Ranger pipeline."
- GSM9722702 / Sample_data_processing: matched `10x` in "Raw sequencing data were processed using the 10x Genomics Cell Ranger pipeline."
- GSM9722703 / Sample_data_processing: matched `10x` in "Raw sequencing data were processed using the 10x Genomics Cell Ranger pipeline."
- GSM9722704 / Sample_data_processing: matched `10x` in "Raw sequencing data were processed using the 10x Genomics Cell Ranger pipeline."
- GSM9722705 / Sample_data_processing: matched `10x` in "Raw sequencing data were processed using the 10x Genomics Cell Ranger pipeline."
- GSM9722706 / Sample_data_processing: matched `10x` in "Raw sequencing data were processed using the 10x Genomics Cell Ranger pipeline."
- GSM9722707 / Sample_data_processing: matched `10x` in "Raw sequencing data were processed using the 10x Genomics Cell Ranger pipeline."
- GSM9722708 / Sample_data_processing: matched `10x` in "Raw sequencing data were processed using the 10x Genomics Cell Ranger pipeline."
### material_type (WARN)
- GSM9722699 / Sample_characteristics_ch1: matched `cell line` in "cell line: Tissue"
- GSM9722700 / Sample_characteristics_ch1: matched `cell line` in "cell line: Tissue"
- GSM9722701 / Sample_characteristics_ch1: matched `cell line` in "cell line: Tissue"
- GSM9722702 / Sample_characteristics_ch1: matched `cell line` in "cell line: Tissue"
- GSM9722703 / Sample_characteristics_ch1: matched `cell line` in "cell line: Tissue"
- GSM9722704 / Sample_characteristics_ch1: matched `cell line` in "cell line: Tissue"
- GSM9722705 / Sample_characteristics_ch1: matched `cell line` in "cell line: Tissue"
- GSM9722706 / Sample_characteristics_ch1: matched `cell line` in "cell line: Tissue"
- GSM9722707 / Sample_characteristics_ch1: matched `cell line` in "cell line: Tissue"
- GSM9722708 / Sample_characteristics_ch1: matched `cell line` in "cell line: Tissue"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: 10x, Single-nucleus, single-nucleus (10 sample(s)))
<!-- /computed -->