# Validation report: GSE138052

mRNA sequencing analysis of a novel model of 'NAFLD in a Dish'

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
| instrument_model | PASS | Illumina HiSeq 4000 6/6 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (6/6), packaged in GSE138052_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE138052_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX6913755, https://www.ncbi.nlm.nih.gov/sra?term=SRX6913756, https://www.ncbi.nlm.nih.gov/sra?term=SRX6913757, https://www.ncbi.nlm.nih.gov/sra?term=SRX6913758, https://www.ncbi.nlm.nih.gov/sra?term=SRX6913759, and 1 more (see sample_metadata.csv) |

## Canonical field distributions

- **treatment**: lactate (10 mM), pyruvate (1 mM) and octanoate (2 mM) (3), none (control) (3)

## Field presence

- cell type: 6/6
- treatment: 6/6 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE138052 / Series_title: matched `NAFLD` in "mRNA sequencing analysis of a novel model of 'NAFLD in a Dish'"
- GSE138052 / Series_summary: matched `NAFLD` in "The goal of this study was to determine the changes to cellular transcriptional programs following induction of intracellular lipid accumulation, with the aim of confirming the utility of this model f"
- GSE138052 / Series_overall_design: matched `NAFLD` in "mRNA profiles were generated for ES-derived hepatocyte-like cells following treatment with lactate (10 mM), pyruvate (1 mM) and octanoate (2 mM) to induce intracellular lipid accumulation, resulting i"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 6 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
<!-- /computed -->