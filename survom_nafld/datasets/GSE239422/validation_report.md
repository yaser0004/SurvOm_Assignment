# Validation report: GSE239422

A functional interaction between hepatic Estrogen Receptor-a and PNPLA3 p.I148M variant drives fatty liver diseases susceptibility in women

<!-- computed -->
Sample count: 125

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 125 samples |
| organism_consistency | PASS | Homo sapiens 125/125 |
| source_tissue | PASS | liver-pattern source 125/125 |
| library_strategy | PASS | RNA-Seq 125/125 |
| library_source | PASS | transcriptomic 125/125 |
| library_selection | PASS | cDNA 125/125 |
| instrument_model | PASS | Illumina HiSeq 4000 125/125 |
| metadata_completeness | PASS | reported consistently: age, disease, sex, steatosis_grade, tissue; not reported anywhere: bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, stage, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (125 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE239422_Normalized_Counts.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE239422_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX21188318, https://www.ncbi.nlm.nih.gov/sra?term=SRX21188319, https://www.ncbi.nlm.nih.gov/sra?term=SRX21188320, https://www.ncbi.nlm.nih.gov/sra?term=SRX21188321, https://www.ncbi.nlm.nih.gov/sra?term=SRX21188322, and 120 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 21 (1), 22 (2), 24 (4), 25 (1), 26 (1), 27 (2), 28 (1), 30 (6), 32 (3), 33 (3), 34 (2), 37 (4), 38 (6), 39 (4), 40 (6), 41 (4), 42 (6), 43 (5), 44 (4), 45 (4), 46 (5), 47 (4), 48 (5), 49 (4), 50 (6), 51 (7), 52 (2), 53 (3), 54 (1), 55 (2), 56 (5), 57 (2), 58 (1), 60 (2), 62 (2), 63 (1), 65 (2), 66 (1), 68 (1)
- **disease**: Obese (125)
- **sex**: F (107), M (18)
- **steatosis_grade**: 0 (20), 1 (48), 2 (29), 3 (28)
- **tissue**: Liver (125)

## Field presence

- Sex: 125/125 (canon: sex)
- age: 125/125 (canon: age)
- disease state: 125/125 (canon: disease)
- nash: 125/125
- pnpla3 rs738409: 125/125
- steatosis grade: 125/125 (canon: steatosis_grade)
- tissue: 125/125 (canon: tissue)

Decision: STRONG_CANDIDATE
<!-- /computed -->