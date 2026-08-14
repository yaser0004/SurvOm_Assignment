# Validation report: GSE238219

Perturb-seq against putative NAFLD target genes in differentiated HepaRG cells

<!-- computed -->
Sample count: 5

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 5 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 5/5 |
| source_tissue | PASS | liver-pattern source 5/5 |
| library_strategy | PASS | RNA-Seq 5/5 |
| library_source | WARN | library_source: transcriptomic single cell 5/5 |
| library_selection | PASS | cDNA 5/5 |
| instrument_model | PASS | Illumina NovaSeq 6000 5/5 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: 10X, Cell Ranger, filtered_feature_bc_matrix (5 sample(s)) |
| material_type | WARN | cell/culture terms in sample metadata: HepaRG, cell line (5/5 samples) |
| expression_data_availability | PASS | processed per-sample counts (5/5), packaged in GSE238219_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE238219_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX21157431, https://www.ncbi.nlm.nih.gov/sra?term=SRX21157432, https://www.ncbi.nlm.nih.gov/sra?term=SRX21157433, https://www.ncbi.nlm.nih.gov/sra?term=SRX21157434, https://www.ncbi.nlm.nih.gov/sra?term=SRX21157435 |

## Canonical field distributions

- **treatment**: Differentiated (5)

## Field presence

- cell line: 5/5
- cell type: 5/5
- genotype: 5/5
- treatment: 5/5 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### library_source (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE238219 / Series_title: matched `NAFLD` in "Perturb-seq against putative NAFLD target genes in differentiated HepaRG cells"
- GSE238219 / Series_summary: matched `NAFLD` in "We used Perturb-seq to characterize the role of putative NAFLD genes prioritized from molecular human genetic studies in differentiated HepaRG cells."
- GSE238219 / Series_overall_design: matched `NAFLD` in "dCas9-expressing HepaRG cells were harvested at Day 42 after transduction with lentiviral vectors carrying sgRNAs targeting multiple putative NAFLD genes in a pooled format. Cells were analysed using "
### single_cell_or_spatial (FAIL)
- GSM7660623 / Sample_extract_protocol_ch1: matched `10X` in "Library was prepared by the Stanford functional genomics core facility according to the manufacturers instruction (single cell 3' v2 protocol with feature barcodes for CRISPRi, 10X Genomics)."
- GSM7660624 / Sample_extract_protocol_ch1: matched `10X` in "Library was prepared by the Stanford functional genomics core facility according to the manufacturers instruction (single cell 3' v2 protocol with feature barcodes for CRISPRi, 10X Genomics)."
- GSM7660625 / Sample_extract_protocol_ch1: matched `10X` in "Library was prepared by the Stanford functional genomics core facility according to the manufacturers instruction (single cell 3' v2 protocol with feature barcodes for CRISPRi, 10X Genomics)."
- GSM7660626 / Sample_extract_protocol_ch1: matched `10X` in "Library was prepared by the Stanford functional genomics core facility according to the manufacturers instruction (single cell 3' v2 protocol with feature barcodes for CRISPRi, 10X Genomics)."
- GSM7660627 / Sample_extract_protocol_ch1: matched `10X` in "Library was prepared by the Stanford functional genomics core facility according to the manufacturers instruction (single cell 3' v2 protocol with feature barcodes for CRISPRi, 10X Genomics)."
- GSM7660623 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, barcode processing, gene counting and aggregation was carried out using Cell Ranger v. 6"
- GSM7660623 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: crispr_analysis generated from standard Cell Ranger v. 6 pipelines"
- GSM7660623 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: filtered feature bc matrices generated from standard Cell Ranger v.6 pipelines"
- GSM7660624 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, barcode processing, gene counting and aggregation was carried out using Cell Ranger v. 6"
- GSM7660624 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: crispr_analysis generated from standard Cell Ranger v. 6 pipelines"
- GSM7660624 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: filtered feature bc matrices generated from standard Cell Ranger v.6 pipelines"
- GSM7660625 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, barcode processing, gene counting and aggregation was carried out using Cell Ranger v. 6"
- GSM7660625 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: crispr_analysis generated from standard Cell Ranger v. 6 pipelines"
- GSM7660625 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: filtered feature bc matrices generated from standard Cell Ranger v.6 pipelines"
- GSM7660626 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, barcode processing, gene counting and aggregation was carried out using Cell Ranger v. 6"
- GSM7660626 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: crispr_analysis generated from standard Cell Ranger v. 6 pipelines"
- GSM7660626 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: filtered feature bc matrices generated from standard Cell Ranger v.6 pipelines"
- GSM7660627 / Sample_data_processing: matched `Cell Ranger` in "Demultiplexing, barcode processing, gene counting and aggregation was carried out using Cell Ranger v. 6"
- GSM7660627 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: crispr_analysis generated from standard Cell Ranger v. 6 pipelines"
- GSM7660627 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: filtered feature bc matrices generated from standard Cell Ranger v.6 pipelines"
- GSM7660623 / Sample_supplementary_file_2: matched `filtered_feature_bc_matrix` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM7660nnn/GSM7660623/suppl/GSM7660623_DIFF_HRG_P_Seq2_filtered_feature_bc_matrix.tar.gz"
- GSM7660624 / Sample_supplementary_file_2: matched `filtered_feature_bc_matrix` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM7660nnn/GSM7660624/suppl/GSM7660624_P_Seq2_filtered_feature_bc_matrix.tar.gz"
- GSM7660625 / Sample_supplementary_file_2: matched `filtered_feature_bc_matrix` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM7660nnn/GSM7660625/suppl/GSM7660625_PSG_1_filtered_feature_bc_matrix.tar.gz"
- GSM7660626 / Sample_supplementary_file_2: matched `filtered_feature_bc_matrix` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM7660nnn/GSM7660626/suppl/GSM7660626_PSG_2_filtered_feature_bc_matrix.tar.gz"
- GSM7660627 / Sample_supplementary_file_2: matched `filtered_feature_bc_matrix` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM7660nnn/GSM7660627/suppl/GSM7660627_PSG_3_filtered_feature_bc_matrix.tar.gz"
### material_type (WARN)
- GSM7660623 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG"
- GSM7660624 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG"
- GSM7660625 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG"
- GSM7660626 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG"
- GSM7660627 / Sample_source_name_ch1: matched `HepaRG` in "HepaRG"
- GSM7660623 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG"
- GSM7660624 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG"
- GSM7660625 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG"
- GSM7660626 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG"
- GSM7660627 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: 10X, Cell Ranger, filtered_feature_bc_matrix (5 sample(s)))
<!-- /computed -->