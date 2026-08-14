# Validation report: GSE136103

Resolving the fibrotic niche of human liver cirrhosis using single-cell transcriptomics

<!-- computed -->
Sample count: 26

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 26 samples |
| organism_consistency | WARN | mixed organisms: Homo sapiens 24/26, Mus musculus 2/26 |
| source_tissue | WARN | liver-pattern source 26/26; off-target tissue signal detected |
| library_strategy | PASS | RNA-Seq 26/26 |
| library_source | PASS | transcriptomic 26/26 |
| library_selection | PASS | cDNA 26/26 |
| instrument_model | PASS | Illumina HiSeq 4000 26/26 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (7 sample(s)) |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: 10X, Cell Ranger, barcodes.tsv, genes.tsv, matrix.mtx (26 sample(s)) |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (26/26), packaged in GSE136103_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE136103-GPL20301_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX6747672, https://www.ncbi.nlm.nih.gov/sra?term=SRX6747673, https://www.ncbi.nlm.nih.gov/sra?term=SRX6747674, https://www.ncbi.nlm.nih.gov/sra?term=SRX6747675, https://www.ncbi.nlm.nih.gov/sra?term=SRX6747676, and 21 more (see sample_metadata.csv) |

## Canonical field distributions

- **sex**: Female (7), Male (19)

## Field presence

- Sex: 26/26 (canon: sex)
- cause of liver disease: 26/26
- cell subtype: 20/26
- disease status: 26/26
- population: 26/26

## Evidence for WARN/FAIL checks

