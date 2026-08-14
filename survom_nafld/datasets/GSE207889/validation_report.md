# Validation report: GSE207889

Stem cell-derived human liver organoids to model the progression of inflammatory and fibrotic injury in non-alcoholic fatty liver disease

<!-- computed -->
Sample count: 19

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 19 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 19/19 |
| source_tissue | PASS | liver-pattern source 19/19 |
| library_strategy | PASS | RNA-Seq 19/19 |
| library_source | WARN | library_source: transcriptomic single cell 19/19 |
| library_selection | PASS | cDNA 19/19 |
| instrument_model | WARN | mixed instruments: Illumina NovaSeq 6000 4/19, NextSeq 2000 15/19 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: .h5ad, 10x, Cell Ranger, barcodes.tsv, cellranger, features.tsv, matrix.mtx, scRNA (20 sample(s)) |
| material_type | WARN | cell/culture terms in sample metadata: cell line, organoid (19/19 samples) |
| expression_data_availability | PASS | processed per-sample counts (19/19), packaged in GSE207889_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE207889-GPL24676_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX16114846, https://www.ncbi.nlm.nih.gov/sra?term=SRX16114847, https://www.ncbi.nlm.nih.gov/sra?term=SRX16114848, https://www.ncbi.nlm.nih.gov/sra?term=SRX16114849, https://www.ncbi.nlm.nih.gov/sra?term=SRX16114850, and 14 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Human liver organoid (HLO) (19)
- **treatment**: Control-OA (2), Control-PA (2), Control-TGFB1 (2), None (7), OA 500 uM (2), PA 500 µM (2), TGF-B1 10 ng/ml (2)

## Field presence

