# Validation report: GSE267195

Single-cell landscape of peripheral immune cells in MAFLD/MASH

<!-- computed -->
Sample count: 68

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 68 samples |
| organism_consistency | PASS | Homo sapiens 68/68 |
| source_tissue | WARN | liver-pattern source 18/68 |
| library_strategy | PASS | RNA-Seq 68/68 |
| library_source | WARN | library_source: transcriptomic 53/68, transcriptomic single cell 15/68 |
| library_selection | PASS | cDNA 68/68 |
| instrument_model | PASS | Illumina NovaSeq 6000 68/68 |
| metadata_completeness | WARN | patchy fields: nas_score 53/68. reported consistently: disease, sex, tissue; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (48 sample(s)) |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: Chromium, cellranger, scRNA, scanpy (15 sample(s)) |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX24499405, https://www.ncbi.nlm.nih.gov/sra?term=SRX24499406, https://www.ncbi.nlm.nih.gov/sra?term=SRX24499407, https://www.ncbi.nlm.nih.gov/sra?term=SRX24499408, https://www.ncbi.nlm.nih.gov/sra?term=SRX24499409, and 63 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE267195_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX24499405, https://www.ncbi.nlm.nih.gov/sra?term=SRX24499406, https://www.ncbi.nlm.nih.gov/sra?term=SRX24499407, https://www.ncbi.nlm.nih.gov/sra?term=SRX24499408, https://www.ncbi.nlm.nih.gov/sra?term=SRX24499409, and 63 more (see sample_metadata.csv) |

## Canonical field distributions

- **disease**: Control | 0_healthy (20), MAFLD/MASH | 1_low (15), MAFLD/MASH | 2_medium (16), MAFLD/MASH | 3_high (17)
- **nas_score**: 0 (2), 1 (7), 2 (4), 3 (5), 4 (7), 5 (4), 6 (8), 8 (2), n/a (14)
- **sex**: f (16), female (18), m (17), male (17)
- **tissue**: Liver (18), White blood cells (50)

## Field presence

- Sex: 68/68 (canon: sex)
- assaytype: 50/68
- batch: 68/68
- celltype: 68/68
- condition: 68/68 (canon: disease)
- disease: 68/68 (canon: disease)
- id sample: 33/68
- id_sample: 35/68
- nas: 53/68 (canon: nas_score)
- tissue: 68/68 (canon: tissue)
- type patient: 33/68
- type_patient: 35/68

## Evidence for WARN/FAIL checks

