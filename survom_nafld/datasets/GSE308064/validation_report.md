# Validation report: GSE308064

PAD4⁺ Neutrophils Promote Hepatic Stellate Cell Activation and Accelerate MASH Fibrosis Progression via NETs-DNA/TAOK1/MAPK Pathways

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
| instrument_model | PASS | BGISEQ-500 6/6 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: LX-2, cell line (6/6 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX23505873, https://www.ncbi.nlm.nih.gov/sra?term=SRX23505874, https://www.ncbi.nlm.nih.gov/sra?term=SRX23505875, https://www.ncbi.nlm.nih.gov/sra?term=SRX23505876, https://www.ncbi.nlm.nih.gov/sra?term=SRX23505877, and 1 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE308064_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX23505873, https://www.ncbi.nlm.nih.gov/sra?term=SRX23505874, https://www.ncbi.nlm.nih.gov/sra?term=SRX23505875, https://www.ncbi.nlm.nih.gov/sra?term=SRX23505876, https://www.ncbi.nlm.nih.gov/sra?term=SRX23505877, and 1 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Human liver (6)
- **treatment**: NETs (3), neutrophi (3)

## Field presence

- batch: 6/6
- cell line: 6/6
- cell type: 6/6
- genotype: 6/6
- tissue: 6/6 (canon: tissue)
- treatment: 6/6 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE308064 / Series_title: matched `MASH` in "PAD4⁺ Neutrophils Promote Hepatic Stellate Cell Activation and Accelerate MASH Fibrosis Progression via NETs-DNA/TAOK1/MAPK Pathways"
- GSE308064 / Series_summary: matched `steatohepatitis` in "Neutrophils play a pivotal role in the progression of metabolic-associated steatohepatitis (MASH) by mediating inflammatory responses. However, the heterogeneity of neutrophil subsets in MASH and thei"
### material_type (WARN)
- GSM9237356 / Sample_title: matched `LX-2` in "Human liver stellate cells LX-2 after neutrophil intervention, con1"
- GSM9237357 / Sample_title: matched `LX-2` in "Human liver stellate cells LX-2 after neutrophil intervention, con2"
- GSM9237358 / Sample_title: matched `LX-2` in "Human liver stellate cells LX-2 after neutrophil intervention, con3"
- GSM9237359 / Sample_title: matched `LX-2` in "Human liver stellate cells LX-2 after NETs intervention, exp1"
- GSM9237360 / Sample_title: matched `LX-2` in "Human liver stellate cells LX-2 after NETs intervention, exp2"
- GSM9237361 / Sample_title: matched `LX-2` in "Human liver stellate cells LX-2 after NETs intervention, exp3"
- GSM9237356 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM9237357 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM9237358 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM9237359 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM9237360 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM9237361 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 6 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: LX-2, cell line (6/6 samples)
<!-- /computed -->