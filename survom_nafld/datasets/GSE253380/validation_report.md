# Validation report: GSE253380

ACMSD inhibition corrects fibrosis, inflammation, and DNA damage in MASLD/MASH

<!-- computed -->
Sample count: 48

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 48 samples |
| organism_consistency | WARN | mixed organisms: Homo sapiens 24/48, Mus musculus 24/48 |
| source_tissue | PASS | liver-pattern source 48/48 |
| library_strategy | PASS | RNA-Seq 48/48 |
| library_source | PASS | transcriptomic 48/48 |
| library_selection | PASS | cDNA 48/48 |
| instrument_model | PASS | BGISEQ-500 48/48 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: organoid (24/48 samples) |
| expression_data_availability | PASS | processed series-level file: GSE253380_mPH_HLO_tmm_normalized_counts.xlsx |
| series_matrix | INFO | present, metadata-only (GSE253380-GPL23227_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX23232552, https://www.ncbi.nlm.nih.gov/sra?term=SRX23232553, https://www.ncbi.nlm.nih.gov/sra?term=SRX23232554, https://www.ncbi.nlm.nih.gov/sra?term=SRX23232555, https://www.ncbi.nlm.nih.gov/sra?term=SRX23232556, and 43 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Human liver organoids (24), Liver (24)
- **treatment**: 12h_DMSO (4), 12h_TLC-065 (4), 24h_DMSO (4), 24h_TLC-065 (4), 6h_DMSO (4), 6h_TLC-065 (4), DMSO (12), TLC065 (12)

## Field presence

- cell type: 24/48
- genotype: 24/48
- tissue: 48/48 (canon: tissue)
- treatment: 48/48 (canon: treatment)

## Evidence for WARN/FAIL checks

### organism_consistency (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE253380 / Series_title: matched `MASLD` in "ACMSD inhibition corrects fibrosis, inflammation, and DNA damage in MASLD/MASH"
- GSE253380 / Series_summary: matched `MASLD` in "Recent findings reveal the importance of tryptophan-initiated de novo nicotinamide adenine dinucleotide (NAD+) synthesis in the liver, a process previously considered secondary to biosynthesis from ni"
- GSE253380 / Series_overall_design: matched `steatohepatitis` in "To investigate the effect of ACMSD inhibition, mouse primary hepatocytes were treated with ACMSD inhibitor TLC-065 for 6, 12, and 24h. The effects of TLC-065 were tested in human liver organoid models"
### material_type (WARN)
- GSM8019474 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM8019475 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM8019476 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM8019477 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM8019478 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM8019479 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM8019480 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM8019481 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM8019482 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM8019483 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM8019484 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM8019485 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM8019486 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM8019487 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM8019488 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM8019489 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM8019490 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM8019491 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM8019492 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM8019493 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM8019494 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM8019495 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM8019496 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM8019497 / Sample_source_name_ch1: matched `organoid` in "Human liver organoids"
- GSM8019474 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM8019475 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM8019476 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM8019477 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM8019478 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM8019479 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM8019480 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM8019481 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM8019482 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM8019483 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM8019484 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM8019485 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM8019486 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM8019487 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM8019488 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM8019489 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM8019490 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM8019491 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM8019492 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM8019493 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM8019494 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM8019495 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM8019496 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"
- GSM8019497 / Sample_characteristics_ch1: matched `organoid` in "tissue: Human liver organoids"

Decision: MANUAL_REVIEW

Reasons:
- organism_consistency: mixed organisms: Homo sapiens 24/48, Mus musculus 24/48
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: organoid (24/48 samples)
<!-- /computed -->