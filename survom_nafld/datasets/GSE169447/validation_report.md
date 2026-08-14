# Validation report: GSE169447

XCR1+ type 1 conventional dendritic cells drive liver pathology in Non-Alcoholic Steatohepatitis.

<!-- computed -->
Sample count: 122

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 122 samples |
| organism_consistency | WARN | mixed organisms: Homo sapiens 2/122, Mus musculus 120/122 |
| source_tissue | WARN | liver-pattern source 108/122 |
| library_strategy | PASS | RNA-Seq 122/122 |
| library_source | PASS | transcriptomic 122/122 |
| library_selection | PASS | cDNA 122/122 |
| instrument_model | WARN | mixed instruments: Illumina NextSeq 500 86/122, Illumina NovaSeq 6000 36/122 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (1 sample(s)) |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: 10x, Single cell suspension, barcodes.tsv, cellranger, features.tsv, matrix.mtx (2 sample(s)) |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (2/122), packaged in GSE169447_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE169447-GPL19057_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX10421418, https://www.ncbi.nlm.nih.gov/sra?term=SRX10421419, https://www.ncbi.nlm.nih.gov/sra?term=SRX10421432, https://www.ncbi.nlm.nih.gov/sra?term=SRX10421433, https://www.ncbi.nlm.nih.gov/sra?term=SRX10421434, and 117 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: mixed samples from multple patients (2)
- **sex**: pooled male and female (2)
- **tissue**: Blood (4), Bone marrow (8), liver (74), liver lymph nodes (34)

## Field presence

- Sex: 2/122 (canon: sex)
- age: 2/122 (canon: age)
- cell type: 122/122
- clinic status: 2/122
- clinical outcome: 2/122
- infection: 120/122
- selection marker: 120/122
- sofa score: 2/122
- strain: 120/122
- time point: 120/122
- tissue: 120/122 (canon: tissue)
- treatment(1): 120/122

## Evidence for WARN/FAIL checks

### organism_consistency (WARN)
### source_tissue (WARN)
### instrument_model (WARN)
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