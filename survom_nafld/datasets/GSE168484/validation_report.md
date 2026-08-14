# Validation report: GSE168484

Hepatic miR20b promotes nonalcholic fatty liver diseases by targeting PPARα

<!-- computed -->
Sample count: 6

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 6 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 6/6 |
| source_tissue | PASS | liver-pattern source 6/6 |
| library_strategy | PASS | RNA-Seq 6/6 |
| library_source | PASS | transcriptomic 6/6 |
| library_selection | PASS | cDNA 6/6 |
| instrument_model | PASS | Illumina HiSeq 2000 6/6 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: HepG2 (6/6 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX10272908, https://www.ncbi.nlm.nih.gov/sra?term=SRX10272909, https://www.ncbi.nlm.nih.gov/sra?term=SRX10272910, https://www.ncbi.nlm.nih.gov/sra?term=SRX10272911, https://www.ncbi.nlm.nih.gov/sra?term=SRX10272912, and 1 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE168484_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX10272908, https://www.ncbi.nlm.nih.gov/sra?term=SRX10272909, https://www.ncbi.nlm.nih.gov/sra?term=SRX10272910, https://www.ncbi.nlm.nih.gov/sra?term=SRX10272911, https://www.ncbi.nlm.nih.gov/sra?term=SRX10272912, and 1 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: liver (6)

## Field presence

- cell type: 6/6
- tissue: 6/6 (canon: tissue)
- transfection: 6/6

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE168484 / Series_title: matched `fatty liver` in "Hepatic miR20b promotes nonalcholic fatty liver diseases by targeting PPARα"
- GSE168484 / Series_summary: matched `non-alcoholic fatty liver` in "Nuclear receptors (NRs) play a crucial role in non-alcoholic fatty liver disease (NAFLD) and have been widely studied(Tran et al. 2018). However, the underlying mechanisms of NR regulation remain larg"
### material_type (WARN)
- GSM5144628 / Sample_source_name_ch1: matched `HepG2` in "Liver HepG2 cells"
- GSM5144629 / Sample_source_name_ch1: matched `HepG2` in "Liver HepG2 cells"
- GSM5144630 / Sample_source_name_ch1: matched `HepG2` in "Liver HepG2 cells"
- GSM5144631 / Sample_source_name_ch1: matched `HepG2` in "Liver HepG2 cells"
- GSM5144632 / Sample_source_name_ch1: matched `HepG2` in "Liver HepG2 cells"
- GSM5144633 / Sample_source_name_ch1: matched `HepG2` in "Liver HepG2 cells"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 6 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: HepG2 (6/6 samples)
<!-- /computed -->