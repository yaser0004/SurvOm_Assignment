# Validation report: GSE317876

A multi-stage transcriptomic resource of Artemisitene (ATT) for enhancing liver organoid functionality and treating metabolic liver disease.

<!-- computed -->
Sample count: 21

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 21 samples |
| organism_consistency | PASS | Homo sapiens 21/21 |
| source_tissue | WARN | liver-pattern source 0/21 |
| library_strategy | PASS | RNA-Seq 21/21 |
| library_source | PASS | transcriptomic 21/21 |
| library_selection | PASS | cDNA 21/21 |
| instrument_model | PASS | Illumina NovaSeq 6000 21/21 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | INFO | series prose mentions organoid; sample metadata does not corroborate |
| expression_data_availability | PASS | processed series-level file: GSE317876_FFA_rawcounts.xls.gz |
| series_matrix | INFO | present, metadata-only (GSE317876_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX31965928, https://www.ncbi.nlm.nih.gov/sra?term=SRX31965929, https://www.ncbi.nlm.nih.gov/sra?term=SRX31965930, https://www.ncbi.nlm.nih.gov/sra?term=SRX31965931, https://www.ncbi.nlm.nih.gov/sra?term=SRX31965932, and 16 more (see sample_metadata.csv) |

## Field presence

- cell type: 21/21

## Evidence for WARN/FAIL checks

### source_tissue (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE317876 / Series_summary: matched `MASLD` in "This study presents an integrated transcriptomic analysis establishing Artemisitene (ATT) as a potent modulator for both engineering functional human liver organoids and treating metabolic-associated "
- GSE317876 / Series_overall_design: matched `steatosis` in "RNA-seq was performed on human stem cell-derived liver organoids under three experimental paradigms: (i) HB-orgs treated with ATT during differentiation (Day 6), (ii) mature P-hep-orgs treated with AT"

Decision: MANUAL_REVIEW

Reasons:
- source_tissue: liver-pattern source 0/21
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
<!-- /computed -->