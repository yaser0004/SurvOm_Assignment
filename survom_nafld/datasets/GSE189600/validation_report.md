# Validation report: GSE189600

Hepatocytes demarcated by EphB2 contribute to the progression of non-alcoholic steatohepatitis

<!-- computed -->
Sample count: 21

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 21 samples |
| organism_consistency | WARN | mixed organisms: Homo sapiens 6/21, Mus musculus 15/21 |
| source_tissue | PASS | liver-pattern source 21/21 |
| library_strategy | WARN | mixed strategies: ATAC-seq 5/21, RNA-Seq 16/21 |
| library_source | WARN | library_source: genomic 5/21, transcriptomic 10/21, transcriptomic single cell 6/21 |
| library_selection | WARN | mixed library_selection: cDNA 16/21, other 5/21 |
| instrument_model | PASS | Illumina NovaSeq 6000 21/21 |
| metadata_completeness | WARN | patchy fields: age 6/21, disease 6/21, ethnicity 6/21, sex 6/21, treatment 15/21. reported consistently: tissue; not reported anywhere: bmi, diagnosis, fibrosis_stage, group, nas_score, stage, steatosis_grade |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (3 sample(s)) |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: 10X, Cellranger, Chromium, barcodes.tsv, features.tsv, matrix.mtx, nuclei were isolat, snRNA (21 sample(s)) |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (10/21), packaged in GSE189600_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE189600-GPL24247_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX13234439, https://www.ncbi.nlm.nih.gov/sra?term=SRX13234440, https://www.ncbi.nlm.nih.gov/sra?term=SRX13234441, https://www.ncbi.nlm.nih.gov/sra?term=SRX13234442, https://www.ncbi.nlm.nih.gov/sra?term=SRX13234443, and 16 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 31 (1), 47 (1), 49 (1), 50 (2), 64 (1)
- **disease**: NASH (3), healthy (3)
- **ethnicity**: Asian or Pacific Islander (1), Caucasian (2), N/A (3)
- **sex**: Female (2), Male (4)
- **tissue**: liver (6), whole liver (15)
- **treatment**: Normal chow for 3 months (3), Normal chow for 9 months (2), injected with AAV8-TBG-Ephb2 (3), injected with AAV8-TBG-GFP (3), modified ALIOS diet for 3 months (2), modified ALIOS diet for 9 months (2)

## Field presence

- Sex: 6/21 (canon: sex)
- age: 6/21 (canon: age)
- disease state: 6/21 (canon: disease)
- genotype: 6/21
- race: 6/21 (canon: ethnicity)
- strain: 15/21
- tissue: 21/21 (canon: tissue)
- treatment: 15/21 (canon: treatment)

## Evidence for WARN/FAIL checks

