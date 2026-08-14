# Validation report: GSE205881

RNA Sequencing Facilitates Quantitative Analysis of Humanized Normal Livers, NASH Livers, and HCC Transcriptomes

<!-- computed -->
Sample count: 66

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 66 samples |
| organism_consistency | PASS | Homo sapiens | Mus musculus 66/66 |
| source_tissue | WARN | liver-pattern source 36/66 |
| library_strategy | PASS | RNA-Seq 66/66 |
| library_source | PASS | transcriptomic 66/66 |
| library_selection | PASS | cDNA 66/66 |
| instrument_model | PASS | Illumina HiSeq 2000 66/66 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (24 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX15675771, https://www.ncbi.nlm.nih.gov/sra?term=SRX15675772, https://www.ncbi.nlm.nih.gov/sra?term=SRX15675773, https://www.ncbi.nlm.nih.gov/sra?term=SRX15675774, https://www.ncbi.nlm.nih.gov/sra?term=SRX15675775, and 61 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE205881_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX15675771, https://www.ncbi.nlm.nih.gov/sra?term=SRX15675772, https://www.ncbi.nlm.nih.gov/sra?term=SRX15675773, https://www.ncbi.nlm.nih.gov/sra?term=SRX15675774, https://www.ncbi.nlm.nih.gov/sra?term=SRX15675775, and 61 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: h-HCC (30), h-Liver (36)

## Field presence

- genotype: 66/66
- strain: 66/66
- tissue: 66/66 (canon: tissue)

## Evidence for WARN/FAIL checks

### source_tissue (WARN)
### metadata_completeness (WARN)

Decision: MANUAL_REVIEW

Reasons:
- source_tissue: liver-pattern source 36/66
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
<!-- /computed -->