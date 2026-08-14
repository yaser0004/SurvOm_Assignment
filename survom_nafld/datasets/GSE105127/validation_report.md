# Validation report: GSE105127

Epigenomic analysis of micro-dissected human liver reveals principles of zonated morphogenic and metabolic control

<!-- computed -->
Sample count: 114

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 114 samples |
| organism_consistency | PASS | Homo sapiens 114/114 |
| source_tissue | PASS | liver-pattern source 114/114 |
| library_strategy | WARN | mixed strategies: Bisulfite-Seq 57/114, RNA-Seq 57/114 |
| library_source | WARN | library_source: genomic 57/114, transcriptomic 57/114 |
| library_selection | WARN | mixed library_selection: Reduced Representation 57/114, cDNA 57/114 |
| instrument_model | PASS | Illumina HiSeq 2500 114/114 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX3298622, https://www.ncbi.nlm.nih.gov/sra?term=SRX3298623, https://www.ncbi.nlm.nih.gov/sra?term=SRX3298624, https://www.ncbi.nlm.nih.gov/sra?term=SRX3298625, https://www.ncbi.nlm.nih.gov/sra?term=SRX3298626, and 109 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE105127_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX3298622, https://www.ncbi.nlm.nih.gov/sra?term=SRX3298623, https://www.ncbi.nlm.nih.gov/sra?term=SRX3298624, https://www.ncbi.nlm.nih.gov/sra?term=SRX3298625, https://www.ncbi.nlm.nih.gov/sra?term=SRX3298626, and 109 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: liver (114)

## Field presence

- hepatic zone: 114/114
- isolation: 114/114
- tissue: 114/114 (canon: tissue)

## Evidence for WARN/FAIL checks

### library_strategy (WARN)
### library_source (WARN)
### library_selection (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE105127 / Series_overall_design: matched `steatosis` in "The study comprises 19 human liver biopsy donors divided into the groups normal control (NC = 7012, 7173, 7194, 7279), healthy obese (HO = 6758, 6922, 7213, 7230, 7252), bland steatosis (STEA = 6967, "

Decision: MANUAL_REVIEW

Reasons:
- library_strategy: mixed strategies: Bisulfite-Seq 57/114, RNA-Seq 57/114
- library_source: library_source: genomic 57/114, transcriptomic 57/114
- library_selection: mixed library_selection: Reduced Representation 57/114, cDNA 57/114
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
<!-- /computed -->