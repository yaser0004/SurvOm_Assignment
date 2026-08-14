# Validation report: GSE197399

Redistribution of lamina-associated domains reshapes Foxa2 binding in development of NAFLD

<!-- computed -->
Sample count: 61

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 61 samples |
| organism_consistency | WARN | mixed organisms: Homo sapiens 21/61, Mus musculus 40/61 |
| source_tissue | PASS | liver-pattern source 61/61 |
| library_strategy | WARN | mixed strategies: ChIP-Seq 46/61, RNA-Seq 15/61 |
| library_source | WARN | library_source: genomic 46/61, transcriptomic 15/61 |
| library_selection | WARN | mixed library_selection: ChIP 46/61, cDNA 15/61 |
| instrument_model | PASS | Illumina NextSeq 500 61/61 |
| metadata_completeness | WARN | patchy fields: age 37/61, disease 18/61. reported consistently: tissue; not reported anywhere: bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (12 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX14280043, https://www.ncbi.nlm.nih.gov/sra?term=SRX14280044, https://www.ncbi.nlm.nih.gov/sra?term=SRX14280045, https://www.ncbi.nlm.nih.gov/sra?term=SRX14280046, https://www.ncbi.nlm.nih.gov/sra?term=SRX14280047, and 56 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE197399-GPL18573_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX14280043, https://www.ncbi.nlm.nih.gov/sra?term=SRX14280044, https://www.ncbi.nlm.nih.gov/sra?term=SRX14280045, https://www.ncbi.nlm.nih.gov/sra?term=SRX14280046, https://www.ncbi.nlm.nih.gov/sra?term=SRX14280047, and 56 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 4 months (18), 5 months (19)
- **disease**: Mild NAFLD (6), NAFLD (6), Normal control (6)
- **tissue**: liver (61)

## Field presence

- age: 37/61 (canon: age)
- chip antibody: 46/61
- diet: 37/61
- disease state: 18/61 (canon: disease)
- genotype: 40/61
- tissue: 61/61 (canon: tissue)

## Evidence for WARN/FAIL checks

### organism_consistency (WARN)
### library_strategy (WARN)
### library_source (WARN)
### library_selection (WARN)
### metadata_completeness (WARN)

Decision: MANUAL_REVIEW

Reasons:
- organism_consistency: mixed organisms: Homo sapiens 21/61, Mus musculus 40/61
- library_strategy: mixed strategies: ChIP-Seq 46/61, RNA-Seq 15/61
- library_source: library_source: genomic 46/61, transcriptomic 15/61
- library_selection: mixed library_selection: ChIP 46/61, cDNA 15/61
- metadata_completeness: patchy fields: age 37/61, disease 18/61. reported consistently: tissue; not reported anywhere: bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade, treatment
<!-- /computed -->