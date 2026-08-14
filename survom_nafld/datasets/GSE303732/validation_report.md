# Validation report: GSE303732

An appendiceal cancer organoid biobank identifies phenotypic evolution and druggable dependencies of peritoneal carcinomatosis

<!-- computed -->
Sample count: 6

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 6 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 6/6 |
| source_tissue | WARN | liver-pattern source 0/6 |
| library_strategy | PASS | RNA-Seq 6/6 |
| library_source | WARN | library_source: other 3/6, transcriptomic single cell 3/6 |
| library_selection | PASS | cDNA 6/6 |
| instrument_model | PASS | Illumina NovaSeq 6000 6/6 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | FAIL | no NAFLD-spectrum term found in series or sample metadata |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: .h5ad, 10x, Scanpy, barcodes.tsv, features.tsv, matrix.mtx, scRNA, single cell suspension (7 sample(s)) |
| material_type | WARN | cell/culture terms in sample metadata: cell line, organoid (6/6 samples) |
| expression_data_availability | PASS | processed per-sample counts (6/6), packaged in GSE303732_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE303732_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX29859509, https://www.ncbi.nlm.nih.gov/sra?term=SRX29859510, https://www.ncbi.nlm.nih.gov/sra?term=SRX29859511, https://www.ncbi.nlm.nih.gov/sra?term=SRX29859512, https://www.ncbi.nlm.nih.gov/sra?term=SRX29859513, and 1 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: patient-derived organoid (6)
- **treatment**: primary tumor PDO (AC), metastatic tumor PDO (PC) (6)

## Field presence

