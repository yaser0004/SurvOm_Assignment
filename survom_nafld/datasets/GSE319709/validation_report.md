# Validation report: GSE319709

Single-cell transcriptomics reveals etiology-specific T-cell heterogeneity in hepatocellular carcinoma and implicates regulatory

<!-- computed -->
Sample count: 18

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 18 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 18/18 |
| source_tissue | WARN | liver-pattern source 10/18 |
| library_strategy | PASS | RNA-Seq 18/18 |
| library_source | WARN | library_source: transcriptomic single cell 18/18 |
| library_selection | PASS | cDNA 18/18 |
| instrument_model | PASS | Illumina NovaSeq 6000 18/18 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: Seurat, barcodes.tsv, features.tsv, matrix.mtx (18 sample(s)) |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (18/18), packaged in GSE319709_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE319709_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX32060548, https://www.ncbi.nlm.nih.gov/sra?term=SRX32060549, https://www.ncbi.nlm.nih.gov/sra?term=SRX32060550, https://www.ncbi.nlm.nih.gov/sra?term=SRX32060551, https://www.ncbi.nlm.nih.gov/sra?term=SRX32060552, and 13 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: blood (8), liver (10)

## Field presence

- tissue: 18/18 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
### library_source (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE319709 / Series_summary: matched `metabolic dysfunction-associated stea` in "Hepatocellular carcinoma (HCC) exhibits remarkable etiological heterogeneity, with hepatitis B virus (HBV) infection and metabolic dysfunction-associated steatohepatitis (MASH) emerging as two leading"
- GSE319709 / Series_overall_design: matched `MASH` in "We performed single-cell RNA sequencing (scRNA-seq) on CD45+ immune cells isolated from peripheral blood mononuclear cells (PBMCs), tumor tissues (T), and peritumor tissues (PT) of HBV-HCC (PBMC: n=4;"
### single_cell_or_spatial (FAIL)
- GSM9524176 / Sample_data_processing: matched `Seurat` in "Raw reads were trimmed of adapters and low-quality bases using Fastp (v0.20.1) and processed with the SeekSoul Tools pipeline to generate a gene-expression matrix. Downstream analyses were performed i"
- GSM9524177 / Sample_data_processing: matched `Seurat` in "Raw reads were trimmed of adapters and low-quality bases using Fastp (v0.20.1) and processed with the SeekSoul Tools pipeline to generate a gene-expression matrix. Downstream analyses were performed i"
- GSM9524178 / Sample_data_processing: matched `Seurat` in "Raw reads were trimmed of adapters and low-quality bases using Fastp (v0.20.1) and processed with the SeekSoul Tools pipeline to generate a gene-expression matrix. Downstream analyses were performed i"
- GSM9524179 / Sample_data_processing: matched `Seurat` in "Raw reads were trimmed of adapters and low-quality bases using Fastp (v0.20.1) and processed with the SeekSoul Tools pipeline to generate a gene-expression matrix. Downstream analyses were performed i"
- GSM9524180 / Sample_data_processing: matched `Seurat` in "Raw reads were trimmed of adapters and low-quality bases using Fastp (v0.20.1) and processed with the SeekSoul Tools pipeline to generate a gene-expression matrix. Downstream analyses were performed i"
- GSM9524181 / Sample_data_processing: matched `Seurat` in "Raw reads were trimmed of adapters and low-quality bases using Fastp (v0.20.1) and processed with the SeekSoul Tools pipeline to generate a gene-expression matrix. Downstream analyses were performed i"
- GSM9524182 / Sample_data_processing: matched `Seurat` in "Raw reads were trimmed of adapters and low-quality bases using Fastp (v0.20.1) and processed with the SeekSoul Tools pipeline to generate a gene-expression matrix. Downstream analyses were performed i"
- GSM9524183 / Sample_data_processing: matched `Seurat` in "Raw reads were trimmed of adapters and low-quality bases using Fastp (v0.20.1) and processed with the SeekSoul Tools pipeline to generate a gene-expression matrix. Downstream analyses were performed i"
- GSM9524184 / Sample_data_processing: matched `Seurat` in "Raw reads were trimmed of adapters and low-quality bases using Fastp (v0.20.1) and processed with the SeekSoul Tools pipeline to generate a gene-expression matrix. Downstream analyses were performed i"
- GSM9524185 / Sample_data_processing: matched `Seurat` in "Raw reads were trimmed of adapters and low-quality bases using Fastp (v0.20.1) and processed with the SeekSoul Tools pipeline to generate a gene-expression matrix. Downstream analyses were performed i"
- GSM9524186 / Sample_data_processing: matched `Seurat` in "Raw reads were trimmed of adapters and low-quality bases using Fastp (v0.20.1) and processed with the SeekSoul Tools pipeline to generate a gene-expression matrix. Downstream analyses were performed i"
- GSM9524187 / Sample_data_processing: matched `Seurat` in "Raw reads were trimmed of adapters and low-quality bases using Fastp (v0.20.1) and processed with the SeekSoul Tools pipeline to generate a gene-expression matrix. Downstream analyses were performed i"
- GSM9524188 / Sample_data_processing: matched `Seurat` in "Raw reads were trimmed of adapters and low-quality bases using Fastp (v0.20.1) and processed with the SeekSoul Tools pipeline to generate a gene-expression matrix. Downstream analyses were performed i"
- GSM9524189 / Sample_data_processing: matched `Seurat` in "Raw reads were trimmed of adapters and low-quality bases using Fastp (v0.20.1) and processed with the SeekSoul Tools pipeline to generate a gene-expression matrix. Downstream analyses were performed i"
- GSM9524190 / Sample_data_processing: matched `Seurat` in "Raw reads were trimmed of adapters and low-quality bases using Fastp (v0.20.1) and processed with the SeekSoul Tools pipeline to generate a gene-expression matrix. Downstream analyses were performed i"
- GSM9524191 / Sample_data_processing: matched `Seurat` in "Raw reads were trimmed of adapters and low-quality bases using Fastp (v0.20.1) and processed with the SeekSoul Tools pipeline to generate a gene-expression matrix. Downstream analyses were performed i"
- GSM9524192 / Sample_data_processing: matched `Seurat` in "Raw reads were trimmed of adapters and low-quality bases using Fastp (v0.20.1) and processed with the SeekSoul Tools pipeline to generate a gene-expression matrix. Downstream analyses were performed i"
- GSM9524193 / Sample_data_processing: matched `Seurat` in "Raw reads were trimmed of adapters and low-quality bases using Fastp (v0.20.1) and processed with the SeekSoul Tools pipeline to generate a gene-expression matrix. Downstream analyses were performed i"
- GSM9524176 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524176/suppl/GSM9524176_PT-1-barcodes.tsv.gz"
- GSM9524176 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524176/suppl/GSM9524176_PT-1-features.tsv.gz"
- GSM9524176 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524176/suppl/GSM9524176_PT-1-matrix.mtx.gz"
- GSM9524177 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524177/suppl/GSM9524177_T-1-barcodes.tsv.gz"
- GSM9524177 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524177/suppl/GSM9524177_T-1-features.tsv.gz"
- GSM9524177 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524177/suppl/GSM9524177_T-1-matrix.mtx.gz"
- GSM9524178 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524178/suppl/GSM9524178_con-1-barcodes.tsv.gz"
- GSM9524178 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524178/suppl/GSM9524178_con-1-features.tsv.gz"
- GSM9524178 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524178/suppl/GSM9524178_con-1-matrix.mtx.gz"
- GSM9524179 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524179/suppl/GSM9524179_con-2-barcodes.tsv.gz"
- GSM9524179 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524179/suppl/GSM9524179_con-2-features.tsv.gz"
- GSM9524179 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524179/suppl/GSM9524179_con-2-matrix.mtx.gz"
- GSM9524180 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524180/suppl/GSM9524180_PT-2-barcodes.tsv.gz"
- GSM9524180 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524180/suppl/GSM9524180_PT-2-features.tsv.gz"
- GSM9524180 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524180/suppl/GSM9524180_PT-2-matrix.mtx.gz"
- GSM9524181 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524181/suppl/GSM9524181_T-2-barcodes.tsv.gz"
- GSM9524181 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524181/suppl/GSM9524181_T-2-features.tsv.gz"
- GSM9524181 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524181/suppl/GSM9524181_T-2-matrix.mtx.gz"
- GSM9524182 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524182/suppl/GSM9524182_con-3-barcodes.tsv.gz"
- GSM9524182 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524182/suppl/GSM9524182_con-3-features.tsv.gz"
- GSM9524182 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524182/suppl/GSM9524182_con-3-matrix.mtx.gz"
- GSM9524183 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524183/suppl/GSM9524183_PT-3-barcodes.tsv.gz"
- GSM9524183 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524183/suppl/GSM9524183_PT-3-features.tsv.gz"
- GSM9524183 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524183/suppl/GSM9524183_PT-3-matrix.mtx.gz"
- GSM9524184 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524184/suppl/GSM9524184_T-3-barcodes.tsv.gz"
- GSM9524184 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524184/suppl/GSM9524184_T-3-features.tsv.gz"
- GSM9524184 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524184/suppl/GSM9524184_T-3-matrix.mtx.gz"
- GSM9524185 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524185/suppl/GSM9524185_con-4-barcodes.tsv.gz"
- GSM9524185 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524185/suppl/GSM9524185_con-4-features.tsv.gz"
- GSM9524185 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524185/suppl/GSM9524185_con-4-matrix.mtx.gz"
- GSM9524186 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524186/suppl/GSM9524186_con-5-barcodes.tsv.gz"
- GSM9524186 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524186/suppl/GSM9524186_con-5-features.tsv.gz"
- GSM9524186 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524186/suppl/GSM9524186_con-5-matrix.mtx.gz"
- GSM9524187 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524187/suppl/GSM9524187_PT-4-barcodes.tsv.gz"
- GSM9524187 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524187/suppl/GSM9524187_PT-4-features.tsv.gz"
- GSM9524187 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524187/suppl/GSM9524187_PT-4-matrix.mtx.gz"
- GSM9524188 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524188/suppl/GSM9524188_T-4-barcodes.tsv.gz"
- GSM9524188 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524188/suppl/GSM9524188_T-4-features.tsv.gz"
- GSM9524188 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524188/suppl/GSM9524188_T-4-matrix.mtx.gz"
- GSM9524189 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524189/suppl/GSM9524189_con-6-barcodes.tsv.gz"
- GSM9524189 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524189/suppl/GSM9524189_con-6-features.tsv.gz"
- GSM9524189 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524189/suppl/GSM9524189_con-6-matrix.mtx.gz"
- GSM9524190 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524190/suppl/GSM9524190_con-7-barcodes.tsv.gz"
- GSM9524190 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524190/suppl/GSM9524190_con-7-features.tsv.gz"
- GSM9524190 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524190/suppl/GSM9524190_con-7-matrix.mtx.gz"
- GSM9524191 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524191/suppl/GSM9524191_con-8-barcodes.tsv.gz"
- GSM9524191 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524191/suppl/GSM9524191_con-8-features.tsv.gz"
- GSM9524191 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524191/suppl/GSM9524191_con-8-matrix.mtx.gz"
- GSM9524192 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524192/suppl/GSM9524192_PT-5-barcodes.tsv.gz"
- GSM9524192 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524192/suppl/GSM9524192_PT-5-features.tsv.gz"
- GSM9524192 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524192/suppl/GSM9524192_PT-5-matrix.mtx.gz"
- GSM9524193 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524193/suppl/GSM9524193_T-5-barcodes.tsv.gz"
- GSM9524193 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524193/suppl/GSM9524193_T-5-features.tsv.gz"
- GSM9524193 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9524nnn/GSM9524193/suppl/GSM9524193_T-5-matrix.mtx.gz"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: Seurat, barcodes.tsv, features.tsv, matrix.mtx (18 sample(s)))
<!-- /computed -->