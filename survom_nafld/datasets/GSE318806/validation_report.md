# Validation report: GSE318806

P21+TREM2+-Senescent Macrophages Fuel Inflammaging and Metabolic Dysfunction-Associated Steatotic Liver Disease. [Blood]

<!-- computed -->
Sample count: 9

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 9 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 9/9 |
| source_tissue | WARN | liver-pattern source 0/9 |
| library_strategy | PASS | RNA-Seq 9/9 |
| library_source | PASS | transcriptomic 9/9 |
| library_selection | PASS | cDNA 9/9 |
| instrument_model | PASS | Illumina NovaSeq X Plus 9/9 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | WARN | series prose mentions single cell; sample metadata does not corroborate |
| material_type | WARN | cell/culture terms in sample metadata: cell line (9/9 samples) |
| expression_data_availability | PASS | processed series-level file: GSE318806_human_counts-gene.xls.gz |
| series_matrix | INFO | present, metadata-only (GSE318806_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | no SRA/raw sequencing links found |

## Canonical field distributions

- **tissue**: PBMCs (9)
- **treatment**: Passage Control (3), Sen(Dox) (3), Sen(IR) (3)

## Field presence

- batch: 9/9
- cell line: 9/9
- cell type: 9/9
- tissue: 9/9 (canon: tissue)
- treatment: 9/9 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE318806 / Series_title: matched `Metabolic Dysfunction-Associated Stea` in "P21+TREM2+-Senescent Macrophages Fuel Inflammaging and Metabolic Dysfunction-Associated Steatotic Liver Disease. [Blood]"
- GSE318806 / Series_summary: matched `MASLD` in "Cellular senescence drives chronic sterile inflammation during aging via the senescence-associated secretory phenotype (SASP); however, the cell types responsible for this pathology remain poorly defi"
### single_cell_or_spatial (WARN)
- GSE318806 / Series_overall_design: matched `single cell` in "Blood from biological male or female human donors were collected and PBMCs were isolated at UCLA's Virology Core. 100 x 106  blood cells were collected from 3-5 donors with no clinical information. PB"
### material_type (WARN)
- GSM9503529 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary"
- GSM9503530 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary"
- GSM9503531 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary"
- GSM9503532 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary"
- GSM9503533 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary"
- GSM9503534 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary"
- GSM9503535 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary"
- GSM9503536 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary"
- GSM9503537 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 9 samples (below 20)
- source_tissue: liver-pattern source 0/9
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- single_cell_or_spatial: series prose mentions single cell; sample metadata does not corroborate
- material_type: cell/culture terms in sample metadata: cell line (9/9 samples)
<!-- /computed -->