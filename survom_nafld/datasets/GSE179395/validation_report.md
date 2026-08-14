# Validation report: GSE179395

Butyrate protects against diet-induced liver fibrosis and suppresses non-canonical TGF-β signaling in human stellate cells

<!-- computed -->
Sample count: 22

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 22 samples |
| organism_consistency | PASS | Homo sapiens 22/22 |
| source_tissue | PASS | liver-pattern source 22/22 |
| library_strategy | PASS | RNA-Seq 22/22 |
| library_source | PASS | transcriptomic 22/22 |
| library_selection | PASS | cDNA 22/22 |
| instrument_model | PASS | Illumina NovaSeq 6000 22/22 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (22/22), packaged in GSE179395_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE179395_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX11346882, https://www.ncbi.nlm.nih.gov/sra?term=SRX11346883, https://www.ncbi.nlm.nih.gov/sra?term=SRX11346884, https://www.ncbi.nlm.nih.gov/sra?term=SRX11346885, https://www.ncbi.nlm.nih.gov/sra?term=SRX11346886, and 17 more (see sample_metadata.csv) |

## Field presence

- treatm_4day_full_info: 22/22
- treatm_code: 22/22

## Evidence for WARN/FAIL checks

### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE179395 / Series_summary: matched `steatohepatitis` in "Background & Aims: In obesity-associated non-alcoholic steatohepatitis (NASH), persistent hepatocellular damage and inflammation are key drivers of fibrosis, the main determinant of NASH-associated mo"

Decision: MANUAL_REVIEW

Reasons:
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
<!-- /computed -->