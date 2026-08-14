# Validation report: GSE207310

Stellate cell expression of SPARC-related modular calcium-binding protein 2 is associated with human non-alcoholic fatty liver disease severity

<!-- computed -->
Sample count: 30

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 30 samples |
| organism_consistency | PASS | Homo sapiens 30/30 |
| source_tissue | PASS | liver-pattern source 30/30 |
| library_strategy | PASS | RNA-Seq 30/30 |
| library_source | PASS | transcriptomic 30/30 |
| library_selection | PASS | cDNA 30/30 |
| instrument_model | PASS | Illumina NovaSeq 6000 30/30 |
| metadata_completeness | PASS | reported consistently: nas_score, sex, tissue; not reported anywhere: age, bmi, diagnosis, disease, ethnicity, fibrosis_stage, group, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (30 sample(s)) |
| single_cell_or_spatial | WARN | series prose mentions single-cell; sample metadata does not corroborate |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX15955186, https://www.ncbi.nlm.nih.gov/sra?term=SRX15955187, https://www.ncbi.nlm.nih.gov/sra?term=SRX15955188, https://www.ncbi.nlm.nih.gov/sra?term=SRX15955189, https://www.ncbi.nlm.nih.gov/sra?term=SRX15955190, and 25 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE207310_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX15955186, https://www.ncbi.nlm.nih.gov/sra?term=SRX15955187, https://www.ncbi.nlm.nih.gov/sra?term=SRX15955188, https://www.ncbi.nlm.nih.gov/sra?term=SRX15955189, https://www.ncbi.nlm.nih.gov/sra?term=SRX15955190, and 25 more (see sample_metadata.csv) |

## Canonical field distributions

- **nas_score**: 0 (4), 1 (1), 2 (7), 3 (5), 4 (6), 5 (5), 7 (1), 8 (1)
- **sex**: Female (27), Male (3)
- **tissue**: Liver biopsy (30)

## Field presence

- Sex: 30/30 (canon: sex)
- kleiner fibrosis_grade: 30/30
- nafld activity_score: 30/30 (canon: nas_score)
- steatosis, activity,_and_fibrosis_score: 30/30
- tissue: 30/30 (canon: tissue)
- tissue preservation: 30/30

## Evidence for WARN/FAIL checks

### single_cell_or_spatial (WARN)
- GSE207310 / Series_summary: matched `single-cell` in "Non-alcoholic fatty liver disease (NAFLD) and its progressive form, non-alcoholic steatohepatitis (NASH), are the hepatic manifestations of metabolic syndrome. Histological assessment of liver biopsie"

Decision: MANUAL_REVIEW

Reasons:
- single_cell_or_spatial: series prose mentions single-cell; sample metadata does not corroborate
<!-- /computed -->