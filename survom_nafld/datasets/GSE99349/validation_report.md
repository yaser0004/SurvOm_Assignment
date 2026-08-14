# Validation report: GSE99349

Gene Network Dysregulation in Dorsolateral Prefrontal Cortex Neurons of Humans with Cocaine Use Disorder

<!-- computed -->
Sample count: 36

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 36 samples |
| organism_consistency | PASS | Homo sapiens 36/36 |
| source_tissue | WARN | liver-pattern source 0/36 |
| library_strategy | PASS | RNA-Seq 36/36 |
| library_source | PASS | transcriptomic 36/36 |
| library_selection | PASS | cDNA 36/36 |
| instrument_model | PASS | Illumina HiSeq 2000 36/36 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | FAIL | no NAFLD-spectrum term found in series or sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE99349_Expression_Matrix.xlsx |
| series_matrix | INFO | present, metadata-only (GSE99349_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX2862557, https://www.ncbi.nlm.nih.gov/sra?term=SRX2862558, https://www.ncbi.nlm.nih.gov/sra?term=SRX2862559, https://www.ncbi.nlm.nih.gov/sra?term=SRX2862560, https://www.ncbi.nlm.nih.gov/sra?term=SRX2862561, and 31 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 20 (1), 21 (3), 22 (1), 23 (3), 26 (1), 27 (1), 28 (1), 29 (4), 30 (1), 31 (1), 33 (1), 34 (1), 35 (3), 36 (1), 38 (1), 39 (1), 44 (1), 45 (2), 46 (1), 47 (1), 48 (1), 50 (1), 52 (1), 53 (1), 54 (1), 58 (1)
- **ethnicity**: Black | Not Hispanic or Latino (13), White | Hispanic or Latino (13), White | Not Hispanic or Latino (10)
- **tissue**: prefrontal cortex (36)

## Field presence

- Cause of death: 36/36
- age: 36/36 (canon: age)
- be in blood (mg/l): 36/36
- be in brain (mg/kg): 36/36
- case/control: 36/36
- cocaine in blood (mg/l): 36/36
- cocaine in brain (mg/kg): 36/36
- ethnicity: 36/36 (canon: ethnicity)
- manner of death: 17/36
- ph: 36/36
- pmi (hours): 36/36
- race: 36/36 (canon: ethnicity)
- tissue: 36/36 (canon: tissue)

## Evidence for WARN/FAIL checks

### source_tissue (WARN)
### metadata_completeness (WARN)
### disease_relevance (FAIL)

Decision: REJECT

Reasons:
- disease_relevance: no NAFLD-spectrum term in series or sample metadata (no NAFLD-spectrum term found in series or sample metadata)
<!-- /computed -->