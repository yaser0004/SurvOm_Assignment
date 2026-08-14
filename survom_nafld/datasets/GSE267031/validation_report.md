# Validation report: GSE267031

Bulk Liver in MAFLD/MASH

<!-- computed -->
Sample count: 18

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 18 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 18/18 |
| source_tissue | PASS | liver-pattern source 18/18 |
| library_strategy | PASS | RNA-Seq 18/18 |
| library_source | PASS | transcriptomic 18/18 |
| library_selection | PASS | cDNA 18/18 |
| instrument_model | PASS | Illumina NovaSeq 6000 18/18 |
| metadata_completeness | PASS | reported consistently: disease, nas_score, sex, tissue; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (18 sample(s)) |
| single_cell_or_spatial | WARN | series prose mentions single cell; sample metadata does not corroborate |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE267031_counts_RNAseq_Liver.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE267031_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX24500478, https://www.ncbi.nlm.nih.gov/sra?term=SRX24500479, https://www.ncbi.nlm.nih.gov/sra?term=SRX24500480, https://www.ncbi.nlm.nih.gov/sra?term=SRX24500481, https://www.ncbi.nlm.nih.gov/sra?term=SRX24500482, and 13 more (see sample_metadata.csv) |

## Canonical field distributions

- **disease**: MAFLD/MASH | 1_low (5), MAFLD/MASH | 2_medium (6), MAFLD/MASH | 3_high (7)
- **nas_score**: 1 (3), 2 (2), 3 (2), 4 (4), 5 (2), 6 (4), 8 (1)
- **sex**: f (9), m (9)
- **tissue**: Liver (18)

## Field presence

- Sex: 18/18 (canon: sex)
- batch: 18/18
- celltype: 18/18
- condition: 18/18 (canon: disease)
- disease: 18/18 (canon: disease)
- id sample: 18/18
- nas: 18/18 (canon: nas_score)
- tissue: 18/18 (canon: tissue)
- type patient: 18/18

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### single_cell_or_spatial (WARN)
- GSE267031 / Series_summary: matched `single cell` in "Background & Aims: Metabolic dysfunction associated steatotic liver disease (MAFLD) progresses to steatohepatitis (MASH) and is a major cause of liver cirrhosis. In the early disease stage, liver infl"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 18 samples (below 20)
- single_cell_or_spatial: series prose mentions single cell; sample metadata does not corroborate
<!-- /computed -->