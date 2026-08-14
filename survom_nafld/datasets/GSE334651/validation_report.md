# Validation report: GSE334651

Alternative splicing- and gene fusion-derived neoepitopes in MASLD-associated hepatocellular carcinoma

<!-- computed -->
Sample count: 120

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 120 samples |
| organism_consistency | PASS | Homo sapiens 120/120 |
| source_tissue | PASS | liver-pattern source 120/120 |
| library_strategy | PASS | RNA-Seq 120/120 |
| library_source | PASS | transcriptomic 120/120 |
| library_selection | PASS | cDNA 120/120 |
| instrument_model | PASS | Illumina NovaSeq 6000 120/120 |
| metadata_completeness | PASS | reported consistently: group, tissue; not reported anywhere: age, bmi, diagnosis, disease, ethnicity, fibrosis_stage, nas_score, sex, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (108 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX33650816, https://www.ncbi.nlm.nih.gov/sra?term=SRX33650817, https://www.ncbi.nlm.nih.gov/sra?term=SRX33650818, https://www.ncbi.nlm.nih.gov/sra?term=SRX33650819, https://www.ncbi.nlm.nih.gov/sra?term=SRX33650820, and 115 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE334651_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX33650816, https://www.ncbi.nlm.nih.gov/sra?term=SRX33650817, https://www.ncbi.nlm.nih.gov/sra?term=SRX33650818, https://www.ncbi.nlm.nih.gov/sra?term=SRX33650819, https://www.ncbi.nlm.nih.gov/sra?term=SRX33650820, and 115 more (see sample_metadata.csv) |

## Canonical field distributions

- **group**: CTRL (12), MASLD (13), MASLD-HCC (95)
- **tissue**: NonTumor liver (72), Tumor liver (48)

## Field presence

- group: 120/120 (canon: group)
- tissue: 120/120 (canon: tissue)

Decision: CANDIDATE

Unmet STRONG_CANDIDATE conditions:
- expression_data_availability not PASS
<!-- /computed -->