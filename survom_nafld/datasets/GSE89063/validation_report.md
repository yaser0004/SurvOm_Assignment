# Validation report: GSE89063

Development of an In Vitro Human Liver System for Interrogating Non-Alcoholic Steatohepatitis

<!-- computed -->
Sample count: 17

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 17 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 17/17 |
| source_tissue | PASS | liver-pattern source 17/17 |
| library_strategy | PASS | RNA-Seq 17/17 |
| library_source | PASS | transcriptomic 17/17 |
| library_selection | PASS | cDNA 17/17 |
| instrument_model | PASS | Illumina HiSeq 2000 17/17 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (8 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | INFO | series prose mentions In Vitro, in vitro; sample metadata does not corroborate |
| expression_data_availability | PASS | processed series-level file: GSE89063_gene_counts.tsv.gz |
| series_matrix | INFO | present, metadata-only (GSE89063_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX2264036, https://www.ncbi.nlm.nih.gov/sra?term=SRX2264037, https://www.ncbi.nlm.nih.gov/sra?term=SRX2264038, https://www.ncbi.nlm.nih.gov/sra?term=SRX2264039, https://www.ncbi.nlm.nih.gov/sra?term=SRX2264040, and 12 more (see sample_metadata.csv) |

## Field presence

- cell type: 17/17
- media: 17/17

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 17 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
<!-- /computed -->