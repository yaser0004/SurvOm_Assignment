# Validation report: GSE326385

Fucoxanthin ameliorates metabolic dysfunction-associated steatohepatitis via suppression of CD36-driven fatty acid uptake

<!-- computed -->
Sample count: 18

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 18 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 18/18 |
| source_tissue | PASS | liver-pattern source 18/18 |
| library_strategy | PASS | RNA-Seq 18/18 |
| library_source | PASS | transcriptomic 18/18 |
| library_selection | PASS | cDNA 18/18 |
| instrument_model | PASS | Illumina NovaSeq X Plus 18/18 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (18/18 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX32714933, https://www.ncbi.nlm.nih.gov/sra?term=SRX32714934, https://www.ncbi.nlm.nih.gov/sra?term=SRX32714935, https://www.ncbi.nlm.nih.gov/sra?term=SRX32714936, https://www.ncbi.nlm.nih.gov/sra?term=SRX32714937, and 13 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE326385_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX32714933, https://www.ncbi.nlm.nih.gov/sra?term=SRX32714934, https://www.ncbi.nlm.nih.gov/sra?term=SRX32714935, https://www.ncbi.nlm.nih.gov/sra?term=SRX32714936, https://www.ncbi.nlm.nih.gov/sra?term=SRX32714937, and 13 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: liver (18)

## Field presence

- cell line: 18/18
- cell type: 18/18
- tissue: 18/18 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE326385 / Series_title: matched `metabolic dysfunction-associated stea` in "Fucoxanthin ameliorates metabolic dysfunction-associated steatohepatitis via suppression of CD36-driven fatty acid uptake"
- GSE326385 / Series_summary: matched `Metabolic dysfunction-associated stea` in "Metabolic dysfunction-associated steatohepatitis (MASH) is a progressive liver disease with limited treatment options. Here, we demonstrate that fucoxanthin (FUCO), a natural marine carotenoid, amelio"
- GSE326385 / Series_overall_design: matched `steatosis` in "RNA seq profiling of fucoxanthin-treated Hep3B steatosis model"
### material_type (WARN)
- GSM9630293 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B"
- GSM9630294 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B"
- GSM9630295 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B"
- GSM9630296 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B"
- GSM9630297 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B"
- GSM9630298 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B"
- GSM9630299 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B"
- GSM9630300 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B"
- GSM9630301 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B"
- GSM9630302 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B"
- GSM9630303 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B"
- GSM9630304 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B"
- GSM9630305 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B"
- GSM9630306 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B"
- GSM9630307 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B"
- GSM9630308 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B"
- GSM9630309 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B"
- GSM9630310 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 18 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (18/18 samples)
<!-- /computed -->