# Validation report: GSE190487

Gastrointestinal B-cells license metabolic T-cell activation in NASH microbiota anigen-independently and contribute to fibrosis by IgA-FcRy signalling

<!-- computed -->
Sample count: 1

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 1 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 1/1 |
| source_tissue | PASS | liver-pattern source 1/1 |
| library_strategy | PASS | RNA-Seq 1/1 |
| library_source | PASS | transcriptomic 1/1 |
| library_selection | PASS | cDNA 1/1 |
| instrument_model | PASS | Illumina HiSeq 4000 1/1 |
| metadata_completeness | PASS | reported consistently: disease, tissue; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (1 sample(s)) |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: 10x, Cell Ranger, barcodes.tsv, features.tsv, matrix.mtx, scRNA (1 sample(s)) |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (1/1), packaged in GSE190487_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE190487_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX13355134 |

## Canonical field distributions

- **disease**: NAFLD (1)
- **tissue**: NAFLD liver explant (1)

## Field presence

- condition: 1/1 (canon: disease)
- source: 1/1 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### single_cell_or_spatial (FAIL)
- GSM5724573 / Sample_extract_protocol_ch1: matched `10x` in "10x Genomics single cell 3' gene expression v3"
- GSM5724573 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, alignment to the GRCh38 reference, and estimation of cell-containing partitions and associated UMIs using Cell Ranger 3.1.0"
- GSM5724573 / Sample_title: matched `scRNA` in "NAFLD liver sample 1 scRNA-seq"
- GSM5724573 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5724nnn/GSM5724573/suppl/GSM5724573_nafld1_barcodes.tsv.gz"
- GSM5724573 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5724nnn/GSM5724573/suppl/GSM5724573_nafld1_features.tsv.gz"
- GSM5724573 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5724nnn/GSM5724573/suppl/GSM5724573_nafld1_matrix.mtx.gz"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: 10x, Cell Ranger, barcodes.tsv, features.tsv, matrix.mtx, scRNA (1 sample(s)))
<!-- /computed -->