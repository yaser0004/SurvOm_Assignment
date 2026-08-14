# Validation report: GSE189175

Single-nucleus RNA-seq of NASH HCC liver tissue

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
| metadata_completeness | PASS | reported consistently: disease, sex, tissue; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (6 sample(s)) |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: 10X, STARsolo, Seurat, barcodes.tsv, features.tsv, matrix.mtx (7 sample(s)) |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE189175_counts_barcodes.tsv.gz |
| series_matrix | INFO | present, metadata-only (GSE189175_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | no SRA/raw sequencing links found |

## Canonical field distributions

- **disease**: NAFLD (2), NASH (4)
- **sex**: Female (6)
- **tissue**: Adjacent non-tumor (3), Tumor (3)

## Field presence

- Sex: 6/6 (canon: sex)
- condition: 6/6 (canon: disease)
- tissue: 6/6 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### single_cell_or_spatial (FAIL)
- GSM5695736 / Sample_extract_protocol_ch1: matched `10X` in "Frozen biposies were homgogenized in lysis buffer, filtered and washed, suspended, and processed with a 10X Chromium using the Single Cell 3' v3 library prep."
- GSM5695736 / Sample_extract_protocol_ch1: matched `10X` in "10X Single Cell 3' v3"
- GSM5695737 / Sample_extract_protocol_ch1: matched `10X` in "Frozen biposies were homgogenized in lysis buffer, filtered and washed, suspended, and processed with a 10X Chromium using the Single Cell 3' v3 library prep."
- GSM5695737 / Sample_extract_protocol_ch1: matched `10X` in "10X Single Cell 3' v3"
- GSM5695738 / Sample_extract_protocol_ch1: matched `10X` in "Frozen biposies were homgogenized in lysis buffer, filtered and washed, suspended, and processed with a 10X Chromium using the Single Cell 3' v3 library prep."
- GSM5695738 / Sample_extract_protocol_ch1: matched `10X` in "10X Single Cell 3' v3"
- GSM5695739 / Sample_extract_protocol_ch1: matched `10X` in "Frozen biposies were homgogenized in lysis buffer, filtered and washed, suspended, and processed with a 10X Chromium using the Single Cell 3' v3 library prep."
- GSM5695739 / Sample_extract_protocol_ch1: matched `10X` in "10X Single Cell 3' v3"
- GSM5695740 / Sample_extract_protocol_ch1: matched `10X` in "Frozen biposies were homgogenized in lysis buffer, filtered and washed, suspended, and processed with a 10X Chromium using the Single Cell 3' v3 library prep."
- GSM5695740 / Sample_extract_protocol_ch1: matched `10X` in "10X Single Cell 3' v3"
- GSM5695741 / Sample_extract_protocol_ch1: matched `10X` in "Frozen biposies were homgogenized in lysis buffer, filtered and washed, suspended, and processed with a 10X Chromium using the Single Cell 3' v3 library prep."
- GSM5695741 / Sample_extract_protocol_ch1: matched `10X` in "10X Single Cell 3' v3"
- GSM5695736 / Sample_data_processing: matched `STARsolo` in "Reads were aligned to the hg38 genome using STARsolo from STAR v2.7.3a."
- GSM5695736 / Sample_data_processing: matched `Seurat` in "Clustering was performed using Seurat with SCTransform and CCA integration."
- GSM5695737 / Sample_data_processing: matched `STARsolo` in "Reads were aligned to the hg38 genome using STARsolo from STAR v2.7.3a."
- GSM5695737 / Sample_data_processing: matched `Seurat` in "Clustering was performed using Seurat with SCTransform and CCA integration."
- GSM5695738 / Sample_data_processing: matched `STARsolo` in "Reads were aligned to the hg38 genome using STARsolo from STAR v2.7.3a."
- GSM5695738 / Sample_data_processing: matched `Seurat` in "Clustering was performed using Seurat with SCTransform and CCA integration."
- GSM5695739 / Sample_data_processing: matched `STARsolo` in "Reads were aligned to the hg38 genome using STARsolo from STAR v2.7.3a."
- GSM5695739 / Sample_data_processing: matched `Seurat` in "Clustering was performed using Seurat with SCTransform and CCA integration."
- GSM5695740 / Sample_data_processing: matched `STARsolo` in "Reads were aligned to the hg38 genome using STARsolo from STAR v2.7.3a."
- GSM5695740 / Sample_data_processing: matched `Seurat` in "Clustering was performed using Seurat with SCTransform and CCA integration."
- GSM5695741 / Sample_data_processing: matched `STARsolo` in "Reads were aligned to the hg38 genome using STARsolo from STAR v2.7.3a."
- GSM5695741 / Sample_data_processing: matched `Seurat` in "Clustering was performed using Seurat with SCTransform and CCA integration."
- GSE189175 / Series_supplementary_file: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE189nnn/GSE189175/suppl/GSE189175_counts_barcodes.tsv.gz"
- GSE189175 / Series_supplementary_file: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE189nnn/GSE189175/suppl/GSE189175_counts_features.tsv.gz"
- GSE189175 / Series_supplementary_file: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE189nnn/GSE189175/suppl/GSE189175_counts_matrix.mtx.gz"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: 10X, STARsolo, Seurat, barcodes.tsv, features.tsv, matrix.mtx (7 sample(s)))
<!-- /computed -->