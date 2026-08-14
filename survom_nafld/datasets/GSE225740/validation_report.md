# Validation report: GSE225740

Clinically Important Alterations in Pharmacogene Expression in Histologically Severe Nonalcoholic Fatty Liver Disease

<!-- computed -->
Sample count: 93

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 93 samples |
| organism_consistency | PASS | Homo sapiens 93/93 |
| source_tissue | PASS | liver-pattern source 93/93 |
| library_strategy | PASS | RNA-Seq 93/93 |
| library_source | PASS | transcriptomic 93/93 |
| library_selection | PASS | cDNA 93/93 |
| instrument_model | PASS | Illumina HiSeq 2500 93/93 |
| metadata_completeness | PASS | reported consistently: fibrosis_stage, nas_score, tissue; not reported anywhere: age, bmi, diagnosis, disease, ethnicity, group, sex, stage, steatosis_grade, treatment |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE225740_NAFLD_RNA_counts.csv.gz |
| series_matrix | INFO | present, metadata-only (GSE225740_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | no SRA/raw sequencing links found |

## Canonical field distributions

- **fibrosis_stage**: 0 (27), 1 (26), 2 (15), 3 (13), 4 (6), NA (6)
- **nas_score**: 0 (5), 1 (6), 2 (15), 3 (14), 4 (18), 5 (18), 6 (12), 7 (5)
- **tissue**: Liver (93)

## Field presence

- fibrosis: 93/93 (canon: fibrosis_stage)
- nas: 93/93 (canon: nas_score)
- steatohep: 93/93
- tissue: 93/93 (canon: tissue)

## Evidence for WARN/FAIL checks

### disease_relevance (WARN)
- GSE225740 / Series_title: matched `Nonalcoholic Fatty Liver` in "Clinically Important Alterations in Pharmacogene Expression in Histologically Severe Nonalcoholic Fatty Liver Disease"
- GSE225740 / Series_summary: matched `NAFLD` in "This study aims to determine if patients with NAFLD are at risk for altered drug response by characterizing changes in hepatic mRNA expression of genes mediating drug disposition (pharmacogenes) acros"
- GSE225740 / Series_overall_design: matched `NAFLD` in "We utilize RNA-seq for 93 liver biopsies with histologically staged NAFLD Activity Score (NAS), fibrosis stage, and steatohepatitis (NASH)."

Decision: MANUAL_REVIEW

Reasons:
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
<!-- /computed -->