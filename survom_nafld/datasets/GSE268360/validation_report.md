# Validation report: GSE268360

Reduced ZMPSTE24 expression leads to prelamin accumulation and development of steatosis in MAFLD patients [RNA-seq]

<!-- computed -->
Sample count: 18

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 18 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 18/18 |
| source_tissue | PASS | liver-pattern source 18/18 |
| library_strategy | PASS | RNA-Seq 18/18 |
| library_source | PASS | transcriptomic 18/18 |
| library_selection | PASS | cDNA 18/18 |
| instrument_model | PASS | NextSeq 2000 18/18 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX24702874, https://www.ncbi.nlm.nih.gov/sra?term=SRX24702875, https://www.ncbi.nlm.nih.gov/sra?term=SRX24702876, https://www.ncbi.nlm.nih.gov/sra?term=SRX24702877, https://www.ncbi.nlm.nih.gov/sra?term=SRX24702878, and 13 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE268360_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX24702874, https://www.ncbi.nlm.nih.gov/sra?term=SRX24702875, https://www.ncbi.nlm.nih.gov/sra?term=SRX24702876, https://www.ncbi.nlm.nih.gov/sra?term=SRX24702877, https://www.ncbi.nlm.nih.gov/sra?term=SRX24702878, and 13 more (see sample_metadata.csv) |

## Canonical field distributions

- **sex**: female (9), male (9)
- **tissue**: Liver (18)

## Field presence

- gender: 18/18 (canon: sex)
- subject status: 18/18
- tissue: 18/18 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE268360 / Series_title: matched `steatosis` in "Reduced ZMPSTE24 expression leads to prelamin accumulation and development of steatosis in MAFLD patients [RNA-seq]"
- GSE268360 / Series_summary: matched `fatty liver` in "Mutations of nuclear lamina-associated proteins LMNA and ZMPSTE24 have been associated with fatty liver. We report that the changes at the nuclear envelope we described in MAFLD patients are caused by"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 18 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
<!-- /computed -->