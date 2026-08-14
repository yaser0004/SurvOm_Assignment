# Validation report: GSE173736

Transcriptional regulation of liver lipotoxicity in non-alcoholic steatohepatitis

<!-- computed -->
Sample count: 52

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 52 samples |
| organism_consistency | WARN | mixed organisms: Homo sapiens 16/52, Mus musculus 36/52 |
| source_tissue | PASS | liver-pattern source 52/52 |
| library_strategy | WARN | mixed strategies: ATAC-seq 14/52, RNA-Seq 38/52 |
| library_source | WARN | library_source: genomic 14/52, transcriptomic 38/52 |
| library_selection | WARN | mixed library_selection: cDNA 38/52, other 14/52 |
| instrument_model | WARN | mixed instruments: Illumina NextSeq 500 28/52, Illumina NovaSeq 6000 24/52 |
| metadata_completeness | WARN | patchy fields: tissue 14/52, treatment 38/52. reported consistently: disease; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (8 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX10756533, https://www.ncbi.nlm.nih.gov/sra?term=SRX10756534, https://www.ncbi.nlm.nih.gov/sra?term=SRX10756535, https://www.ncbi.nlm.nih.gov/sra?term=SRX10756536, https://www.ncbi.nlm.nih.gov/sra?term=SRX10756537, and 47 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE173736-GPL18573_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX10756533, https://www.ncbi.nlm.nih.gov/sra?term=SRX10756534, https://www.ncbi.nlm.nih.gov/sra?term=SRX10756535, https://www.ncbi.nlm.nih.gov/sra?term=SRX10756536, https://www.ncbi.nlm.nih.gov/sra?term=SRX10756537, and 47 more (see sample_metadata.csv) |

## Canonical field distributions

- **disease**: BSA (18), Healthy (8), NASH (8), PAL (18)
- **tissue**: FL83B hepatocytes (6), Liver (8)
- **treatment**: Mafk sgRNA (6), Tcf4 sgRNA (6), non-targeting sgRNA (12), none (14)

## Field presence

- condition: 52/52 (canon: disease)
- tissue: 14/52 (canon: tissue)
- tissue/cell type: 38/52
- treatment: 38/52 (canon: treatment)

## Evidence for WARN/FAIL checks

### organism_consistency (WARN)
### library_strategy (WARN)
### library_source (WARN)
### library_selection (WARN)
### instrument_model (WARN)
### metadata_completeness (WARN)

Decision: MANUAL_REVIEW

Reasons:
- organism_consistency: mixed organisms: Homo sapiens 16/52, Mus musculus 36/52
- library_strategy: mixed strategies: ATAC-seq 14/52, RNA-Seq 38/52
- library_source: library_source: genomic 14/52, transcriptomic 38/52
- library_selection: mixed library_selection: cDNA 38/52, other 14/52
- instrument_model: mixed instruments: Illumina NextSeq 500 28/52, Illumina NovaSeq 6000 24/52
- metadata_completeness: patchy fields: tissue 14/52, treatment 38/52. reported consistently: disease; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade
<!-- /computed -->