# Validation report: GSE313271

S100A10-ANXA2 TETRAMER INHIBITION HAMPERS HEPATIC STELLATE CELL ACTIVATION IN MASLD MODELING HUMAN LIVER ORGANOIDS

<!-- computed -->
Sample count: 1

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 1 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 1/1 |
| source_tissue | PASS | liver-pattern source 1/1 |
| library_strategy | PASS | RNA-Seq 1/1 |
| library_source | WARN | library_source: transcriptomic single cell 1/1 |
| library_selection | PASS | cDNA 1/1 |
| instrument_model | PASS | Illumina NovaSeq 6000 1/1 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: 10x, Cell Ranger, Chromium, Seurat, features.tsv, single-cell suspension (1 sample(s)) |
| material_type | WARN | cell/culture terms in sample metadata: cell line, organoid (1/1 samples) |
| expression_data_availability | PASS | processed per-sample counts (1/1), packaged in GSE313271_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE313271_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX31424383 |

## Canonical field distributions

- **tissue**: Human liver organoid (HLO) (1)

## Field presence

- cell line: 1/1
- cell type: 1/1
- tissue: 1/1 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### library_source (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE313271 / Series_title: matched `MASLD` in "S100A10-ANXA2 TETRAMER INHIBITION HAMPERS HEPATIC STELLATE CELL ACTIVATION IN MASLD MODELING HUMAN LIVER ORGANOIDS"
- GSE313271 / Series_summary: matched `Metabolic dysfunction-associated stea` in "Metabolic dysfunction-associated steatotic liver disease (MASLD), which begins with the pathological lipid accumulation within hepatocytes, can progress to metabolic dysfunction-associated steatohepat"
### single_cell_or_spatial (FAIL)
- GSM9365059 / Sample_extract_protocol_ch1: matched `single-cell suspension` in "On D21, HLOs from three wells of an ultra-low attachment 24-well plate were collected and washed 2x with DPBS (-/-). The HLOs were then dissociated using TrypLE Express for 15 minutes at 37 °C. Follow"
- GSM9365059 / Sample_extract_protocol_ch1: matched `Chromium` in "The 10× Genomics Chromium equipment and the 3′v3.1 reagent kit were used to create single-cell RNA-Seq libraries in accordance with the manufacturer's instructions. A Qubit fluorometer (ThermoFisher S"
- GSM9365059 / Sample_data_processing: matched `Cell Ranger` in "Raw sequencing data were processed with Cell Ranger v7.2.0 using the GRCh38-2020-A reference to generate filtered gene–cell count matrices."
- GSM9365059 / Sample_data_processing: matched `Seurat` in "Quality control was performed in Seurat, removing genes expressed in fewer than 3 cells and cells with fewer than 200 detected genes. Cells were retained if they contained ≥40,000 UMIs and ≤20% mitoch"
- GSM9365059 / Sample_data_processing: matched `10x` in "Assembly: GRCh38 (GRCh38-2020-A, 10x Genomics reference)"
- GSM9365059 / Sample_data_processing: matched `Cell Ranger` in "Supplementary files format and content: Filtered gene–cell count matrices output by Cell Ranger are provided in Matrix Market format (matrix.mtx, barcodes.tsv, features.tsv)."
- GSM9365059 / Sample_supplementary_file_3: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM9365nnn/GSM9365059/suppl/GSM9365059_features.tsv.gz"
### material_type (WARN)
- GSM9365059 / Sample_source_name_ch1: matched `organoid` in "Human liver organoid (HLO)"
- GSM9365059 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoid (HLO)"
- GSM9365059 / Sample_characteristics_ch1: matched `cell line` in "cell line: hESCs, HS420, BAG-hES-IMP-0046"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: 10x, Cell Ranger, Chromium, Seurat, features.tsv, single-cell suspension (1 sample(s)))
<!-- /computed -->