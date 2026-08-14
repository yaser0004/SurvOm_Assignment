# Validation report: GSE341780

ERα/miR-26a/ANKRD52 axis regulates progression of MASH- associated HCC in HDTVi HCC models

<!-- computed -->
Sample count: 6

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 6 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 6/6 |
| source_tissue | WARN | liver-pattern source 0/6 |
| library_strategy | PASS | RNA-Seq 6/6 |
| library_source | PASS | transcriptomic 6/6 |
| library_selection | PASS | cDNA 6/6 |
| instrument_model | PASS | Illumina NovaSeq 6000 6/6 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (6/6 samples) |
| expression_data_availability | PASS | processed series-level file: GSE341780_gene_count_matrix.xlsx |
| series_matrix | INFO | present, metadata-only (GSE341780_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX34563676, https://www.ncbi.nlm.nih.gov/sra?term=SRX34563677, https://www.ncbi.nlm.nih.gov/sra?term=SRX34563678, https://www.ncbi.nlm.nih.gov/sra?term=SRX34563679, https://www.ncbi.nlm.nih.gov/sra?term=SRX34563680, and 1 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: cell culture (6)
- **treatment**: shANKRD52, treatment (1), shNC, control (1), siANKRD52, treatment (2), siNC, control (2)

## Field presence

- cell line: 6/6
- tissue: 6/6 (canon: tissue)
- treatment: 6/6 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE341780 / Series_title: matched `MASH` in "ERα/miR-26a/ANKRD52 axis regulates progression of MASH- associated HCC in HDTVi HCC models"
- GSE341780 / Series_summary: matched `metabolic dysfunction-associated stea` in "The lack of robust mouse models for metabolic dysfunction-associated steatohepatitis-hepatocellular carcinoma (MASH-HCC) severely hinders mechanistic investigation and therapeutic drug development. Co"
- GSE341780 / Series_overall_design: matched `MASH` in "Herein, we combined hydrodynamic tail vein injection (HDTVi) with the Sleeping Beauty (SB) transposon system and oncogenic drivers to generate mouse MASH-HCC models and longitudinally monitor tumor de"
### material_type (WARN)
- GSM9916831 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3b"
- GSM9916832 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3b"
- GSM9916833 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3b"
- GSM9916834 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3b"
- GSM9916835 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3b"
- GSM9916836 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3b"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 6 samples (below 20)
- source_tissue: liver-pattern source 0/6
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (6/6 samples)
<!-- /computed -->