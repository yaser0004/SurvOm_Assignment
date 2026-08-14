# Validation report: GSE273561

Aldehydes alter TGF-β signaling and induce obesity and cancer

<!-- computed -->
Sample count: 27

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 27 samples |
| organism_consistency | WARN | mixed organisms: Homo sapiens 9/27, Mus musculus 18/27 |
| source_tissue | PASS | liver-pattern source 27/27 |
| library_strategy | PASS | RNA-Seq 27/27 |
| library_source | WARN | library_source: transcriptomic 23/27, transcriptomic single cell 4/27 |
| library_selection | PASS | cDNA 27/27 |
| instrument_model | PASS | Illumina NovaSeq 6000 27/27 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: filtered_feature_bc_matrix, snRNA (13 sample(s)) |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (4/27), packaged in GSE273561_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE273561-GPL24247_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX25524103, https://www.ncbi.nlm.nih.gov/sra?term=SRX25524104, https://www.ncbi.nlm.nih.gov/sra?term=SRX25524105, https://www.ncbi.nlm.nih.gov/sra?term=SRX25524106, https://www.ncbi.nlm.nih.gov/sra?term=SRX25524107, and 22 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 12 months (4)
- **tissue**: liver (27)
- **treatment**: 25nM siSptbn1 (3), 50nM siSptbn1 (3), siControl (3)

## Field presence

- age: 4/27 (canon: age)
- cell type: 27/27
- genotype: 4/27
- strain: 4/27
- time: 9/27
- tissue: 27/27 (canon: tissue)
- treatment: 9/27 (canon: treatment)

## Evidence for WARN/FAIL checks

