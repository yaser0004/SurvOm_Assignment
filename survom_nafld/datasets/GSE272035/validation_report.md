# Validation report: GSE272035

Gene community-regulated pathway analysis successfully deciphers pathogenesis and biomarkers of viral versus metabolic hepatocellular carcinoma

<!-- computed -->
Sample count: 71

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 71 samples |
| organism_consistency | PASS | Homo sapiens 71/71 |
| source_tissue | PASS | liver-pattern source 71/71 |
| library_strategy | PASS | RNA-Seq 71/71 |
| library_source | PASS | transcriptomic 71/71 |
| library_selection | PASS | cDNA 71/71 |
| instrument_model | PASS | Illumina NovaSeq 6000 71/71 |
| metadata_completeness | PASS | reported consistently: disease, sex, tissue; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (71 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE272035_matrix.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE272035_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX25289923, https://www.ncbi.nlm.nih.gov/sra?term=SRX25289924, https://www.ncbi.nlm.nih.gov/sra?term=SRX25289925, https://www.ncbi.nlm.nih.gov/sra?term=SRX25289926, https://www.ncbi.nlm.nih.gov/sra?term=SRX25289927, and 66 more (see sample_metadata.csv) |

## Canonical field distributions

- **disease**: No (55), Yes (16)
- **sex**: Female (20), Male (51)
- **tissue**: Liver tissue (71)

## Field presence

- Sex: 71/71 (canon: sex)
- alcoholism: 71/71
- cirrhosis: 71/71
- non-alcoholic fatty_liver_disease_(nafld): 71/71 (canon: disease)
- pathology stage(ajcc_7th_edition): 71/71
- tissue: 71/71 (canon: tissue)
- virus infection: 71/71
- vital status: 71/71

Decision: STRONG_CANDIDATE
<!-- /computed -->