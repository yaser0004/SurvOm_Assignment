# Validation report: GSE129933

Chronic Liver Disease in Humans Causes Expansion and Differentiation of Liver Lymphatic Endothelial Cells

<!-- computed -->
Sample count: 4

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 4 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 4/4 |
| source_tissue | PASS | liver-pattern source 4/4 |
| library_strategy | PASS | RNA-Seq 4/4 |
| library_source | PASS | transcriptomic 4/4 |
| library_selection | PASS | cDNA 4/4 |
| instrument_model | WARN | mixed instruments: Illumina HiSeq 4000 2/4, Illumina NovaSeq 6000 2/4 |
| metadata_completeness | PASS | reported consistently: disease, tissue; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (1 sample(s)) |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: 10x, Seurat (4 sample(s)) |
| material_type | INFO | series prose mentions in vitro; sample metadata does not corroborate |
| expression_data_availability | PASS | processed series-level file: GSE129933_count_matrix.tsv.gz |
| series_matrix | INFO | present, metadata-only (GSE129933-GPL20301_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX5702672, https://www.ncbi.nlm.nih.gov/sra?term=SRX5702673, https://www.ncbi.nlm.nih.gov/sra?term=SRX5702674, https://www.ncbi.nlm.nih.gov/sra?term=SRX5702675 |

## Canonical field distributions

- **disease**: HCV (1), NASH (1), Non-diseased (2)
- **tissue**: liver (4)

## Field presence

- cell type: 4/4
- disease state: 4/4 (canon: disease)
- tissue: 4/4 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### instrument_model (WARN)
### single_cell_or_spatial (FAIL)
- GSM3728304 / Sample_extract_protocol_ch1: matched `10x` in "To enrich LECs from hepatic NPCs we thawed frozen samples in RPMI containing 10% Human Serum AB (Gemini Bio-products, West Sacramento, CA) and 1% DNASE (MP Biomedicals, Santa Ana, CA). Cells were wash"
- GSM3728304 / Sample_extract_protocol_ch1: matched `10x` in "10x Genomics 3' end library kit"
- GSM3728305 / Sample_extract_protocol_ch1: matched `10x` in "To enrich LECs from hepatic NPCs we thawed frozen samples in RPMI containing 10% Human Serum AB (Gemini Bio-products, West Sacramento, CA) and 1% DNASE (MP Biomedicals, Santa Ana, CA). Cells were wash"
- GSM3728305 / Sample_extract_protocol_ch1: matched `10x` in "10x Genomics 3' end library kit"
- GSM3728306 / Sample_extract_protocol_ch1: matched `10x` in "To enrich LECs from hepatic NPCs we thawed frozen samples in RPMI containing 10% Human Serum AB (Gemini Bio-products, West Sacramento, CA) and 1% DNASE (MP Biomedicals, Santa Ana, CA). Cells were wash"
- GSM3728306 / Sample_extract_protocol_ch1: matched `10x` in "10x Genomics 3' end library kit"
- GSM3728307 / Sample_extract_protocol_ch1: matched `10x` in "To enrich LECs from hepatic NPCs we thawed frozen samples in RPMI containing 10% Human Serum AB (Gemini Bio-products, West Sacramento, CA) and 1% DNASE (MP Biomedicals, Santa Ana, CA). Cells were wash"
- GSM3728307 / Sample_extract_protocol_ch1: matched `10x` in "10x Genomics 3' end library kit"
- GSM3728304 / Sample_data_processing: matched `10x` in "UMI count matrices were generated using the 10x genomics CellRanger count (3.0.1) pipeline with default parameters."
- GSM3728304 / Sample_data_processing: matched `Seurat` in "The count matrices were combined and normalized using Seurat."
- GSM3728305 / Sample_data_processing: matched `10x` in "UMI count matrices were generated using the 10x genomics CellRanger count (3.0.1) pipeline with default parameters."
- GSM3728305 / Sample_data_processing: matched `Seurat` in "The count matrices were combined and normalized using Seurat."
- GSM3728306 / Sample_data_processing: matched `10x` in "UMI count matrices were generated using the 10x genomics CellRanger count (3.0.1) pipeline with default parameters."
- GSM3728306 / Sample_data_processing: matched `Seurat` in "The count matrices were combined and normalized using Seurat."
- GSM3728307 / Sample_data_processing: matched `10x` in "UMI count matrices were generated using the 10x genomics CellRanger count (3.0.1) pipeline with default parameters."
- GSM3728307 / Sample_data_processing: matched `Seurat` in "The count matrices were combined and normalized using Seurat."

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: 10x, Seurat (4 sample(s)))
<!-- /computed -->