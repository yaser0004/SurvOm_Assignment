# Validation report: GSE192741

Spatial proteogenomics reveals distinct and evolutionarily-conserved hepatic macrophage niches (spatial)

<!-- computed -->
Sample count: 15

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 15 samples (below 20) |
| organism_consistency | WARN | mixed organisms: Homo sapiens 5/15, Mus musculus 10/15 |
| source_tissue | PASS | liver-pattern source 15/15 |
| library_strategy | PASS | RNA-Seq 15/15 |
| library_source | PASS | transcriptomic 15/15 |
| library_selection | PASS | cDNA 15/15 |
| instrument_model | PASS | Illumina NovaSeq 6000 15/15 |
| metadata_completeness | PASS | reported consistently: disease; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade, tissue, treatment |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: 10X, Seurat, Visium, filtered_feature_bc_matrix, tissue_positions (15 sample(s)) |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (15/15), packaged in GSE192741_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE192741-GPL24247_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX13549293, https://www.ncbi.nlm.nih.gov/sra?term=SRX13549294, https://www.ncbi.nlm.nih.gov/sra?term=SRX13549295, https://www.ncbi.nlm.nih.gov/sra?term=SRX13549296, https://www.ncbi.nlm.nih.gov/sra?term=SRX13549297, and 10 more (see sample_metadata.csv) |

## Canonical field distributions

- **disease**: Healthy (2), SD (1), StSt (6), Steatotic (3), WD (3)

## Field presence