### organism_consistency (WARN)
### source_tissue (WARN)
- GSM4041170 / Sample_source_name_ch1: matched `PBMC` in "PBMC"
- GSM4041171 / Sample_source_name_ch1: matched `PBMC` in "PBMC"
- GSM4041172 / Sample_source_name_ch1: matched `PBMC` in "PBMC"
- GSM4041173 / Sample_source_name_ch1: matched `PBMC` in "PBMC"
- GSM4041170 / Sample_characteristics_ch1: matched `PBMC` in "population: PBMC"
- GSM4041171 / Sample_characteristics_ch1: matched `PBMC` in "population: PBMC"
- GSM4041172 / Sample_characteristics_ch1: matched `PBMC` in "population: PBMC"
- GSM4041173 / Sample_characteristics_ch1: matched `PBMC` in "population: PBMC"
### metadata_completeness (WARN)
### single_cell_or_spatial (FAIL)
- GSM4041150 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041151 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041152 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041153 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041154 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041155 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041156 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041157 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041158 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041159 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041160 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041161 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041162 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041163 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041164 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041165 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041166 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041167 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041168 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041169 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041170 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041171 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041172 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041173 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041174 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041175 / Sample_extract_protocol_ch1: matched `10X` in "10X Genomics Single cell 3' gene expression V2"
- GSM4041150 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041151 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041152 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041153 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041154 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041155 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041156 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041157 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041158 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041159 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041160 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041161 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041162 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041163 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041164 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041165 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041166 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041167 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041168 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041169 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041170 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041171 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041172 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041173 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041174 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041175 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 2.1.0."
- GSM4041150 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041150/suppl/GSM4041150_healthy1_cd45+_barcodes.tsv.gz"
- GSM4041150 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041150/suppl/GSM4041150_healthy1_cd45+_genes.tsv.gz"
- GSM4041150 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041150/suppl/GSM4041150_healthy1_cd45+_matrix.mtx.gz"
- GSM4041151 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041151/suppl/GSM4041151_healthy1_cd45-A_barcodes.tsv.gz"
- GSM4041151 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041151/suppl/GSM4041151_healthy1_cd45-A_genes.tsv.gz"
- GSM4041151 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041151/suppl/GSM4041151_healthy1_cd45-A_matrix.mtx.gz"
- GSM4041152 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041152/suppl/GSM4041152_healthy1_cd45-B_barcodes.tsv.gz"
- GSM4041152 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041152/suppl/GSM4041152_healthy1_cd45-B_genes.tsv.gz"
- GSM4041152 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041152/suppl/GSM4041152_healthy1_cd45-B_matrix.mtx.gz"
- GSM4041153 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041153/suppl/GSM4041153_healthy2_cd45+_barcodes.tsv.gz"
- GSM4041153 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041153/suppl/GSM4041153_healthy2_cd45+_genes.tsv.gz"
- GSM4041153 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041153/suppl/GSM4041153_healthy2_cd45+_matrix.mtx.gz"
- GSM4041154 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041154/suppl/GSM4041154_healthy2_cd45-_barcodes.tsv.gz"
- GSM4041154 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041154/suppl/GSM4041154_healthy2_cd45-_genes.tsv.gz"
- GSM4041154 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041154/suppl/GSM4041154_healthy2_cd45-_matrix.mtx.gz"
- GSM4041155 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041155/suppl/GSM4041155_healthy3_cd45+_barcodes.tsv.gz"
- GSM4041155 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041155/suppl/GSM4041155_healthy3_cd45+_genes.tsv.gz"
- GSM4041155 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041155/suppl/GSM4041155_healthy3_cd45+_matrix.mtx.gz"
- GSM4041156 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041156/suppl/GSM4041156_healthy3_cd45-A_barcodes.tsv.gz"
- GSM4041156 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041156/suppl/GSM4041156_healthy3_cd45-A_genes.tsv.gz"
- GSM4041156 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041156/suppl/GSM4041156_healthy3_cd45-A_matrix.mtx.gz"
- GSM4041157 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041157/suppl/GSM4041157_healthy3_cd45-B_barcodes.tsv.gz"
- GSM4041157 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041157/suppl/GSM4041157_healthy3_cd45-B_genes.tsv.gz"
- GSM4041157 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041157/suppl/GSM4041157_healthy3_cd45-B_matrix.mtx.gz"
- GSM4041158 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041158/suppl/GSM4041158_healthy4_cd45+_barcodes.tsv.gz"
- GSM4041158 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041158/suppl/GSM4041158_healthy4_cd45+_genes.tsv.gz"
- GSM4041158 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041158/suppl/GSM4041158_healthy4_cd45+_matrix.mtx.gz"
- GSM4041159 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041159/suppl/GSM4041159_healthy4_cd45-_barcodes.tsv.gz"
- GSM4041159 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041159/suppl/GSM4041159_healthy4_cd45-_genes.tsv.gz"
- GSM4041159 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041159/suppl/GSM4041159_healthy4_cd45-_matrix.mtx.gz"
- GSM4041160 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041160/suppl/GSM4041160_healthy5_cd45+_barcodes.tsv.gz"
- GSM4041160 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041160/suppl/GSM4041160_healthy5_cd45+_genes.tsv.gz"
- GSM4041160 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041160/suppl/GSM4041160_healthy5_cd45+_matrix.mtx.gz"
- GSM4041161 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041161/suppl/GSM4041161_cirrhotic1_cd45+_barcodes.tsv.gz"
- GSM4041161 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041161/suppl/GSM4041161_cirrhotic1_cd45+_genes.tsv.gz"
- GSM4041161 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041161/suppl/GSM4041161_cirrhotic1_cd45+_matrix.mtx.gz"
- GSM4041162 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041162/suppl/GSM4041162_cirrhotic1_cd45-A_barcodes.tsv.gz"
- GSM4041162 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041162/suppl/GSM4041162_cirrhotic1_cd45-A_genes.tsv.gz"
- GSM4041162 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041162/suppl/GSM4041162_cirrhotic1_cd45-A_matrix.mtx.gz"
- GSM4041163 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041163/suppl/GSM4041163_cirrhotic1_cd45-B_barcodes.tsv.gz"
- GSM4041163 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041163/suppl/GSM4041163_cirrhotic1_cd45-B_genes.tsv.gz"
- GSM4041163 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041163/suppl/GSM4041163_cirrhotic1_cd45-B_matrix.mtx.gz"
- GSM4041164 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041164/suppl/GSM4041164_cirrhotic2_cd45+_barcodes.tsv.gz"
- GSM4041164 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041164/suppl/GSM4041164_cirrhotic2_cd45+_genes.tsv.gz"
- GSM4041164 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041164/suppl/GSM4041164_cirrhotic2_cd45+_matrix.mtx.gz"
- GSM4041165 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041165/suppl/GSM4041165_cirrhotic2_cd45-_barcodes.tsv.gz"
- GSM4041165 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041165/suppl/GSM4041165_cirrhotic2_cd45-_genes.tsv.gz"
- GSM4041165 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041165/suppl/GSM4041165_cirrhotic2_cd45-_matrix.mtx.gz"
- GSM4041166 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041166/suppl/GSM4041166_cirrhotic3_cd45+_barcodes.tsv.gz"
- GSM4041166 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041166/suppl/GSM4041166_cirrhotic3_cd45+_genes.tsv.gz"
- GSM4041166 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041166/suppl/GSM4041166_cirrhotic3_cd45+_matrix.mtx.gz"
- GSM4041167 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041167/suppl/GSM4041167_cirrhotic3_cd45-_barcodes.tsv.gz"
- GSM4041167 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041167/suppl/GSM4041167_cirrhotic3_cd45-_genes.tsv.gz"
- GSM4041167 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041167/suppl/GSM4041167_cirrhotic3_cd45-_matrix.mtx.gz"
- GSM4041168 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041168/suppl/GSM4041168_cirrhotic4_cd45+_barcodes.tsv.gz"
- GSM4041168 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041168/suppl/GSM4041168_cirrhotic4_cd45+_genes.tsv.gz"
- GSM4041168 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041168/suppl/GSM4041168_cirrhotic4_cd45+_matrix.mtx.gz"
- GSM4041169 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041169/suppl/GSM4041169_cirrhotic5_cd45+_barcodes.tsv.gz"
- GSM4041169 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041169/suppl/GSM4041169_cirrhotic5_cd45+_genes.tsv.gz"
- GSM4041169 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041169/suppl/GSM4041169_cirrhotic5_cd45+_matrix.mtx.gz"
- GSM4041170 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041170/suppl/GSM4041170_blood1_barcodes.tsv.gz"
- GSM4041170 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041170/suppl/GSM4041170_blood1_genes.tsv.gz"
- GSM4041170 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041170/suppl/GSM4041170_blood1_matrix.mtx.gz"
- GSM4041171 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041171/suppl/GSM4041171_blood2_barcodes.tsv.gz"
- GSM4041171 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041171/suppl/GSM4041171_blood2_genes.tsv.gz"
- GSM4041171 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041171/suppl/GSM4041171_blood2_matrix.mtx.gz"
- GSM4041172 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041172/suppl/GSM4041172_blood3_barcodes.tsv.gz"
- GSM4041172 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041172/suppl/GSM4041172_blood3_genes.tsv.gz"
- GSM4041172 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041172/suppl/GSM4041172_blood3_matrix.mtx.gz"
- GSM4041173 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041173/suppl/GSM4041173_blood4_barcodes.tsv.gz"
- GSM4041173 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041173/suppl/GSM4041173_blood4_genes.tsv.gz"
- GSM4041173 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041173/suppl/GSM4041173_blood4_matrix.mtx.gz"
- GSM4041174 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041174/suppl/GSM4041174_mouse_healthy_barcodes.tsv.gz"
- GSM4041174 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041174/suppl/GSM4041174_mouse_healthy_genes.tsv.gz"
- GSM4041174 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041174/suppl/GSM4041174_mouse_healthy_matrix.mtx.gz"
- GSM4041175 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041175/suppl/GSM4041175_mouse_fibrotic_barcodes.tsv.gz"
- GSM4041175 / Sample_supplementary_file_2: matched `genes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041175/suppl/GSM4041175_mouse_fibrotic_genes.tsv.gz"
- GSM4041175 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4041nnn/GSM4041175/suppl/GSM4041175_mouse_fibrotic_matrix.mtx.gz"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: 10X, Cell Ranger, barcodes.tsv, genes.tsv, matrix.mtx (26 sample(s)))
<!-- /computed -->