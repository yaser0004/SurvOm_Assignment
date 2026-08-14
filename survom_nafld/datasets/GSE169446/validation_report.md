# Validation report: GSE169446

XCR1+ type 1 conventional dendritic cells drive liver pathology in Non-Alcoholic Steatohepatitis [10x scRNA-seq]

<!-- computed -->
Sample count: 2

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 2 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 2/2 |
| source_tissue | WARN | liver-pattern source 0/2 |
| library_strategy | PASS | RNA-Seq 2/2 |
| library_source | PASS | transcriptomic 2/2 |
| library_selection | PASS | cDNA 2/2 |
| instrument_model | PASS | Illumina NovaSeq 6000 2/2 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (1 sample(s)) |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: 10x, Single cell suspension, barcodes.tsv, cellranger, features.tsv, matrix.mtx (2 sample(s)) |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (2/2), packaged in GSE169446_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE169446_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX10421418, https://www.ncbi.nlm.nih.gov/sra?term=SRX10421419 |

## Canonical field distributions

- **age**: mixed samples from multple patients (2)
- **sex**: pooled male and female (2)

## Field presence

- Sex: 2/2 (canon: sex)
- age: 2/2 (canon: age)
- cell type: 2/2
- clinic status: 2/2
- clinical outcome: 2/2
- sofa score: 2/2

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
### metadata_completeness (WARN)
### single_cell_or_spatial (FAIL)
- GSM5203285 / Sample_extract_protocol_ch1: matched `Single cell suspension` in "Liver biopsies from bariatric surgery patients were collected in RPMI (Supplemented with 10%FBS) and immediately transported on ice to the laboratory. A section of tissue was formalin fixed for histop"
- GSM5203285 / Sample_extract_protocol_ch1: matched `10x` in "10x v.3; Single cell RNA-seq 3’ : 28bp R1 and 91 bp R2"
- GSM5203286 / Sample_extract_protocol_ch1: matched `Single cell suspension` in "Liver biopsies from bariatric surgery patients were collected in RPMI (Supplemented with 10%FBS) and immediately transported on ice to the laboratory. A section of tissue was formalin fixed for histop"
- GSM5203286 / Sample_extract_protocol_ch1: matched `10x` in "10x v.3; Single cell RNA-seq 3’ : 28bp R1 and 91 bp R2"
- GSM5203285 / Sample_data_processing: matched `10x` in "10x genomics pipeline"
- GSM5203285 / Sample_data_processing: matched `cellranger` in "Genome_build: refdata-cellranger-GRCh38-1.2.0.tar.gz"
- GSM5203286 / Sample_data_processing: matched `10x` in "10x genomics pipeline"
- GSM5203286 / Sample_data_processing: matched `cellranger` in "Genome_build: refdata-cellranger-GRCh38-1.2.0.tar.gz"
- GSM5203285 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5203nnn/GSM5203285/suppl/GSM5203285_NASH_DC_barcodes.tsv.gz"
- GSM5203285 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5203nnn/GSM5203285/suppl/GSM5203285_NASH_DC_features.tsv.gz"
- GSM5203285 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5203nnn/GSM5203285/suppl/GSM5203285_NASH_DC_matrix.mtx.gz"
- GSM5203286 / Sample_supplementary_file_1: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5203nnn/GSM5203286/suppl/GSM5203286_CONTROL_DC_barcodes.tsv.gz"
- GSM5203286 / Sample_supplementary_file_2: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5203nnn/GSM5203286/suppl/GSM5203286_CONTROL_DC_features.tsv.gz"
- GSM5203286 / Sample_supplementary_file_3: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5203nnn/GSM5203286/suppl/GSM5203286_CONTROL_DC_matrix.mtx.gz"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: 10x, Single cell suspension, barcodes.tsv, cellranger, features.tsv, matrix.mtx (2 sample(s)))
<!-- /computed -->