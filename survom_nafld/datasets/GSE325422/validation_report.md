# Validation report: GSE325422

RNA-seq analysis of sodium butyrate effects on palmitate-induced insulin resistance in HepG2 cells

<!-- computed -->
Sample count: 15

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 15 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 15/15 |
| source_tissue | PASS | liver-pattern source 15/15 |
| library_strategy | PASS | RNA-Seq 15/15 |
| library_source | PASS | transcriptomic 15/15 |
| library_selection | PASS | cDNA 15/15 |
| instrument_model | PASS | DNBSEQ-T7 15/15 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: HepG2, cell line (15/15 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX32573679, https://www.ncbi.nlm.nih.gov/sra?term=SRX32573680, https://www.ncbi.nlm.nih.gov/sra?term=SRX32573681, https://www.ncbi.nlm.nih.gov/sra?term=SRX32573682, https://www.ncbi.nlm.nih.gov/sra?term=SRX32573683, and 10 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE325422_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX32573679, https://www.ncbi.nlm.nih.gov/sra?term=SRX32573680, https://www.ncbi.nlm.nih.gov/sra?term=SRX32573681, https://www.ncbi.nlm.nih.gov/sra?term=SRX32573682, https://www.ncbi.nlm.nih.gov/sra?term=SRX32573683, and 10 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: liver (15)
- **treatment**: Control (3), palmitate (3), palmitate + high sodium butyrate (3), palmitate + low sodium butyrate (3), palmitate + medium sodium butyrate (3)

## Field presence

- batch: 15/15
- cell line: 15/15
- cell type: 15/15
- genotype: 15/15
- tissue: 15/15 (canon: tissue)
- treatment: 15/15 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE325422 / Series_summary: matched `Metabolic dysfunction-associated stea` in "Objective: Metabolic dysfunction-associated steatotic liver disease (MASLD) is characterized by hepatic insulin resistance (IR) and impaired lipid–glucose metabolism. Sodium butyrate (NaB), a short-ch"
### material_type (WARN)
- GSM9603113 / Sample_title: matched `HepG2` in "Control HepG2 48h replicate 1"
- GSM9603114 / Sample_title: matched `HepG2` in "Control HepG2 48h replicate 2"
- GSM9603115 / Sample_title: matched `HepG2` in "Control HepG2 48h replicate 3"
- GSM9603116 / Sample_title: matched `HepG2` in "Palmitate-treated HepG2 48h replicate 1"
- GSM9603117 / Sample_title: matched `HepG2` in "Palmitate-treated HepG2 48h replicate 2"
- GSM9603118 / Sample_title: matched `HepG2` in "Palmitate-treated HepG2 48h replicate 3"
- GSM9603119 / Sample_title: matched `HepG2` in "IR + low Sodium butyrate HepG2 replicate 1"
- GSM9603120 / Sample_title: matched `HepG2` in "IR + low Sodium butyrate HepG2 replicate 2"
- GSM9603121 / Sample_title: matched `HepG2` in "IR + low Sodium butyrate HepG2 replicate 3"
- GSM9603122 / Sample_title: matched `HepG2` in "IR + medium Sodium butyrate HepG2 replicate 1"
- GSM9603123 / Sample_title: matched `HepG2` in "IR + medium Sodium butyrate HepG2 replicate 2"
- GSM9603124 / Sample_title: matched `HepG2` in "IR + medium Sodium butyrate HepG2 replicate 3"
- GSM9603125 / Sample_title: matched `HepG2` in "IR + high Sodium butyrate HepG2 replicate 1"
- GSM9603126 / Sample_title: matched `HepG2` in "IR + high Sodium butyrate HepG2 replicate 2"
- GSM9603127 / Sample_title: matched `HepG2` in "IR + high Sodium butyrate HepG2 replicate 3"
- GSM9603113 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9603113 / Sample_characteristics_ch1: matched `cell line` in "cell type: hepatocellular carcinoma cell line"
- GSM9603114 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9603114 / Sample_characteristics_ch1: matched `cell line` in "cell type: hepatocellular carcinoma cell line"
- GSM9603115 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9603115 / Sample_characteristics_ch1: matched `cell line` in "cell type: hepatocellular carcinoma cell line"
- GSM9603116 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9603116 / Sample_characteristics_ch1: matched `cell line` in "cell type: hepatocellular carcinoma cell line"
- GSM9603117 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9603117 / Sample_characteristics_ch1: matched `cell line` in "cell type: hepatocellular carcinoma cell line"
- GSM9603118 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9603118 / Sample_characteristics_ch1: matched `cell line` in "cell type: hepatocellular carcinoma cell line"
- GSM9603119 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9603119 / Sample_characteristics_ch1: matched `cell line` in "cell type: hepatocellular carcinoma cell line"
- GSM9603120 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9603120 / Sample_characteristics_ch1: matched `cell line` in "cell type: hepatocellular carcinoma cell line"
- GSM9603121 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9603121 / Sample_characteristics_ch1: matched `cell line` in "cell type: hepatocellular carcinoma cell line"
- GSM9603122 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9603122 / Sample_characteristics_ch1: matched `cell line` in "cell type: hepatocellular carcinoma cell line"
- GSM9603123 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9603123 / Sample_characteristics_ch1: matched `cell line` in "cell type: hepatocellular carcinoma cell line"
- GSM9603124 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9603124 / Sample_characteristics_ch1: matched `cell line` in "cell type: hepatocellular carcinoma cell line"
- GSM9603125 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9603125 / Sample_characteristics_ch1: matched `cell line` in "cell type: hepatocellular carcinoma cell line"
- GSM9603126 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9603126 / Sample_characteristics_ch1: matched `cell line` in "cell type: hepatocellular carcinoma cell line"
- GSM9603127 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9603127 / Sample_characteristics_ch1: matched `cell line` in "cell type: hepatocellular carcinoma cell line"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 15 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: HepG2, cell line (15/15 samples)
<!-- /computed -->