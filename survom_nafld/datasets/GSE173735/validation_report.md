# Validation report: GSE173735

Transcriptional regulation of liver lipotoxicity in non-alcoholic steatohepatitis [RNA-seq]

<!-- computed -->
Sample count: 38

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 38 samples |
| organism_consistency | WARN | mixed organisms: Homo sapiens 8/38, Mus musculus 30/38 |
| source_tissue | PASS | liver-pattern source 38/38 |
| library_strategy | PASS | RNA-Seq 38/38 |
| library_source | PASS | transcriptomic 38/38 |
| library_selection | PASS | cDNA 38/38 |
| instrument_model | WARN | mixed instruments: Illumina NextSeq 500 14/38, Illumina NovaSeq 6000 24/38 |
| metadata_completeness | PASS | reported consistently: disease, treatment; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade, tissue |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (4 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX10756533, https://www.ncbi.nlm.nih.gov/sra?term=SRX10756534, https://www.ncbi.nlm.nih.gov/sra?term=SRX10756535, https://www.ncbi.nlm.nih.gov/sra?term=SRX10756536, https://www.ncbi.nlm.nih.gov/sra?term=SRX10756537, and 33 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE173735-GPL18573_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX10756533, https://www.ncbi.nlm.nih.gov/sra?term=SRX10756534, https://www.ncbi.nlm.nih.gov/sra?term=SRX10756535, https://www.ncbi.nlm.nih.gov/sra?term=SRX10756536, https://www.ncbi.nlm.nih.gov/sra?term=SRX10756537, and 33 more (see sample_metadata.csv) |

## Canonical field distributions

- **disease**: BSA (15), Healthy (4), NASH (4), PAL (15)
- **treatment**: Mafk sgRNA (6), Tcf4 sgRNA (6), non-targeting sgRNA (12), none (14)

## Field presence

- condition: 38/38 (canon: disease)
- tissue/cell type: 38/38
- treatment: 38/38 (canon: treatment)

## Evidence for WARN/FAIL checks

### organism_consistency (WARN)
### instrument_model (WARN)

Decision: MANUAL_REVIEW

Reasons:
- organism_consistency: mixed organisms: Homo sapiens 8/38, Mus musculus 30/38
- instrument_model: mixed instruments: Illumina NextSeq 500 14/38, Illumina NovaSeq 6000 24/38
<!-- /computed -->