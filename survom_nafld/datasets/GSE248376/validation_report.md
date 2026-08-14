# Validation report: GSE248376

Inferring secretory and metabolic pathway activity from omic data with secCellFie

<!-- computed -->
Sample count: 6

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 6 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 6/6 |
| source_tissue | PASS | liver-pattern source 6/6 |
| library_strategy | PASS | RNA-Seq 6/6 |
| library_source | PASS | transcriptomic 6/6 |
| library_selection | PASS | cDNA 6/6 |
| instrument_model | PASS | Illumina NovaSeq 6000 6/6 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (6/6 samples) |
| expression_data_availability | PASS | processed series-level file: GSE248376_hepatokineTPM_GEO.csv.gz |
| series_matrix | INFO | present, metadata-only (GSE248376_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX22595441, https://www.ncbi.nlm.nih.gov/sra?term=SRX22595442, https://www.ncbi.nlm.nih.gov/sra?term=SRX22595443, https://www.ncbi.nlm.nih.gov/sra?term=SRX22595444, https://www.ncbi.nlm.nih.gov/sra?term=SRX22595445, and 1 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: liver (6)
- **treatment**: control (3), palmitic acid (3)

## Field presence

- cell line: 6/6
- cell type: 6/6
- tissue: 6/6 (canon: tissue)
- treatment: 6/6 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE248376 / Series_summary: matched `NAFLD` in "Understanding protein secretion has considerable importance in the biotechnology industry and important implications in a broad range of normal and pathological conditions including development, immun"
- GSE248376 / Series_overall_design: matched `NAFLD` in "Gene expression profiling analysis of RNA-seq data comparing control vs invitro model of NAFLD in Huh7 cells"
### material_type (WARN)
- GSM7912303 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM7912304 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM7912305 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM7912306 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM7912307 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM7912308 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 6 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (6/6 samples)
<!-- /computed -->