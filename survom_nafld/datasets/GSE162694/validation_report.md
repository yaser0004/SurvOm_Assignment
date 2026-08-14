# Validation report: GSE162694

Molecular Characterization and Cell Type Composition Deconvolution of Fibrosis in NAFLD

<!-- computed -->
Sample count: 143

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 143 samples |
| organism_consistency | PASS | Homo sapiens 143/143 |
| source_tissue | PASS | liver-pattern source 143/143 |
| library_strategy | PASS | RNA-Seq 143/143 |
| library_source | PASS | transcriptomic 143/143 |
| library_selection | PASS | cDNA 143/143 |
| instrument_model | PASS | Illumina HiSeq 3000 143/143 |
| metadata_completeness | PASS | reported consistently: age, fibrosis_stage, nas_score, sex, tissue; not reported anywhere: bmi, diagnosis, disease, ethnicity, group, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (143 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE162694_raw_counts.csv.gz |
| series_matrix | INFO | present, metadata-only (GSE162694_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX9633405, https://www.ncbi.nlm.nih.gov/sra?term=SRX9633406, https://www.ncbi.nlm.nih.gov/sra?term=SRX9633407, https://www.ncbi.nlm.nih.gov/sra?term=SRX9633408, https://www.ncbi.nlm.nih.gov/sra?term=SRX9633409, and 138 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 18 (1), 20 (3), 21 (1), 22 (3), 25 (5), 26 (1), 28 (4), 29 (1), 30 (2), 32 (5), 33 (3), 34 (5), 35 (3), 36 (2), 37 (4), 39 (2), 40 (2), 41 (3), 42 (4), 43 (1), 44 (4), 45 (3), 46 (4), 47 (3), 48 (5), 49 (5), 50 (3), 51 (4), 52 (4), 53 (4), 54 (6), 55 (5), 56 (3), 57 (5), 58 (3), 59 (4), 60 (4), 61 (4), 62 (3), 64 (4), 65 (3), 66 (1), 68 (2), 69 (1), 72 (1)
- **fibrosis_stage**: 0 (35), 1 (30), 2 (27), 3 (8), 4 (12), normal liver histology (31)
- **nas_score**: 0 (32), 1 (12), 2 (9), 3 (11), 4 (13), 5 (19), 6 (12), 7 (9), NA (26)
- **sex**: Female (103), Male (40)
- **tissue**: Liver (143)

## Field presence

- Sex: 143/143 (canon: sex)
- age: 143/143 (canon: age)
- fibrosis stage: 143/143 (canon: fibrosis_stage)
- nas score: 143/143 (canon: nas_score)
- tissue: 143/143 (canon: tissue)

Decision: STRONG_CANDIDATE
<!-- /computed -->