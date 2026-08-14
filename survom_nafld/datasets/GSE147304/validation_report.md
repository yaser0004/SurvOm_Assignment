# Validation report: GSE147304

RNA-Seq analylsis of human NASH and Normal liver tissues

<!-- computed -->
Sample count: 10

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 10 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 10/10 |
| source_tissue | PASS | liver-pattern source 10/10 |
| library_strategy | PASS | RNA-Seq 10/10 |
| library_source | PASS | transcriptomic 10/10 |
| library_selection | PASS | cDNA 10/10 |
| instrument_model | PASS | HiSeq X Ten 10/10 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (10 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE147304_gene_expression.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE147304_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX7963120, https://www.ncbi.nlm.nih.gov/sra?term=SRX7963121, https://www.ncbi.nlm.nih.gov/sra?term=SRX7963122, https://www.ncbi.nlm.nih.gov/sra?term=SRX7963123, https://www.ncbi.nlm.nih.gov/sra?term=SRX7963124, and 5 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: liver tissue (10)

## Field presence

- tissue: 10/10 (canon: tissue)
- with nash: 10/10

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 10 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
<!-- /computed -->