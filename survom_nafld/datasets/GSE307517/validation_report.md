# Validation report: GSE307517

ClinASO: a guideline for rapid drug discovery of gapmer antisense oligonucleotidess

<!-- computed -->
Sample count: 12

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 12 samples (below 20) |
| organism_consistency | WARN | mixed organisms: Homo sapiens 6/12, Mus musculus 6/12 |
| source_tissue | WARN | liver-pattern source 6/12 |
| library_strategy | PASS | RNA-Seq 12/12 |
| library_source | PASS | transcriptomic 12/12 |
| library_selection | PASS | cDNA 12/12 |
| instrument_model | PASS | GenoLab M 12/12 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (6/12 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX30408912, https://www.ncbi.nlm.nih.gov/sra?term=SRX30408913, https://www.ncbi.nlm.nih.gov/sra?term=SRX30408914, https://www.ncbi.nlm.nih.gov/sra?term=SRX30408915, https://www.ncbi.nlm.nih.gov/sra?term=SRX30408916, and 7 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE307517-GPL35109_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX30408912, https://www.ncbi.nlm.nih.gov/sra?term=SRX30408913, https://www.ncbi.nlm.nih.gov/sra?term=SRX30408914, https://www.ncbi.nlm.nih.gov/sra?term=SRX30408915, https://www.ncbi.nlm.nih.gov/sra?term=SRX30408916, and 7 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: liver (6)

## Field presence

- cell line: 6/12
- tissue: 6/12 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### organism_consistency (WARN)
### source_tissue (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE307517 / Series_summary: matched `Metabolic dysfunction-associated stea` in "Metabolic dysfunction-associated steatotic liver disease (MASLD) is a chronic disorder that threatens global health, yet current treatments lack efficacy and patient compliance. Antisense oligonucleot"
### material_type (WARN)
- GSM9241120 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep-G2"
- GSM9241121 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep-G2"
- GSM9241122 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep-G2"
- GSM9241123 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep-G2"
- GSM9241124 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep-G2"
- GSM9241125 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep-G2"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 12 samples (below 20)
- organism_consistency: mixed organisms: Homo sapiens 6/12, Mus musculus 6/12
- source_tissue: liver-pattern source 6/12
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (6/12 samples)
<!-- /computed -->