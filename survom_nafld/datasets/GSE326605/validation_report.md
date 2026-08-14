# Validation report: GSE326605

Bile acid uptake activates STAT signaling and impairs natural killer cells in metabolic dysfunction–associated steatohepatitis

<!-- computed -->
Sample count: 4

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 4 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 4/4 |
| source_tissue | PASS | liver-pattern source 4/4 |
| library_strategy | PASS | RNA-Seq 4/4 |
| library_source | WARN | library_source: transcriptomic single cell 4/4 |
| library_selection | PASS | cDNA 4/4 |
| instrument_model | PASS | Illumina NovaSeq 6000 4/4 |
| metadata_completeness | PASS | reported consistently: disease, tissue, treatment; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: Chromium, Seurat, barcodes.tsv, cellranger, features.tsv, matrix.mtx (4 sample(s)) |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (4/4), packaged in GSE326605_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE326605_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX32741491, https://www.ncbi.nlm.nih.gov/sra?term=SRX32741492, https://www.ncbi.nlm.nih.gov/sra?term=SRX32741493, https://www.ncbi.nlm.nih.gov/sra?term=SRX32741494 |

## Canonical field distributions

- **disease**: Liver fibrosis F4 score (4)
- **tissue**: Blood (4)
- **treatment**: FACS sorted NTCP+ (2), FACS sorted NTCP- (2)

## Field presence

- cell type: 4/4
- disease state: 4/4 (canon: disease)
- tissue: 4/4 (canon: tissue)
- treatment: 4/4 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### library_source (WARN)
### disease_relevance (WARN)
- GSE326605 / Series_title: matched `steatohepatitis` in "Bile acid uptake activates STAT signaling and impairs natural killer cells in metabolic dysfunction–associated steatohepatitis"
- GSE326605 / Series_summary: matched `Metabolic dysfunction-associated stea` in "Metabolic dysfunction-associated steatotic liver disease (MASLD) encompasses a spectrum of fatty liver diseases ranging from steatotic liver disease to metabolic dysfunction-associated steatohepatitis"
- GSE326605 / Series_overall_design: matched `MASH` in "Peripheral NK cells were isolated from two representative F3/F4 advanced liver fibrosis MASH patients (A and B) selected based on age and sex and were sorted on the basis of positive/negative NTCP exp"
### single_cell_or_spatial (FAIL)
- GSM9635514 / Sample_extract_protocol_ch1: matched `Chromium` in "Approximately 10,000 cells from each NK cell subpopulation (NKNTCP+ and NKNTCP-) were loaded into the Chromium Controller system. The RNA libraries were subsequently prepared via the Chromium Single C"
- GSM9635515 / Sample_extract_protocol_ch1: matched `Chromium` in "Approximately 10,000 cells from each NK cell subpopulation (NKNTCP+ and NKNTCP-) were loaded into the Chromium Controller system. The RNA libraries were subsequently prepared via the Chromium Single C"
- GSM9635516 / Sample_extract_protocol_ch1: matched `Chromium` in "Approximately 10,000 cells from each NK cell subpopulation (NKNTCP+ and NKNTCP-) were loaded into the Chromium Controller system. The RNA libraries were subsequently prepared via the Chromium Single C"
- GSM9635517 / Sample_extract_protocol_ch1: matched `Chromium` in "Approximately 10,000 cells from each NK cell subpopulation (NKNTCP+ and NKNTCP-) were loaded into the Chromium Controller system. The RNA libraries were subsequently prepared via the Chromium Single C"
- GSM9635514 / Sample_data_processing: matched `cellranger` in "The counts data was generated with cellranger, v6.0.2, aligning against the human genome GRCh38 with gene annotations from Ensembl release 99. Default parameters were used with expected number of cell"
- GSM9635514 / Sample_data_processing: matched `Seurat` in "Single-cell analysis was performed via Seurat version 5.2.0 40 in R version 4.4.3."
- GSM9635514 / Sample_data_processing: matched `Seurat` in "Integration was conducted with default parameters, using SCT normalization, embedded within Seurat."
- GSM9635515 / Sample_data_processing: matched `cellranger` in "The counts data was generated with cellranger, v6.0.2, aligning against the human genome GRCh38 with gene annotations from Ensembl release 99. Default parameters were used with expected number of cell"
- GSM9635515 / Sample_data_processing: matched `Seurat` in "Single-cell analysis was performed via Seurat version 5.2.0 40 in R version 4.4.3."
- GSM9635515 / Sample_data_processing: matched `Seurat` in "Integration was conducted with default parameters, using SCT normalization, embedded within Seurat."
- GSM9635516 / Sample_data_processing: matched `cellranger` in "The counts data was generated with cellranger, v6.0.2, aligning against the human genome GRCh38 with gene annotations from Ensembl release 99. Default parameters were used with expected number of cell"
- GSM9635516 / Sample_data_processing: matched `Seurat` in "Single-cell analysis was performed via Seurat version 5.2.0 40 in R version 4.4.3."
- GSM9635516 / Sample_data_processing: matched `Seurat` in "Integration was conducted with default parameters, using SCT normalization, embedded within Seurat."
- GSM9635517 / Sample_data_processing: matched `cellranger` in "The counts data was generated with cellranger, v6.0.2, aligning against the human genome GRCh38 with gene annotations from Ensembl release 99. Default parameters were used with expected number of cell"
- GSM9635517 / Sample_data_processing: matched `Seurat` in "Single-cell analysis was performed via Seurat version 5.2.0 40 in R version 4.4.3."
- GSM9635517 / Sample_data_processing: matched `Seurat` in "Integration was conducted with default parameters, using SCT normalization, embedded within Seurat."
- GSM9635514 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9635nnn/GSM9635514/suppl/GSM9635514_NTCP_Negative_A_barcodes.tsv.gz"
- GSM9635514 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9635nnn/GSM9635514/suppl/GSM9635514_NTCP_Negative_A_features.tsv.gz"
- GSM9635514 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9635nnn/GSM9635514/suppl/GSM9635514_NTCP_Negative_A_matrix.mtx.gz"
- GSM9635515 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9635nnn/GSM9635515/suppl/GSM9635515_NTCP_Positive_A_barcodes.tsv.gz"
- GSM9635515 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9635nnn/GSM9635515/suppl/GSM9635515_NTCP_Positive_A_features.tsv.gz"
- GSM9635515 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9635nnn/GSM9635515/suppl/GSM9635515_NTCP_Positive_A_matrix.mtx.gz"
- GSM9635516 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9635nnn/GSM9635516/suppl/GSM9635516_NTCP_Negative_B_barcodes.tsv.gz"
- GSM9635516 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9635nnn/GSM9635516/suppl/GSM9635516_NTCP_Negative_B_features.tsv.gz"
- GSM9635516 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9635nnn/GSM9635516/suppl/GSM9635516_NTCP_Negative_B_matrix.mtx.gz"
- GSM9635517 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9635nnn/GSM9635517/suppl/GSM9635517_NTCP_Positive_B_barcodes.tsv.gz"
- GSM9635517 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9635nnn/GSM9635517/suppl/GSM9635517_NTCP_Positive_B_features.tsv.gz"
- GSM9635517 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9635nnn/GSM9635517/suppl/GSM9635517_NTCP_Positive_B_matrix.mtx.gz"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: Chromium, Seurat, barcodes.tsv, cellranger, features.tsv, matrix.mtx (4 sample(s)))
<!-- /computed -->