### source_tissue (WARN)
### library_source (WARN)
### metadata_completeness (WARN)
### single_cell_or_spatial (FAIL)
- GSM8258781 / Sample_extract_protocol_ch1: matched `scRNA` in "For scRNA-seq, isolated WBCs were resuspended in ice-cold buffer (1xPBS + 0.04% BSA) and filtered through a 40µm Flowmi® cell filter (Partec). Cell concentration, viability, and aggregate were determi"
- GSM8258781 / Sample_extract_protocol_ch1: matched `Chromium` in "Chromium Next GEM Single Cell 3' Kit v3.1 (10x Genomics) according to the manufacturer’s instructions (CG000315 Rev D)"
- GSM8258782 / Sample_extract_protocol_ch1: matched `scRNA` in "For scRNA-seq, isolated WBCs were resuspended in ice-cold buffer (1xPBS + 0.04% BSA) and filtered through a 40µm Flowmi® cell filter (Partec). Cell concentration, viability, and aggregate were determi"
- GSM8258782 / Sample_extract_protocol_ch1: matched `Chromium` in "Chromium Next GEM Single Cell 3' Kit v3.1 (10x Genomics) according to the manufacturer’s instructions (CG000315 Rev D)"
- GSM8258783 / Sample_extract_protocol_ch1: matched `scRNA` in "For scRNA-seq, isolated WBCs were resuspended in ice-cold buffer (1xPBS + 0.04% BSA) and filtered through a 40µm Flowmi® cell filter (Partec). Cell concentration, viability, and aggregate were determi"
- GSM8258783 / Sample_extract_protocol_ch1: matched `Chromium` in "Chromium Next GEM Single Cell 3' Kit v3.1 (10x Genomics) according to the manufacturer’s instructions (CG000315 Rev D)"
- GSM8258784 / Sample_extract_protocol_ch1: matched `scRNA` in "For scRNA-seq, isolated WBCs were resuspended in ice-cold buffer (1xPBS + 0.04% BSA) and filtered through a 40µm Flowmi® cell filter (Partec). Cell concentration, viability, and aggregate were determi"
- GSM8258784 / Sample_extract_protocol_ch1: matched `Chromium` in "Chromium Next GEM Single Cell 3' Kit v3.1 (10x Genomics) according to the manufacturer’s instructions (CG000315 Rev D)"
- GSM8258785 / Sample_extract_protocol_ch1: matched `scRNA` in "For scRNA-seq, isolated WBCs were resuspended in ice-cold buffer (1xPBS + 0.04% BSA) and filtered through a 40µm Flowmi® cell filter (Partec). Cell concentration, viability, and aggregate were determi"
- GSM8258785 / Sample_extract_protocol_ch1: matched `Chromium` in "Chromium Next GEM Single Cell 3' Kit v3.1 (10x Genomics) according to the manufacturer’s instructions (CG000315 Rev D)"
- GSM8258786 / Sample_extract_protocol_ch1: matched `scRNA` in "For scRNA-seq, isolated WBCs were resuspended in ice-cold buffer (1xPBS + 0.04% BSA) and filtered through a 40µm Flowmi® cell filter (Partec). Cell concentration, viability, and aggregate were determi"
- GSM8258786 / Sample_extract_protocol_ch1: matched `Chromium` in "Chromium Next GEM Single Cell 3' Kit v3.1 (10x Genomics) according to the manufacturer’s instructions (CG000315 Rev D)"
- GSM8258787 / Sample_extract_protocol_ch1: matched `scRNA` in "For scRNA-seq, isolated WBCs were resuspended in ice-cold buffer (1xPBS + 0.04% BSA) and filtered through a 40µm Flowmi® cell filter (Partec). Cell concentration, viability, and aggregate were determi"
- GSM8258787 / Sample_extract_protocol_ch1: matched `Chromium` in "Chromium Next GEM Single Cell 3' Kit v3.1 (10x Genomics) according to the manufacturer’s instructions (CG000315 Rev D)"
- GSM8258788 / Sample_extract_protocol_ch1: matched `scRNA` in "For scRNA-seq, isolated WBCs were resuspended in ice-cold buffer (1xPBS + 0.04% BSA) and filtered through a 40µm Flowmi® cell filter (Partec). Cell concentration, viability, and aggregate were determi"
- GSM8258788 / Sample_extract_protocol_ch1: matched `Chromium` in "Chromium Next GEM Single Cell 3' Kit v3.1 (10x Genomics) according to the manufacturer’s instructions (CG000315 Rev D)"
- GSM8258789 / Sample_extract_protocol_ch1: matched `scRNA` in "For scRNA-seq, isolated WBCs were resuspended in ice-cold buffer (1xPBS + 0.04% BSA) and filtered through a 40µm Flowmi® cell filter (Partec). Cell concentration, viability, and aggregate were determi"
- GSM8258789 / Sample_extract_protocol_ch1: matched `Chromium` in "Chromium Next GEM Single Cell 3' Kit v3.1 (10x Genomics) according to the manufacturer’s instructions (CG000315 Rev D)"
- GSM8258790 / Sample_extract_protocol_ch1: matched `scRNA` in "For scRNA-seq, isolated WBCs were resuspended in ice-cold buffer (1xPBS + 0.04% BSA) and filtered through a 40µm Flowmi® cell filter (Partec). Cell concentration, viability, and aggregate were determi"
- GSM8258790 / Sample_extract_protocol_ch1: matched `Chromium` in "Chromium Next GEM Single Cell 3' Kit v3.1 (10x Genomics) according to the manufacturer’s instructions (CG000315 Rev D)"
- GSM8258791 / Sample_extract_protocol_ch1: matched `scRNA` in "For scRNA-seq, isolated WBCs were resuspended in ice-cold buffer (1xPBS + 0.04% BSA) and filtered through a 40µm Flowmi® cell filter (Partec). Cell concentration, viability, and aggregate were determi"
- GSM8258791 / Sample_extract_protocol_ch1: matched `Chromium` in "Chromium Next GEM Single Cell 3' Kit v3.1 (10x Genomics) according to the manufacturer’s instructions (CG000315 Rev D)"
- GSM8258792 / Sample_extract_protocol_ch1: matched `scRNA` in "For scRNA-seq, isolated WBCs were resuspended in ice-cold buffer (1xPBS + 0.04% BSA) and filtered through a 40µm Flowmi® cell filter (Partec). Cell concentration, viability, and aggregate were determi"
- GSM8258792 / Sample_extract_protocol_ch1: matched `Chromium` in "Chromium Next GEM Single Cell 3' Kit v3.1 (10x Genomics) according to the manufacturer’s instructions (CG000315 Rev D)"
- GSM8258793 / Sample_extract_protocol_ch1: matched `scRNA` in "For scRNA-seq, isolated WBCs were resuspended in ice-cold buffer (1xPBS + 0.04% BSA) and filtered through a 40µm Flowmi® cell filter (Partec). Cell concentration, viability, and aggregate were determi"
- GSM8258793 / Sample_extract_protocol_ch1: matched `Chromium` in "Chromium Next GEM Single Cell 3' Kit v3.1 (10x Genomics) according to the manufacturer’s instructions (CG000315 Rev D)"
- GSM8258794 / Sample_extract_protocol_ch1: matched `scRNA` in "For scRNA-seq, isolated WBCs were resuspended in ice-cold buffer (1xPBS + 0.04% BSA) and filtered through a 40µm Flowmi® cell filter (Partec). Cell concentration, viability, and aggregate were determi"
- GSM8258794 / Sample_extract_protocol_ch1: matched `Chromium` in "Chromium Next GEM Single Cell 3' Kit v3.1 (10x Genomics) according to the manufacturer’s instructions (CG000315 Rev D)"
- GSM8258795 / Sample_extract_protocol_ch1: matched `scRNA` in "For scRNA-seq, isolated WBCs were resuspended in ice-cold buffer (1xPBS + 0.04% BSA) and filtered through a 40µm Flowmi® cell filter (Partec). Cell concentration, viability, and aggregate were determi"
- GSM8258795 / Sample_extract_protocol_ch1: matched `Chromium` in "Chromium Next GEM Single Cell 3' Kit v3.1 (10x Genomics) according to the manufacturer’s instructions (CG000315 Rev D)"
- GSM8258781 / Sample_data_processing: matched `cellranger` in "Demultiplexing and count matrix generation were performed with cellranger v6.0.0. Reads were mapped to reference genome GRCh38.86."
- GSM8258781 / Sample_data_processing: matched `scanpy` in "Quality control and clustering were performed in Python using scanpy v1.9.3 with following parameters: Cells with <30 genes or with >30% mitochondrial genes expressed were excluded. Moreover, cells we"
- GSM8258782 / Sample_data_processing: matched `cellranger` in "Demultiplexing and count matrix generation were performed with cellranger v6.0.0. Reads were mapped to reference genome GRCh38.86."
- GSM8258782 / Sample_data_processing: matched `scanpy` in "Quality control and clustering were performed in Python using scanpy v1.9.3 with following parameters: Cells with <30 genes or with >30% mitochondrial genes expressed were excluded. Moreover, cells we"
- GSM8258783 / Sample_data_processing: matched `cellranger` in "Demultiplexing and count matrix generation were performed with cellranger v6.0.0. Reads were mapped to reference genome GRCh38.86."
- GSM8258783 / Sample_data_processing: matched `scanpy` in "Quality control and clustering were performed in Python using scanpy v1.9.3 with following parameters: Cells with <30 genes or with >30% mitochondrial genes expressed were excluded. Moreover, cells we"
- GSM8258784 / Sample_data_processing: matched `cellranger` in "Demultiplexing and count matrix generation were performed with cellranger v6.0.0. Reads were mapped to reference genome GRCh38.86."
- GSM8258784 / Sample_data_processing: matched `scanpy` in "Quality control and clustering were performed in Python using scanpy v1.9.3 with following parameters: Cells with <30 genes or with >30% mitochondrial genes expressed were excluded. Moreover, cells we"
- GSM8258785 / Sample_data_processing: matched `cellranger` in "Demultiplexing and count matrix generation were performed with cellranger v6.0.0. Reads were mapped to reference genome GRCh38.86."
- GSM8258785 / Sample_data_processing: matched `scanpy` in "Quality control and clustering were performed in Python using scanpy v1.9.3 with following parameters: Cells with <30 genes or with >30% mitochondrial genes expressed were excluded. Moreover, cells we"
- GSM8258786 / Sample_data_processing: matched `cellranger` in "Demultiplexing and count matrix generation were performed with cellranger v6.0.0. Reads were mapped to reference genome GRCh38.86."
- GSM8258786 / Sample_data_processing: matched `scanpy` in "Quality control and clustering were performed in Python using scanpy v1.9.3 with following parameters: Cells with <30 genes or with >30% mitochondrial genes expressed were excluded. Moreover, cells we"
- GSM8258787 / Sample_data_processing: matched `cellranger` in "Demultiplexing and count matrix generation were performed with cellranger v6.0.0. Reads were mapped to reference genome GRCh38.86."
- GSM8258787 / Sample_data_processing: matched `scanpy` in "Quality control and clustering were performed in Python using scanpy v1.9.3 with following parameters: Cells with <30 genes or with >30% mitochondrial genes expressed were excluded. Moreover, cells we"
- GSM8258788 / Sample_data_processing: matched `cellranger` in "Demultiplexing and count matrix generation were performed with cellranger v6.0.0. Reads were mapped to reference genome GRCh38.86."
- GSM8258788 / Sample_data_processing: matched `scanpy` in "Quality control and clustering were performed in Python using scanpy v1.9.3 with following parameters: Cells with <30 genes or with >30% mitochondrial genes expressed were excluded. Moreover, cells we"
- GSM8258789 / Sample_data_processing: matched `cellranger` in "Demultiplexing and count matrix generation were performed with cellranger v6.0.0. Reads were mapped to reference genome GRCh38.86."
- GSM8258789 / Sample_data_processing: matched `scanpy` in "Quality control and clustering were performed in Python using scanpy v1.9.3 with following parameters: Cells with <30 genes or with >30% mitochondrial genes expressed were excluded. Moreover, cells we"
- GSM8258790 / Sample_data_processing: matched `cellranger` in "Demultiplexing and count matrix generation were performed with cellranger v6.0.0. Reads were mapped to reference genome GRCh38.86."
- GSM8258790 / Sample_data_processing: matched `scanpy` in "Quality control and clustering were performed in Python using scanpy v1.9.3 with following parameters: Cells with <30 genes or with >30% mitochondrial genes expressed were excluded. Moreover, cells we"
- GSM8258791 / Sample_data_processing: matched `cellranger` in "Demultiplexing and count matrix generation were performed with cellranger v6.0.0. Reads were mapped to reference genome GRCh38.86."
- GSM8258791 / Sample_data_processing: matched `scanpy` in "Quality control and clustering were performed in Python using scanpy v1.9.3 with following parameters: Cells with <30 genes or with >30% mitochondrial genes expressed were excluded. Moreover, cells we"
- GSM8258792 / Sample_data_processing: matched `cellranger` in "Demultiplexing and count matrix generation were performed with cellranger v6.0.0. Reads were mapped to reference genome GRCh38.86."
- GSM8258792 / Sample_data_processing: matched `scanpy` in "Quality control and clustering were performed in Python using scanpy v1.9.3 with following parameters: Cells with <30 genes or with >30% mitochondrial genes expressed were excluded. Moreover, cells we"
- GSM8258793 / Sample_data_processing: matched `cellranger` in "Demultiplexing and count matrix generation were performed with cellranger v6.0.0. Reads were mapped to reference genome GRCh38.86."
- GSM8258793 / Sample_data_processing: matched `scanpy` in "Quality control and clustering were performed in Python using scanpy v1.9.3 with following parameters: Cells with <30 genes or with >30% mitochondrial genes expressed were excluded. Moreover, cells we"
- GSM8258794 / Sample_data_processing: matched `cellranger` in "Demultiplexing and count matrix generation were performed with cellranger v6.0.0. Reads were mapped to reference genome GRCh38.86."
- GSM8258794 / Sample_data_processing: matched `scanpy` in "Quality control and clustering were performed in Python using scanpy v1.9.3 with following parameters: Cells with <30 genes or with >30% mitochondrial genes expressed were excluded. Moreover, cells we"
- GSM8258795 / Sample_data_processing: matched `cellranger` in "Demultiplexing and count matrix generation were performed with cellranger v6.0.0. Reads were mapped to reference genome GRCh38.86."
- GSM8258795 / Sample_data_processing: matched `scanpy` in "Quality control and clustering were performed in Python using scanpy v1.9.3 with following parameters: Cells with <30 genes or with >30% mitochondrial genes expressed were excluded. Moreover, cells we"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: Chromium, cellranger, scRNA, scanpy (15 sample(s)))
<!-- /computed -->