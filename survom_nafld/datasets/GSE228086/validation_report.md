# Validation report: GSE228086

Hepatic Stellate Cell Activation after 72hr

<!-- computed -->
Sample count: 12

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 12 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 12/12 |
| source_tissue | PASS | liver-pattern source 12/12 |
| library_strategy | PASS | RNA-Seq 12/12 |
| library_source | PASS | transcriptomic 12/12 |
| library_selection | PASS | cDNA 12/12 |
| instrument_model | PASS | Illumina HiSeq 2000 12/12 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | INFO | series prose mentions in vitro; sample metadata does not corroborate |
| expression_data_availability | PASS | processed series-level file: GSE228086_HSC_counts.csv.gz |
| series_matrix | INFO | present, metadata-only (GSE228086_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX19758713, https://www.ncbi.nlm.nih.gov/sra?term=SRX19758714, https://www.ncbi.nlm.nih.gov/sra?term=SRX19758715, https://www.ncbi.nlm.nih.gov/sra?term=SRX19758716, https://www.ncbi.nlm.nih.gov/sra?term=SRX19758717, and 7 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: liver (12)
- **treatment**: IL13_10ng_per_ml (3), TGFB1_5ng_per_ml (3), TNFA_20ng_per_ml (3), Unstimulated control (3)

## Field presence

- cell type: 12/12
- tissue: 12/12 (canon: tissue)
- treatment: 12/12 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE228086 / Series_summary: matched `steatohepatitis` in "Chronic liver diseases as non-alcoholic steatohepatitis (NASH)-induced cirrhosis are characterized by an increasing accumulation of stressed, damaged, or dying hepatocytes. Hepatocyte damage triggers "

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 12 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
<!-- /computed -->