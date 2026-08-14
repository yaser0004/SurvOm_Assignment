# Validation report: GSE134146

circRNA expression profiles of fibroblasts: normal vs. NASH cirrhosis

<!-- computed -->
Sample count: 8

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 8 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 8/8 |
| source_tissue | PASS | liver-pattern source 8/8 |
| library_strategy | FAIL | no expression-profiling strategy found (none reported) |
| library_source | WARN | library_source: unreported 8/8 |
| library_selection | PASS |  8/8 |
| instrument_model | INFO | instrument model not reported |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (8 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE134146_quantile.txt.gz |
| series_matrix | PASS | present with expression data: GSE134146_series_matrix.txt.gz |
| raw_sra_availability | INFO | no SRA/raw sequencing links found |

## Canonical field distributions

- **tissue**: NASH cirrhosis Liver (4), Normal Liver (4)

## Field presence

- tissue: 8/8 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### library_strategy (FAIL)
### library_source (WARN)
### metadata_completeness (WARN)

Decision: REJECT

Reasons:
- library_strategy: no expression-profiling samples (no expression-profiling strategy found (none reported))
<!-- /computed -->