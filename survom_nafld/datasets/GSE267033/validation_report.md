# Validation report: GSE267033

Single-cell landscape of peripheral immune cells in MAFLD/MASH [scRNA-seq]

<!-- computed -->
Sample count: 15

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 15 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 15/15 |
| source_tissue | WARN | liver-pattern source 0/15 |
| library_strategy | PASS | RNA-Seq 15/15 |
| library_source | WARN | library_source: transcriptomic single cell 15/15 |
| library_selection | PASS | cDNA 15/15 |
| instrument_model | PASS | Illumina NovaSeq 6000 15/15 |
| metadata_completeness | PASS | reported consistently: disease, sex, tissue; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (9 sample(s)) |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: Chromium, cellranger, scRNA, scanpy (15 sample(s)) |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE267033_counts_RNAseq_sc_WBC.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE267033_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX24500007, https://www.ncbi.nlm.nih.gov/sra?term=SRX24500008, https://www.ncbi.nlm.nih.gov/sra?term=SRX24500009, https://www.ncbi.nlm.nih.gov/sra?term=SRX24500010, https://www.ncbi.nlm.nih.gov/sra?term=SRX24500011, and 10 more (see sample_metadata.csv) |

## Canonical field distributions

- **disease**: Control | 0_healthy (6), MAFLD/MASH | 1_low (2), MAFLD/MASH | 2_medium (4), MAFLD/MASH | 3_high (3)
- **sex**: f (7), m (8)
- **tissue**: White blood cells (15)

## Field presence

- Sex: 15/15 (canon: sex)
- assaytype: 15/15
- batch: 15/15
- celltype: 15/15
- condition: 15/15 (canon: disease)
- disease: 15/15 (canon: disease)
- id sample: 15/15
- tissue: 15/15 (canon: tissue)
- type patient: 15/15

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
### library_source (WARN)
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