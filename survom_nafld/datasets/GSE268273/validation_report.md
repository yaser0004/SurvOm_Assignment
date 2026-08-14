# Validation report: GSE268273

Clinical and molecular characterization of steatotic liver disease in the setting of immune-mediated inflammatory diseases

<!-- computed -->
Sample count: 109

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 109 samples |
| organism_consistency | PASS | Homo sapiens 109/109 |
| source_tissue | PASS | liver-pattern source 109/109 |
| library_strategy | PASS | RNA-Seq 109/109 |
| library_source | PASS | transcriptomic 109/109 |
| library_selection | PASS | cDNA 109/109 |
| instrument_model | PASS | Illumina NovaSeq 6000 109/109 |
| metadata_completeness | PASS | reported consistently: disease, sex, tissue; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (109 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX24684209, https://www.ncbi.nlm.nih.gov/sra?term=SRX24684210, https://www.ncbi.nlm.nih.gov/sra?term=SRX24684211, https://www.ncbi.nlm.nih.gov/sra?term=SRX24684212, https://www.ncbi.nlm.nih.gov/sra?term=SRX24684213, and 104 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE268273_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX24684209, https://www.ncbi.nlm.nih.gov/sra?term=SRX24684210, https://www.ncbi.nlm.nih.gov/sra?term=SRX24684211, https://www.ncbi.nlm.nih.gov/sra?term=SRX24684212, https://www.ncbi.nlm.nih.gov/sra?term=SRX24684213, and 104 more (see sample_metadata.csv) |

## Canonical field distributions

- **disease**: NAFLD & Hidradenitis (9), NAFLD & IBD (42), NAFLD & Psoriasis (14), NAFLD & Spondylitis (4), NAFLD/NASH (40)
- **sex**: Female (52), Male (57)
- **tissue**: Liver (109)

## Field presence

- Sex: 109/109 (canon: sex)
- case/control: 109/109
- disease: 109/109 (canon: disease)
- fasting glycemia: 109/109
- fibrosis degree: 109/109
- hba1c: 109/109
- hdl-cholesterol: 108/109
- hypertension: 109/109
- ldl-cholesterol: 108/109
- obesity: 109/109
- t2d/ir: 109/109
- tissue: 109/109 (canon: tissue)
- total cholesterol: 109/109
- tryglicerides: 109/109

Decision: CANDIDATE

Unmet STRONG_CANDIDATE conditions:
- expression_data_availability not PASS
<!-- /computed -->