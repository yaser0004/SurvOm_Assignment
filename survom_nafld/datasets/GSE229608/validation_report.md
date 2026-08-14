# Validation report: GSE229608

Multicellular liver organoid model for recapitulating hepatitis C virus infection and non-alcoholic fatty liver disease progression [scRNA-Seq]

<!-- computed -->
Sample count: 3

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 3 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 3/3 |
| source_tissue | WARN | liver-pattern source 2/3 |
| library_strategy | PASS | RNA-Seq 3/3 |
| library_source | WARN | library_source: transcriptomic single cell 3/3 |
| library_selection | PASS | cDNA 3/3 |
| instrument_model | PASS | HiSeq X Ten 3/3 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: 10x, Cell Ranger, barcodes.tsv, features.tsv, matrix.mtx, scRNA (3 sample(s)) |
| material_type | WARN | cell/culture terms in sample metadata: organoid (2/3 samples) |
| expression_data_availability | PASS | processed per-sample counts (3/3), packaged in GSE229608_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE229608_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX19951146, https://www.ncbi.nlm.nih.gov/sra?term=SRX19951147, https://www.ncbi.nlm.nih.gov/sra?term=SRX19951148 |

## Field presence

- cell type: 3/3

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
### library_source (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE229608 / Series_title: matched `non-alcoholic fatty liver` in "Multicellular liver organoid model for recapitulating hepatitis C virus infection and non-alcoholic fatty liver disease progression [scRNA-Seq]"
- GSE229608 / Series_summary: matched `non-alcoholic fatty liver` in "Hepatitis C virus (HCV) infection has been successfully managed by anti-viral therapies, however, high prevalence to severe chronic liver disease state including non-alcoholic fatty liver disease (NAF"
### single_cell_or_spatial (FAIL)
- GSM7166275 / Sample_extract_protocol_ch1: matched `scRNA` in "The matrigel was gently removed by pipetting and spinning down liver organoids, and the organoids were then washed with co-culture media. Organoids were chopped into pieces and collected. Organoid fra"
- GSM7166275 / Sample_extract_protocol_ch1: matched `10x` in "Library was performed according to the manufacter’s instructions (single cell 3’ v3 protocol, 10x Genomics). Briefly, single cells were resuspended in the master mix and loaded together with partition"
- GSM7166276 / Sample_extract_protocol_ch1: matched `scRNA` in "The matrigel was gently removed by pipetting and spinning down liver organoids, and the organoids were then washed with co-culture media. Organoids were chopped into pieces and collected. Organoid fra"
- GSM7166276 / Sample_extract_protocol_ch1: matched `10x` in "Library was performed according to the manufacter’s instructions (single cell 3’ v3 protocol, 10x Genomics). Briefly, single cells were resuspended in the master mix and loaded together with partition"
- GSM7166277 / Sample_extract_protocol_ch1: matched `scRNA` in "The matrigel was gently removed by pipetting and spinning down liver organoids, and the organoids were then washed with co-culture media. Organoids were chopped into pieces and collected. Organoid fra"
- GSM7166277 / Sample_extract_protocol_ch1: matched `10x` in "Library was performed according to the manufacter’s instructions (single cell 3’ v3 protocol, 10x Genomics). Briefly, single cells were resuspended in the master mix and loaded together with partition"
- GSM7166275 / Sample_data_processing: matched `Cell Ranger` in "The demultiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v5.0.0 (https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/5"
- GSM7166276 / Sample_data_processing: matched `Cell Ranger` in "The demultiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v5.0.0 (https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/5"
- GSM7166277 / Sample_data_processing: matched `Cell Ranger` in "The demultiplexing, barcoded processing, gene counting and aggregation were made using the Cell Ranger software v5.0.0 (https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/5"
- GSM7166275 / Sample_title: matched `scRNA` in "iMAC,scRNAseq"
- GSM7166276 / Sample_title: matched `scRNA` in "LO,scRNAseq"
- GSM7166277 / Sample_title: matched `scRNA` in "LOiMAC,scRNAseq"
- GSM7166275 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM7166nnn/GSM7166275/suppl/GSM7166275_iMAC_barcodes.tsv.gz"
- GSM7166275 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM7166nnn/GSM7166275/suppl/GSM7166275_iMAC_features.tsv.gz"
- GSM7166275 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM7166nnn/GSM7166275/suppl/GSM7166275_iMAC_matrix.mtx.gz"
- GSM7166276 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM7166nnn/GSM7166276/suppl/GSM7166276_LO_barcodes.tsv.gz"
- GSM7166276 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM7166nnn/GSM7166276/suppl/GSM7166276_LO_features.tsv.gz"
- GSM7166276 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM7166nnn/GSM7166276/suppl/GSM7166276_LO_matrix.mtx.gz"
- GSM7166277 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM7166nnn/GSM7166277/suppl/GSM7166277_LOiMAC_barcodes.tsv.gz"
- GSM7166277 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM7166nnn/GSM7166277/suppl/GSM7166277_LOiMAC_features.tsv.gz"
- GSM7166277 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM7166nnn/GSM7166277/suppl/GSM7166277_LOiMAC_matrix.mtx.gz"
### material_type (WARN)
- GSM7166276 / Sample_source_name_ch1: matched `organoid` in "liver organoid"
- GSM7166277 / Sample_source_name_ch1: matched `organoid` in "liver organoid co-cultured with macrophage"
- GSM7166276 / Sample_characteristics_ch1: matched `organoid` in "cell type: liver organoid"
- GSM7166277 / Sample_characteristics_ch1: matched `organoid` in "cell type: liver organoid co-cultured with macrophage"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: 10x, Cell Ranger, barcodes.tsv, features.tsv, matrix.mtx, scRNA (3 sample(s)))
<!-- /computed -->