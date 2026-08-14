# Validation report: GSE274898

TGF-beta mediated hepatic stellate cells activation is dampened in the absence of EPHB2 in vitro.

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
| expression_data_availability | PASS | processed series-level file: GSE274898_20073R_counts.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE274898_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX25711613, https://www.ncbi.nlm.nih.gov/sra?term=SRX25711614, https://www.ncbi.nlm.nih.gov/sra?term=SRX25711615, https://www.ncbi.nlm.nih.gov/sra?term=SRX25711616, https://www.ncbi.nlm.nih.gov/sra?term=SRX25711617, and 1 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Liver (6)
- **treatment**: TGF-b1 (6)

## Field presence

- cell line: 6/6
- cell type: 6/6
- genotype: 6/6
- tissue: 6/6 (canon: tissue)
- treatment: 6/6 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE274898 / Series_summary: matched `MASH` in "Hepatic stellate cells (HSCs) are the major effector cell-type responsible for the production of collagens in hepatic fibrogenesis. In this study we showed that when EPHB2 is silenced in  human  prima"
### material_type (WARN)
- GSM8460945 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary cell"
- GSM8460946 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary cell"
- GSM8460947 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary cell"
- GSM8460948 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary cell"
- GSM8460949 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary cell"
- GSM8460950 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary cell"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 6 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (6/6 samples)
<!-- /computed -->