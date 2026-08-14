# Validation report: GSE256398

Hepatic stellate cells control liver zonation and function via R-spondin 3

<!-- computed -->
Sample count: 30

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 30 samples |
| organism_consistency | WARN | mixed organisms: Homo sapiens 26/30, Mus musculus 4/30 |
| source_tissue | PASS | liver-pattern source 30/30 |
| library_strategy | PASS | RNA-Seq 30/30 |
| library_source | WARN | library_source: transcriptomic single cell 30/30 |
| library_selection | PASS | cDNA 30/30 |
| instrument_model | WARN | mixed instruments: Illumina NovaSeq 6000 28/30, Illumina NovaSeq X 2/30 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (11 sample(s)) |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: 10x, Cellranger, Chromium (30 sample(s)) |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (30/30), packaged in GSE256398_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE256398-GPL24247_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX23708051, https://www.ncbi.nlm.nih.gov/sra?term=SRX23708052, https://www.ncbi.nlm.nih.gov/sra?term=SRX23708053, https://www.ncbi.nlm.nih.gov/sra?term=SRX23708054, https://www.ncbi.nlm.nih.gov/sra?term=SRX23708055, and 25 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 20 year-old (1), 23 year-old (1), 26 year-old (1), 29 year-old (1), 31 year-old (1), 34 year-old (2), 35 year-old (2), 37 year-old (1), 41 year-old (1), 42 year-old (1), 45 year-old (2), 48 year-old (2), 49 year-old (1), 52 year-old (1), 56 year-old (1), 58 year-old (1), 61 year-old (1), 62 year-old (1), 65 year-old (1), 7 weeks old (1), 70 year-old (1), 71 year-old (1), 8 weeks old (1), 80 year-old (1)
- **sex**: female (11), male (17)
- **tissue**: Liver (28), liver (2)

## Field presence

- Sex: 28/30 (canon: sex)
- age: 28/30 (canon: age)
- cell type: 28/30
- genotype: 4/30
- tissue: 30/30 (canon: tissue)

## Evidence for WARN/FAIL checks

### organism_consistency (WARN)
### library_source (WARN)
### instrument_model (WARN)
### metadata_completeness (WARN)
### single_cell_or_spatial (FAIL)
- GSM8097071 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097072 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097073 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097074 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097075 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097076 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097077 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097078 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097079 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097080 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097081 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097082 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097083 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097084 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097085 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097086 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097087 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097088 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097089 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097090 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097091 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097092 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097093 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097094 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097095 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097096 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8648657 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8648658 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8812541 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8812542 / Sample_extract_protocol_ch1: matched `Chromium` in "Single-cell RNA-seq libraries were prepared using the Chromium Single Cell 5′ v2 Reagent Kit (10x Genomics) according to manufacturer’s instructions, 12 cycles of cDNA amplification and 12 cycles of l"
- GSM8097071 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097071 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097072 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097072 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097073 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097073 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097074 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097074 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097075 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097075 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097076 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097076 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097077 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097077 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097078 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097078 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097079 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097079 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097080 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097080 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097081 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097081 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097082 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097082 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097083 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097083 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097084 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097084 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097085 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097085 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097086 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097086 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097087 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097087 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097088 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097088 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097089 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097089 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097090 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097090 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097091 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097091 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097092 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097092 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097093 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097093 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097094 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097094 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097095 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097095 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8097096 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8097096 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8648657 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8648657 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8648658 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8648658 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8812541 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8812541 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."
- GSM8812542 / Sample_data_processing: matched `Cellranger` in "Cellranger software (v2.0.0) for human samples and cell ranger (v8.0.1) for mice sample was used to process the data."
- GSM8812542 / Sample_data_processing: matched `10x` in "BCL files were demultiplexed with 10x Cell Ranger's mkfastq command and analysis and alignment were performed using Cell Ranger's count command with Cell Ranger's reference mm10 (mouse)."

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: 10x, Cellranger, Chromium (30 sample(s)))
<!-- /computed -->