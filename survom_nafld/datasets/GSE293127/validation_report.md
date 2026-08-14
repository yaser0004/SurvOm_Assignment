# Validation report: GSE293127

Activation of the Imprinted Gene Network is a conserved signature of MASLD induced by the early life environment

<!-- computed -->
Sample count: 28

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 28 samples |
| organism_consistency | PASS | Homo sapiens 28/28 |
| source_tissue | PASS | liver-pattern source 28/28 |
| library_strategy | PASS | RNA-Seq 28/28 |
| library_source | PASS | transcriptomic 28/28 |
| library_selection | PASS | cDNA 28/28 |
| instrument_model | PASS | Illumina NovaSeq 6000 28/28 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: HepG2, cell line (28/28 samples) |
| expression_data_availability | PASS | processed series-level file: GSE293127_All_counts.csv.gz |
| series_matrix | INFO | present, metadata-only (GSE293127_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX28167004, https://www.ncbi.nlm.nih.gov/sra?term=SRX28167005, https://www.ncbi.nlm.nih.gov/sra?term=SRX28167006, https://www.ncbi.nlm.nih.gov/sra?term=SRX28167007, https://www.ncbi.nlm.nih.gov/sra?term=SRX28167008, and 23 more (see sample_metadata.csv) |

## Canonical field distributions

- **treatment**: BPA (4), CdCl2 (4), DMSO (4), H2O (4), PFOS (4), TBTCl (4), TCDD (4)

## Field presence

- cell line: 28/28
- cell type: 28/28
- treatment: 28/28 (canon: treatment)

## Evidence for WARN/FAIL checks

### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE293127 / Series_title: matched `MASLD` in "Activation of the Imprinted Gene Network is a conserved signature of MASLD induced by the early life environment"
- GSE293127 / Series_summary: matched `Metabolic dysfunction-associated stea` in "Metabolic dysfunction-associated steatotic liver disease (MASLD) affects 30% of the world population. Its prevalence in the pediatric population is increasing, suggesting that the early life environme"
### material_type (WARN)
- GSM8877024 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877025 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877026 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877027 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877028 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877029 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877030 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877031 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877032 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877033 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877034 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877035 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877036 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877037 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877038 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877039 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877040 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877041 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877042 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877043 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877044 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877045 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877046 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877047 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877048 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877049 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877050 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877051 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM8877024 / Sample_title: matched `HepG2` in "HepG2 cells, control H2O rep 1"
- GSM8877025 / Sample_title: matched `HepG2` in "HepG2 cells, control H2O rep 2"
- GSM8877026 / Sample_title: matched `HepG2` in "HepG2 cells, control H2O rep 3"
- GSM8877027 / Sample_title: matched `HepG2` in "HepG2 cells, control H2O rep 4"
- GSM8877028 / Sample_title: matched `HepG2` in "HepG2 cells, CdCl2 rep 1"
- GSM8877029 / Sample_title: matched `HepG2` in "HepG2 cells, CdCl2 rep 2"
- GSM8877030 / Sample_title: matched `HepG2` in "HepG2 cells, CdCl2 rep 3"
- GSM8877031 / Sample_title: matched `HepG2` in "HepG2 cells, CdCl2 rep 4"
- GSM8877032 / Sample_title: matched `HepG2` in "HepG2 cells, control DMSO, rep 1"
- GSM8877033 / Sample_title: matched `HepG2` in "HepG2 cells, control DMSO, rep 2"
- GSM8877034 / Sample_title: matched `HepG2` in "HepG2 cells, control DMSO, rep 3"
- GSM8877035 / Sample_title: matched `HepG2` in "HepG2 cells, control DMSO, rep 4"
- GSM8877036 / Sample_title: matched `HepG2` in "HepG2 cells, TCDD, rep 1"
- GSM8877037 / Sample_title: matched `HepG2` in "HepG2 cells, TCDD, rep 2"
- GSM8877038 / Sample_title: matched `HepG2` in "HepG2 cells, TCDD, rep 3"
- GSM8877039 / Sample_title: matched `HepG2` in "HepG2 cells, TCDD, rep 4"
- GSM8877040 / Sample_title: matched `HepG2` in "HepG2 cells, PFOS, rep 1"
- GSM8877041 / Sample_title: matched `HepG2` in "HepG2 cells, PFOS, rep 2"
- GSM8877042 / Sample_title: matched `HepG2` in "HepG2 cells, PFOS, rep 3"
- GSM8877043 / Sample_title: matched `HepG2` in "HepG2 cells, PFOS, rep 4"
- GSM8877044 / Sample_title: matched `HepG2` in "HepG2 cells, BPA, rep 1"
- GSM8877045 / Sample_title: matched `HepG2` in "HepG2 cells, BPA, rep 2"
- GSM8877046 / Sample_title: matched `HepG2` in "HepG2 cells, BPA, rep 3"
- GSM8877047 / Sample_title: matched `HepG2` in "HepG2 cells, BPA, rep 4"
- GSM8877048 / Sample_title: matched `HepG2` in "HepG2 cells, TBTCl, rep 1"
- GSM8877049 / Sample_title: matched `HepG2` in "HepG2 cells, TBTCl, rep 2"
- GSM8877050 / Sample_title: matched `HepG2` in "HepG2 cells, TBTCl, rep 3"
- GSM8877051 / Sample_title: matched `HepG2` in "HepG2 cells, TBTCl, rep 4"
- GSM8877024 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877025 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877026 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877027 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877028 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877029 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877030 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877031 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877032 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877033 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877034 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877035 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877036 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877037 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877038 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877039 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877040 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877041 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877042 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877043 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877044 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877045 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877046 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877047 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877048 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877049 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877050 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8877051 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"

Decision: MANUAL_REVIEW

Reasons:
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: HepG2, cell line (28/28 samples)
<!-- /computed -->