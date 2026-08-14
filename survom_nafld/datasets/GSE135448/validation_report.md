# Validation report: GSE135448

High- and low-protein diet: effects on human hepatic fat content, autophagy, mitochondrial function and fat metabolism

<!-- computed -->
Sample count: 19

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 19 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 19/19 |
| source_tissue | PASS | liver-pattern source 19/19 |
| library_strategy | PASS | RNA-Seq 19/19 |
| library_source | PASS | transcriptomic 19/19 |
| library_selection | PASS | cDNA 19/19 |
| instrument_model | PASS | Illumina HiSeq 4000 19/19 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE135448_Diff_Expression_LPvsHP.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE135448_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX6660008, https://www.ncbi.nlm.nih.gov/sra?term=SRX6660009, https://www.ncbi.nlm.nih.gov/sra?term=SRX6660010, https://www.ncbi.nlm.nih.gov/sra?term=SRX6660011, https://www.ncbi.nlm.nih.gov/sra?term=SRX6660012, and 14 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Liver (19)

## Field presence

- diet intervention: 19/19
- tissue: 19/19 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE135448 / Series_summary: matched `Non-alcoholic fatty liver` in "Non-alcoholic fatty liver disease (NAFLD) is becoming increasingly prevalent and nutrition intervention remains the most important therapeutic approach for NAFLD. Our aim was to investigate whether lo"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 19 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
<!-- /computed -->