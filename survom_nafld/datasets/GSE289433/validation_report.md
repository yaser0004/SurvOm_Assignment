# Validation report: GSE289433

Transcription factor REST regulates activation and growth of human Hepatic Stellate Cells

<!-- computed -->
Sample count: 8

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 8 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 8/8 |
| source_tissue | PASS | liver-pattern source 8/8 |
| library_strategy | PASS | RNA-Seq 8/8 |
| library_source | PASS | transcriptomic 8/8 |
| library_selection | PASS | cDNA 8/8 |
| instrument_model | PASS | Illumina NovaSeq 6000 8/8 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (8/8 samples) |
| expression_data_availability | PASS | processed per-sample counts (8/8), packaged in GSE289433_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE289433_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX27658220, https://www.ncbi.nlm.nih.gov/sra?term=SRX27658221, https://www.ncbi.nlm.nih.gov/sra?term=SRX27658222, https://www.ncbi.nlm.nih.gov/sra?term=SRX27658223, https://www.ncbi.nlm.nih.gov/sra?term=SRX27658224, and 3 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Liver (8)
- **treatment**: REST siRNA (4), Scrambled siRNA (4)

## Field presence

- cell line: 8/8
- cell type: 8/8
- tissue: 8/8 (canon: tissue)
- treatment: 8/8 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE289433 / Series_summary: matched `metabolic dysfunction-associated stea` in "Activation of hepatic stellate cells (HSC) is a key component in the progression of metabolic dysfunction-associated steatotic liver disease (MASLD) to metabolic-associated steatohepatitis (MASH) and "
### material_type (WARN)
- GSM8791416 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary human Hepatic Stellate Cells"
- GSM8791417 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary human Hepatic Stellate Cells"
- GSM8791418 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary human Hepatic Stellate Cells"
- GSM8791419 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary human Hepatic Stellate Cells"
- GSM8791420 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary human Hepatic Stellate Cells"
- GSM8791421 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary human Hepatic Stellate Cells"
- GSM8791422 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary human Hepatic Stellate Cells"
- GSM8791423 / Sample_characteristics_ch1: matched `cell line` in "cell line: Primary human Hepatic Stellate Cells"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 8 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (8/8 samples)
<!-- /computed -->