# Validation report: GSE107650

Low carbohydrate diet study for non-alcoholic fatty liver disease patients

<!-- computed -->
Sample count: 14

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 14 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 14/14 |
| source_tissue | PASS | liver-pattern source 14/14 |
| library_strategy | PASS | RNA-Seq 14/14 |
| library_source | PASS | transcriptomic 14/14 |
| library_selection | PASS | cDNA 14/14 |
| instrument_model | PASS | Illumina HiSeq 2500 14/14 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (14 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (14/14), packaged in GSE107650_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE107650_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX3441716, https://www.ncbi.nlm.nih.gov/sra?term=SRX3441717, https://www.ncbi.nlm.nih.gov/sra?term=SRX3441718, https://www.ncbi.nlm.nih.gov/sra?term=SRX3441719, https://www.ncbi.nlm.nih.gov/sra?term=SRX3441720, and 9 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: liver (14)

## Field presence

- subject id: 14/14
- subject status: 14/14
- time point: 14/14
- tissue: 14/14 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 14 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
<!-- /computed -->