### organism_consistency (WARN)
### library_strategy (WARN)
### library_source (WARN)
### library_selection (WARN)
### metadata_completeness (WARN)
### single_cell_or_spatial (FAIL)
- GSM5704309 / Sample_extract_protocol_ch1: matched `snRNA` in "For snRNA-seq and snATAC-seq, liver nuclei were isolated and loaded to 10X Genomics Chromium controller"
- GSM5704309 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNAseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell 3′ Kit"
- GSM5704309 / Sample_extract_protocol_ch1: matched `Chromium` in "snATACseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell ATAC kit"
- GSM5704309 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq, snATAC-seq, bulk RNA-seq"
- GSM5704310 / Sample_extract_protocol_ch1: matched `snRNA` in "For snRNA-seq and snATAC-seq, liver nuclei were isolated and loaded to 10X Genomics Chromium controller"
- GSM5704310 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNAseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell 3′ Kit"
- GSM5704310 / Sample_extract_protocol_ch1: matched `Chromium` in "snATACseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell ATAC kit"
- GSM5704310 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq, snATAC-seq, bulk RNA-seq"
- GSM5704311 / Sample_extract_protocol_ch1: matched `snRNA` in "For snRNA-seq and snATAC-seq, liver nuclei were isolated and loaded to 10X Genomics Chromium controller"
- GSM5704311 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNAseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell 3′ Kit"
- GSM5704311 / Sample_extract_protocol_ch1: matched `Chromium` in "snATACseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell ATAC kit"
- GSM5704311 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq, snATAC-seq, bulk RNA-seq"
- GSM5704312 / Sample_extract_protocol_ch1: matched `snRNA` in "For snRNA-seq and snATAC-seq, liver nuclei were isolated and loaded to 10X Genomics Chromium controller"
- GSM5704312 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNAseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell 3′ Kit"
- GSM5704312 / Sample_extract_protocol_ch1: matched `Chromium` in "snATACseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell ATAC kit"
- GSM5704312 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq, snATAC-seq, bulk RNA-seq"
- GSM5704313 / Sample_extract_protocol_ch1: matched `snRNA` in "For snRNA-seq and snATAC-seq, liver nuclei were isolated and loaded to 10X Genomics Chromium controller"
- GSM5704313 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNAseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell 3′ Kit"
- GSM5704313 / Sample_extract_protocol_ch1: matched `Chromium` in "snATACseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell ATAC kit"
- GSM5704313 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq, snATAC-seq, bulk RNA-seq"
- GSM5704314 / Sample_extract_protocol_ch1: matched `snRNA` in "For snRNA-seq and snATAC-seq, liver nuclei were isolated and loaded to 10X Genomics Chromium controller"
- GSM5704314 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNAseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell 3′ Kit"
- GSM5704314 / Sample_extract_protocol_ch1: matched `Chromium` in "snATACseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell ATAC kit"
- GSM5704314 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq, snATAC-seq, bulk RNA-seq"
- GSM5704315 / Sample_extract_protocol_ch1: matched `snRNA` in "For snRNA-seq and snATAC-seq, liver nuclei were isolated and loaded to 10X Genomics Chromium controller"
- GSM5704315 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNAseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell 3′ Kit"
- GSM5704315 / Sample_extract_protocol_ch1: matched `Chromium` in "snATACseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell ATAC kit"
- GSM5704315 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq, snATAC-seq, bulk RNA-seq"
- GSM5704316 / Sample_extract_protocol_ch1: matched `snRNA` in "For snRNA-seq and snATAC-seq, liver nuclei were isolated and loaded to 10X Genomics Chromium controller"
- GSM5704316 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNAseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell 3′ Kit"
- GSM5704316 / Sample_extract_protocol_ch1: matched `Chromium` in "snATACseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell ATAC kit"
- GSM5704316 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq, snATAC-seq, bulk RNA-seq"
- GSM5704317 / Sample_extract_protocol_ch1: matched `snRNA` in "For snRNA-seq and snATAC-seq, liver nuclei were isolated and loaded to 10X Genomics Chromium controller"
- GSM5704317 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNAseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell 3′ Kit"
- GSM5704317 / Sample_extract_protocol_ch1: matched `Chromium` in "snATACseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell ATAC kit"
- GSM5704317 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq, snATAC-seq, bulk RNA-seq"
- GSM5704321 / Sample_extract_protocol_ch1: matched `snRNA` in "For snRNA-seq and snATAC-seq, liver nuclei were isolated and loaded to 10X Genomics Chromium controller"
- GSM5704321 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNAseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell 3′ Kit"
- GSM5704321 / Sample_extract_protocol_ch1: matched `Chromium` in "snATACseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell ATAC kit"
- GSM5704321 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq, snATAC-seq, bulk RNA-seq"
- GSM5704322 / Sample_extract_protocol_ch1: matched `snRNA` in "For snRNA-seq and snATAC-seq, liver nuclei were isolated and loaded to 10X Genomics Chromium controller"
- GSM5704322 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNAseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell 3′ Kit"
- GSM5704322 / Sample_extract_protocol_ch1: matched `Chromium` in "snATACseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell ATAC kit"
- GSM5704322 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq, snATAC-seq, bulk RNA-seq"
- GSM5704323 / Sample_extract_protocol_ch1: matched `snRNA` in "For snRNA-seq and snATAC-seq, liver nuclei were isolated and loaded to 10X Genomics Chromium controller"
- GSM5704323 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNAseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell 3′ Kit"
- GSM5704323 / Sample_extract_protocol_ch1: matched `Chromium` in "snATACseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell ATAC kit"
- GSM5704323 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq, snATAC-seq, bulk RNA-seq"
- GSM5704324 / Sample_extract_protocol_ch1: matched `snRNA` in "For snRNA-seq and snATAC-seq, liver nuclei were isolated and loaded to 10X Genomics Chromium controller"
- GSM5704324 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNAseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell 3′ Kit"
- GSM5704324 / Sample_extract_protocol_ch1: matched `Chromium` in "snATACseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell ATAC kit"
- GSM5704324 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq, snATAC-seq, bulk RNA-seq"
- GSM5704325 / Sample_extract_protocol_ch1: matched `snRNA` in "For snRNA-seq and snATAC-seq, liver nuclei were isolated and loaded to 10X Genomics Chromium controller"
- GSM5704325 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNAseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell 3′ Kit"
- GSM5704325 / Sample_extract_protocol_ch1: matched `Chromium` in "snATACseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell ATAC kit"
- GSM5704325 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq, snATAC-seq, bulk RNA-seq"
- GSM5704326 / Sample_extract_protocol_ch1: matched `snRNA` in "For snRNA-seq and snATAC-seq, liver nuclei were isolated and loaded to 10X Genomics Chromium controller"
- GSM5704326 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNAseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell 3′ Kit"
- GSM5704326 / Sample_extract_protocol_ch1: matched `Chromium` in "snATACseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell ATAC kit"
- GSM5704326 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq, snATAC-seq, bulk RNA-seq"
- GSM6808755 / Sample_extract_protocol_ch1: matched `nuclei were isolat` in "human study: liver nuclei were isolated and loaded to 10X Genomics Chromium controller"
- GSM6808755 / Sample_extract_protocol_ch1: matched `snRNA` in "human study: snRNAseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell 3′ Kit"
- GSM6808755 / Sample_extract_protocol_ch1: matched `10X` in "human study: In addition to the standard 10X Genomic snRNAseq library preparation, targeted sequencing libraries for EPHB2 were prepared using xGen Hybridization and Wash Kit from IDT"
- GSM6808755 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq"
- GSM6808756 / Sample_extract_protocol_ch1: matched `nuclei were isolat` in "human study: liver nuclei were isolated and loaded to 10X Genomics Chromium controller"
- GSM6808756 / Sample_extract_protocol_ch1: matched `snRNA` in "human study: snRNAseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell 3′ Kit"
- GSM6808756 / Sample_extract_protocol_ch1: matched `10X` in "human study: In addition to the standard 10X Genomic snRNAseq library preparation, targeted sequencing libraries for EPHB2 were prepared using xGen Hybridization and Wash Kit from IDT"
- GSM6808756 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq"
- GSM6808757 / Sample_extract_protocol_ch1: matched `nuclei were isolat` in "human study: liver nuclei were isolated and loaded to 10X Genomics Chromium controller"
- GSM6808757 / Sample_extract_protocol_ch1: matched `snRNA` in "human study: snRNAseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell 3′ Kit"
- GSM6808757 / Sample_extract_protocol_ch1: matched `10X` in "human study: In addition to the standard 10X Genomic snRNAseq library preparation, targeted sequencing libraries for EPHB2 were prepared using xGen Hybridization and Wash Kit from IDT"
- GSM6808757 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq"
- GSM6808758 / Sample_extract_protocol_ch1: matched `nuclei were isolat` in "human study: liver nuclei were isolated and loaded to 10X Genomics Chromium controller"
- GSM6808758 / Sample_extract_protocol_ch1: matched `snRNA` in "human study: snRNAseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell 3′ Kit"
- GSM6808758 / Sample_extract_protocol_ch1: matched `10X` in "human study: In addition to the standard 10X Genomic snRNAseq library preparation, targeted sequencing libraries for EPHB2 were prepared using xGen Hybridization and Wash Kit from IDT"
- GSM6808758 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq"
- GSM6808759 / Sample_extract_protocol_ch1: matched `nuclei were isolat` in "human study: liver nuclei were isolated and loaded to 10X Genomics Chromium controller"
- GSM6808759 / Sample_extract_protocol_ch1: matched `snRNA` in "human study: snRNAseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell 3′ Kit"
- GSM6808759 / Sample_extract_protocol_ch1: matched `10X` in "human study: In addition to the standard 10X Genomic snRNAseq library preparation, targeted sequencing libraries for EPHB2 were prepared using xGen Hybridization and Wash Kit from IDT"
- GSM6808759 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq"
- GSM6808760 / Sample_extract_protocol_ch1: matched `nuclei were isolat` in "human study: liver nuclei were isolated and loaded to 10X Genomics Chromium controller"
- GSM6808760 / Sample_extract_protocol_ch1: matched `snRNA` in "human study: snRNAseq libraries were prepared according to manufacturer’s instructions of Chromium Next GEM Single Cell 3′ Kit"
- GSM6808760 / Sample_extract_protocol_ch1: matched `10X` in "human study: In addition to the standard 10X Genomic snRNAseq library preparation, targeted sequencing libraries for EPHB2 were prepared using xGen Hybridization and Wash Kit from IDT"
- GSM6808760 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq"
- GSM5704309 / Sample_data_processing: matched `snRNA` in "The raw fastq files of snRNA-seq were mapped to Mus musculus assembly GRCm38 (mm10) using CellRanger (3.0.2). Unique molecular identifiers (UMI) count matrices were imported into Seurat (3.2.0) (Stuar"
- GSM5704309 / Sample_data_processing: matched `Cellranger` in "The raw fastq files of mouse livers and human livers were mapped to Mus musculus genome assembly GRCm38 (mm10) and Homo sapiens genome assembly GRCh38 (hg38) respectively using Cellranger-atac (1.2.0)"
- GSM5704309 / Sample_data_processing: matched `snRNA` in "Supplementary_files_format_and_content: raw counts files and metadata of cell identity with assigned cluster identity for snRNA-seq; fragment counts files and metadata with assigned cluster identity f"
- GSM5704310 / Sample_data_processing: matched `snRNA` in "The raw fastq files of snRNA-seq were mapped to Mus musculus assembly GRCm38 (mm10) using CellRanger (3.0.2). Unique molecular identifiers (UMI) count matrices were imported into Seurat (3.2.0) (Stuar"
- GSM5704310 / Sample_data_processing: matched `Cellranger` in "The raw fastq files of mouse livers and human livers were mapped to Mus musculus genome assembly GRCm38 (mm10) and Homo sapiens genome assembly GRCh38 (hg38) respectively using Cellranger-atac (1.2.0)"
- GSM5704310 / Sample_data_processing: matched `snRNA` in "Supplementary_files_format_and_content: raw counts files and metadata of cell identity with assigned cluster identity for snRNA-seq; fragment counts files and metadata with assigned cluster identity f"
- GSM5704311 / Sample_data_processing: matched `snRNA` in "The raw fastq files of snRNA-seq were mapped to Mus musculus assembly GRCm38 (mm10) using CellRanger (3.0.2). Unique molecular identifiers (UMI) count matrices were imported into Seurat (3.2.0) (Stuar"
- GSM5704311 / Sample_data_processing: matched `Cellranger` in "The raw fastq files of mouse livers and human livers were mapped to Mus musculus genome assembly GRCm38 (mm10) and Homo sapiens genome assembly GRCh38 (hg38) respectively using Cellranger-atac (1.2.0)"
- GSM5704311 / Sample_data_processing: matched `snRNA` in "Supplementary_files_format_and_content: raw counts files and metadata of cell identity with assigned cluster identity for snRNA-seq; fragment counts files and metadata with assigned cluster identity f"
- GSM5704312 / Sample_data_processing: matched `snRNA` in "The raw fastq files of snRNA-seq were mapped to Mus musculus assembly GRCm38 (mm10) using CellRanger (3.0.2). Unique molecular identifiers (UMI) count matrices were imported into Seurat (3.2.0) (Stuar"
- GSM5704312 / Sample_data_processing: matched `Cellranger` in "The raw fastq files of mouse livers and human livers were mapped to Mus musculus genome assembly GRCm38 (mm10) and Homo sapiens genome assembly GRCh38 (hg38) respectively using Cellranger-atac (1.2.0)"
- GSM5704312 / Sample_data_processing: matched `snRNA` in "Supplementary_files_format_and_content: raw counts files and metadata of cell identity with assigned cluster identity for snRNA-seq; fragment counts files and metadata with assigned cluster identity f"
- GSM5704313 / Sample_data_processing: matched `snRNA` in "The raw fastq files of snRNA-seq were mapped to Mus musculus assembly GRCm38 (mm10) using CellRanger (3.0.2). Unique molecular identifiers (UMI) count matrices were imported into Seurat (3.2.0) (Stuar"
- GSM5704313 / Sample_data_processing: matched `Cellranger` in "The raw fastq files of mouse livers and human livers were mapped to Mus musculus genome assembly GRCm38 (mm10) and Homo sapiens genome assembly GRCh38 (hg38) respectively using Cellranger-atac (1.2.0)"
- GSM5704313 / Sample_data_processing: matched `snRNA` in "Supplementary_files_format_and_content: raw counts files and metadata of cell identity with assigned cluster identity for snRNA-seq; fragment counts files and metadata with assigned cluster identity f"
- GSM5704314 / Sample_data_processing: matched `snRNA` in "The raw fastq files of snRNA-seq were mapped to Mus musculus assembly GRCm38 (mm10) using CellRanger (3.0.2). Unique molecular identifiers (UMI) count matrices were imported into Seurat (3.2.0) (Stuar"
- GSM5704314 / Sample_data_processing: matched `Cellranger` in "The raw fastq files of mouse livers and human livers were mapped to Mus musculus genome assembly GRCm38 (mm10) and Homo sapiens genome assembly GRCh38 (hg38) respectively using Cellranger-atac (1.2.0)"
- GSM5704314 / Sample_data_processing: matched `snRNA` in "Supplementary_files_format_and_content: raw counts files and metadata of cell identity with assigned cluster identity for snRNA-seq; fragment counts files and metadata with assigned cluster identity f"
- GSM5704315 / Sample_data_processing: matched `snRNA` in "The raw fastq files of snRNA-seq were mapped to Mus musculus assembly GRCm38 (mm10) using CellRanger (3.0.2). Unique molecular identifiers (UMI) count matrices were imported into Seurat (3.2.0) (Stuar"
- GSM5704315 / Sample_data_processing: matched `Cellranger` in "The raw fastq files of mouse livers and human livers were mapped to Mus musculus genome assembly GRCm38 (mm10) and Homo sapiens genome assembly GRCh38 (hg38) respectively using Cellranger-atac (1.2.0)"
- GSM5704315 / Sample_data_processing: matched `snRNA` in "Supplementary_files_format_and_content: raw counts files and metadata of cell identity with assigned cluster identity for snRNA-seq; fragment counts files and metadata with assigned cluster identity f"
- GSM5704316 / Sample_data_processing: matched `snRNA` in "The raw fastq files of snRNA-seq were mapped to Mus musculus assembly GRCm38 (mm10) using CellRanger (3.0.2). Unique molecular identifiers (UMI) count matrices were imported into Seurat (3.2.0) (Stuar"
- GSM5704316 / Sample_data_processing: matched `Cellranger` in "The raw fastq files of mouse livers and human livers were mapped to Mus musculus genome assembly GRCm38 (mm10) and Homo sapiens genome assembly GRCh38 (hg38) respectively using Cellranger-atac (1.2.0)"
- GSM5704316 / Sample_data_processing: matched `snRNA` in "Supplementary_files_format_and_content: raw counts files and metadata of cell identity with assigned cluster identity for snRNA-seq; fragment counts files and metadata with assigned cluster identity f"
- GSM5704317 / Sample_data_processing: matched `snRNA` in "The raw fastq files of snRNA-seq were mapped to Mus musculus assembly GRCm38 (mm10) using CellRanger (3.0.2). Unique molecular identifiers (UMI) count matrices were imported into Seurat (3.2.0) (Stuar"
- GSM5704317 / Sample_data_processing: matched `Cellranger` in "The raw fastq files of mouse livers and human livers were mapped to Mus musculus genome assembly GRCm38 (mm10) and Homo sapiens genome assembly GRCh38 (hg38) respectively using Cellranger-atac (1.2.0)"
- GSM5704317 / Sample_data_processing: matched `snRNA` in "Supplementary_files_format_and_content: raw counts files and metadata of cell identity with assigned cluster identity for snRNA-seq; fragment counts files and metadata with assigned cluster identity f"
- GSM5704321 / Sample_data_processing: matched `snRNA` in "The raw fastq files of snRNA-seq were mapped to Mus musculus assembly GRCm38 (mm10) using CellRanger (3.0.2). Unique molecular identifiers (UMI) count matrices were imported into Seurat (3.2.0) (Stuar"
- GSM5704321 / Sample_data_processing: matched `Cellranger` in "The raw fastq files of mouse livers and human livers were mapped to Mus musculus genome assembly GRCm38 (mm10) and Homo sapiens genome assembly GRCh38 (hg38) respectively using Cellranger-atac (1.2.0)"
- GSM5704321 / Sample_data_processing: matched `snRNA` in "Supplementary_files_format_and_content: raw counts files and metadata of cell identity with assigned cluster identity for snRNA-seq; fragment counts files and metadata with assigned cluster identity f"
- GSM5704322 / Sample_data_processing: matched `snRNA` in "The raw fastq files of snRNA-seq were mapped to Mus musculus assembly GRCm38 (mm10) using CellRanger (3.0.2). Unique molecular identifiers (UMI) count matrices were imported into Seurat (3.2.0) (Stuar"
- GSM5704322 / Sample_data_processing: matched `Cellranger` in "The raw fastq files of mouse livers and human livers were mapped to Mus musculus genome assembly GRCm38 (mm10) and Homo sapiens genome assembly GRCh38 (hg38) respectively using Cellranger-atac (1.2.0)"
- GSM5704322 / Sample_data_processing: matched `snRNA` in "Supplementary_files_format_and_content: raw counts files and metadata of cell identity with assigned cluster identity for snRNA-seq; fragment counts files and metadata with assigned cluster identity f"
- GSM5704323 / Sample_data_processing: matched `snRNA` in "The raw fastq files of snRNA-seq were mapped to Mus musculus assembly GRCm38 (mm10) using CellRanger (3.0.2). Unique molecular identifiers (UMI) count matrices were imported into Seurat (3.2.0) (Stuar"
- GSM5704323 / Sample_data_processing: matched `Cellranger` in "The raw fastq files of mouse livers and human livers were mapped to Mus musculus genome assembly GRCm38 (mm10) and Homo sapiens genome assembly GRCh38 (hg38) respectively using Cellranger-atac (1.2.0)"
- GSM5704323 / Sample_data_processing: matched `snRNA` in "Supplementary_files_format_and_content: raw counts files and metadata of cell identity with assigned cluster identity for snRNA-seq; fragment counts files and metadata with assigned cluster identity f"
- GSM5704324 / Sample_data_processing: matched `snRNA` in "The raw fastq files of snRNA-seq were mapped to Mus musculus assembly GRCm38 (mm10) using CellRanger (3.0.2). Unique molecular identifiers (UMI) count matrices were imported into Seurat (3.2.0) (Stuar"
- GSM5704324 / Sample_data_processing: matched `Cellranger` in "The raw fastq files of mouse livers and human livers were mapped to Mus musculus genome assembly GRCm38 (mm10) and Homo sapiens genome assembly GRCh38 (hg38) respectively using Cellranger-atac (1.2.0)"
- GSM5704324 / Sample_data_processing: matched `snRNA` in "Supplementary_files_format_and_content: raw counts files and metadata of cell identity with assigned cluster identity for snRNA-seq; fragment counts files and metadata with assigned cluster identity f"
- GSM5704325 / Sample_data_processing: matched `snRNA` in "The raw fastq files of snRNA-seq were mapped to Mus musculus assembly GRCm38 (mm10) using CellRanger (3.0.2). Unique molecular identifiers (UMI) count matrices were imported into Seurat (3.2.0) (Stuar"
- GSM5704325 / Sample_data_processing: matched `Cellranger` in "The raw fastq files of mouse livers and human livers were mapped to Mus musculus genome assembly GRCm38 (mm10) and Homo sapiens genome assembly GRCh38 (hg38) respectively using Cellranger-atac (1.2.0)"
- GSM5704325 / Sample_data_processing: matched `snRNA` in "Supplementary_files_format_and_content: raw counts files and metadata of cell identity with assigned cluster identity for snRNA-seq; fragment counts files and metadata with assigned cluster identity f"
- GSM5704326 / Sample_data_processing: matched `snRNA` in "The raw fastq files of snRNA-seq were mapped to Mus musculus assembly GRCm38 (mm10) using CellRanger (3.0.2). Unique molecular identifiers (UMI) count matrices were imported into Seurat (3.2.0) (Stuar"
- GSM5704326 / Sample_data_processing: matched `Cellranger` in "The raw fastq files of mouse livers and human livers were mapped to Mus musculus genome assembly GRCm38 (mm10) and Homo sapiens genome assembly GRCh38 (hg38) respectively using Cellranger-atac (1.2.0)"
- GSM5704326 / Sample_data_processing: matched `snRNA` in "Supplementary_files_format_and_content: raw counts files and metadata of cell identity with assigned cluster identity for snRNA-seq; fragment counts files and metadata with assigned cluster identity f"
- GSM6808755 / Sample_data_processing: matched `snRNA` in "The raw fastq files of snRNA-seq were mapped to Homo sapiens genome assembly GRCh38 (hg38) using CellRanger (3.0.2). Unique molecular identifiers (UMI) count matrices were imported into Seurat (3.2.0)"
- GSM6808756 / Sample_data_processing: matched `snRNA` in "The raw fastq files of snRNA-seq were mapped to Homo sapiens genome assembly GRCh38 (hg38) using CellRanger (3.0.2). Unique molecular identifiers (UMI) count matrices were imported into Seurat (3.2.0)"
- GSM6808757 / Sample_data_processing: matched `snRNA` in "The raw fastq files of snRNA-seq were mapped to Homo sapiens genome assembly GRCh38 (hg38) using CellRanger (3.0.2). Unique molecular identifiers (UMI) count matrices were imported into Seurat (3.2.0)"
- GSM6808758 / Sample_data_processing: matched `snRNA` in "The raw fastq files of snRNA-seq were mapped to Homo sapiens genome assembly GRCh38 (hg38) using CellRanger (3.0.2). Unique molecular identifiers (UMI) count matrices were imported into Seurat (3.2.0)"
- GSM6808759 / Sample_data_processing: matched `snRNA` in "The raw fastq files of snRNA-seq were mapped to Homo sapiens genome assembly GRCh38 (hg38) using CellRanger (3.0.2). Unique molecular identifiers (UMI) count matrices were imported into Seurat (3.2.0)"
- GSM6808760 / Sample_data_processing: matched `snRNA` in "The raw fastq files of snRNA-seq were mapped to Homo sapiens genome assembly GRCh38 (hg38) using CellRanger (3.0.2). Unique molecular identifiers (UMI) count matrices were imported into Seurat (3.2.0)"
- GSM5704309 / Sample_title: matched `snRNA` in "snRNA-seq_NC_3mo"
- GSM5704310 / Sample_title: matched `snRNA` in "snRNA-seq_NC_9mo"
- GSM5704311 / Sample_title: matched `snRNA` in "snRNA-seq_ALIOS_3mo"
- GSM5704312 / Sample_title: matched `snRNA` in "snRNA-seq_ALIOS_9mo"
- GSM6808755 / Sample_title: matched `snRNA` in "snRNA-seq_human_healthy_rep1"
- GSM6808756 / Sample_title: matched `snRNA` in "snRNA-seq_human_healthy_rep2"
- GSM6808757 / Sample_title: matched `snRNA` in "snRNA-seq_human_healthy_rep3"
- GSM6808758 / Sample_title: matched `snRNA` in "snRNA-seq_human_NASH_rep1"
- GSM6808759 / Sample_title: matched `snRNA` in "snRNA-seq_human_NASH_rep2"
- GSM6808760 / Sample_title: matched `snRNA` in "snRNA-seq_human_NASH_rep3"
- GSM5704309 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5704nnn/GSM5704309/suppl/GSM5704309_snRNAseq_3moNC_barcodes.tsv.gz"
- GSM5704309 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5704nnn/GSM5704309/suppl/GSM5704309_snRNAseq_3moNC_features.tsv.gz"
- GSM5704309 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5704nnn/GSM5704309/suppl/GSM5704309_snRNAseq_3moNC_matrix.mtx.gz"
- GSM5704310 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5704nnn/GSM5704310/suppl/GSM5704310_snRNAseq_9moNC_barcodes.tsv.gz"
- GSM5704310 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5704nnn/GSM5704310/suppl/GSM5704310_snRNAseq_9moNC_features.tsv.gz"
- GSM5704310 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5704nnn/GSM5704310/suppl/GSM5704310_snRNAseq_9moNC_matrix.mtx.gz"
- GSM5704311 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5704nnn/GSM5704311/suppl/GSM5704311_snRNAseq_3moNASH_barcodes.tsv.gz"
- GSM5704311 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5704nnn/GSM5704311/suppl/GSM5704311_snRNAseq_3moNASH_features.tsv.gz"
- GSM5704311 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5704nnn/GSM5704311/suppl/GSM5704311_snRNAseq_3moNASH_matrix.mtx.gz"
- GSM5704312 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5704nnn/GSM5704312/suppl/GSM5704312_snRNAseq_9moNASH_barcodes.tsv.gz"
- GSM5704312 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5704nnn/GSM5704312/suppl/GSM5704312_snRNAseq_9moNASH_features.tsv.gz"
- GSM5704312 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5704nnn/GSM5704312/suppl/GSM5704312_snRNAseq_9moNASH_matrix.mtx.gz"
- GSM6808755 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6808nnn/GSM6808755/suppl/GSM6808755_Y21822A1_barcodes.tsv.gz"
- GSM6808755 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6808nnn/GSM6808755/suppl/GSM6808755_Y21822A1_features.tsv.gz"
- GSM6808755 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6808nnn/GSM6808755/suppl/GSM6808755_Y21822A1_matrix.mtx.gz"
- GSM6808756 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6808nnn/GSM6808756/suppl/GSM6808756_Y31122A5_barcodes.tsv.gz"
- GSM6808756 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6808nnn/GSM6808756/suppl/GSM6808756_Y31122A5_features.tsv.gz"
- GSM6808756 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6808nnn/GSM6808756/suppl/GSM6808756_Y31122A5_matrix.mtx.gz"
- GSM6808757 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6808nnn/GSM6808757/suppl/GSM6808757_Y31122A8_barcodes.tsv.gz"
- GSM6808757 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6808nnn/GSM6808757/suppl/GSM6808757_Y31122A8_features.tsv.gz"
- GSM6808757 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6808nnn/GSM6808757/suppl/GSM6808757_Y31122A8_matrix.mtx.gz"
- GSM6808758 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6808nnn/GSM6808758/suppl/GSM6808758_Y21822A2_barcodes.tsv.gz"
- GSM6808758 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6808nnn/GSM6808758/suppl/GSM6808758_Y21822A2_features.tsv.gz"
- GSM6808758 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6808nnn/GSM6808758/suppl/GSM6808758_Y21822A2_matrix.mtx.gz"
- GSM6808759 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6808nnn/GSM6808759/suppl/GSM6808759_Y31122A6_barcodes.tsv.gz"
- GSM6808759 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6808nnn/GSM6808759/suppl/GSM6808759_Y31122A6_features.tsv.gz"
- GSM6808759 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6808nnn/GSM6808759/suppl/GSM6808759_Y31122A6_matrix.mtx.gz"
- GSM6808760 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6808nnn/GSM6808760/suppl/GSM6808760_Y31122A7_barcodes.tsv.gz"
- GSM6808760 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6808nnn/GSM6808760/suppl/GSM6808760_Y31122A7_features.tsv.gz"
- GSM6808760 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6808nnn/GSM6808760/suppl/GSM6808760_Y31122A7_matrix.mtx.gz"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: 10X, Cellranger, Chromium, barcodes.tsv, features.tsv, matrix.mtx, nuclei were isolat, snRNA (21 sample(s)))
<!-- /computed -->