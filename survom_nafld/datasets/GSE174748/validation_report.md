# Validation report: GSE174748

An imbalance of tumour-suppressing and tumour-promoting hepatic stellate cell populations in liver fibrosis contributes to hepatocarcinogenesis

<!-- computed -->
Sample count: 4

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 4 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 4/4 |
| source_tissue | PASS | liver-pattern source 4/4 |
| library_strategy | PASS | RNA-Seq 4/4 |
| library_source | PASS | transcriptomic 4/4 |
| library_selection | PASS | cDNA 4/4 |
| instrument_model | PASS | Illumina HiSeq 4000 4/4 |
| metadata_completeness | PASS | reported consistently: disease, tissue; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (2 sample(s)) |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: 10x, Cell Ranger, Seurat, barcodes.tsv, features.tsv, matrix.mtx (4 sample(s)) |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (4/4), packaged in GSE174748_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE174748_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX10947803, https://www.ncbi.nlm.nih.gov/sra?term=SRX10947804, https://www.ncbi.nlm.nih.gov/sra?term=SRX10947805, https://www.ncbi.nlm.nih.gov/sra?term=SRX10947806 |

## Canonical field distributions

- **disease**: Healthy (2), NAFLD (2)
- **tissue**: liver explant (4)

## Field presence

- condition: 4/4 (canon: disease)
- tissue: 4/4 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### single_cell_or_spatial (FAIL)
- GSM5325534 / Sample_extract_protocol_ch1: matched `10x` in "10x Genomics single cell 3' gene expression v3"
- GSM5325535 / Sample_extract_protocol_ch1: matched `10x` in "10x Genomics single cell 3' gene expression v3"
- GSM5325536 / Sample_extract_protocol_ch1: matched `10x` in "10x Genomics single cell 3' gene expression v3"
- GSM5325537 / Sample_extract_protocol_ch1: matched `10x` in "10x Genomics single cell 3' gene expression v3"
- GSM5325534 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment (to a modified version of the GRCh38 reference counting intronic reads in addition to those aligned to exons), and estimation of cell-containing partitions and associated UMI"
- GSM5325534 / Sample_data_processing: matched `Seurat` in "Quality control, normalisation, data integration, and downstream analysis using Seurat 3.1.2"
- GSM5325535 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment (to a modified version of the GRCh38 reference counting intronic reads in addition to those aligned to exons), and estimation of cell-containing partitions and associated UMI"
- GSM5325535 / Sample_data_processing: matched `Seurat` in "Quality control, normalisation, data integration, and downstream analysis using Seurat 3.1.2"
- GSM5325536 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment (to a modified version of the GRCh38 reference counting intronic reads in addition to those aligned to exons), and estimation of cell-containing partitions and associated UMI"
- GSM5325536 / Sample_data_processing: matched `Seurat` in "Quality control, normalisation, data integration, and downstream analysis using Seurat 3.1.2"
- GSM5325537 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment (to a modified version of the GRCh38 reference counting intronic reads in addition to those aligned to exons), and estimation of cell-containing partitions and associated UMI"
- GSM5325537 / Sample_data_processing: matched `Seurat` in "Quality control, normalisation, data integration, and downstream analysis using Seurat 3.1.2"
- GSM5325534 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5325nnn/GSM5325534/suppl/GSM5325534_healthy1_barcodes.tsv.gz"
- GSM5325534 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5325nnn/GSM5325534/suppl/GSM5325534_healthy1_features.tsv.gz"
- GSM5325534 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5325nnn/GSM5325534/suppl/GSM5325534_healthy1_matrix.mtx.gz"
- GSM5325535 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5325nnn/GSM5325535/suppl/GSM5325535_healthy2_barcodes.tsv.gz"
- GSM5325535 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5325nnn/GSM5325535/suppl/GSM5325535_healthy2_features.tsv.gz"
- GSM5325535 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5325nnn/GSM5325535/suppl/GSM5325535_healthy2_matrix.mtx.gz"
- GSM5325536 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5325nnn/GSM5325536/suppl/GSM5325536_nafld1_barcodes.tsv.gz"
- GSM5325536 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5325nnn/GSM5325536/suppl/GSM5325536_nafld1_features.tsv.gz"
- GSM5325536 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5325nnn/GSM5325536/suppl/GSM5325536_nafld1_matrix.mtx.gz"
- GSM5325537 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5325nnn/GSM5325537/suppl/GSM5325537_nafld2_barcodes.tsv.gz"
- GSM5325537 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5325nnn/GSM5325537/suppl/GSM5325537_nafld2_features.tsv.gz"
- GSM5325537 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5325nnn/GSM5325537/suppl/GSM5325537_nafld2_matrix.mtx.gz"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: 10x, Cell Ranger, Seurat, barcodes.tsv, features.tsv, matrix.mtx (4 sample(s)))
<!-- /computed -->