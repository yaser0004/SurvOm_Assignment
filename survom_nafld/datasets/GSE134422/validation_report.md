# Validation report: GSE134422

HNF4α nuclear localization correlates with the clinical progression of terminal hepatic failure in humans

<!-- computed -->
Sample count: 7

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 7 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 7/7 |
| source_tissue | PASS | liver-pattern source 7/7 |
| library_strategy | PASS | RNA-Seq 7/7 |
| library_source | PASS | transcriptomic 7/7 |
| library_selection | PASS | cDNA 7/7 |
| instrument_model | PASS | Illumina NextSeq 500 7/7 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (2 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX6456985, https://www.ncbi.nlm.nih.gov/sra?term=SRX6456986, https://www.ncbi.nlm.nih.gov/sra?term=SRX6456987, https://www.ncbi.nlm.nih.gov/sra?term=SRX6456988, https://www.ncbi.nlm.nih.gov/sra?term=SRX6456989, and 2 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE134422_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX6456985, https://www.ncbi.nlm.nih.gov/sra?term=SRX6456986, https://www.ncbi.nlm.nih.gov/sra?term=SRX6456987, https://www.ncbi.nlm.nih.gov/sra?term=SRX6456988, https://www.ncbi.nlm.nih.gov/sra?term=SRX6456989, and 2 more (see sample_metadata.csv) |

## Field presence

- cell type: 7/7
- individual: 7/7

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 7 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
<!-- /computed -->