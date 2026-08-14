# Validation report: GSE279712

Unraveling and enhancing the dynamics of hepatic bile acid and cholesterol metabolism during ex vivo normothermic machine perfusion; a path to improved liver function through conjugated bile acid infusion

<!-- computed -->
Sample count: 22

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 22 samples |
| organism_consistency | WARN | mixed organisms: Homo sapiens 12/22, Sus scrofa domesticus 10/22 |
| source_tissue | PASS | liver-pattern source 22/22 |
| library_strategy | PASS | RNA-Seq 22/22 |
| library_source | PASS | transcriptomic 22/22 |
| library_selection | PASS | cDNA 22/22 |
| instrument_model | PASS | Illumina NovaSeq 6000 22/22 |
| metadata_completeness | WARN | patchy fields: sex 10/22. reported consistently: diagnosis, tissue, treatment; not reported anywhere: age, bmi, disease, ethnicity, fibrosis_stage, group, nas_score, stage, steatosis_grade |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (2 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (22/22), packaged in GSE279712_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE279712-GPL24676_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX26414731, https://www.ncbi.nlm.nih.gov/sra?term=SRX26414732, https://www.ncbi.nlm.nih.gov/sra?term=SRX26414733, https://www.ncbi.nlm.nih.gov/sra?term=SRX26414734, https://www.ncbi.nlm.nih.gov/sra?term=SRX26414735, and 17 more (see sample_metadata.csv) |

## Canonical field distributions

- **diagnosis**: Alcoholic_Liver_Disease (4), Healthy_Liver (12), Hepatitis_B_+_hepatocellular_carcinoma (2), NASH (2), Primary_biliary_cholangitis (2)
- **sex**: male (10)
- **tissue**: liver (22)
- **treatment**: H0 (6), H6 (6), P0 (5), P6 (5)

## Field presence

- Sex: 10/22 (canon: sex)
- diagn: 22/22
- diagnosis: 22/22 (canon: diagnosis)
- subject id: 22/22
- tissue: 22/22 (canon: tissue)
- treat(non)cirrhotic: 22/22
- treatment: 22/22 (canon: treatment)
- treatorganism: 22/22
- treatperfusionhr: 22/22

## Evidence for WARN/FAIL checks

### organism_consistency (WARN)
### metadata_completeness (WARN)

Decision: MANUAL_REVIEW

Reasons:
- organism_consistency: mixed organisms: Homo sapiens 12/22, Sus scrofa domesticus 10/22
- metadata_completeness: patchy fields: sex 10/22. reported consistently: diagnosis, tissue, treatment; not reported anywhere: age, bmi, disease, ethnicity, fibrosis_stage, group, nas_score, stage, steatosis_grade
<!-- /computed -->