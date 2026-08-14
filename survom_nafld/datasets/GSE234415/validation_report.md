# Validation report: GSE234415

A new Nuclear-erythroid-2-Related Factor 2 activator for the treatment of human metabolic associated fatty liver disease

<!-- computed -->
Sample count: 36

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 36 samples |
| organism_consistency | PASS | Homo sapiens 36/36 |
| source_tissue | PASS | liver-pattern source 36/36 |
| library_strategy | PASS | RNA-Seq 36/36 |
| library_source | PASS | transcriptomic 36/36 |
| library_selection | PASS | cDNA 36/36 |
| instrument_model | PASS | Illumina NovaSeq 6000 36/36 |
| metadata_completeness | PASS | reported consistently: age, bmi, fibrosis_stage, nas_score, sex, steatosis_grade, tissue, treatment; not reported anywhere: diagnosis, disease, ethnicity, group, stage |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (36 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE234415_normalized_counts.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE234415_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX20635054, https://www.ncbi.nlm.nih.gov/sra?term=SRX20635055, https://www.ncbi.nlm.nih.gov/sra?term=SRX20635056, https://www.ncbi.nlm.nih.gov/sra?term=SRX20635057, https://www.ncbi.nlm.nih.gov/sra?term=SRX20635058, and 31 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 48 (3), 51 (3), 52 (3), 58 (3), 65 (6), 66 (3), 67 (6), 68 (3), 74 (6)
- **bmi**: 28.6 (3), 29.3 (6), 29.8 (3), 30 (6), 30.4 (3), 34.1 (3), 34.5 (3), 34.7 (3), 35.6 (3), 50.3 (3)
- **fibrosis_stage**: 1 (9), 3 (9), 4 (18)
- **nas_score**: 1 (6), 2 (9), 3 (3), 4 (12), 5 (6)
- **sex**: F (21), M (15)
- **steatosis_grade**: 0 | 5 (6), 1 | 10 (3), 1 | 15 (9), 1 | 20 (3), 1 | 25 (3), 1 | 6 (3), 2 | 40 (6), 2 | 50 (3)
- **tissue**: Liver (36)
- **treatment**: DMSO (12), Elafibranor (12), S217879 (12)

## Field presence

- Sex: 36/36 (canon: sex)
- activity.score.saf: 36/36
- age: 36/36 (canon: age)
- alcool.consumption: 36/36
- alt: 36/36
- ast: 36/36
- ballooning.score.nas: 36/36
- ballooning.score.saf: 36/36
- bmi: 36/36 (canon: bmi)
- fibrosis.score: 36/36 (canon: fibrosis_stage)
- inflammation.score.nas: 36/36
- inflammation.score.saf: 36/36
- nas.score: 36/36 (canon: nas_score)
- patient: 36/36
- steatosis.score: 36/36 (canon: steatosis_grade)
- steatosis.score.%: 36/36 (canon: steatosis_grade)
- tissue: 36/36 (canon: tissue)
- treatment: 36/36 (canon: treatment)

Decision: STRONG_CANDIDATE
<!-- /computed -->