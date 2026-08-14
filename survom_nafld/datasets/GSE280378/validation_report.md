# Validation report: GSE280378

Induction of MASH in Three-Dimensional Bioprinted Human Liver Tissue

<!-- computed -->
Sample count: 22

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 22 samples |
| organism_consistency | PASS | Homo sapiens 22/22 |
| source_tissue | PASS | liver-pattern source 22/22 |
| library_strategy | FAIL | no expression-profiling strategy found (ssRNA-seq) |
| library_source | PASS | transcriptomic 22/22 |
| library_selection | PASS | cDNA 22/22 |
| instrument_model | PASS | Illumina HiSeq 2500 22/22 |
| metadata_completeness | PASS | reported consistently: stage, tissue; not reported anywhere: age, bmi, diagnosis, disease, ethnicity, fibrosis_stage, group, nas_score, sex, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (12 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | INFO | series prose mentions In vitro; sample metadata does not corroborate |
| expression_data_availability | PASS | processed series-level file: GSE280378_20240206115043_raw_pc_genes_counts.csv.gz |
| series_matrix | INFO | present, metadata-only (GSE280378_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX26509564, https://www.ncbi.nlm.nih.gov/sra?term=SRX26509565, https://www.ncbi.nlm.nih.gov/sra?term=SRX26509566, https://www.ncbi.nlm.nih.gov/sra?term=SRX26509567, https://www.ncbi.nlm.nih.gov/sra?term=SRX26509568, and 17 more (see sample_metadata.csv) |

## Canonical field distributions

- **stage**: MASH (12), healthy (10)
- **tissue**: bioprinted liver (22)

## Field presence

- disease stage: 22/22 (canon: stage)
- timepoint: 22/22
- tissue: 22/22 (canon: tissue)

## Evidence for WARN/FAIL checks

### library_strategy (FAIL)

Decision: REJECT

Reasons:
- library_strategy: no expression-profiling samples (no expression-profiling strategy found (ssRNA-seq))
<!-- /computed -->