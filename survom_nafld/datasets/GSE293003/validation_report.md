# Validation report: GSE293003

Hepatocyte FoxO1 depletion exacerbates hepatic inflammation in MASH

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
| instrument_model | PASS | Illumina NovaSeq X Plus 6/6 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (6/6 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX28143691, https://www.ncbi.nlm.nih.gov/sra?term=SRX28143692, https://www.ncbi.nlm.nih.gov/sra?term=SRX28143693, https://www.ncbi.nlm.nih.gov/sra?term=SRX28143694, https://www.ncbi.nlm.nih.gov/sra?term=SRX28143695, and 1 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE293003_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX28143691, https://www.ncbi.nlm.nih.gov/sra?term=SRX28143692, https://www.ncbi.nlm.nih.gov/sra?term=SRX28143693, https://www.ncbi.nlm.nih.gov/sra?term=SRX28143694, https://www.ncbi.nlm.nih.gov/sra?term=SRX28143695, and 1 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: liver (6)
- **treatment**: LPS (6)

## Field presence

- cell line: 6/6
- cell type: 6/6
- genotype: 6/6
- tissue: 6/6 (canon: tissue)
- treatment: 6/6 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE293003 / Series_title: matched `MASH` in "Hepatocyte FoxO1 depletion exacerbates hepatic inflammation in MASH"
- GSE293003 / Series_summary: matched `metabolic dysfunction-associated stea` in "The transcription factor Forkhead box protein O1 (FoxO1) is a well-established regulator of glucose and lipid metabolism, yet its role in metabolic dysfunction-associated steatohepatitis (MASH) pathog"
### material_type (WARN)
- GSM8873338 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8873339 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8873340 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8873341 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8873342 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8873343 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 6 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (6/6 samples)
<!-- /computed -->