- cell line: 6/6
- cell type: 6/6
- hto: 3/6
- tissue: 6/6 (canon: tissue)
- treatment: 6/6 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
### library_source (WARN)
### metadata_completeness (WARN)
### disease_relevance (FAIL)
### single_cell_or_spatial (FAIL)
- GSM9134872 / Sample_extract_protocol_ch1: matched `single cell suspension` in "Organoids were harvested from Matrigel 3mM EDTA in DPBS then dissociated into single cells using TrypLE (Thermo Fisher Scientific) for 5–10 min at 37 °C and serially filtered through a 40-μm then 20-μ"
- GSM9134872 / Sample_extract_protocol_ch1: matched `scRNA` in "scRNA-seq was performed on the Chromium instrument (10x Genomics) according to the 3′ RNA v3.1 user manual. Cells were captured in droplets and subjected to reverse transcription and cell barcoding; e"
- GSM9134873 / Sample_extract_protocol_ch1: matched `single cell suspension` in "Organoids were harvested from Matrigel 3mM EDTA in DPBS then dissociated into single cells using TrypLE (Thermo Fisher Scientific) for 5–10 min at 37 °C and serially filtered through a 40-μm then 20-μ"
- GSM9134873 / Sample_extract_protocol_ch1: matched `scRNA` in "scRNA-seq was performed on the Chromium instrument (10x Genomics) according to the 3′ RNA v3.1 user manual. Cells were captured in droplets and subjected to reverse transcription and cell barcoding; e"
- GSM9134874 / Sample_extract_protocol_ch1: matched `single cell suspension` in "Organoids were harvested from Matrigel 3mM EDTA in DPBS then dissociated into single cells using TrypLE (Thermo Fisher Scientific) for 5–10 min at 37 °C and serially filtered through a 40-μm then 20-μ"
- GSM9134874 / Sample_extract_protocol_ch1: matched `scRNA` in "scRNA-seq was performed on the Chromium instrument (10x Genomics) according to the 3′ RNA v3.1 user manual. Cells were captured in droplets and subjected to reverse transcription and cell barcoding; e"
- GSM9134875 / Sample_extract_protocol_ch1: matched `single cell suspension` in "Organoids were harvested from Matrigel 3mM EDTA in DPBS then dissociated into single cells using TrypLE (Thermo Fisher Scientific) for 5–10 min at 37 °C and serially filtered through a 40-μm then 20-μ"
- GSM9134875 / Sample_extract_protocol_ch1: matched `scRNA` in "scRNA-seq was performed on the Chromium instrument (10x Genomics) according to the 3′ RNA v3.1 user manual. Cells were captured in droplets and subjected to reverse transcription and cell barcoding; e"
- GSM9134876 / Sample_extract_protocol_ch1: matched `single cell suspension` in "Organoids were harvested from Matrigel 3mM EDTA in DPBS then dissociated into single cells using TrypLE (Thermo Fisher Scientific) for 5–10 min at 37 °C and serially filtered through a 40-μm then 20-μ"
- GSM9134876 / Sample_extract_protocol_ch1: matched `scRNA` in "scRNA-seq was performed on the Chromium instrument (10x Genomics) according to the 3′ RNA v3.1 user manual. Cells were captured in droplets and subjected to reverse transcription and cell barcoding; e"
- GSM9134877 / Sample_extract_protocol_ch1: matched `single cell suspension` in "Organoids were harvested from Matrigel 3mM EDTA in DPBS then dissociated into single cells using TrypLE (Thermo Fisher Scientific) for 5–10 min at 37 °C and serially filtered through a 40-μm then 20-μ"
- GSM9134877 / Sample_extract_protocol_ch1: matched `scRNA` in "scRNA-seq was performed on the Chromium instrument (10x Genomics) according to the 3′ RNA v3.1 user manual. Cells were captured in droplets and subjected to reverse transcription and cell barcoding; e"
- GSM9134872 / Sample_data_processing: matched `10x` in "FASTQ files from organoid samples were processed with the SEQC pipeline using the GRCh38 human genome reference, default parameters, and platform set to 10x Genomics v3 3′ scRNA-seq kit. The SEQC pipe"
- GSM9134872 / Sample_data_processing: matched `scRNA` in "CellBender (v.0.3.0), an unsupervised method for removing ambient RNA from scRNA-seq data, was used to generate a denoised (i.e., ambient-RNA-corrected) count matrix, as well as the probability that e"
- GSM9134872 / Sample_data_processing: matched `Scanpy` in "The k-nearest-neighbor graph based on the scANVI embedding and the correlation metric was computed using Scanpy (v.1.10.0), with otherwise default parameter settings. The Uniform Manifold Approximatio"
- GSM9134872 / Sample_data_processing: matched `10x` in "Supplementary files format and content: 10x MEX-formatted (*barcodes.tsv.gz, *features.tsv.gz, *matrix.mtx.gz) CellBender-corrected GEX counts for cells passing QC"
- GSM9134872 / Sample_data_processing: matched `10x` in "Supplementary files format and content: 10x MEX-formatted (*barcodes.tsv.gz, *features.tsv.gz, *matrix.mtx.gz) HTO counts for cells passing QC"
- GSM9134873 / Sample_data_processing: matched `10x` in "FASTQ files from organoid samples were processed with the SEQC pipeline using the GRCh38 human genome reference, default parameters, and platform set to 10x Genomics v3 3′ scRNA-seq kit. The SEQC pipe"
- GSM9134873 / Sample_data_processing: matched `scRNA` in "CellBender (v.0.3.0), an unsupervised method for removing ambient RNA from scRNA-seq data, was used to generate a denoised (i.e., ambient-RNA-corrected) count matrix, as well as the probability that e"
- GSM9134873 / Sample_data_processing: matched `Scanpy` in "The k-nearest-neighbor graph based on the scANVI embedding and the correlation metric was computed using Scanpy (v.1.10.0), with otherwise default parameter settings. The Uniform Manifold Approximatio"
- GSM9134873 / Sample_data_processing: matched `10x` in "Supplementary files format and content: 10x MEX-formatted (*barcodes.tsv.gz, *features.tsv.gz, *matrix.mtx.gz) CellBender-corrected GEX counts for cells passing QC"
- GSM9134873 / Sample_data_processing: matched `10x` in "Supplementary files format and content: 10x MEX-formatted (*barcodes.tsv.gz, *features.tsv.gz, *matrix.mtx.gz) HTO counts for cells passing QC"
- GSM9134874 / Sample_data_processing: matched `10x` in "FASTQ files from organoid samples were processed with the SEQC pipeline using the GRCh38 human genome reference, default parameters, and platform set to 10x Genomics v3 3′ scRNA-seq kit. The SEQC pipe"
- GSM9134874 / Sample_data_processing: matched `scRNA` in "CellBender (v.0.3.0), an unsupervised method for removing ambient RNA from scRNA-seq data, was used to generate a denoised (i.e., ambient-RNA-corrected) count matrix, as well as the probability that e"
- GSM9134874 / Sample_data_processing: matched `Scanpy` in "The k-nearest-neighbor graph based on the scANVI embedding and the correlation metric was computed using Scanpy (v.1.10.0), with otherwise default parameter settings. The Uniform Manifold Approximatio"
- GSM9134874 / Sample_data_processing: matched `10x` in "Supplementary files format and content: 10x MEX-formatted (*barcodes.tsv.gz, *features.tsv.gz, *matrix.mtx.gz) CellBender-corrected GEX counts for cells passing QC"
- GSM9134874 / Sample_data_processing: matched `10x` in "Supplementary files format and content: 10x MEX-formatted (*barcodes.tsv.gz, *features.tsv.gz, *matrix.mtx.gz) HTO counts for cells passing QC"
- GSM9134875 / Sample_data_processing: matched `10x` in "FASTQ files from organoid samples were processed with the SEQC pipeline using the GRCh38 human genome reference, default parameters, and platform set to 10x Genomics v3 3′ scRNA-seq kit. The SEQC pipe"
- GSM9134875 / Sample_data_processing: matched `scRNA` in "CellBender (v.0.3.0), an unsupervised method for removing ambient RNA from scRNA-seq data, was used to generate a denoised (i.e., ambient-RNA-corrected) count matrix, as well as the probability that e"
- GSM9134875 / Sample_data_processing: matched `Scanpy` in "The k-nearest-neighbor graph based on the scANVI embedding and the correlation metric was computed using Scanpy (v.1.10.0), with otherwise default parameter settings. The Uniform Manifold Approximatio"
- GSM9134875 / Sample_data_processing: matched `10x` in "Supplementary files format and content: 10x MEX-formatted (*barcodes.tsv.gz, *features.tsv.gz, *matrix.mtx.gz) CellBender-corrected GEX counts for cells passing QC"
- GSM9134875 / Sample_data_processing: matched `10x` in "Supplementary files format and content: 10x MEX-formatted (*barcodes.tsv.gz, *features.tsv.gz, *matrix.mtx.gz) HTO counts for cells passing QC"
- GSM9134876 / Sample_data_processing: matched `10x` in "FASTQ files from organoid samples were processed with the SEQC pipeline using the GRCh38 human genome reference, default parameters, and platform set to 10x Genomics v3 3′ scRNA-seq kit. The SEQC pipe"
- GSM9134876 / Sample_data_processing: matched `scRNA` in "CellBender (v.0.3.0), an unsupervised method for removing ambient RNA from scRNA-seq data, was used to generate a denoised (i.e., ambient-RNA-corrected) count matrix, as well as the probability that e"
- GSM9134876 / Sample_data_processing: matched `Scanpy` in "The k-nearest-neighbor graph based on the scANVI embedding and the correlation metric was computed using Scanpy (v.1.10.0), with otherwise default parameter settings. The Uniform Manifold Approximatio"
- GSM9134876 / Sample_data_processing: matched `10x` in "Supplementary files format and content: 10x MEX-formatted (*barcodes.tsv.gz, *features.tsv.gz, *matrix.mtx.gz) CellBender-corrected GEX counts for cells passing QC"
- GSM9134876 / Sample_data_processing: matched `10x` in "Supplementary files format and content: 10x MEX-formatted (*barcodes.tsv.gz, *features.tsv.gz, *matrix.mtx.gz) HTO counts for cells passing QC"
- GSM9134877 / Sample_data_processing: matched `10x` in "FASTQ files from organoid samples were processed with the SEQC pipeline using the GRCh38 human genome reference, default parameters, and platform set to 10x Genomics v3 3′ scRNA-seq kit. The SEQC pipe"
- GSM9134877 / Sample_data_processing: matched `scRNA` in "CellBender (v.0.3.0), an unsupervised method for removing ambient RNA from scRNA-seq data, was used to generate a denoised (i.e., ambient-RNA-corrected) count matrix, as well as the probability that e"
- GSM9134877 / Sample_data_processing: matched `Scanpy` in "The k-nearest-neighbor graph based on the scANVI embedding and the correlation metric was computed using Scanpy (v.1.10.0), with otherwise default parameter settings. The Uniform Manifold Approximatio"
- GSM9134877 / Sample_data_processing: matched `10x` in "Supplementary files format and content: 10x MEX-formatted (*barcodes.tsv.gz, *features.tsv.gz, *matrix.mtx.gz) CellBender-corrected GEX counts for cells passing QC"
- GSM9134877 / Sample_data_processing: matched `10x` in "Supplementary files format and content: 10x MEX-formatted (*barcodes.tsv.gz, *features.tsv.gz, *matrix.mtx.gz) HTO counts for cells passing QC"
- GSM9134872 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9134nnn/GSM9134872/suppl/GSM9134872_KG208_post_qc_gex_barcodes.tsv.gz"
- GSM9134872 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9134nnn/GSM9134872/suppl/GSM9134872_KG208_post_qc_gex_features.tsv.gz"
- GSM9134872 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9134nnn/GSM9134872/suppl/GSM9134872_KG208_post_qc_gex_matrix.mtx.gz"
- GSM9134873 / Sample_supplementary_file_2: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9134nnn/GSM9134873/suppl/GSM9134873_KG208_post_qc_hto_barcodes.tsv.gz"
- GSM9134873 / Sample_supplementary_file_3: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9134nnn/GSM9134873/suppl/GSM9134873_KG208_post_qc_hto_features.tsv.gz"
- GSM9134873 / Sample_supplementary_file_4: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9134nnn/GSM9134873/suppl/GSM9134873_KG208_post_qc_hto_matrix.mtx.gz"
- GSM9134874 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9134nnn/GSM9134874/suppl/GSM9134874_KG215_post_qc_gex_barcodes.tsv.gz"
- GSM9134874 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9134nnn/GSM9134874/suppl/GSM9134874_KG215_post_qc_gex_features.tsv.gz"
- GSM9134874 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9134nnn/GSM9134874/suppl/GSM9134874_KG215_post_qc_gex_matrix.mtx.gz"
- GSM9134875 / Sample_supplementary_file_2: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9134nnn/GSM9134875/suppl/GSM9134875_KG215_post_qc_hto_barcodes.tsv.gz"
- GSM9134875 / Sample_supplementary_file_3: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9134nnn/GSM9134875/suppl/GSM9134875_KG215_post_qc_hto_features.tsv.gz"
- GSM9134875 / Sample_supplementary_file_4: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9134nnn/GSM9134875/suppl/GSM9134875_KG215_post_qc_hto_matrix.mtx.gz"
- GSM9134876 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9134nnn/GSM9134876/suppl/GSM9134876_KG236_post_qc_gex_barcodes.tsv.gz"
- GSM9134876 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9134nnn/GSM9134876/suppl/GSM9134876_KG236_post_qc_gex_features.tsv.gz"
- GSM9134876 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9134nnn/GSM9134876/suppl/GSM9134876_KG236_post_qc_gex_matrix.mtx.gz"
- GSM9134877 / Sample_supplementary_file_2: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9134nnn/GSM9134877/suppl/GSM9134877_KG236_post_qc_hto_barcodes.tsv.gz"
- GSM9134877 / Sample_supplementary_file_3: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9134nnn/GSM9134877/suppl/GSM9134877_KG236_post_qc_hto_features.tsv.gz"
- GSM9134877 / Sample_supplementary_file_4: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9134nnn/GSM9134877/suppl/GSM9134877_KG236_post_qc_hto_matrix.mtx.gz"
- GSE303732 / Series_supplementary_file: matched `.h5ad` in "ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE303nnn/GSE303732/suppl/GSE303732_mahmoud_et_al_ac_pc_pdo_pooled_processed.h5ad"
### material_type (WARN)
- GSM9134872 / Sample_source_name_ch1: matched `organoid` in "patient-derived organoid"
- GSM9134873 / Sample_source_name_ch1: matched `organoid` in "patient-derived organoid"
- GSM9134874 / Sample_source_name_ch1: matched `organoid` in "patient-derived organoid"
- GSM9134875 / Sample_source_name_ch1: matched `organoid` in "patient-derived organoid"
- GSM9134876 / Sample_source_name_ch1: matched `organoid` in "patient-derived organoid"
- GSM9134877 / Sample_source_name_ch1: matched `organoid` in "patient-derived organoid"
- GSM9134872 / Sample_title: matched `organoid` in "matched AC-PC pair patient-derived organoid (PDO) cells, originating donor KG208, GEX"
- GSM9134873 / Sample_title: matched `organoid` in "matched AC-PC pair patient-derived organoid (PDO) cells, originating donor KG208, HTO"
- GSM9134874 / Sample_title: matched `organoid` in "matched AC-PC pair patient-derived organoid (PDO) cells, originating donor KG215, GEX"
- GSM9134875 / Sample_title: matched `organoid` in "matched AC-PC pair patient-derived organoid (PDO) cells, originating donor KG215, HTO"
- GSM9134876 / Sample_title: matched `organoid` in "matched AC-PC pair patient-derived organoid (PDO) cells, originating donor KG236, GEX"
- GSM9134877 / Sample_title: matched `organoid` in "matched AC-PC pair patient-derived organoid (PDO) cells, originating donor KG236, HTO"
- GSM9134872 / Sample_characteristics_ch1: matched `organoid` in "tissue: patient-derived organoid"
- GSM9134872 / Sample_characteristics_ch1: matched `cell line` in "cell line: KG208Ap, KG208PW (mixture)"
- GSM9134873 / Sample_characteristics_ch1: matched `organoid` in "tissue: patient-derived organoid"
- GSM9134873 / Sample_characteristics_ch1: matched `cell line` in "cell line: KG208Ap, KG208PW (mixture)"
- GSM9134874 / Sample_characteristics_ch1: matched `organoid` in "tissue: patient-derived organoid"
- GSM9134874 / Sample_characteristics_ch1: matched `cell line` in "cell line: KG215Ap, KG215Om (mixture)"
- GSM9134875 / Sample_characteristics_ch1: matched `organoid` in "tissue: patient-derived organoid"
- GSM9134875 / Sample_characteristics_ch1: matched `cell line` in "cell line: KG215Ap, KG215Om (mixture)"
- GSM9134876 / Sample_characteristics_ch1: matched `organoid` in "tissue: patient-derived organoid"
- GSM9134876 / Sample_characteristics_ch1: matched `cell line` in "cell line: KG236Ap, KG236Om, two additional lines excluded from downstream analysis (mixture)"
- GSM9134877 / Sample_characteristics_ch1: matched `organoid` in "tissue: patient-derived organoid"
- GSM9134877 / Sample_characteristics_ch1: matched `cell line` in "cell line: KG236Ap, KG236Om, two additional lines excluded from downstream analysis (mixture)"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: .h5ad, 10x, Scanpy, barcodes.tsv, features.tsv, matrix.mtx, scRNA, single cell suspension (7 sample(s)))
<!-- /computed -->