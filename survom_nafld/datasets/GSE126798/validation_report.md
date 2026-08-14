# Validation report: GSE126798

Human liver organoids; a patient-derived primary model for HBV Infection, Replication and Related Hepatocellular Carcinoma

<!-- computed -->
Sample count: 25

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 25 samples |
| organism_consistency | PASS | Homo sapiens 25/25 |
| source_tissue | PASS | liver-pattern source 25/25 |
| library_strategy | PASS | RNA-Seq 25/25 |
| library_source | PASS | transcriptomic 25/25 |
| library_selection | PASS | cDNA 25/25 |
| instrument_model | PASS | Ion Torrent Proton 25/25 |
| metadata_completeness | WARN | patchy fields: disease 16/25. reported consistently: age, tissue; not reported anywhere: bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (4 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: organoid (16/25 samples) |
| expression_data_availability | PASS | processed series-level file: GSE126798_P_vs_H_DESeq_normalized_counts.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE126798_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX11384137, https://www.ncbi.nlm.nih.gov/sra?term=SRX11384138, https://www.ncbi.nlm.nih.gov/sra?term=SRX11384139, https://www.ncbi.nlm.nih.gov/sra?term=SRX11384140, https://www.ncbi.nlm.nih.gov/sra?term=SRX11384141, and 20 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 28 (1), 44 (1), 48 (1), 49 (1), 51 (1), 52 (1), 54 (2), 56 (1), 59 (1), 60 (2), 62 (2), 65 (1), 66 (1), 68 (1), 69 (1), 71 (1), NA (6)
- **disease**: HBV HDV infected (3), HBV infected (8), Healthy donor (5)
- **tissue**: liver (9), liver organoids (16)

## Field presence

- age: 25/25 (canon: age)
- disease state: 16/25 (canon: disease)
- genotype: 9/25
- strain: 9/25
- tissue: 25/25 (canon: tissue)

## Evidence for WARN/FAIL checks

### metadata_completeness (WARN)
### material_type (WARN)
- GSM3613432 / Sample_characteristics_ch1: matched `organoid` in "tissue: liver organoids"
- GSM3613433 / Sample_characteristics_ch1: matched `organoid` in "tissue: liver organoids"
- GSM3613434 / Sample_characteristics_ch1: matched `organoid` in "tissue: liver organoids"
- GSM3613435 / Sample_characteristics_ch1: matched `organoid` in "tissue: liver organoids"
- GSM3613436 / Sample_characteristics_ch1: matched `organoid` in "tissue: liver organoids"
- GSM3613437 / Sample_characteristics_ch1: matched `organoid` in "tissue: liver organoids"
- GSM3613438 / Sample_characteristics_ch1: matched `organoid` in "tissue: liver organoids"
- GSM3613439 / Sample_characteristics_ch1: matched `organoid` in "tissue: liver organoids"
- GSM3613440 / Sample_characteristics_ch1: matched `organoid` in "tissue: liver organoids"
- GSM3613441 / Sample_characteristics_ch1: matched `organoid` in "tissue: liver organoids"
- GSM3613442 / Sample_characteristics_ch1: matched `organoid` in "tissue: liver organoids"
- GSM3613443 / Sample_characteristics_ch1: matched `organoid` in "tissue: liver organoids"
- GSM3613444 / Sample_characteristics_ch1: matched `organoid` in "tissue: liver organoids"
- GSM3613445 / Sample_characteristics_ch1: matched `organoid` in "tissue: liver organoids"
- GSM3613446 / Sample_characteristics_ch1: matched `organoid` in "tissue: liver organoids"
- GSM3613447 / Sample_characteristics_ch1: matched `organoid` in "tissue: liver organoids"

Decision: MANUAL_REVIEW

Reasons:
- metadata_completeness: patchy fields: disease 16/25. reported consistently: age, tissue; not reported anywhere: bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade, treatment
- material_type: cell/culture terms in sample metadata: organoid (16/25 samples)
<!-- /computed -->