- condition: 15/15 (canon: disease)
- number of added abs: 15/15
- number of spots: 15/15
- platform: 15/15
- shortfilename: 15/15
- strain: 15/15

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### organism_consistency (WARN)
### disease_relevance (WARN)
- GSE192741 / Series_summary: matched `NAFLD` in "Analysis of CITE-seq data , Nuclei RNA-seq data and single cell RNA-seq data on CD45+ and CD45- cells isolated from the livers of mice fed a standard diet (SD) or western diet (WD; fat, cholesterol an"
- GSE192741 / Series_overall_design: matched `NAFLD` in "10 Visium Spatial Seq = mouse StSt liver, mouse StSt capsule, mouse NAFLD liver,  human non-steatotic liver, human steatotic liver."
### single_cell_or_spatial (FAIL)
- GSM5764414 / Sample_data_processing: matched `10X` in "Raw sequencing data for each sample was converted to matrices of expression counts using the Space Ranger software provided by 10X Genomics (version 1.0)."
- GSM5764414 / Sample_data_processing: matched `Seurat` in "Supplementary_files_format_and_content: rds file: Seurat object"
- GSM5764415 / Sample_data_processing: matched `10X` in "Raw sequencing data for each sample was converted to matrices of expression counts using the Space Ranger software provided by 10X Genomics (version 1.0)."
- GSM5764415 / Sample_data_processing: matched `Seurat` in "Supplementary_files_format_and_content: rds file: Seurat object"
- GSM5764416 / Sample_data_processing: matched `10X` in "Raw sequencing data for each sample was converted to matrices of expression counts using the Space Ranger software provided by 10X Genomics (version 1.0)."
- GSM5764416 / Sample_data_processing: matched `Seurat` in "Supplementary_files_format_and_content: rds file: Seurat object"
- GSM5764417 / Sample_data_processing: matched `10X` in "Raw sequencing data for each sample was converted to matrices of expression counts using the Space Ranger software provided by 10X Genomics (version 1.0)."
- GSM5764417 / Sample_data_processing: matched `Seurat` in "Supplementary_files_format_and_content: rds file: Seurat object"
- GSM5764418 / Sample_data_processing: matched `10X` in "Raw sequencing data for each sample was converted to matrices of expression counts using the Space Ranger software provided by 10X Genomics (version 1.0)."
- GSM5764418 / Sample_data_processing: matched `Seurat` in "Supplementary_files_format_and_content: rds file: Seurat object"
- GSM5764419 / Sample_data_processing: matched `10X` in "Raw sequencing data for each sample was converted to matrices of expression counts using the Space Ranger software provided by 10X Genomics (version 1.0)."
- GSM5764419 / Sample_data_processing: matched `Seurat` in "Supplementary_files_format_and_content: rds file: Seurat object"
- GSM5764420 / Sample_data_processing: matched `10X` in "Raw sequencing data for each sample was converted to matrices of expression counts using the Space Ranger software provided by 10X Genomics (version 1.0)."
- GSM5764420 / Sample_data_processing: matched `Seurat` in "Supplementary_files_format_and_content: rds file: Seurat object"
- GSM5764421 / Sample_data_processing: matched `10X` in "Raw sequencing data for each sample was converted to matrices of expression counts using the Space Ranger software provided by 10X Genomics (version 1.0)."
- GSM5764421 / Sample_data_processing: matched `Seurat` in "Supplementary_files_format_and_content: rds file: Seurat object"
- GSM5764422 / Sample_data_processing: matched `10X` in "Raw sequencing data for each sample was converted to matrices of expression counts using the Space Ranger software provided by 10X Genomics (version 1.0)."
- GSM5764422 / Sample_data_processing: matched `Seurat` in "Supplementary_files_format_and_content: rds file: Seurat object"
- GSM5764423 / Sample_data_processing: matched `10X` in "Raw sequencing data for each sample was converted to matrices of expression counts using the Space Ranger software provided by 10X Genomics (version 1.0)."
- GSM5764423 / Sample_data_processing: matched `Seurat` in "Supplementary_files_format_and_content: rds file: Seurat object"
- GSM5764424 / Sample_data_processing: matched `10X` in "Raw sequencing data for each sample was converted to matrices of expression counts using the Space Ranger software provided by 10X Genomics (version 1.0)."
- GSM5764424 / Sample_data_processing: matched `Seurat` in "Supplementary_files_format_and_content: rds file: Seurat object"
- GSM5764425 / Sample_data_processing: matched `10X` in "Raw sequencing data for each sample was converted to matrices of expression counts using the Space Ranger software provided by 10X Genomics (version 1.0)."
- GSM5764425 / Sample_data_processing: matched `Seurat` in "Supplementary_files_format_and_content: rds file: Seurat object"
- GSM5764426 / Sample_data_processing: matched `10X` in "Raw sequencing data for each sample was converted to matrices of expression counts using the Space Ranger software provided by 10X Genomics (version 1.0)."
- GSM5764426 / Sample_data_processing: matched `Seurat` in "Supplementary_files_format_and_content: rds file: Seurat object"
- GSM5764427 / Sample_data_processing: matched `10X` in "Raw sequencing data for each sample was converted to matrices of expression counts using the Space Ranger software provided by 10X Genomics (version 1.0)."
- GSM5764427 / Sample_data_processing: matched `Seurat` in "Supplementary_files_format_and_content: rds file: Seurat object"
- GSM5764428 / Sample_data_processing: matched `10X` in "Raw sequencing data for each sample was converted to matrices of expression counts using the Space Ranger software provided by 10X Genomics (version 1.0)."
- GSM5764428 / Sample_data_processing: matched `Seurat` in "Supplementary_files_format_and_content: rds file: Seurat object"
- GSM5764424 / Sample_title: matched `Visium` in "Whole Liver_Visium of Human H35 (sample1)"
- GSM5764425 / Sample_title: matched `Visium` in "Whole Liver_Visium of Human H35 (sample2)"
- GSM5764426 / Sample_title: matched `Visium` in "Whole Liver_Visium of Human H36"
- GSM5764427 / Sample_title: matched `Visium` in "Whole Liver_Visium of Human H37"
- GSM5764428 / Sample_title: matched `Visium` in "Whole Liver_Visium of Human H38"
- GSM5764414 / Sample_supplementary_file_1: matched `filtered_feature_bc_matrix` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764414/suppl/GSM5764414_filtered_feature_bc_matrix_JBO001.h5"
- GSM5764414 / Sample_supplementary_file_5: matched `tissue_positions` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764414/suppl/GSM5764414_tissue_positions_list_JBO001.csv.gz"
- GSM5764415 / Sample_supplementary_file_1: matched `filtered_feature_bc_matrix` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764415/suppl/GSM5764415_filtered_feature_bc_matrix_JBO002.h5"
- GSM5764415 / Sample_supplementary_file_5: matched `tissue_positions` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764415/suppl/GSM5764415_tissue_positions_list_JBO002.csv.gz"
- GSM5764416 / Sample_supplementary_file_1: matched `filtered_feature_bc_matrix` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764416/suppl/GSM5764416_filtered_feature_bc_matrix_JBO003.h5"
- GSM5764416 / Sample_supplementary_file_5: matched `tissue_positions` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764416/suppl/GSM5764416_tissue_positions_list_JBO003.csv.gz"
- GSM5764417 / Sample_supplementary_file_1: matched `filtered_feature_bc_matrix` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764417/suppl/GSM5764417_filtered_feature_bc_matrix_JBO004.h5"
- GSM5764417 / Sample_supplementary_file_5: matched `tissue_positions` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764417/suppl/GSM5764417_tissue_positions_list_JBO004.csv.gz"
- GSM5764418 / Sample_supplementary_file_1: matched `filtered_feature_bc_matrix` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764418/suppl/GSM5764418_filtered_feature_bc_matrix_CAP002.h5"
- GSM5764418 / Sample_supplementary_file_5: matched `tissue_positions` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764418/suppl/GSM5764418_tissue_positions_list_CAP002.csv.gz"
- GSM5764419 / Sample_supplementary_file_1: matched `filtered_feature_bc_matrix` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764419/suppl/GSM5764419_filtered_feature_bc_matrix_JBO006.h5"
- GSM5764419 / Sample_supplementary_file_5: matched `tissue_positions` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764419/suppl/GSM5764419_tissue_positions_list_JBO006.csv.gz"
- GSM5764420 / Sample_supplementary_file_1: matched `filtered_feature_bc_matrix` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764420/suppl/GSM5764420_filtered_feature_bc_matrix_JBO009.h5"
- GSM5764420 / Sample_supplementary_file_5: matched `tissue_positions` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764420/suppl/GSM5764420_tissue_positions_list_JBO009.csv.gz"
- GSM5764421 / Sample_supplementary_file_1: matched `filtered_feature_bc_matrix` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764421/suppl/GSM5764421_filtered_feature_bc_matrix_JBO010.h5"
- GSM5764421 / Sample_supplementary_file_5: matched `tissue_positions` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764421/suppl/GSM5764421_tissue_positions_list_JBO010.csv.gz"
- GSM5764422 / Sample_supplementary_file_1: matched `filtered_feature_bc_matrix` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764422/suppl/GSM5764422_filtered_feature_bc_matrix_JBO012.h5"
- GSM5764422 / Sample_supplementary_file_5: matched `tissue_positions` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764422/suppl/GSM5764422_tissue_positions_list_JBO012.csv.gz"
- GSM5764423 / Sample_supplementary_file_2: matched `filtered_feature_bc_matrix` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764423/suppl/GSM5764423_filtered_feature_bc_matrix_BH001.h5"
- GSM5764423 / Sample_supplementary_file_6: matched `tissue_positions` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764423/suppl/GSM5764423_tissue_positions_list_BH001.csv.gz"
- GSM5764424 / Sample_supplementary_file_1: matched `filtered_feature_bc_matrix` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764424/suppl/GSM5764424_filtered_feature_bc_matrix_JBO014.h5"
- GSM5764424 / Sample_supplementary_file_5: matched `tissue_positions` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764424/suppl/GSM5764424_tissue_positions_list_JBO014.csv.gz"
- GSM5764425 / Sample_supplementary_file_1: matched `filtered_feature_bc_matrix` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764425/suppl/GSM5764425_filtered_feature_bc_matrix_JBO015.h5"
- GSM5764425 / Sample_supplementary_file_5: matched `tissue_positions` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764425/suppl/GSM5764425_tissue_positions_list_JBO015.csv.gz"
- GSM5764426 / Sample_supplementary_file_1: matched `filtered_feature_bc_matrix` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764426/suppl/GSM5764426_filtered_feature_bc_matrix_JBO018.h5"
- GSM5764426 / Sample_supplementary_file_5: matched `tissue_positions` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764426/suppl/GSM5764426_tissue_positions_list_JBO018.csv.gz"
- GSM5764427 / Sample_supplementary_file_1: matched `filtered_feature_bc_matrix` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764427/suppl/GSM5764427_filtered_feature_bc_matrix_JBO019.h5"
- GSM5764427 / Sample_supplementary_file_5: matched `tissue_positions` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764427/suppl/GSM5764427_tissue_positions_list_JBO019.csv.gz"
- GSM5764428 / Sample_supplementary_file_1: matched `filtered_feature_bc_matrix` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764428/suppl/GSM5764428_filtered_feature_bc_matrix_JBO022.h5"
- GSM5764428 / Sample_supplementary_file_5: matched `tissue_positions` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5764nnn/GSM5764428/suppl/GSM5764428_tissue_positions_list_JBO022.csv.gz"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: 10X, Seurat, Visium, filtered_feature_bc_matrix, tissue_positions (15 sample(s)))
<!-- /computed -->