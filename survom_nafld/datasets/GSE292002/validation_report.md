# Validation report: GSE292002

Endoplasmic reticulum stress sensor protein PERK in hepatic stellate cells promotes the progression of hepatocellular carcinoma via p38δ MAPK/IL-1β axis

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
| instrument_model | PASS | Illumina NextSeq 500 6/6 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: LX-2, cell line (6/6 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX28002653, https://www.ncbi.nlm.nih.gov/sra?term=SRX28002654, https://www.ncbi.nlm.nih.gov/sra?term=SRX28002655, https://www.ncbi.nlm.nih.gov/sra?term=SRX28002656, https://www.ncbi.nlm.nih.gov/sra?term=SRX28002657, and 1 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE292002_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX28002653, https://www.ncbi.nlm.nih.gov/sra?term=SRX28002654, https://www.ncbi.nlm.nih.gov/sra?term=SRX28002655, https://www.ncbi.nlm.nih.gov/sra?term=SRX28002656, https://www.ncbi.nlm.nih.gov/sra?term=SRX28002657, and 1 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: cell line (6)

## Field presence

- cell line: 6/6
- cell type: 6/6
- tissue: 6/6 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE292002 / Series_summary: matched `metabolic dysfunction-associated stea` in "Palmitic acid (PA) absorption from the intestine is increased in metabolic dysfunction-associated steatohepatitis (MASH). It induces endoplasmic reticulum (ER) stress and interleukin-1 beta (IL-1β) pr"
### material_type (WARN)
- GSM8846370 / Sample_source_name_ch1: matched `cell line` in "cell line"
- GSM8846371 / Sample_source_name_ch1: matched `cell line` in "cell line"
- GSM8846372 / Sample_source_name_ch1: matched `cell line` in "cell line"
- GSM8846373 / Sample_source_name_ch1: matched `cell line` in "cell line"
- GSM8846374 / Sample_source_name_ch1: matched `cell line` in "cell line"
- GSM8846375 / Sample_source_name_ch1: matched `cell line` in "cell line"
- GSM8846370 / Sample_title: matched `LX-2` in "LX-2_control siRNA + palmitic acid_1"
- GSM8846371 / Sample_title: matched `LX-2` in "LX-2_control siRNA + palmitic acid_2"
- GSM8846372 / Sample_title: matched `LX-2` in "LX-2_control siRNA + palmitic acid_3"
- GSM8846373 / Sample_title: matched `LX-2` in "LX-2_PERK siRNA + palmitic acid_1"
- GSM8846374 / Sample_title: matched `LX-2` in "LX-2_PERK siRNA + palmitic acid_2"
- GSM8846375 / Sample_title: matched `LX-2` in "LX-2_PERK siRNA + palmitic acid_3"
- GSM8846370 / Sample_characteristics_ch1: matched `cell line` in "tissue: cell line"
- GSM8846370 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM8846371 / Sample_characteristics_ch1: matched `cell line` in "tissue: cell line"
- GSM8846371 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM8846372 / Sample_characteristics_ch1: matched `cell line` in "tissue: cell line"
- GSM8846372 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM8846373 / Sample_characteristics_ch1: matched `cell line` in "tissue: cell line"
- GSM8846373 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM8846374 / Sample_characteristics_ch1: matched `cell line` in "tissue: cell line"
- GSM8846374 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM8846375 / Sample_characteristics_ch1: matched `cell line` in "tissue: cell line"
- GSM8846375 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 6 samples (below 20)
- source_tissue: liver-pattern source 0/6
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: LX-2, cell line (6/6 samples)
<!-- /computed -->