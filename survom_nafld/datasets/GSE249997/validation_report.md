# Validation report: GSE249997

Liver dysfunction in obesity is associated with cerebrovascular health independently of diabetes and hypertension.

<!-- computed -->
Sample count: 77

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 77 samples |
| organism_consistency | PASS | Homo sapiens 77/77 |
| source_tissue | PASS | liver-pattern source 77/77 |
| library_strategy | PASS | RNA-Seq 77/77 |
| library_source | PASS | transcriptomic 77/77 |
| library_selection | PASS | cDNA 77/77 |
| instrument_model | PASS | Illumina NovaSeq 6000 77/77 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (77 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (77/77), packaged in GSE249997_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE249997_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX22870099, https://www.ncbi.nlm.nih.gov/sra?term=SRX22870100, https://www.ncbi.nlm.nih.gov/sra?term=SRX22870101, https://www.ncbi.nlm.nih.gov/sra?term=SRX22870102, https://www.ncbi.nlm.nih.gov/sra?term=SRX22870103, and 72 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: middle aged (77)
- **tissue**: liver (77)

## Field presence

- age: 77/77 (canon: age)
- brainparameters: 77/77
- liverbraincorrset68samp: 77/77
- refset11samp: 77/77
- refset14samp: 77/77
- subject id: 77/77
- subject status: 77/77
- tissue: 77/77 (canon: tissue)

## Evidence for WARN/FAIL checks

### metadata_completeness (WARN)

Decision: MANUAL_REVIEW

Reasons:
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
<!-- /computed -->