### organism_consistency (WARN)
### library_source (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE273561 / Series_summary: matched `fatty liver` in "Obesity and fatty liver diseases-metabolic dysfunction-associated steatotic liver disease (MASLD and MASH) affect over a third of the global population and are exacerbated in individuals with reduced "
- GSE273561 / Series_overall_design: matched `MASH` in "Using unbiased transcriptome methods snRNA-seq and RNA-seq to characterize liver metabolism alterations in mice (WT, Sptbn1+/-, Aldh2-/-, Aldh2-/-Sptbn1+/-) under normal chow diet. Using bulk RNA-seq "
### single_cell_or_spatial (FAIL)
- GSM8432342 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were isolated by lysing frozen mouse livers with a pestle and cold lysing buffer (10mM Tris-Cl, PH 7.4, 10mM NaCl, 3mM MgCl2, 0.1% NP-40, 0.4 U/ul RNase Inhibitor, 1mM DTT) for 4 min"
- GSM8432342 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were labeled with 7-AAD (Sigma) and sorted on a BD FACS Aria to purify nuclei from the remaining debris. Sorted nuclei were counted and loaded onto a Chip G and 10X Genomics Chromium"
- GSM8432343 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were isolated by lysing frozen mouse livers with a pestle and cold lysing buffer (10mM Tris-Cl, PH 7.4, 10mM NaCl, 3mM MgCl2, 0.1% NP-40, 0.4 U/ul RNase Inhibitor, 1mM DTT) for 4 min"
- GSM8432343 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were labeled with 7-AAD (Sigma) and sorted on a BD FACS Aria to purify nuclei from the remaining debris. Sorted nuclei were counted and loaded onto a Chip G and 10X Genomics Chromium"
- GSM8432344 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were isolated by lysing frozen mouse livers with a pestle and cold lysing buffer (10mM Tris-Cl, PH 7.4, 10mM NaCl, 3mM MgCl2, 0.1% NP-40, 0.4 U/ul RNase Inhibitor, 1mM DTT) for 4 min"
- GSM8432344 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were labeled with 7-AAD (Sigma) and sorted on a BD FACS Aria to purify nuclei from the remaining debris. Sorted nuclei were counted and loaded onto a Chip G and 10X Genomics Chromium"
- GSM8432345 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were isolated by lysing frozen mouse livers with a pestle and cold lysing buffer (10mM Tris-Cl, PH 7.4, 10mM NaCl, 3mM MgCl2, 0.1% NP-40, 0.4 U/ul RNase Inhibitor, 1mM DTT) for 4 min"
- GSM8432345 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were labeled with 7-AAD (Sigma) and sorted on a BD FACS Aria to purify nuclei from the remaining debris. Sorted nuclei were counted and loaded onto a Chip G and 10X Genomics Chromium"
- GSM8432346 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were isolated by lysing frozen mouse livers with a pestle and cold lysing buffer (10mM Tris-Cl, PH 7.4, 10mM NaCl, 3mM MgCl2, 0.1% NP-40, 0.4 U/ul RNase Inhibitor, 1mM DTT) for 4 min"
- GSM8432346 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were labeled with 7-AAD (Sigma) and sorted on a BD FACS Aria to purify nuclei from the remaining debris. Sorted nuclei were counted and loaded onto a Chip G and 10X Genomics Chromium"
- GSM8432347 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were isolated by lysing frozen mouse livers with a pestle and cold lysing buffer (10mM Tris-Cl, PH 7.4, 10mM NaCl, 3mM MgCl2, 0.1% NP-40, 0.4 U/ul RNase Inhibitor, 1mM DTT) for 4 min"
- GSM8432347 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were labeled with 7-AAD (Sigma) and sorted on a BD FACS Aria to purify nuclei from the remaining debris. Sorted nuclei were counted and loaded onto a Chip G and 10X Genomics Chromium"
- GSM8432348 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were isolated by lysing frozen mouse livers with a pestle and cold lysing buffer (10mM Tris-Cl, PH 7.4, 10mM NaCl, 3mM MgCl2, 0.1% NP-40, 0.4 U/ul RNase Inhibitor, 1mM DTT) for 4 min"
- GSM8432348 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were labeled with 7-AAD (Sigma) and sorted on a BD FACS Aria to purify nuclei from the remaining debris. Sorted nuclei were counted and loaded onto a Chip G and 10X Genomics Chromium"
- GSM8432349 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were isolated by lysing frozen mouse livers with a pestle and cold lysing buffer (10mM Tris-Cl, PH 7.4, 10mM NaCl, 3mM MgCl2, 0.1% NP-40, 0.4 U/ul RNase Inhibitor, 1mM DTT) for 4 min"
- GSM8432349 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were labeled with 7-AAD (Sigma) and sorted on a BD FACS Aria to purify nuclei from the remaining debris. Sorted nuclei were counted and loaded onto a Chip G and 10X Genomics Chromium"
- GSM8432350 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were isolated by lysing frozen mouse livers with a pestle and cold lysing buffer (10mM Tris-Cl, PH 7.4, 10mM NaCl, 3mM MgCl2, 0.1% NP-40, 0.4 U/ul RNase Inhibitor, 1mM DTT) for 4 min"
- GSM8432350 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were labeled with 7-AAD (Sigma) and sorted on a BD FACS Aria to purify nuclei from the remaining debris. Sorted nuclei were counted and loaded onto a Chip G and 10X Genomics Chromium"
- GSM8432351 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were isolated by lysing frozen mouse livers with a pestle and cold lysing buffer (10mM Tris-Cl, PH 7.4, 10mM NaCl, 3mM MgCl2, 0.1% NP-40, 0.4 U/ul RNase Inhibitor, 1mM DTT) for 4 min"
- GSM8432351 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were labeled with 7-AAD (Sigma) and sorted on a BD FACS Aria to purify nuclei from the remaining debris. Sorted nuclei were counted and loaded onto a Chip G and 10X Genomics Chromium"
- GSM8432352 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were isolated by lysing frozen mouse livers with a pestle and cold lysing buffer (10mM Tris-Cl, PH 7.4, 10mM NaCl, 3mM MgCl2, 0.1% NP-40, 0.4 U/ul RNase Inhibitor, 1mM DTT) for 4 min"
- GSM8432352 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were labeled with 7-AAD (Sigma) and sorted on a BD FACS Aria to purify nuclei from the remaining debris. Sorted nuclei were counted and loaded onto a Chip G and 10X Genomics Chromium"
- GSM8432353 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were isolated by lysing frozen mouse livers with a pestle and cold lysing buffer (10mM Tris-Cl, PH 7.4, 10mM NaCl, 3mM MgCl2, 0.1% NP-40, 0.4 U/ul RNase Inhibitor, 1mM DTT) for 4 min"
- GSM8432353 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were labeled with 7-AAD (Sigma) and sorted on a BD FACS Aria to purify nuclei from the remaining debris. Sorted nuclei were counted and loaded onto a Chip G and 10X Genomics Chromium"
- GSM8432354 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were isolated by lysing frozen mouse livers with a pestle and cold lysing buffer (10mM Tris-Cl, PH 7.4, 10mM NaCl, 3mM MgCl2, 0.1% NP-40, 0.4 U/ul RNase Inhibitor, 1mM DTT) for 4 min"
- GSM8432354 / Sample_extract_protocol_ch1: matched `snRNA` in "snRNA-seq: Nuclei were labeled with 7-AAD (Sigma) and sorted on a BD FACS Aria to purify nuclei from the remaining debris. Sorted nuclei were counted and loaded onto a Chip G and 10X Genomics Chromium"
- GSM8432342 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The demutiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v7.0.0."
- GSM8432342 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The preprocessing, QC, normalizing, clustering, and visulization were made using the Seurat v4."
- GSM8432342 / Sample_data_processing: matched `snRNA` in "Supplementary files format and content: snRNA-seq: H5, with molecule, feature and matrix files for each sample"
- GSM8432343 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The demutiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v7.0.0."
- GSM8432343 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The preprocessing, QC, normalizing, clustering, and visulization were made using the Seurat v4."
- GSM8432343 / Sample_data_processing: matched `snRNA` in "Supplementary files format and content: snRNA-seq: H5, with molecule, feature and matrix files for each sample"
- GSM8432344 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The demutiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v7.0.0."
- GSM8432344 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The preprocessing, QC, normalizing, clustering, and visulization were made using the Seurat v4."
- GSM8432344 / Sample_data_processing: matched `snRNA` in "Supplementary files format and content: snRNA-seq: H5, with molecule, feature and matrix files for each sample"
- GSM8432345 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The demutiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v7.0.0."
- GSM8432345 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The preprocessing, QC, normalizing, clustering, and visulization were made using the Seurat v4."
- GSM8432345 / Sample_data_processing: matched `snRNA` in "Supplementary files format and content: snRNA-seq: H5, with molecule, feature and matrix files for each sample"
- GSM8432346 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The demutiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v7.0.0."
- GSM8432346 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The preprocessing, QC, normalizing, clustering, and visulization were made using the Seurat v4."
- GSM8432346 / Sample_data_processing: matched `snRNA` in "Supplementary files format and content: snRNA-seq: H5, with molecule, feature and matrix files for each sample"
- GSM8432347 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The demutiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v7.0.0."
- GSM8432347 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The preprocessing, QC, normalizing, clustering, and visulization were made using the Seurat v4."
- GSM8432347 / Sample_data_processing: matched `snRNA` in "Supplementary files format and content: snRNA-seq: H5, with molecule, feature and matrix files for each sample"
- GSM8432348 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The demutiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v7.0.0."
- GSM8432348 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The preprocessing, QC, normalizing, clustering, and visulization were made using the Seurat v4."
- GSM8432348 / Sample_data_processing: matched `snRNA` in "Supplementary files format and content: snRNA-seq: H5, with molecule, feature and matrix files for each sample"
- GSM8432349 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The demutiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v7.0.0."
- GSM8432349 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The preprocessing, QC, normalizing, clustering, and visulization were made using the Seurat v4."
- GSM8432349 / Sample_data_processing: matched `snRNA` in "Supplementary files format and content: snRNA-seq: H5, with molecule, feature and matrix files for each sample"
- GSM8432350 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The demutiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v7.0.0."
- GSM8432350 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The preprocessing, QC, normalizing, clustering, and visulization were made using the Seurat v4."
- GSM8432350 / Sample_data_processing: matched `snRNA` in "Supplementary files format and content: snRNA-seq: H5, with molecule, feature and matrix files for each sample"
- GSM8432351 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The demutiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v7.0.0."
- GSM8432351 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The preprocessing, QC, normalizing, clustering, and visulization were made using the Seurat v4."
- GSM8432351 / Sample_data_processing: matched `snRNA` in "Supplementary files format and content: snRNA-seq: H5, with molecule, feature and matrix files for each sample"
- GSM8432352 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The demutiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v7.0.0."
- GSM8432352 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The preprocessing, QC, normalizing, clustering, and visulization were made using the Seurat v4."
- GSM8432352 / Sample_data_processing: matched `snRNA` in "Supplementary files format and content: snRNA-seq: H5, with molecule, feature and matrix files for each sample"
- GSM8432353 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The demutiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v7.0.0."
- GSM8432353 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The preprocessing, QC, normalizing, clustering, and visulization were made using the Seurat v4."
- GSM8432353 / Sample_data_processing: matched `snRNA` in "Supplementary files format and content: snRNA-seq: H5, with molecule, feature and matrix files for each sample"
- GSM8432354 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The demutiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v7.0.0."
- GSM8432354 / Sample_data_processing: matched `snRNA` in "snRNA-seq: The preprocessing, QC, normalizing, clustering, and visulization were made using the Seurat v4."
- GSM8432354 / Sample_data_processing: matched `snRNA` in "Supplementary files format and content: snRNA-seq: H5, with molecule, feature and matrix files for each sample"
- GSM8432342 / Sample_title: matched `snRNA` in "Aldh2-/-, snRNAseq"
- GSM8432343 / Sample_title: matched `snRNA` in "Aldh2-/-Sptbn1+/-, snRNAseq"
- GSM8432344 / Sample_title: matched `snRNA` in "WT, snRNAseq"
- GSM8432345 / Sample_title: matched `snRNA` in "Sptbn1+/-, snRNAseq"
- GSM8432342 / Sample_supplementary_file_1: matched `filtered_feature_bc_matrix` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM8432nnn/GSM8432342/suppl/GSM8432342_A624_filtered_feature_bc_matrix.h5"
- GSM8432343 / Sample_supplementary_file_1: matched `filtered_feature_bc_matrix` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM8432nnn/GSM8432343/suppl/GSM8432343_A625_filtered_feature_bc_matrix.h5"
- GSM8432344 / Sample_supplementary_file_1: matched `filtered_feature_bc_matrix` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM8432nnn/GSM8432344/suppl/GSM8432344_A757_filtered_feature_bc_matrix.h5"
- GSM8432345 / Sample_supplementary_file_1: matched `filtered_feature_bc_matrix` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM8432nnn/GSM8432345/suppl/GSM8432345_A894_filtered_feature_bc_matrix.h5"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: filtered_feature_bc_matrix, snRNA (13 sample(s)))
<!-- /computed -->