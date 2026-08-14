# Validation report: GSE246223

A Mouse Model for Metabolic Dysfunction-associated Steatotic Liver Disease and Hepatocellular Carcinoma

<!-- computed -->
Sample count: 160

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 160 samples |
| organism_consistency | WARN | mixed organisms: Homo sapiens 32/160, Mus musculus 128/160 |
| source_tissue | PASS | liver-pattern source 160/160 |
| library_strategy | WARN | mixed strategies: ATAC-seq 12/160, RNA-Seq 148/160 |
| library_source | WARN | library_source: genomic 12/160, transcriptomic 148/160 |
| library_selection | WARN | mixed library_selection: cDNA 148/160, other 12/160 |
| instrument_model | WARN | mixed instruments: HiSeq X Ten 12/160, Illumina NovaSeq 6000 148/160 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (28 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX22219328, https://www.ncbi.nlm.nih.gov/sra?term=SRX22219329, https://www.ncbi.nlm.nih.gov/sra?term=SRX22219330, https://www.ncbi.nlm.nih.gov/sra?term=SRX22219331, https://www.ncbi.nlm.nih.gov/sra?term=SRX22219332, and 155 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE246223-GPL21273_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX22219328, https://www.ncbi.nlm.nih.gov/sra?term=SRX22219329, https://www.ncbi.nlm.nih.gov/sra?term=SRX22219330, https://www.ncbi.nlm.nih.gov/sra?term=SRX22219331, https://www.ncbi.nlm.nih.gov/sra?term=SRX22219332, and 155 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 14 weeks (5), 20 weeks (29), 26 weeks (8), 32 weeks (25), 38 weeks (8), 44 weeks (9), 50 weeks (16), 52 weeks (8), 56 weeks (12), 7 weeks (5), 8 weeks (3)
- **sex**: Female (8), Male (152)
- **tissue**: Liver (146), Liver (tumor) (14)

## Field presence

- Sex: 160/160 (canon: sex)
- age: 128/160 (canon: age)
- diet: 128/160
- drug treatment: 128/160
- genotype: 128/160
- strain: 128/160
- streptozotocin treatment: 128/160
- tissue: 160/160 (canon: tissue)

## Evidence for WARN/FAIL checks

### organism_consistency (WARN)
### library_strategy (WARN)
### library_source (WARN)
### library_selection (WARN)
### instrument_model (WARN)
### metadata_completeness (WARN)

Decision: MANUAL_REVIEW

Reasons:
- organism_consistency: mixed organisms: Homo sapiens 32/160, Mus musculus 128/160
- library_strategy: mixed strategies: ATAC-seq 12/160, RNA-Seq 148/160
- library_source: library_source: genomic 12/160, transcriptomic 148/160
- library_selection: mixed library_selection: cDNA 148/160, other 12/160
- instrument_model: mixed instruments: HiSeq X Ten 12/160, Illumina NovaSeq 6000 148/160
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
<!-- /computed -->