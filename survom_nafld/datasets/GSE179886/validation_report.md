# Validation report: GSE179886

Endothelial-immune crosstalk contributes to vasculopathy in nonalcoholic fatty liver disease

<!-- computed -->
Sample count: 2

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 2 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 2/2 |
| source_tissue | WARN | liver-pattern source 0/2; off-target tissue signal detected |
| library_strategy | PASS | RNA-Seq 2/2 |
| library_source | PASS | transcriptomic 2/2 |
| library_selection | PASS | cDNA 2/2 |
| instrument_model | PASS | Illumina NovaSeq 6000 2/2 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: 10X, CellRanger, barcodes.tsv, features.tsv, matrix.mtx (2 sample(s)) |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (2/2), packaged in GSE179886_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE179886_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX11407650, https://www.ncbi.nlm.nih.gov/sra?term=SRX11407651 |

## Field presence

- cell type: 2/2

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
- GSM5436516 / Sample_source_name_ch1: matched `PBMC` in "PBMC"
- GSM5436517 / Sample_source_name_ch1: matched `PBMC` in "PBMC"
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE179886 / Series_title: matched `nonalcoholic fatty liver` in "Endothelial-immune crosstalk contributes to vasculopathy in nonalcoholic fatty liver disease"
- GSE179886 / Series_summary: matched `non-alcoholic fatty liver` in "Cardiovascular complications are major causes of death in non-alcoholic fatty liver disease (NAFLD) but the underlying endothelial pathophysiology remains understudied. Here, we cultivated blood outgr"
### single_cell_or_spatial (FAIL)
- GSM5436516 / Sample_extract_protocol_ch1: matched `10X` in "Cell suspensions were then loaded onto 10X Genomics Chromium Controller chip by facility personnel at Single-cell Omics Centre (SCOC), Genome Institute Singapore (GIS). NAFLD and healthy PBMC pools we"
- GSM5436517 / Sample_extract_protocol_ch1: matched `10X` in "Cell suspensions were then loaded onto 10X Genomics Chromium Controller chip by facility personnel at Single-cell Omics Centre (SCOC), Genome Institute Singapore (GIS). NAFLD and healthy PBMC pools we"
- GSM5436516 / Sample_data_processing: matched `CellRanger` in "Raw sequencing data was also processed by NovogeneAIT Genomics (Singapore) using CellRanger (10x Genomics) with reads mapped to the human genome assembly (GRCh38)."
- GSM5436517 / Sample_data_processing: matched `CellRanger` in "Raw sequencing data was also processed by NovogeneAIT Genomics (Singapore) using CellRanger (10x Genomics) with reads mapped to the human genome assembly (GRCh38)."
- GSM5436516 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5436nnn/GSM5436516/suppl/GSM5436516_FLV_barcodes.tsv.gz"
- GSM5436516 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5436nnn/GSM5436516/suppl/GSM5436516_FLV_features.tsv.gz"
- GSM5436516 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5436nnn/GSM5436516/suppl/GSM5436516_FLV_matrix.mtx.gz"
- GSM5436517 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5436nnn/GSM5436517/suppl/GSM5436517_Healthy_barcodes.tsv.gz"
- GSM5436517 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5436nnn/GSM5436517/suppl/GSM5436517_Healthy_features.tsv.gz"
- GSM5436517 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5436nnn/GSM5436517/suppl/GSM5436517_Healthy_matrix.mtx.gz"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: 10X, CellRanger, barcodes.tsv, features.tsv, matrix.mtx (2 sample(s)))
<!-- /computed -->