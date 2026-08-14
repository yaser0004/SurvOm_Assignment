# Validation report: GSE208413

EXCESSIVE INFLAMMATION DRIVES POSTOPERATIVE LIVER FAILURE IN HUMANS - mRNA datasets

<!-- computed -->
Sample count: 57

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 57 samples |
| organism_consistency | PASS | Homo sapiens 57/57 |
| source_tissue | PASS | liver-pattern source 57/57 |
| library_strategy | PASS | RNA-Seq 57/57 |
| library_source | PASS | transcriptomic 57/57 |
| library_selection | PASS | cDNA 57/57 |
| instrument_model | PASS | Illumina NovaSeq 6000 57/57 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | WARN | series prose mentions spatial transcriptom; sample metadata does not corroborate |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE208413_mRNA_counts.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE208413_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX16318975, https://www.ncbi.nlm.nih.gov/sra?term=SRX16318976, https://www.ncbi.nlm.nih.gov/sra?term=SRX16318977, https://www.ncbi.nlm.nih.gov/sra?term=SRX16318978, https://www.ncbi.nlm.nih.gov/sra?term=SRX16318979, and 52 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: liver | ATROPHIE1 (3), liver | ATROPHIE2 (3), liver | POST (21), liver | PRE (24), liver | REG1 (3), liver | REG2 (3)

## Field presence

- sample type: 57/57 (canon: tissue)
- tissue: 57/57 (canon: tissue)

## Evidence for WARN/FAIL checks

### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE208413 / Series_summary: matched `NASH` in "While extensive experimental evidence on rodent liver regeneration (LR) exists, in human LR is poorly understood as underlying liver disease significantly complicates this process. Within our analyses"
### single_cell_or_spatial (WARN)
- GSE208413 / Series_summary: matched `spatial transcriptom` in "While extensive experimental evidence on rodent liver regeneration (LR) exists, in human LR is poorly understood as underlying liver disease significantly complicates this process. Within our analyses"

Decision: MANUAL_REVIEW

Reasons:
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- single_cell_or_spatial: series prose mentions spatial transcriptom; sample metadata does not corroborate
<!-- /computed -->