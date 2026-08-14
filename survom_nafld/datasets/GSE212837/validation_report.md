# Validation report: GSE212837

An autocrine signaling circuit in hepatic stellate cells underlies advanced fibrosis in non-alcoholic steatohepatitis

<!-- computed -->
Sample count: 20

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 20 samples |
| organism_consistency | WARN | mixed organisms: Homo sapiens 18/20, Mus musculus 2/20 |
| source_tissue | PASS | liver-pattern source 20/20 |
| library_strategy | PASS | RNA-Seq 20/20 |
| library_source | WARN | library_source: transcriptomic single cell 20/20 |
| library_selection | PASS | cDNA 20/20 |
| instrument_model | WARN | mixed instruments: Illumina NextSeq 500 14/20, Illumina NovaSeq 6000 6/20 |
| metadata_completeness | PASS | reported consistently: age, disease, sex, tissue; not reported anywhere: bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (17 sample(s)) |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: .h5ad, 10x, Cell Ranger, Chromium, barcodes.tsv, features.tsv, matrix.mtx, snRNA (21 sample(s)) |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (20/20), packaged in GSE212837_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE212837-GPL18573_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX17477635, https://www.ncbi.nlm.nih.gov/sra?term=SRX17477636, https://www.ncbi.nlm.nih.gov/sra?term=SRX17477637, https://www.ncbi.nlm.nih.gov/sra?term=SRX17477638, https://www.ncbi.nlm.nih.gov/sra?term=SRX17477639, and 15 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 30 weeks (2), 34 years (2), 50 years (2), 51 years (3), 53 years (3), 56 years (1), 62 years (1), 63 years (1), 64 years (2), 68 years (1), 69 years (1), 72 years (1)
- **disease**: Control (3), NASH (17)
- **sex**: F (10), M (10)
- **tissue**: Liver (20)

## Field presence

- Sex: 20/20 (canon: sex)
- age: 20/20 (canon: age)
- disease state: 20/20 (canon: disease)
- tissue: 20/20 (canon: tissue)

## Evidence for WARN/FAIL checks

