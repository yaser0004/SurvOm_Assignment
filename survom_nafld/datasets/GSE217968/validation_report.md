# Validation report: GSE217968

Characterization of human hepatic natural killer cells in end-stage chronic liver diseases

<!-- computed -->
Sample count: 16

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 16 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 16/16 |
| source_tissue | WARN | liver-pattern source 0/16 |
| library_strategy | PASS | RNA-Seq 16/16 |
| library_source | WARN | library_source: transcriptomic single cell 16/16 |
| library_selection | PASS | cDNA 16/16 |
| instrument_model | PASS | Illumina NextSeq 500 16/16 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (4 sample(s)) |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: 10X, Cell Ranger, barcodes.tsv, features.tsv, matrix.mtx (16 sample(s)) |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (16/16), packaged in GSE217968_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE217968_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX18259680, https://www.ncbi.nlm.nih.gov/sra?term=SRX18259681, https://www.ncbi.nlm.nih.gov/sra?term=SRX18259682, https://www.ncbi.nlm.nih.gov/sra?term=SRX18259683, https://www.ncbi.nlm.nih.gov/sra?term=SRX18259684, and 11 more (see sample_metadata.csv) |

## Field presence

- cell type: 16/16
- pathology: 16/16

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
### library_source (WARN)
### metadata_completeness (WARN)
### single_cell_or_spatial (FAIL)
- GSM6731263 / Sample_data_processing: matched `Cell Ranger` in "Illumina BCL files were de-multiplexed and converted to FASTQs using Cell Ranger mkfastq (version 5.0.1, 10X Genomics https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/lat"
- GSM6731263 / Sample_data_processing: matched `Cell Ranger` in "FASTQs were then used to quantify gene expression using Cell Ranger count (version 5.0.1) and the GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics) human genome reference."
- GSM6731263 / Sample_data_processing: matched `10X` in "Assembly: GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics)"
- GSM6731263 / Sample_data_processing: matched `10X` in "Supplementary files format and content: Position sorted BAMs, BAM indexes, and gene expression counts in 10X format (separate barcodes, features, and matrix files for each sample)."
- GSM6731264 / Sample_data_processing: matched `Cell Ranger` in "Illumina BCL files were de-multiplexed and converted to FASTQs using Cell Ranger mkfastq (version 5.0.1, 10X Genomics https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/lat"
- GSM6731264 / Sample_data_processing: matched `Cell Ranger` in "FASTQs were then used to quantify gene expression using Cell Ranger count (version 5.0.1) and the GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics) human genome reference."
- GSM6731264 / Sample_data_processing: matched `10X` in "Assembly: GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics)"
- GSM6731264 / Sample_data_processing: matched `10X` in "Supplementary files format and content: Position sorted BAMs, BAM indexes, and gene expression counts in 10X format (separate barcodes, features, and matrix files for each sample)."
- GSM6731265 / Sample_data_processing: matched `Cell Ranger` in "Illumina BCL files were de-multiplexed and converted to FASTQs using Cell Ranger mkfastq (version 5.0.1, 10X Genomics https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/lat"
- GSM6731265 / Sample_data_processing: matched `Cell Ranger` in "FASTQs were then used to quantify gene expression using Cell Ranger count (version 5.0.1) and the GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics) human genome reference."
- GSM6731265 / Sample_data_processing: matched `10X` in "Assembly: GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics)"
- GSM6731265 / Sample_data_processing: matched `10X` in "Supplementary files format and content: Position sorted BAMs, BAM indexes, and gene expression counts in 10X format (separate barcodes, features, and matrix files for each sample)."
- GSM6731266 / Sample_data_processing: matched `Cell Ranger` in "Illumina BCL files were de-multiplexed and converted to FASTQs using Cell Ranger mkfastq (version 5.0.1, 10X Genomics https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/lat"
- GSM6731266 / Sample_data_processing: matched `Cell Ranger` in "FASTQs were then used to quantify gene expression using Cell Ranger count (version 5.0.1) and the GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics) human genome reference."
- GSM6731266 / Sample_data_processing: matched `10X` in "Assembly: GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics)"
- GSM6731266 / Sample_data_processing: matched `10X` in "Supplementary files format and content: Position sorted BAMs, BAM indexes, and gene expression counts in 10X format (separate barcodes, features, and matrix files for each sample)."
- GSM6731267 / Sample_data_processing: matched `Cell Ranger` in "Illumina BCL files were de-multiplexed and converted to FASTQs using Cell Ranger mkfastq (version 5.0.1, 10X Genomics https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/lat"
- GSM6731267 / Sample_data_processing: matched `Cell Ranger` in "FASTQs were then used to quantify gene expression using Cell Ranger count (version 5.0.1) and the GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics) human genome reference."
- GSM6731267 / Sample_data_processing: matched `10X` in "Assembly: GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics)"
- GSM6731267 / Sample_data_processing: matched `10X` in "Supplementary files format and content: Position sorted BAMs, BAM indexes, and gene expression counts in 10X format (separate barcodes, features, and matrix files for each sample)."
- GSM6731268 / Sample_data_processing: matched `Cell Ranger` in "Illumina BCL files were de-multiplexed and converted to FASTQs using Cell Ranger mkfastq (version 5.0.1, 10X Genomics https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/lat"
- GSM6731268 / Sample_data_processing: matched `Cell Ranger` in "FASTQs were then used to quantify gene expression using Cell Ranger count (version 5.0.1) and the GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics) human genome reference."
- GSM6731268 / Sample_data_processing: matched `10X` in "Assembly: GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics)"
- GSM6731268 / Sample_data_processing: matched `10X` in "Supplementary files format and content: Position sorted BAMs, BAM indexes, and gene expression counts in 10X format (separate barcodes, features, and matrix files for each sample)."
- GSM6731269 / Sample_data_processing: matched `Cell Ranger` in "Illumina BCL files were de-multiplexed and converted to FASTQs using Cell Ranger mkfastq (version 5.0.1, 10X Genomics https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/lat"
- GSM6731269 / Sample_data_processing: matched `Cell Ranger` in "FASTQs were then used to quantify gene expression using Cell Ranger count (version 5.0.1) and the GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics) human genome reference."
- GSM6731269 / Sample_data_processing: matched `10X` in "Assembly: GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics)"
- GSM6731269 / Sample_data_processing: matched `10X` in "Supplementary files format and content: Position sorted BAMs, BAM indexes, and gene expression counts in 10X format (separate barcodes, features, and matrix files for each sample)."
- GSM6731270 / Sample_data_processing: matched `Cell Ranger` in "Illumina BCL files were de-multiplexed and converted to FASTQs using Cell Ranger mkfastq (version 5.0.1, 10X Genomics https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/lat"
- GSM6731270 / Sample_data_processing: matched `Cell Ranger` in "FASTQs were then used to quantify gene expression using Cell Ranger count (version 5.0.1) and the GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics) human genome reference."
- GSM6731270 / Sample_data_processing: matched `10X` in "Assembly: GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics)"
- GSM6731270 / Sample_data_processing: matched `10X` in "Supplementary files format and content: Position sorted BAMs, BAM indexes, and gene expression counts in 10X format (separate barcodes, features, and matrix files for each sample)."
- GSM6731271 / Sample_data_processing: matched `Cell Ranger` in "Illumina BCL files were de-multiplexed and converted to FASTQs using Cell Ranger mkfastq (version 5.0.1, 10X Genomics https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/lat"
- GSM6731271 / Sample_data_processing: matched `Cell Ranger` in "FASTQs were then used to quantify gene expression using Cell Ranger count (version 5.0.1) and the GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics) human genome reference."
- GSM6731271 / Sample_data_processing: matched `10X` in "Assembly: GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics)"
- GSM6731271 / Sample_data_processing: matched `10X` in "Supplementary files format and content: Position sorted BAMs, BAM indexes, and gene expression counts in 10X format (separate barcodes, features, and matrix files for each sample)."
- GSM6731272 / Sample_data_processing: matched `Cell Ranger` in "Illumina BCL files were de-multiplexed and converted to FASTQs using Cell Ranger mkfastq (version 5.0.1, 10X Genomics https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/lat"
- GSM6731272 / Sample_data_processing: matched `Cell Ranger` in "FASTQs were then used to quantify gene expression using Cell Ranger count (version 5.0.1) and the GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics) human genome reference."
- GSM6731272 / Sample_data_processing: matched `10X` in "Assembly: GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics)"
- GSM6731272 / Sample_data_processing: matched `10X` in "Supplementary files format and content: Position sorted BAMs, BAM indexes, and gene expression counts in 10X format (separate barcodes, features, and matrix files for each sample)."
- GSM6731273 / Sample_data_processing: matched `Cell Ranger` in "Illumina BCL files were de-multiplexed and converted to FASTQs using Cell Ranger mkfastq (version 5.0.1, 10X Genomics https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/lat"
- GSM6731273 / Sample_data_processing: matched `Cell Ranger` in "FASTQs were then used to quantify gene expression using Cell Ranger count (version 5.0.1) and the GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics) human genome reference."
- GSM6731273 / Sample_data_processing: matched `10X` in "Assembly: GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics)"
- GSM6731273 / Sample_data_processing: matched `10X` in "Supplementary files format and content: Position sorted BAMs, BAM indexes, and gene expression counts in 10X format (separate barcodes, features, and matrix files for each sample)."
- GSM6731274 / Sample_data_processing: matched `Cell Ranger` in "Illumina BCL files were de-multiplexed and converted to FASTQs using Cell Ranger mkfastq (version 5.0.1, 10X Genomics https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/lat"
- GSM6731274 / Sample_data_processing: matched `Cell Ranger` in "FASTQs were then used to quantify gene expression using Cell Ranger count (version 5.0.1) and the GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics) human genome reference."
- GSM6731274 / Sample_data_processing: matched `10X` in "Assembly: GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics)"
- GSM6731274 / Sample_data_processing: matched `10X` in "Supplementary files format and content: Position sorted BAMs, BAM indexes, and gene expression counts in 10X format (separate barcodes, features, and matrix files for each sample)."
- GSM6731275 / Sample_data_processing: matched `Cell Ranger` in "Illumina BCL files were de-multiplexed and converted to FASTQs using Cell Ranger mkfastq (version 5.0.1, 10X Genomics https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/lat"
- GSM6731275 / Sample_data_processing: matched `Cell Ranger` in "FASTQs were then used to quantify gene expression using Cell Ranger count (version 5.0.1) and the GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics) human genome reference."
- GSM6731275 / Sample_data_processing: matched `10X` in "Assembly: GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics)"
- GSM6731275 / Sample_data_processing: matched `10X` in "Supplementary files format and content: Position sorted BAMs, BAM indexes, and gene expression counts in 10X format (separate barcodes, features, and matrix files for each sample)."
- GSM6731276 / Sample_data_processing: matched `Cell Ranger` in "Illumina BCL files were de-multiplexed and converted to FASTQs using Cell Ranger mkfastq (version 5.0.1, 10X Genomics https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/lat"
- GSM6731276 / Sample_data_processing: matched `Cell Ranger` in "FASTQs were then used to quantify gene expression using Cell Ranger count (version 5.0.1) and the GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics) human genome reference."
- GSM6731276 / Sample_data_processing: matched `10X` in "Assembly: GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics)"
- GSM6731276 / Sample_data_processing: matched `10X` in "Supplementary files format and content: Position sorted BAMs, BAM indexes, and gene expression counts in 10X format (separate barcodes, features, and matrix files for each sample)."
- GSM6731277 / Sample_data_processing: matched `Cell Ranger` in "Illumina BCL files were de-multiplexed and converted to FASTQs using Cell Ranger mkfastq (version 5.0.1, 10X Genomics https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/lat"
- GSM6731277 / Sample_data_processing: matched `Cell Ranger` in "FASTQs were then used to quantify gene expression using Cell Ranger count (version 5.0.1) and the GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics) human genome reference."
- GSM6731277 / Sample_data_processing: matched `10X` in "Assembly: GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics)"
- GSM6731277 / Sample_data_processing: matched `10X` in "Supplementary files format and content: Position sorted BAMs, BAM indexes, and gene expression counts in 10X format (separate barcodes, features, and matrix files for each sample)."
- GSM6731278 / Sample_data_processing: matched `Cell Ranger` in "Illumina BCL files were de-multiplexed and converted to FASTQs using Cell Ranger mkfastq (version 5.0.1, 10X Genomics https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/lat"
- GSM6731278 / Sample_data_processing: matched `Cell Ranger` in "FASTQs were then used to quantify gene expression using Cell Ranger count (version 5.0.1) and the GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics) human genome reference."
- GSM6731278 / Sample_data_processing: matched `10X` in "Assembly: GRCh38 (version refdata-gex-GRCh38-2020-A, 10X Genomics)"
- GSM6731278 / Sample_data_processing: matched `10X` in "Supplementary files format and content: Position sorted BAMs, BAM indexes, and gene expression counts in 10X format (separate barcodes, features, and matrix files for each sample)."
- GSM6731263 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731263/suppl/GSM6731263_hNK1_barcodes.tsv.gz"
- GSM6731263 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731263/suppl/GSM6731263_hNK1_features.tsv.gz"
- GSM6731263 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731263/suppl/GSM6731263_hNK1_matrix.mtx.gz"
- GSM6731264 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731264/suppl/GSM6731264_hNK2_barcodes.tsv.gz"
- GSM6731264 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731264/suppl/GSM6731264_hNK2_features.tsv.gz"
- GSM6731264 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731264/suppl/GSM6731264_hNK2_matrix.mtx.gz"
- GSM6731265 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731265/suppl/GSM6731265_hNK3_barcodes.tsv.gz"
- GSM6731265 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731265/suppl/GSM6731265_hNK3_features.tsv.gz"
- GSM6731265 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731265/suppl/GSM6731265_hNK3_matrix.mtx.gz"
- GSM6731266 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731266/suppl/GSM6731266_hNK4_barcodes.tsv.gz"
- GSM6731266 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731266/suppl/GSM6731266_hNK4_features.tsv.gz"
- GSM6731266 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731266/suppl/GSM6731266_hNK4_matrix.mtx.gz"
- GSM6731267 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731267/suppl/GSM6731267_hNK5_barcodes.tsv.gz"
- GSM6731267 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731267/suppl/GSM6731267_hNK5_features.tsv.gz"
- GSM6731267 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731267/suppl/GSM6731267_hNK5_matrix.mtx.gz"
- GSM6731268 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731268/suppl/GSM6731268_hNK6_barcodes.tsv.gz"
- GSM6731268 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731268/suppl/GSM6731268_hNK6_features.tsv.gz"
- GSM6731268 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731268/suppl/GSM6731268_hNK6_matrix.mtx.gz"
- GSM6731269 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731269/suppl/GSM6731269_hNK7_barcodes.tsv.gz"
- GSM6731269 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731269/suppl/GSM6731269_hNK7_features.tsv.gz"
- GSM6731269 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731269/suppl/GSM6731269_hNK7_matrix.mtx.gz"
- GSM6731270 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731270/suppl/GSM6731270_hNK8_barcodes.tsv.gz"
- GSM6731270 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731270/suppl/GSM6731270_hNK8_features.tsv.gz"
- GSM6731270 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731270/suppl/GSM6731270_hNK8_matrix.mtx.gz"
- GSM6731271 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731271/suppl/GSM6731271_hNK9_barcodes.tsv.gz"
- GSM6731271 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731271/suppl/GSM6731271_hNK9_features.tsv.gz"
- GSM6731271 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731271/suppl/GSM6731271_hNK9_matrix.mtx.gz"
- GSM6731272 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731272/suppl/GSM6731272_hNK10_barcodes.tsv.gz"
- GSM6731272 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731272/suppl/GSM6731272_hNK10_features.tsv.gz"
- GSM6731272 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731272/suppl/GSM6731272_hNK10_matrix.mtx.gz"
- GSM6731273 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731273/suppl/GSM6731273_hNK11_barcodes.tsv.gz"
- GSM6731273 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731273/suppl/GSM6731273_hNK11_features.tsv.gz"
- GSM6731273 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731273/suppl/GSM6731273_hNK11_matrix.mtx.gz"
- GSM6731274 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731274/suppl/GSM6731274_hNK12_barcodes.tsv.gz"
- GSM6731274 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731274/suppl/GSM6731274_hNK12_features.tsv.gz"
- GSM6731274 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731274/suppl/GSM6731274_hNK12_matrix.mtx.gz"
- GSM6731275 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731275/suppl/GSM6731275_hNK13_barcodes.tsv.gz"
- GSM6731275 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731275/suppl/GSM6731275_hNK13_features.tsv.gz"
- GSM6731275 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731275/suppl/GSM6731275_hNK13_matrix.mtx.gz"
- GSM6731276 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731276/suppl/GSM6731276_hNK14_barcodes.tsv.gz"
- GSM6731276 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731276/suppl/GSM6731276_hNK14_features.tsv.gz"
- GSM6731276 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731276/suppl/GSM6731276_hNK14_matrix.mtx.gz"
- GSM6731277 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731277/suppl/GSM6731277_hNK15_barcodes.tsv.gz"
- GSM6731277 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731277/suppl/GSM6731277_hNK15_features.tsv.gz"
- GSM6731277 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731277/suppl/GSM6731277_hNK15_matrix.mtx.gz"
- GSM6731278 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731278/suppl/GSM6731278_hNK16_barcodes.tsv.gz"
- GSM6731278 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731278/suppl/GSM6731278_hNK16_features.tsv.gz"
- GSM6731278 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6731nnn/GSM6731278/suppl/GSM6731278_hNK16_matrix.mtx.gz"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: 10X, Cell Ranger, barcodes.tsv, features.tsv, matrix.mtx (16 sample(s)))
<!-- /computed -->