- cell line: 19/19
- cell type: 19/19
- genotype: 19/19
- time: 19/19
- tissue: 19/19 (canon: tissue)
- treatment: 19/19 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### library_source (WARN)
### instrument_model (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE207889 / Series_title: matched `non-alcoholic fatty liver` in "Stem cell-derived human liver organoids to model the progression of inflammatory and fibrotic injury in non-alcoholic fatty liver disease"
- GSE207889 / Series_summary: matched `steatohepatitis` in "Chronic liver injury promotes fibrosis, which can progress to cirrhosis, a major cause of morbidity and mortality worldwide. Resolving the cell-type-specific transcriptional changes orchestrating this"
### single_cell_or_spatial (FAIL)
- GSM6322568 / Sample_extract_protocol_ch1: matched `10x` in "Library was performed according to the manufacter’s instructions (single cell 3’ v3 protocol, 10x Genomics)."
- GSM6322569 / Sample_extract_protocol_ch1: matched `10x` in "Library was performed according to the manufacter’s instructions (single cell 3’ v3 protocol, 10x Genomics)."
- GSM6322570 / Sample_extract_protocol_ch1: matched `10x` in "Library was performed according to the manufacter’s instructions (single cell 3’ v3 protocol, 10x Genomics)."
- GSM6322571 / Sample_extract_protocol_ch1: matched `10x` in "Library was performed according to the manufacter’s instructions (single cell 3’ v3 protocol, 10x Genomics)."
- GSM6322572 / Sample_extract_protocol_ch1: matched `10x` in "Library was performed according to the manufacter’s instructions (single cell 3’ v3 protocol, 10x Genomics)."
- GSM6322573 / Sample_extract_protocol_ch1: matched `10x` in "Library was performed according to the manufacter’s instructions (single cell 3’ v3 protocol, 10x Genomics)."
- GSM6322574 / Sample_extract_protocol_ch1: matched `10x` in "Library was performed according to the manufacter’s instructions (single cell 3’ v3 protocol, 10x Genomics)."
- GSM6322575 / Sample_extract_protocol_ch1: matched `10x` in "Library was performed according to the manufacter’s instructions (single cell 3’ v3 protocol, 10x Genomics)."
- GSM6322576 / Sample_extract_protocol_ch1: matched `10x` in "Library was performed according to the manufacter’s instructions (single cell 3’ v3 protocol, 10x Genomics)."
- GSM6322577 / Sample_extract_protocol_ch1: matched `10x` in "Library was performed according to the manufacter’s instructions (single cell 3’ v3 protocol, 10x Genomics)."
- GSM6322578 / Sample_extract_protocol_ch1: matched `10x` in "Library was performed according to the manufacter’s instructions (single cell 3’ v3 protocol, 10x Genomics)."
- GSM6322579 / Sample_extract_protocol_ch1: matched `10x` in "Library was performed according to the manufacter’s instructions (single cell 3’ v3 protocol, 10x Genomics)."
- GSM6322580 / Sample_extract_protocol_ch1: matched `10x` in "Library was performed according to the manufacter’s instructions (single cell 3’ v3 protocol, 10x Genomics)."
- GSM6900332 / Sample_extract_protocol_ch1: matched `10x` in "Library was performed according to the manufacturer’s instructions (single cell 3’ v3 protocol, 10x Genomics)."
- GSM6900333 / Sample_extract_protocol_ch1: matched `10x` in "Library was performed according to the manufacturer’s instructions (single cell 3’ v3 protocol, 10x Genomics)."
- GSM6900334 / Sample_extract_protocol_ch1: matched `10x` in "Library was performed according to the manufacturer’s instructions (single cell 3’ v3 protocol, 10x Genomics)."
- GSM6900335 / Sample_extract_protocol_ch1: matched `10x` in "Library was performed according to the manufacturer’s instructions (single cell 3’ v3 protocol, 10x Genomics)."
- GSM6900336 / Sample_extract_protocol_ch1: matched `10x` in "Library was performed according to the manufacturer’s instructions (single cell 3’ v3 protocol, 10x Genomics)."
- GSM6900337 / Sample_extract_protocol_ch1: matched `10x` in "Library was performed according to the manufacturer’s instructions (single cell 3’ v3 protocol, 10x Genomics)."
- GSM6322568 / Sample_data_processing: matched `cellranger` in "Raw bcl files were converted to fastq by the command bcl2fastq --use-bases-mask Y26,I8,Y98. Demultiplexing, barcoded processing, gene counting, aggregation and alignment to the GRCh38 genome was   per"
- GSM6322568 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6322569 / Sample_data_processing: matched `cellranger` in "Raw bcl files were converted to fastq by the command bcl2fastq --use-bases-mask Y26,I8,Y98. Demultiplexing, barcoded processing, gene counting, aggregation and alignment to the GRCh38 genome was   per"
- GSM6322569 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6322570 / Sample_data_processing: matched `cellranger` in "Raw bcl files were converted to fastq by the command bcl2fastq --use-bases-mask Y26,I8,Y98. Demultiplexing, barcoded processing, gene counting, aggregation and alignment to the GRCh38 genome was   per"
- GSM6322570 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6322571 / Sample_data_processing: matched `cellranger` in "Raw bcl files were converted to fastq by the command bcl2fastq --use-bases-mask Y26,I8,Y98. Demultiplexing, barcoded processing, gene counting, aggregation and alignment to the GRCh38 genome was   per"
- GSM6322571 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6322572 / Sample_data_processing: matched `cellranger` in "Raw bcl files were converted to fastq by the command bcl2fastq --use-bases-mask Y26,I8,Y98. Demultiplexing, barcoded processing, gene counting, aggregation and alignment to the GRCh38 genome was   per"
- GSM6322572 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6322573 / Sample_data_processing: matched `cellranger` in "Raw bcl files were converted to fastq by the command bcl2fastq --use-bases-mask Y26,I8,Y98. Demultiplexing, barcoded processing, gene counting, aggregation and alignment to the GRCh38 genome was   per"
- GSM6322573 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6322574 / Sample_data_processing: matched `cellranger` in "Raw bcl files were converted to fastq by the command bcl2fastq --use-bases-mask Y26,I8,Y98. Demultiplexing, barcoded processing, gene counting, aggregation and alignment to the GRCh38 genome was   per"
- GSM6322574 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6322575 / Sample_data_processing: matched `cellranger` in "Raw bcl files were converted to fastq by the command bcl2fastq --use-bases-mask Y26,I8,Y98. Demultiplexing, barcoded processing, gene counting, aggregation and alignment to the GRCh38 genome was   per"
- GSM6322575 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6322576 / Sample_data_processing: matched `cellranger` in "Raw bcl files were converted to fastq by the command bcl2fastq --use-bases-mask Y26,I8,Y98. Demultiplexing, barcoded processing, gene counting, aggregation and alignment to the GRCh38 genome was   per"
- GSM6322576 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6322577 / Sample_data_processing: matched `cellranger` in "Raw bcl files were converted to fastq by the command bcl2fastq --use-bases-mask Y26,I8,Y98. Demultiplexing, barcoded processing, gene counting, aggregation and alignment to the GRCh38 genome was   per"
- GSM6322577 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6322578 / Sample_data_processing: matched `cellranger` in "Raw bcl files were converted to fastq by the command bcl2fastq --use-bases-mask Y26,I8,Y98. Demultiplexing, barcoded processing, gene counting, aggregation and alignment to the GRCh38 genome was   per"
- GSM6322578 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6322579 / Sample_data_processing: matched `cellranger` in "Raw bcl files were converted to fastq by the command bcl2fastq --use-bases-mask Y26,I8,Y98. Demultiplexing, barcoded processing, gene counting, aggregation and alignment to the GRCh38 genome was   per"
- GSM6322579 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6322580 / Sample_data_processing: matched `cellranger` in "Raw bcl files were converted to fastq by the command bcl2fastq --use-bases-mask Y26,I8,Y98. Demultiplexing, barcoded processing, gene counting, aggregation and alignment to the GRCh38 genome was   per"
- GSM6322580 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)"
- GSM6900332 / Sample_data_processing: matched `cellranger` in "Raw bcl files were converted to fastq by the command bcl2fastq --use-bases-mask Y26,I8,Y98. Demultiplexing, barcoded processing, gene counting, aggregation and alignment to the GRCh38 genome was perfo"
- GSM6900332 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)."
- GSM6900333 / Sample_data_processing: matched `cellranger` in "Raw bcl files were converted to fastq by the command bcl2fastq --use-bases-mask Y26,I8,Y98. Demultiplexing, barcoded processing, gene counting, aggregation and alignment to the GRCh38 genome was perfo"
- GSM6900333 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)."
- GSM6900334 / Sample_data_processing: matched `cellranger` in "Raw bcl files were converted to fastq by the command bcl2fastq --use-bases-mask Y26,I8,Y98. Demultiplexing, barcoded processing, gene counting, aggregation and alignment to the GRCh38 genome was perfo"
- GSM6900334 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)."
- GSM6900335 / Sample_data_processing: matched `cellranger` in "Raw bcl files were converted to fastq by the command bcl2fastq --use-bases-mask Y26,I8,Y98. Demultiplexing, barcoded processing, gene counting, aggregation and alignment to the GRCh38 genome was perfo"
- GSM6900335 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)."
- GSM6900336 / Sample_data_processing: matched `cellranger` in "Raw bcl files were converted to fastq by the command bcl2fastq --use-bases-mask Y26,I8,Y98. Demultiplexing, barcoded processing, gene counting, aggregation and alignment to the GRCh38 genome was perfo"
- GSM6900336 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)."
- GSM6900337 / Sample_data_processing: matched `cellranger` in "Raw bcl files were converted to fastq by the command bcl2fastq --use-bases-mask Y26,I8,Y98. Demultiplexing, barcoded processing, gene counting, aggregation and alignment to the GRCh38 genome was perfo"
- GSM6900337 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Cell Ranger output files (barcodes.tsv, features.tsv, matrix.mtx)."
- GSM6322568 / Sample_title: matched `scRNA` in "Day 21 ULA-HLOs, replicate 1, scRNAseq"
- GSM6322569 / Sample_title: matched `scRNA` in "Day 21 ULA-HLOs, replicate 2, scRNAseq"
- GSM6322570 / Sample_title: matched `scRNA` in "Day 21 ULA-HLOs, replicate 3, scRNAseq"
- GSM6322571 / Sample_title: matched `scRNA` in "Day 34 ULA-HLOs, replicate 1, scRNAseq"
- GSM6322572 / Sample_title: matched `scRNA` in "Day 34 ULA-HLOs, replicate 2, scRNAseq"
- GSM6322573 / Sample_title: matched `scRNA` in "Control-for-TGFB1 day 25 OS-HLOs, replicate 1, scRNAseq"
- GSM6322574 / Sample_title: matched `scRNA` in "Control-for-TGFB1 day 25 OS-HLOs, replicate 2, scRNAseq"
- GSM6322575 / Sample_title: matched `scRNA` in "TGFB1-10ng/ml treated day 25 OS-HLOs, replicate 1, scRNAseq"
- GSM6322576 / Sample_title: matched `scRNA` in "TGFB1-10ng/ml treated day 25 OS-HLOs, replicate 2, scRNAseq"
- GSM6322577 / Sample_title: matched `scRNA` in "Control-for-PA day 25 OS-HLOs, replicate 1, scRNAseq"
- GSM6322578 / Sample_title: matched `scRNA` in "Control-for-PA day 25 OS-HLOs, replicate 2, scRNAseq"
- GSM6322579 / Sample_title: matched `scRNA` in "PA-500 µM treated day 25 OS-HLOs, replicate 1, scRNAseq"
- GSM6322580 / Sample_title: matched `scRNA` in "PA-500 µM treated day 25 OS-HLOs, replicate 2, scRNAseq"
- GSM6900332 / Sample_title: matched `scRNA` in "Day 25 OS-HLOs, replicate 1, scRNAseq"
- GSM6900333 / Sample_title: matched `scRNA` in "Day 25 OS-HLOs, replicate 2, scRNAseq"
- GSM6900334 / Sample_title: matched `scRNA` in "Control-for-OA day 25 OS-HLOs, replicate 1, scRNAseq"
- GSM6900335 / Sample_title: matched `scRNA` in "Control-for-OA day 25 OS-HLOs, replicate 2, scRNAseq"
- GSM6900336 / Sample_title: matched `scRNA` in "OA-500 µM treated day 25 OS-HLOs, replicate 1, scRNAseq"
- GSM6900337 / Sample_title: matched `scRNA` in "OA-500 µM treated day 25 OS-HLOs, replicate 2, scRNAseq"
- GSM6322568 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322568/suppl/GSM6322568_AmA-45_barcodes.tsv.gz"
- GSM6322568 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322568/suppl/GSM6322568_AmA-45_features.tsv.gz"
- GSM6322568 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322568/suppl/GSM6322568_AmA-45_matrix.mtx.gz"
- GSM6322569 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322569/suppl/GSM6322569_AmA-46_barcodes.tsv.gz"
- GSM6322569 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322569/suppl/GSM6322569_AmA-46_features.tsv.gz"
- GSM6322569 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322569/suppl/GSM6322569_AmA-46_matrix.mtx.gz"
- GSM6322570 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322570/suppl/GSM6322570_AmA-47_barcodes.tsv.gz"
- GSM6322570 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322570/suppl/GSM6322570_AmA-47_features.tsv.gz"
- GSM6322570 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322570/suppl/GSM6322570_AmA-47_matrix.mtx.gz"
- GSM6322571 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322571/suppl/GSM6322571_AmA-48_barcodes.tsv.gz"
- GSM6322571 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322571/suppl/GSM6322571_AmA-48_features.tsv.gz"
- GSM6322571 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322571/suppl/GSM6322571_AmA-48_matrix.mtx.gz"
- GSM6322572 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322572/suppl/GSM6322572_AmA-49_barcodes.tsv.gz"
- GSM6322572 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322572/suppl/GSM6322572_AmA-49_features.tsv.gz"
- GSM6322572 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322572/suppl/GSM6322572_AmA-49_matrix.mtx.gz"
- GSM6322573 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322573/suppl/GSM6322573_AmA-50_barcodes.tsv.gz"
- GSM6322573 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322573/suppl/GSM6322573_AmA-50_features.tsv.gz"
- GSM6322573 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322573/suppl/GSM6322573_AmA-50_matrix.mtx.gz"
- GSM6322574 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322574/suppl/GSM6322574_AmA-51_barcodes.tsv.gz"
- GSM6322574 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322574/suppl/GSM6322574_AmA-51_features.tsv.gz"
- GSM6322574 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322574/suppl/GSM6322574_AmA-51_matrix.mtx.gz"
- GSM6322575 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322575/suppl/GSM6322575_AmA-52_barcodes.tsv.gz"
- GSM6322575 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322575/suppl/GSM6322575_AmA-52_features.tsv.gz"
- GSM6322575 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322575/suppl/GSM6322575_AmA-52_matrix.mtx.gz"
- GSM6322576 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322576/suppl/GSM6322576_AmA-53_barcodes.tsv.gz"
- GSM6322576 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322576/suppl/GSM6322576_AmA-53_features.tsv.gz"
- GSM6322576 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322576/suppl/GSM6322576_AmA-53_matrix.mtx.gz"
- GSM6322577 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322577/suppl/GSM6322577_SM-KBV62_barcodes.tsv.gz"
- GSM6322577 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322577/suppl/GSM6322577_SM-KBV62_features.tsv.gz"
- GSM6322577 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322577/suppl/GSM6322577_SM-KBV62_matrix.mtx.gz"
- GSM6322578 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322578/suppl/GSM6322578_SM-KBV63_barcodes.tsv.gz"
- GSM6322578 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322578/suppl/GSM6322578_SM-KBV63_features.tsv.gz"
- GSM6322578 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322578/suppl/GSM6322578_SM-KBV63_matrix.mtx.gz"
- GSM6322579 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322579/suppl/GSM6322579_SM-KBV64_barcodes.tsv.gz"
- GSM6322579 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322579/suppl/GSM6322579_SM-KBV64_features.tsv.gz"
- GSM6322579 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322579/suppl/GSM6322579_SM-KBV64_matrix.mtx.gz"
- GSM6322580 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322580/suppl/GSM6322580_SM-KBV65_barcodes.tsv.gz"
- GSM6322580 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322580/suppl/GSM6322580_SM-KBV65_features.tsv.gz"
- GSM6322580 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6322nnn/GSM6322580/suppl/GSM6322580_SM-KBV65_matrix.mtx.gz"
- GSM6900332 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6900nnn/GSM6900332/suppl/GSM6900332_SM-L3XWE_barcodes.tsv.gz"
- GSM6900332 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6900nnn/GSM6900332/suppl/GSM6900332_SM-L3XWE_features.tsv.gz"
- GSM6900332 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6900nnn/GSM6900332/suppl/GSM6900332_SM-L3XWE_matrix.mtx.gz"
- GSM6900333 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6900nnn/GSM6900333/suppl/GSM6900333_SM-L3XWF_barcodes.tsv.gz"
- GSM6900333 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6900nnn/GSM6900333/suppl/GSM6900333_SM-L3XWF_features.tsv.gz"
- GSM6900333 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6900nnn/GSM6900333/suppl/GSM6900333_SM-L3XWF_matrix.mtx.gz"
- GSM6900334 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6900nnn/GSM6900334/suppl/GSM6900334_SM-L3XWG_barcodes.tsv.gz"
- GSM6900334 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6900nnn/GSM6900334/suppl/GSM6900334_SM-L3XWG_features.tsv.gz"
- GSM6900334 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6900nnn/GSM6900334/suppl/GSM6900334_SM-L3XWG_matrix.mtx.gz"
- GSM6900335 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6900nnn/GSM6900335/suppl/GSM6900335_SM-L3XWH_barcodes.tsv.gz"
- GSM6900335 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6900nnn/GSM6900335/suppl/GSM6900335_SM-L3XWH_features.tsv.gz"
- GSM6900335 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6900nnn/GSM6900335/suppl/GSM6900335_SM-L3XWH_matrix.mtx.gz"
- GSM6900336 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6900nnn/GSM6900336/suppl/GSM6900336_SM-L3XWI_barcodes.tsv.gz"
- GSM6900336 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6900nnn/GSM6900336/suppl/GSM6900336_SM-L3XWI_features.tsv.gz"
- GSM6900336 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6900nnn/GSM6900336/suppl/GSM6900336_SM-L3XWI_matrix.mtx.gz"
- GSM6900337 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6900nnn/GSM6900337/suppl/GSM6900337_SM-L3XWJ_barcodes.tsv.gz"
- GSM6900337 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6900nnn/GSM6900337/suppl/GSM6900337_SM-L3XWJ_features.tsv.gz"
- GSM6900337 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6900nnn/GSM6900337/suppl/GSM6900337_SM-L3XWJ_matrix.mtx.gz"
- GSE207889 / Series_supplementary_file: matched `.h5ad` in "ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE207nnn/GSE207889/suppl/GSE207889_day21.h5ad.gz"
- GSE207889 / Series_supplementary_file: matched `.h5ad` in "ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE207nnn/GSE207889/suppl/GSE207889_masld-hlos_merged.h5ad.gz"
- GSE207889 / Series_supplementary_file: matched `.h5ad` in "ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE207nnn/GSE207889/suppl/GSE207889_os.h5ad.gz"
### material_type (WARN)
- GSM6322568 / Sample_source_name_ch1: matched `organoid` in "Human liver organoid (HLO)"
- GSM6322569 / Sample_source_name_ch1: matched `organoid` in "Human liver organoid (HLO)"
- GSM6322570 / Sample_source_name_ch1: matched `organoid` in "Human liver organoid (HLO)"
- GSM6322571 / Sample_source_name_ch1: matched `organoid` in "Human liver organoid (HLO)"
- GSM6322572 / Sample_source_name_ch1: matched `organoid` in "Human liver organoid (HLO)"
- GSM6322573 / Sample_source_name_ch1: matched `organoid` in "Human liver organoid (HLO)"
- GSM6322574 / Sample_source_name_ch1: matched `organoid` in "Human liver organoid (HLO)"
- GSM6322575 / Sample_source_name_ch1: matched `organoid` in "Human liver organoid (HLO)"
- GSM6322576 / Sample_source_name_ch1: matched `organoid` in "Human liver organoid (HLO)"
- GSM6322577 / Sample_source_name_ch1: matched `organoid` in "Human liver organoid (HLO)"
- GSM6322578 / Sample_source_name_ch1: matched `organoid` in "Human liver organoid (HLO)"
- GSM6322579 / Sample_source_name_ch1: matched `organoid` in "Human liver organoid (HLO)"
- GSM6322580 / Sample_source_name_ch1: matched `organoid` in "Human liver organoid (HLO)"
- GSM6900332 / Sample_source_name_ch1: matched `organoid` in "Human liver organoid (HLO)"
- GSM6900333 / Sample_source_name_ch1: matched `organoid` in "Human liver organoid (HLO)"
- GSM6900334 / Sample_source_name_ch1: matched `organoid` in "Human liver organoid (HLO)"
- GSM6900335 / Sample_source_name_ch1: matched `organoid` in "Human liver organoid (HLO)"
- GSM6900336 / Sample_source_name_ch1: matched `organoid` in "Human liver organoid (HLO)"
- GSM6900337 / Sample_source_name_ch1: matched `organoid` in "Human liver organoid (HLO)"
- GSM6322568 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoid (HLO)"
- GSM6322568 / Sample_characteristics_ch1: matched `cell line` in "cell line: W01, WiCell"
- GSM6322569 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoid (HLO)"
- GSM6322569 / Sample_characteristics_ch1: matched `cell line` in "cell line: W01, WiCell"
- GSM6322570 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoid (HLO)"
- GSM6322570 / Sample_characteristics_ch1: matched `cell line` in "cell line: W01, WiCell"
- GSM6322571 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoid (HLO)"
- GSM6322571 / Sample_characteristics_ch1: matched `cell line` in "cell line: W01, WiCell"
- GSM6322572 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoid (HLO)"
- GSM6322572 / Sample_characteristics_ch1: matched `cell line` in "cell line: W01, WiCell"
- GSM6322573 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoid (HLO)"
- GSM6322573 / Sample_characteristics_ch1: matched `cell line` in "cell line: W01, WiCell"
- GSM6322574 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoid (HLO)"
- GSM6322574 / Sample_characteristics_ch1: matched `cell line` in "cell line: W01, WiCell"
- GSM6322575 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoid (HLO)"
- GSM6322575 / Sample_characteristics_ch1: matched `cell line` in "cell line: W01, WiCell"
- GSM6322576 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoid (HLO)"
- GSM6322576 / Sample_characteristics_ch1: matched `cell line` in "cell line: W01, WiCell"
- GSM6322577 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoid (HLO)"
- GSM6322577 / Sample_characteristics_ch1: matched `cell line` in "cell line: W01, WiCell"
- GSM6322578 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoid (HLO)"
- GSM6322578 / Sample_characteristics_ch1: matched `cell line` in "cell line: W01, WiCell"
- GSM6322579 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoid (HLO)"
- GSM6322579 / Sample_characteristics_ch1: matched `cell line` in "cell line: W01, WiCell"
- GSM6322580 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoid (HLO)"
- GSM6322580 / Sample_characteristics_ch1: matched `cell line` in "cell line: W01, WiCell"
- GSM6900332 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoid (HLO)"
- GSM6900332 / Sample_characteristics_ch1: matched `cell line` in "cell line: W01, WiCell"
- GSM6900333 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoid (HLO)"
- GSM6900333 / Sample_characteristics_ch1: matched `cell line` in "cell line: W01, WiCell"
- GSM6900334 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoid (HLO)"
- GSM6900334 / Sample_characteristics_ch1: matched `cell line` in "cell line: W01, WiCell"
- GSM6900335 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoid (HLO)"
- GSM6900335 / Sample_characteristics_ch1: matched `cell line` in "cell line: W01, WiCell"
- GSM6900336 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoid (HLO)"
- GSM6900336 / Sample_characteristics_ch1: matched `cell line` in "cell line: W01, WiCell"
- GSM6900337 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoid (HLO)"
- GSM6900337 / Sample_characteristics_ch1: matched `cell line` in "cell line: W01, WiCell"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: .h5ad, 10x, Cell Ranger, barcodes.tsv, cellranger, features.tsv, matrix.mtx, scRNA (20 sample(s)))
<!-- /computed -->