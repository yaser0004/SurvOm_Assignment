# Validation report: GSE160200

Cholesterol-induced M4-like Macrophages in Non-alcoholic Steatohepatitis recruit Neutrophils and induce NETosis

<!-- computed -->
Sample count: 20

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 20 samples |
| organism_consistency | PASS | Homo sapiens 20/20 |
| source_tissue | WARN | liver-pattern source 0/20 |
| library_strategy | PASS | RNA-Seq 20/20 |
| library_source | PASS | transcriptomic 20/20 |
| library_selection | PASS | cDNA 20/20 |
| instrument_model | PASS | Illumina NextSeq 500 20/20 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (20/20), packaged in GSE160200_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE160200_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX9370765, https://www.ncbi.nlm.nih.gov/sra?term=SRX9370766, https://www.ncbi.nlm.nih.gov/sra?term=SRX9370767, https://www.ncbi.nlm.nih.gov/sra?term=SRX9370768, https://www.ncbi.nlm.nih.gov/sra?term=SRX9370769, and 15 more (see sample_metadata.csv) |

## Canonical field distributions

- **treatment**: HoxLDL (5), MoxLDL (5), native LDL (5), untreated (5)

## Field presence

- cell type: 20/20
- individual: 20/20
- treatment: 20/20 (canon: treatment)

## Evidence for WARN/FAIL checks

### source_tissue (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE160200 / Series_title: matched `Steatohepatitis` in "Cholesterol-induced M4-like Macrophages in Non-alcoholic Steatohepatitis recruit Neutrophils and induce NETosis"
- GSE160200 / Series_summary: matched `NASH` in "The liver is the central organ for cholesterol synthesis and homeostasis. The effects of dietary cholesterol on hepatic injury, mainly of oxidized low-density lipoproteins (OxLDL), are not fully under"

Decision: MANUAL_REVIEW

Reasons:
- source_tissue: liver-pattern source 0/20
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
<!-- /computed -->