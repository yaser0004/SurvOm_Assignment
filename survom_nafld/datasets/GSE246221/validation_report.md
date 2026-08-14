# Validation report: GSE246221

A Mouse Model for Metabolic Dysfunction-associated Steatotic Liver Disease and Hepatocellular Carcinoma [RNA-seq]

<!-- computed -->
Sample count: 148

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 148 samples |
| organism_consistency | WARN | mixed organisms: Homo sapiens 32/148, Mus musculus 116/148 |
| source_tissue | PASS | liver-pattern source 148/148 |
| library_strategy | PASS | RNA-Seq 148/148 |
| library_source | PASS | transcriptomic 148/148 |
| library_selection | PASS | cDNA 148/148 |
| instrument_model | PASS | Illumina NovaSeq 6000 148/148 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (28 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE246221_rawcounts_allsamples_human.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE246221-GPL24247_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX22224738, https://www.ncbi.nlm.nih.gov/sra?term=SRX22224739, https://www.ncbi.nlm.nih.gov/sra?term=SRX22224740, https://www.ncbi.nlm.nih.gov/sra?term=SRX22224741, https://www.ncbi.nlm.nih.gov/sra?term=SRX22224742, and 143 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 14 weeks (5), 20 weeks (17), 26 weeks (8), 32 weeks (25), 38 weeks (8), 44 weeks (9), 50 weeks (16), 52 weeks (8), 56 weeks (12), 7 weeks (5), 8 weeks (3)
- **sex**: Female (8), Male (140)
- **tissue**: Liver (134), Liver (tumor) (14)

## Field presence

- Sex: 148/148 (canon: sex)
- age: 116/148 (canon: age)
- diet: 116/148
- drug treatment: 116/148
- genotype: 116/148
- strain: 116/148
- streptozotocin treatment: 116/148
- tissue: 148/148 (canon: tissue)

## Evidence for WARN/FAIL checks

### organism_consistency (WARN)
### metadata_completeness (WARN)

Decision: MANUAL_REVIEW

Reasons:
- organism_consistency: mixed organisms: Homo sapiens 32/148, Mus musculus 116/148
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
<!-- /computed -->