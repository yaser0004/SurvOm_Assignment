# Validation report: GSE217235

Multi cytokine producing liver CD4+ T cells characterize the liver of NASH patients

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
| metadata_completeness | PASS | reported consistently: disease, tissue; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (6 sample(s)) |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: 10x, Chromium, barcodes.tsv, features.tsv, genes.tsv, matrix.mtx (6 sample(s)) |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (6/6), packaged in GSE217235_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE217235_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX18158491, https://www.ncbi.nlm.nih.gov/sra?term=SRX18158492, https://www.ncbi.nlm.nih.gov/sra?term=SRX18158493, https://www.ncbi.nlm.nih.gov/sra?term=SRX18158494, https://www.ncbi.nlm.nih.gov/sra?term=SRX18158495, and 1 more (see sample_metadata.csv) |

## Canonical field distributions

- **disease**: NAFLD (3), NASH (3)
- **tissue**: liver (6)

## Field presence

- disease: 6/6 (canon: disease)
- patient id: 6/6
- tissue: 6/6 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### single_cell_or_spatial (FAIL)
- GSM6709882 / Sample_extract_protocol_ch1: matched `10x` in "Cells were loaded on a 10x Chromium single cell instrument."
- GSM6709882 / Sample_extract_protocol_ch1: matched `Chromium` in "All steps were performed according to standard protocol of the Chromium single cell 3' v2 kit to generate high-quality cDNA libraries."
- GSM6709883 / Sample_extract_protocol_ch1: matched `10x` in "Cells were loaded on a 10x Chromium single cell instrument."
- GSM6709883 / Sample_extract_protocol_ch1: matched `Chromium` in "All steps were performed according to standard protocol of the Chromium single cell 3' v2 kit to generate high-quality cDNA libraries."
- GSM6709884 / Sample_extract_protocol_ch1: matched `10x` in "Cells were loaded on a 10x Chromium single cell instrument."
- GSM6709884 / Sample_extract_protocol_ch1: matched `Chromium` in "All steps were performed according to standard protocol of the Chromium single cell 3' v2 kit to generate high-quality cDNA libraries."
- GSM6709885 / Sample_extract_protocol_ch1: matched `10x` in "Cells were loaded on a 10x Chromium single cell instrument."
- GSM6709885 / Sample_extract_protocol_ch1: matched `Chromium` in "All steps were performed according to standard protocol of the Chromium single cell 3' v2 kit to generate high-quality cDNA libraries."
- GSM6709886 / Sample_extract_protocol_ch1: matched `10x` in "Cells were loaded on a 10x Chromium single cell instrument."
- GSM6709886 / Sample_extract_protocol_ch1: matched `Chromium` in "All steps were performed according to standard protocol of the Chromium single cell 3' v2 kit to generate high-quality cDNA libraries."
- GSM6709887 / Sample_extract_protocol_ch1: matched `10x` in "Cells were loaded on a 10x Chromium single cell instrument."
- GSM6709887 / Sample_extract_protocol_ch1: matched `Chromium` in "All steps were performed according to standard protocol of the Chromium single cell 3' v2 kit to generate high-quality cDNA libraries."
- GSM6709882 / Sample_data_processing: matched `10x` in "10x Genomics raw sequencing data were processed using CellRanger software (version 2.1.0, 10x Genomics, Pleasanton, CA) and the human genome GRCh38 release(function cellranger count). The matrices of "
- GSM6709883 / Sample_data_processing: matched `10x` in "10x Genomics raw sequencing data were processed using CellRanger software (version 2.1.0, 10x Genomics, Pleasanton, CA) and the human genome GRCh38 release(function cellranger count). The matrices of "
- GSM6709884 / Sample_data_processing: matched `10x` in "10x Genomics raw sequencing data were processed using CellRanger software (version 2.1.0, 10x Genomics, Pleasanton, CA) and the human genome GRCh38 release(function cellranger count). The matrices of "
- GSM6709885 / Sample_data_processing: matched `10x` in "10x Genomics raw sequencing data were processed using CellRanger software (version 2.1.0, 10x Genomics, Pleasanton, CA) and the human genome GRCh38 release(function cellranger count). The matrices of "
- GSM6709886 / Sample_data_processing: matched `10x` in "10x Genomics raw sequencing data were processed using CellRanger software (version 2.1.0, 10x Genomics, Pleasanton, CA) and the human genome GRCh38 release(function cellranger count). The matrices of "
- GSM6709887 / Sample_data_processing: matched `10x` in "10x Genomics raw sequencing data were processed using CellRanger software (version 2.1.0, 10x Genomics, Pleasanton, CA) and the human genome GRCh38 release(function cellranger count). The matrices of "
- GSM6709882 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6709nnn/GSM6709882/suppl/GSM6709882_S001_barcodes.tsv.gz"
- GSM6709882 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6709nnn/GSM6709882/suppl/GSM6709882_S001_genes.tsv.gz"
- GSM6709882 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6709nnn/GSM6709882/suppl/GSM6709882_S001_matrix.mtx.gz"
- GSM6709883 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6709nnn/GSM6709883/suppl/GSM6709883_S003_barcodes.tsv.gz"
- GSM6709883 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6709nnn/GSM6709883/suppl/GSM6709883_S003_genes.tsv.gz"
- GSM6709883 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6709nnn/GSM6709883/suppl/GSM6709883_S003_matrix.mtx.gz"
- GSM6709884 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6709nnn/GSM6709884/suppl/GSM6709884_S004_barcodes.tsv.gz"
- GSM6709884 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6709nnn/GSM6709884/suppl/GSM6709884_S004_genes.tsv.gz"
- GSM6709884 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6709nnn/GSM6709884/suppl/GSM6709884_S004_matrix.mtx.gz"
- GSM6709885 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6709nnn/GSM6709885/suppl/GSM6709885_S005_barcodes.tsv.gz"
- GSM6709885 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6709nnn/GSM6709885/suppl/GSM6709885_S005_genes.tsv.gz"
- GSM6709885 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6709nnn/GSM6709885/suppl/GSM6709885_S005_matrix.mtx.gz"
- GSM6709886 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6709nnn/GSM6709886/suppl/GSM6709886_S006_barcodes.tsv.gz"
- GSM6709886 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6709nnn/GSM6709886/suppl/GSM6709886_S006_genes.tsv.gz"
- GSM6709886 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6709nnn/GSM6709886/suppl/GSM6709886_S006_matrix.mtx.gz"
- GSM6709887 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6709nnn/GSM6709887/suppl/GSM6709887_S008_barcodes.tsv.gz"
- GSM6709887 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6709nnn/GSM6709887/suppl/GSM6709887_S008_features.tsv.gz"
- GSM6709887 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6709nnn/GSM6709887/suppl/GSM6709887_S008_matrix.mtx.gz"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: 10x, Chromium, barcodes.tsv, features.tsv, genes.tsv, matrix.mtx (6 sample(s)))
<!-- /computed -->