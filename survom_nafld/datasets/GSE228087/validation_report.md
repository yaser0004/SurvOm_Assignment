# Validation report: GSE228087

Monocyte-derived Macrophages

<!-- computed -->
Sample count: 16

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 16 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 16/16 |
| source_tissue | WARN | liver-pattern source 0/16; off-target tissue signal detected |
| library_strategy | PASS | RNA-Seq 16/16 |
| library_source | PASS | transcriptomic 16/16 |
| library_selection | PASS | cDNA 16/16 |
| instrument_model | PASS | Illumina HiSeq 2000 16/16 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | INFO | series prose mentions in vitro; sample metadata does not corroborate |
| expression_data_availability | PASS | processed series-level file: GSE228087_MoMF_counts.csv.gz |
| series_matrix | INFO | present, metadata-only (GSE228087_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX19758688, https://www.ncbi.nlm.nih.gov/sra?term=SRX19758689, https://www.ncbi.nlm.nih.gov/sra?term=SRX19758690, https://www.ncbi.nlm.nih.gov/sra?term=SRX19758691, https://www.ncbi.nlm.nih.gov/sra?term=SRX19758692, and 11 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: blood (PBMC) (16)
- **treatment**: M-CSF (5), M-CSF+IL4_+IL13 (5), M-CSF+LPS+IFN-gamma (4), Untreated control (2)

## Field presence

- cell type: 16/16
- donor id: 16/16
- tissue: 16/16 (canon: tissue)
- treatment: 16/16 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
- GSM7113703 / Sample_source_name_ch1: matched `PBMC` in "blood (PBMC)"
- GSM7113704 / Sample_source_name_ch1: matched `PBMC` in "blood (PBMC)"
- GSM7113705 / Sample_source_name_ch1: matched `PBMC` in "blood (PBMC)"
- GSM7113706 / Sample_source_name_ch1: matched `PBMC` in "blood (PBMC)"
- GSM7113707 / Sample_source_name_ch1: matched `PBMC` in "blood (PBMC)"
- GSM7113708 / Sample_source_name_ch1: matched `PBMC` in "blood (PBMC)"
- GSM7113709 / Sample_source_name_ch1: matched `PBMC` in "blood (PBMC)"
- GSM7113710 / Sample_source_name_ch1: matched `PBMC` in "blood (PBMC)"
- GSM7113711 / Sample_source_name_ch1: matched `PBMC` in "blood (PBMC)"
- GSM7113712 / Sample_source_name_ch1: matched `PBMC` in "blood (PBMC)"
- GSM7113713 / Sample_source_name_ch1: matched `PBMC` in "blood (PBMC)"
- GSM7113714 / Sample_source_name_ch1: matched `PBMC` in "blood (PBMC)"
- GSM7113715 / Sample_source_name_ch1: matched `PBMC` in "blood (PBMC)"
- GSM7113716 / Sample_source_name_ch1: matched `PBMC` in "blood (PBMC)"
- GSM7113717 / Sample_source_name_ch1: matched `PBMC` in "blood (PBMC)"
- GSM7113718 / Sample_source_name_ch1: matched `PBMC` in "blood (PBMC)"
- GSM7113703 / Sample_characteristics_ch1: matched `PBMC` in "tissue: blood (PBMC)"
- GSM7113704 / Sample_characteristics_ch1: matched `PBMC` in "tissue: blood (PBMC)"
- GSM7113705 / Sample_characteristics_ch1: matched `PBMC` in "tissue: blood (PBMC)"
- GSM7113706 / Sample_characteristics_ch1: matched `PBMC` in "tissue: blood (PBMC)"
- GSM7113707 / Sample_characteristics_ch1: matched `PBMC` in "tissue: blood (PBMC)"
- GSM7113708 / Sample_characteristics_ch1: matched `PBMC` in "tissue: blood (PBMC)"
- GSM7113709 / Sample_characteristics_ch1: matched `PBMC` in "tissue: blood (PBMC)"
- GSM7113710 / Sample_characteristics_ch1: matched `PBMC` in "tissue: blood (PBMC)"
- GSM7113711 / Sample_characteristics_ch1: matched `PBMC` in "tissue: blood (PBMC)"
- GSM7113712 / Sample_characteristics_ch1: matched `PBMC` in "tissue: blood (PBMC)"
- GSM7113713 / Sample_characteristics_ch1: matched `PBMC` in "tissue: blood (PBMC)"
- GSM7113714 / Sample_characteristics_ch1: matched `PBMC` in "tissue: blood (PBMC)"
- GSM7113715 / Sample_characteristics_ch1: matched `PBMC` in "tissue: blood (PBMC)"
- GSM7113716 / Sample_characteristics_ch1: matched `PBMC` in "tissue: blood (PBMC)"
- GSM7113717 / Sample_characteristics_ch1: matched `PBMC` in "tissue: blood (PBMC)"
- GSM7113718 / Sample_characteristics_ch1: matched `PBMC` in "tissue: blood (PBMC)"
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE228087 / Series_summary: matched `steatohepatitis` in "Chronic liver diseases as non-alcoholic steatohepatitis (NASH)-induced cirrhosis are characterized by an increasing accumulation of stressed, damaged, or dying hepatocytes. Hepatocyte damage triggers "

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 16 samples (below 20)
- source_tissue: liver-pattern source 0/16; off-target tissue signal detected
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
<!-- /computed -->