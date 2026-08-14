# Validation report: GSE269412

The transcription factor ZNF469 regulates collagen production in liver fibrosis [RNA-Seq liver]

<!-- computed -->
Sample count: 262

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 262 samples |
| organism_consistency | PASS | Homo sapiens 262/262 |
| source_tissue | PASS | liver-pattern source 262/262 |
| library_strategy | PASS | RNA-Seq 262/262 |
| library_source | PASS | transcriptomic 262/262 |
| library_selection | PASS | cDNA 262/262 |
| instrument_model | PASS | Illumina NovaSeq 6000 262/262 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX24829193, https://www.ncbi.nlm.nih.gov/sra?term=SRX24829194, https://www.ncbi.nlm.nih.gov/sra?term=SRX24829195, https://www.ncbi.nlm.nih.gov/sra?term=SRX24829196, https://www.ncbi.nlm.nih.gov/sra?term=SRX24829197, and 257 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE269412_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX24829193, https://www.ncbi.nlm.nih.gov/sra?term=SRX24829194, https://www.ncbi.nlm.nih.gov/sra?term=SRX24829195, https://www.ncbi.nlm.nih.gov/sra?term=SRX24829196, https://www.ncbi.nlm.nih.gov/sra?term=SRX24829197, and 257 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Liver (262)

## Field presence

- tissue: 262/262 (canon: tissue)

## Evidence for WARN/FAIL checks

### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE269412 / Series_summary: matched `Non-alcoholic fatty liver` in "Non-alcoholic fatty liver disease (NAFLD)—characterized by excess accumulation of fat in the liver—now affects one third of the world’s population. As NAFLD progresses, extracellular matrix components"

Decision: MANUAL_REVIEW

Reasons:
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
<!-- /computed -->