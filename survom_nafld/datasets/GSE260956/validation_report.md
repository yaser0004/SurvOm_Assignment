# Validation report: GSE260956

Hepatic GPNMB aggravates NASH through binding to RYK [RNA-Seq]

<!-- computed -->
Sample count: 8

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 8 samples (below 20) |
| organism_consistency | WARN | mixed organisms: Homo sapiens 4/8, Mus musculus 4/8 |
| source_tissue | PASS | liver-pattern source 8/8 |
| library_strategy | PASS | RNA-Seq 8/8 |
| library_source | PASS | transcriptomic 8/8 |
| library_selection | PASS | cDNA 8/8 |
| instrument_model | PASS | MGISEQ-2000RS 8/8 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: Huh7, cell line (4/8 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX23849565, https://www.ncbi.nlm.nih.gov/sra?term=SRX23849566, https://www.ncbi.nlm.nih.gov/sra?term=SRX23849567, https://www.ncbi.nlm.nih.gov/sra?term=SRX23849568, https://www.ncbi.nlm.nih.gov/sra?term=SRX23849569, and 3 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE260956-GPL30209_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX23849565, https://www.ncbi.nlm.nih.gov/sra?term=SRX23849566, https://www.ncbi.nlm.nih.gov/sra?term=SRX23849567, https://www.ncbi.nlm.nih.gov/sra?term=SRX23849568, https://www.ncbi.nlm.nih.gov/sra?term=SRX23849569, and 3 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: liver (4)
- **treatment**: AMLN diet (2), GPNMB ECD for 8 h (2), high fat high cholesterol diet (1), normal chow diet (1), vehicle for 8 h (2)

## Field presence

- cell line: 4/8
- cell type: 4/8
- genotype: 8/8
- tissue: 4/8 (canon: tissue)
- treatment: 8/8 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### organism_consistency (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE260956 / Series_title: matched `NASH` in "Hepatic GPNMB aggravates NASH through binding to RYK [RNA-Seq]"
- GSE260956 / Series_summary: matched `NASH` in "The goals of this study are to define the moelcular events in NASH and to determine the role of GPNMB and RYK in NASH development"
### material_type (WARN)
- GSM8128637 / Sample_source_name_ch1: matched `Huh7` in "Huh7 cell line"
- GSM8128638 / Sample_source_name_ch1: matched `Huh7` in "Huh7 cell line"
- GSM8128639 / Sample_source_name_ch1: matched `Huh7` in "Huh7 cell line"
- GSM8128640 / Sample_source_name_ch1: matched `Huh7` in "Huh7 cell line"
- GSM8128637 / Sample_title: matched `Huh7` in "Huh7 RYK1, Veh, 8 h"
- GSM8128638 / Sample_title: matched `Huh7` in "Huh7 RYK1, Gpnmb ECD, 8 h"
- GSM8128639 / Sample_title: matched `Huh7` in "Huh7 RYK2, Veh, 8 h"
- GSM8128640 / Sample_title: matched `Huh7` in "Huh7 RYK2, Gpnmb ECD, 8 h"
- GSM8128637 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7 cell line"
- GSM8128638 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7 cell line"
- GSM8128639 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7 cell line"
- GSM8128640 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7 cell line"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 8 samples (below 20)
- organism_consistency: mixed organisms: Homo sapiens 4/8, Mus musculus 4/8
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: Huh7, cell line (4/8 samples)
<!-- /computed -->