# Validation report: GSE274114

Metabolic dysfunction-associated steatohepatitis reduces interferon and macrophage liver gene signatures in chronic HBV patients

<!-- computed -->
Sample count: 39

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 39 samples |
| organism_consistency | PASS | Homo sapiens 39/39 |
| source_tissue | PASS | liver-pattern source 39/39 |
| library_strategy | PASS | RNA-Seq 39/39 |
| library_source | PASS | transcriptomic 39/39 |
| library_selection | PASS | cDNA 39/39 |
| instrument_model | WARN | mixed instruments: Illumina HiSeq 4000 20/39, Illumina NovaSeq 6000 19/39 |
| metadata_completeness | PASS | reported consistently: group, tissue; not reported anywhere: age, bmi, diagnosis, disease, ethnicity, fibrosis_stage, nas_score, sex, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (19 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (39/39), packaged in GSE274114_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE274114-GPL20301_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX25619505, https://www.ncbi.nlm.nih.gov/sra?term=SRX25619506, https://www.ncbi.nlm.nih.gov/sra?term=SRX25619507, https://www.ncbi.nlm.nih.gov/sra?term=SRX25619508, https://www.ncbi.nlm.nih.gov/sra?term=SRX25619509, and 34 more (see sample_metadata.csv) |

## Canonical field distributions

- **group**: CTRL (9), ENEG (11), ENEG_NASH (9), NASH (10)
- **tissue**: liver (39)

## Field presence

- group: 39/39 (canon: group)
- material: 39/39
- name of_sample: 39/39
- sample id: 39/39
- tissue: 39/39 (canon: tissue)

## Evidence for WARN/FAIL checks

### instrument_model (WARN)

Decision: MANUAL_REVIEW

Reasons:
- instrument_model: mixed instruments: Illumina HiSeq 4000 20/39, Illumina NovaSeq 6000 19/39
<!-- /computed -->