### organism_consistency (WARN)
### library_source (WARN)
### instrument_model (WARN)
### single_cell_or_spatial (FAIL)
- GSM6556449 / Sample_extract_protocol_ch1: matched `Chromium` in "Nuclei preparations were processed by the Chromium 3′ Gene Expression V3 Kit according to the manufacturer’s guidelines. Qubit 3 (Fisher Scientific) and 2100 Bioanalyzer (Agilent Technologies, Santa C"
- GSM6556450 / Sample_extract_protocol_ch1: matched `Chromium` in "Nuclei preparations were processed by the Chromium 3′ Gene Expression V3 Kit according to the manufacturer’s guidelines. Qubit 3 (Fisher Scientific) and 2100 Bioanalyzer (Agilent Technologies, Santa C"
- GSM6556451 / Sample_extract_protocol_ch1: matched `Chromium` in "Nuclei preparations were processed by the Chromium 3′ Gene Expression V3 Kit according to the manufacturer’s guidelines. Qubit 3 (Fisher Scientific) and 2100 Bioanalyzer (Agilent Technologies, Santa C"
- GSM6556452 / Sample_extract_protocol_ch1: matched `10x` in "frozen human liver tissue (~60 mm3) was lysed by Dounce homogenization (Kimble 2mL: 20 times with Pestle A over ~60 seconds) in 2mL lysis buffer (10mM Tris pH 7.0, 10mM NaCl, 3mM MgCl2, 0.05% Triton X"
- GSM6556452 / Sample_extract_protocol_ch1: matched `Chromium` in "Nuclei preparations were processed by the Chromium 3′ Gene Expression V3 Kit according to the manufacturer’s guidelines. Qubit 3 (Fisher Scientific) and 2100 Bioanalyzer (Agilent Technologies, Santa C"
- GSM6556453 / Sample_extract_protocol_ch1: matched `10x` in "frozen human liver tissue (~60 mm3) was lysed by Dounce homogenization (Kimble 2mL: 20 times with Pestle A over ~60 seconds) in 2mL lysis buffer (10mM Tris pH 7.0, 10mM NaCl, 3mM MgCl2, 0.05% Triton X"
- GSM6556453 / Sample_extract_protocol_ch1: matched `Chromium` in "Nuclei preparations were processed by the Chromium 3′ Gene Expression V3 Kit according to the manufacturer’s guidelines. Qubit 3 (Fisher Scientific) and 2100 Bioanalyzer (Agilent Technologies, Santa C"
- GSM6556454 / Sample_extract_protocol_ch1: matched `10x` in "frozen human liver tissue (~60 mm3) was lysed by Dounce homogenization (Kimble 2mL: 20 times with Pestle A over ~60 seconds) in 2mL lysis buffer (10mM Tris pH 7.0, 10mM NaCl, 3mM MgCl2, 0.05% Triton X"
- GSM6556454 / Sample_extract_protocol_ch1: matched `Chromium` in "Nuclei preparations were processed by the Chromium 3′ Gene Expression V3 Kit according to the manufacturer’s guidelines. Qubit 3 (Fisher Scientific) and 2100 Bioanalyzer (Agilent Technologies, Santa C"
- GSM6556455 / Sample_extract_protocol_ch1: matched `10x` in "frozen human liver tissue (~60 mm3) was lysed by Dounce homogenization (Kimble 2mL: 20 times with Pestle A over ~60 seconds) in 2mL lysis buffer (10mM Tris pH 7.0, 10mM NaCl, 3mM MgCl2, 0.05% Triton X"
- GSM6556455 / Sample_extract_protocol_ch1: matched `Chromium` in "Nuclei preparations were processed by the Chromium 3′ Gene Expression V3 Kit according to the manufacturer’s guidelines. Qubit 3 (Fisher Scientific) and 2100 Bioanalyzer (Agilent Technologies, Santa C"
- GSM6556456 / Sample_extract_protocol_ch1: matched `10x` in "frozen human liver tissue (~60 mm3) was lysed by Dounce homogenization (Kimble 2mL: 20 times with Pestle A over ~60 seconds) in 2mL lysis buffer (10mM Tris pH 7.0, 10mM NaCl, 3mM MgCl2, 0.05% Triton X"
- GSM6556456 / Sample_extract_protocol_ch1: matched `Chromium` in "Nuclei preparations were processed by the Chromium 3′ Gene Expression V3 Kit according to the manufacturer’s guidelines. Qubit 3 (Fisher Scientific) and 2100 Bioanalyzer (Agilent Technologies, Santa C"
- GSM6556457 / Sample_extract_protocol_ch1: matched `10x` in "frozen human liver tissue (~60 mm3) was lysed by Dounce homogenization (Kimble 2mL: 20 times with Pestle A over ~60 seconds) in 2mL lysis buffer (10mM Tris pH 7.0, 10mM NaCl, 3mM MgCl2, 0.05% Triton X"
- GSM6556457 / Sample_extract_protocol_ch1: matched `Chromium` in "Nuclei preparations were processed by the Chromium 3′ Gene Expression V3 Kit according to the manufacturer’s guidelines. Qubit 3 (Fisher Scientific) and 2100 Bioanalyzer (Agilent Technologies, Santa C"
- GSM6556458 / Sample_extract_protocol_ch1: matched `10x` in "frozen human liver tissue (~60 mm3) was lysed by Dounce homogenization (Kimble 2mL: 20 times with Pestle A over ~60 seconds) in 2mL lysis buffer (10mM Tris pH 7.0, 10mM NaCl, 3mM MgCl2, 0.05% Triton X"
- GSM6556458 / Sample_extract_protocol_ch1: matched `Chromium` in "Nuclei preparations were processed by the Chromium 3′ Gene Expression V3 Kit according to the manufacturer’s guidelines. Qubit 3 (Fisher Scientific) and 2100 Bioanalyzer (Agilent Technologies, Santa C"
- GSM6556459 / Sample_extract_protocol_ch1: matched `10x` in "frozen human liver tissue (~60 mm3) was lysed by Dounce homogenization (Kimble 2mL: 20 times with Pestle A over ~60 seconds) in 2mL lysis buffer (10mM Tris pH 7.0, 10mM NaCl, 3mM MgCl2, 0.05% Triton X"
- GSM6556459 / Sample_extract_protocol_ch1: matched `Chromium` in "Nuclei preparations were processed by the Chromium 3′ Gene Expression V3 Kit according to the manufacturer’s guidelines. Qubit 3 (Fisher Scientific) and 2100 Bioanalyzer (Agilent Technologies, Santa C"
- GSM6556460 / Sample_extract_protocol_ch1: matched `10x` in "frozen human liver tissue (~60 mm3) was lysed by Dounce homogenization (Kimble 2mL: 20 times with Pestle A over ~60 seconds) in 2mL lysis buffer (10mM Tris pH 7.0, 10mM NaCl, 3mM MgCl2, 0.05% Triton X"
- GSM6556460 / Sample_extract_protocol_ch1: matched `Chromium` in "Nuclei preparations were processed by the Chromium 3′ Gene Expression V3 Kit according to the manufacturer’s guidelines. Qubit 3 (Fisher Scientific) and 2100 Bioanalyzer (Agilent Technologies, Santa C"
- GSM6556461 / Sample_extract_protocol_ch1: matched `10x` in "frozen human liver tissue (~60 mm3) was lysed by Dounce homogenization (Kimble 2mL: 20 times with Pestle A over ~60 seconds) in 2mL lysis buffer (10mM Tris pH 7.0, 10mM NaCl, 3mM MgCl2, 0.05% Triton X"
- GSM6556461 / Sample_extract_protocol_ch1: matched `Chromium` in "Nuclei preparations were processed by the Chromium 3′ Gene Expression V3 Kit according to the manufacturer’s guidelines. Qubit 3 (Fisher Scientific) and 2100 Bioanalyzer (Agilent Technologies, Santa C"
- GSM6556462 / Sample_extract_protocol_ch1: matched `10x` in "frozen human liver tissue (~60 mm3) was lysed by Dounce homogenization (Kimble 2mL: 20 times with Pestle A over ~60 seconds) in 2mL lysis buffer (10mM Tris pH 7.0, 10mM NaCl, 3mM MgCl2, 0.05% Triton X"
- GSM6556462 / Sample_extract_protocol_ch1: matched `Chromium` in "Nuclei preparations were processed by the Chromium 3′ Gene Expression V3 Kit according to the manufacturer’s guidelines. Qubit 3 (Fisher Scientific) and 2100 Bioanalyzer (Agilent Technologies, Santa C"
- GSM6556463 / Sample_extract_protocol_ch1: matched `Chromium` in "Nuclei preparations were processed by the Chromium 3′ Gene Expression V3 Kit according to the manufacturer’s guidelines. Qubit 3 (Fisher Scientific) and 2100 Bioanalyzer (Agilent Technologies, Santa C"
- GSM6556464 / Sample_extract_protocol_ch1: matched `Chromium` in "Nuclei preparations were processed by the Chromium 3′ Gene Expression V3 Kit according to the manufacturer’s guidelines. Qubit 3 (Fisher Scientific) and 2100 Bioanalyzer (Agilent Technologies, Santa C"
- GSM6556465 / Sample_extract_protocol_ch1: matched `Chromium` in "Nuclei preparations were processed by the Chromium 3′ Gene Expression V3 Kit according to the manufacturer’s guidelines. Qubit 3 (Fisher Scientific) and 2100 Bioanalyzer (Agilent Technologies, Santa C"
- GSM6556466 / Sample_extract_protocol_ch1: matched `Chromium` in "Nuclei preparations were processed by the Chromium 3′ Gene Expression V3 Kit according to the manufacturer’s guidelines. Qubit 3 (Fisher Scientific) and 2100 Bioanalyzer (Agilent Technologies, Santa C"
- GSM6556467 / Sample_extract_protocol_ch1: matched `Chromium` in "Nuclei preparations were processed by the Chromium 3′ Gene Expression V2 Kit according to the manufacturer’s guidelines. Qubit 3 (Fisher Scientific) and 2100 Bioanalyzer (Agilent Technologies, Santa C"
- GSM6556468 / Sample_extract_protocol_ch1: matched `Chromium` in "Nuclei preparations were processed by the Chromium 3′ Gene Expression V2 Kit according to the manufacturer’s guidelines. Qubit 3 (Fisher Scientific) and 2100 Bioanalyzer (Agilent Technologies, Santa C"
- GSM6556449 / Sample_data_processing: matched `Cell Ranger` in "The demultiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v6.1.2 (https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/l"
- GSM6556449 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6556450 / Sample_data_processing: matched `Cell Ranger` in "The demultiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v6.1.2 (https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/l"
- GSM6556450 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6556451 / Sample_data_processing: matched `Cell Ranger` in "The demultiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v6.1.2 (https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/l"
- GSM6556451 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6556452 / Sample_data_processing: matched `Cell Ranger` in "The demultiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v6.1.2 (https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/l"
- GSM6556452 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6556453 / Sample_data_processing: matched `Cell Ranger` in "The demultiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v6.1.2 (https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/l"
- GSM6556453 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6556454 / Sample_data_processing: matched `Cell Ranger` in "The demultiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v6.1.2 (https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/l"
- GSM6556454 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6556455 / Sample_data_processing: matched `Cell Ranger` in "The demultiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v6.1.2 (https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/l"
- GSM6556455 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6556456 / Sample_data_processing: matched `Cell Ranger` in "The demultiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v6.1.2 (https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/l"
- GSM6556456 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6556457 / Sample_data_processing: matched `Cell Ranger` in "The demultiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v6.1.2 (https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/l"
- GSM6556457 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6556458 / Sample_data_processing: matched `Cell Ranger` in "The demultiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v6.1.2 (https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/l"
- GSM6556458 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6556459 / Sample_data_processing: matched `Cell Ranger` in "The demultiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v6.1.2 (https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/l"
- GSM6556459 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6556460 / Sample_data_processing: matched `Cell Ranger` in "The demultiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v6.1.2 (https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/l"
- GSM6556460 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6556461 / Sample_data_processing: matched `Cell Ranger` in "The demultiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v6.1.2 (https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/l"
- GSM6556461 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6556462 / Sample_data_processing: matched `Cell Ranger` in "The demultiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v6.1.2 (https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/l"
- GSM6556462 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6556463 / Sample_data_processing: matched `Cell Ranger` in "The demultiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v6.1.2 (https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/l"
- GSM6556463 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6556464 / Sample_data_processing: matched `Cell Ranger` in "The demultiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v6.1.2 (https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/l"
- GSM6556464 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6556465 / Sample_data_processing: matched `Cell Ranger` in "The demultiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v6.1.2 (https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/l"
- GSM6556465 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6556466 / Sample_data_processing: matched `Cell Ranger` in "The demultiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v6.1.2 (https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/l"
- GSM6556466 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6556467 / Sample_data_processing: matched `Cell Ranger` in "The demultiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v6.1.2 (https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/l"
- GSM6556467 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6556468 / Sample_data_processing: matched `Cell Ranger` in "The demultiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v6.1.2 (https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/l"
- GSM6556468 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6556449 / Sample_title: matched `snRNA` in "Human Control Liver 1, snRNA-seq"
- GSM6556450 / Sample_title: matched `snRNA` in "Human Control Liver 2, snRNA-seq"
- GSM6556451 / Sample_title: matched `snRNA` in "Human Control Liver 3, snRNA-seq"
- GSM6556452 / Sample_title: matched `snRNA` in "Human NASH Liver 1 R1C1, snRNA-seq"
- GSM6556453 / Sample_title: matched `snRNA` in "Human NASH Liver 1 R1C2, snRNA-seq"
- GSM6556454 / Sample_title: matched `snRNA` in "Human NASH Liver 2 R1C2, snRNA-seq"
- GSM6556455 / Sample_title: matched `snRNA` in "Human NASH Liver 2 R2C1, snRNA-seq"
- GSM6556456 / Sample_title: matched `snRNA` in "Human NASH Liver 3 R4C1, snRNA-seq"
- GSM6556457 / Sample_title: matched `snRNA` in "Human NASH Liver 3 R5C2, snRNA-seq"
- GSM6556458 / Sample_title: matched `snRNA` in "Human NASH Liver 3 R6C1, snRNA-seq"
- GSM6556459 / Sample_title: matched `snRNA` in "Human NASH Liver 4 R4C1, snRNA-seq"
- GSM6556460 / Sample_title: matched `snRNA` in "Human NASH Liver 4 R6C1, snRNA-seq"
- GSM6556461 / Sample_title: matched `snRNA` in "Human NASH Liver 5 R3C8, snRNA-seq"
- GSM6556462 / Sample_title: matched `snRNA` in "Human NASH Liver 5 R5C5, snRNA-seq"
- GSM6556463 / Sample_title: matched `snRNA` in "Human NASH Liver 6, snRNA-seq"
- GSM6556464 / Sample_title: matched `snRNA` in "Human NASH Liver 7, snRNA-seq"
- GSM6556465 / Sample_title: matched `snRNA` in "Human NASH Liver 8, snRNA-seq"
- GSM6556466 / Sample_title: matched `snRNA` in "Human NASH Liver 9, snRNA-seq"
- GSM6556467 / Sample_title: matched `snRNA` in "Mouse NASH 1, snRNA-seq"
- GSM6556468 / Sample_title: matched `snRNA` in "Mouse NASH 2, snRNA-seq"
- GSM6556449 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556449/suppl/GSM6556449_humanCTRL_1_barcodes.tsv.gz"
- GSM6556449 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556449/suppl/GSM6556449_humanCTRL_1_features.tsv.gz"
- GSM6556449 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556449/suppl/GSM6556449_humanCTRL_1_matrix.mtx.gz"
- GSM6556450 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556450/suppl/GSM6556450_humanCTRL_2_barcodes.tsv.gz"
- GSM6556450 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556450/suppl/GSM6556450_humanCTRL_2_features.tsv.gz"
- GSM6556450 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556450/suppl/GSM6556450_humanCTRL_2_matrix.mtx.gz"
- GSM6556451 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556451/suppl/GSM6556451_humanCTRL_3_barcodes.tsv.gz"
- GSM6556451 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556451/suppl/GSM6556451_humanCTRL_3_features.tsv.gz"
- GSM6556451 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556451/suppl/GSM6556451_humanCTRL_3_matrix.mtx.gz"
- GSM6556452 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556452/suppl/GSM6556452_humanNASH_1_40kNuclei_R1C1_DMSO_barcodes.tsv.gz"
- GSM6556452 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556452/suppl/GSM6556452_humanNASH_1_40kNuclei_R1C1_DMSO_features.tsv.gz"
- GSM6556452 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556452/suppl/GSM6556452_humanNASH_1_40kNuclei_R1C1_DMSO_matrix.mtx.gz"
- GSM6556453 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556453/suppl/GSM6556453_humanNASH_1_40kNuclei_R1C2_Flash_barcodes.tsv.gz"
- GSM6556453 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556453/suppl/GSM6556453_humanNASH_1_40kNuclei_R1C2_Flash_features.tsv.gz"
- GSM6556453 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556453/suppl/GSM6556453_humanNASH_1_40kNuclei_R1C2_Flash_matrix.mtx.gz"
- GSM6556454 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556454/suppl/GSM6556454_humanNASH_2_R1C1_30kNuclei_barcodes.tsv.gz"
- GSM6556454 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556454/suppl/GSM6556454_humanNASH_2_R1C1_30kNuclei_features.tsv.gz"
- GSM6556454 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556454/suppl/GSM6556454_humanNASH_2_R1C1_30kNuclei_matrix.mtx.gz"
- GSM6556455 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556455/suppl/GSM6556455_humanNASH_2_R2C1_30kNuclei_barcodes.tsv.gz"
- GSM6556455 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556455/suppl/GSM6556455_humanNASH_2_R2C1_30kNuclei_features.tsv.gz"
- GSM6556455 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556455/suppl/GSM6556455_humanNASH_2_R2C1_30kNuclei_matrix.mtx.gz"
- GSM6556456 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556456/suppl/GSM6556456_humanNASH_3_R4C1_30kNuclei_barcodes.tsv.gz"
- GSM6556456 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556456/suppl/GSM6556456_humanNASH_3_R4C1_30kNuclei_features.tsv.gz"
- GSM6556456 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556456/suppl/GSM6556456_humanNASH_3_R4C1_30kNuclei_matrix.mtx.gz"
- GSM6556457 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556457/suppl/GSM6556457_humanNASH_3_R5C2_20kNoFacsNuclei_barcodes.tsv.gz"
- GSM6556457 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556457/suppl/GSM6556457_humanNASH_3_R5C2_20kNoFacsNuclei_features.tsv.gz"
- GSM6556457 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556457/suppl/GSM6556457_humanNASH_3_R5C2_20kNoFacsNuclei_matrix.mtx.gz"
- GSM6556458 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556458/suppl/GSM6556458_humanNASH_3_R6C1_20kNoFacsNuclei_barcodes.tsv.gz"
- GSM6556458 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556458/suppl/GSM6556458_humanNASH_3_R6C1_20kNoFacsNuclei_features.tsv.gz"
- GSM6556458 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556458/suppl/GSM6556458_humanNASH_3_R6C1_20kNoFacsNuclei_matrix.mtx.gz"
- GSM6556459 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556459/suppl/GSM6556459_humanNASH_4_R4C1_20kNoFacsNuclei_barcodes.tsv.gz"
- GSM6556459 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556459/suppl/GSM6556459_humanNASH_4_R4C1_20kNoFacsNuclei_features.tsv.gz"
- GSM6556459 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556459/suppl/GSM6556459_humanNASH_4_R4C1_20kNoFacsNuclei_matrix.mtx.gz"
- GSM6556460 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556460/suppl/GSM6556460_humanNASH_4_R6C1_20kNoFacsNuclei_barcodes.tsv.gz"
- GSM6556460 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556460/suppl/GSM6556460_humanNASH_4_R6C1_20kNoFacsNuclei_features.tsv.gz"
- GSM6556460 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556460/suppl/GSM6556460_humanNASH_4_R6C1_20kNoFacsNuclei_matrix.mtx.gz"
- GSM6556461 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556461/suppl/GSM6556461_humanNASH_5_R3C8_20kNoFacsNuclei_barcodes.tsv.gz"
- GSM6556461 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556461/suppl/GSM6556461_humanNASH_5_R3C8_20kNoFacsNuclei_features.tsv.gz"
- GSM6556461 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556461/suppl/GSM6556461_humanNASH_5_R3C8_20kNoFacsNuclei_matrix.mtx.gz"
- GSM6556462 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556462/suppl/GSM6556462_humanNASH_5_R5C5_20kNoFacsNuclei_barcodes.tsv.gz"
- GSM6556462 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556462/suppl/GSM6556462_humanNASH_5_R5C5_20kNoFacsNuclei_features.tsv.gz"
- GSM6556462 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556462/suppl/GSM6556462_humanNASH_5_R5C5_20kNoFacsNuclei_matrix.mtx.gz"
- GSM6556463 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556463/suppl/GSM6556463_humanNASH_6_barcodes.tsv.gz"
- GSM6556463 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556463/suppl/GSM6556463_humanNASH_6_features.tsv.gz"
- GSM6556463 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556463/suppl/GSM6556463_humanNASH_6_matrix.mtx.gz"
- GSM6556464 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556464/suppl/GSM6556464_humanNASH_7_barcodes.tsv.gz"
- GSM6556464 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556464/suppl/GSM6556464_humanNASH_7_features.tsv.gz"
- GSM6556464 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556464/suppl/GSM6556464_humanNASH_7_matrix.mtx.gz"
- GSM6556465 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556465/suppl/GSM6556465_humanNASH_8_barcodes.tsv.gz"
- GSM6556465 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556465/suppl/GSM6556465_humanNASH_8_features.tsv.gz"
- GSM6556465 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556465/suppl/GSM6556465_humanNASH_8_matrix.mtx.gz"
- GSM6556466 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556466/suppl/GSM6556466_humanNASH_9_barcodes.tsv.gz"
- GSM6556466 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556466/suppl/GSM6556466_humanNASH_9_features.tsv.gz"
- GSM6556466 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556466/suppl/GSM6556466_humanNASH_9_matrix.mtx.gz"
- GSM6556467 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556467/suppl/GSM6556467_mouseNASH_1_barcodes.tsv.gz"
- GSM6556467 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556467/suppl/GSM6556467_mouseNASH_1_features.tsv.gz"
- GSM6556467 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556467/suppl/GSM6556467_mouseNASH_1_matrix.mtx.gz"
- GSM6556468 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556468/suppl/GSM6556468_mouseNASH_2_barcodes.tsv.gz"
- GSM6556468 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556468/suppl/GSM6556468_mouseNASH_2_features.tsv.gz"
- GSM6556468 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6556nnn/GSM6556468/suppl/GSM6556468_mouseNASH_2_matrix.mtx.gz"
- GSE212837 / Series_supplementary_file: matched `.h5ad` in "ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE212nnn/GSE212837/suppl/GSE212837_all_data_labeled_processed.h5ad.gz"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: .h5ad, 10x, Cell Ranger, Chromium, barcodes.tsv, features.tsv, matrix.mtx, snRNA (21 sample(s)))
<!-- /computed -->