# Validation report: GSE268518

Duodenal-derived organoids from MASH patients exhibit altered digestive homeostasis.

<!-- computed -->
Sample count: 39

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 39 samples |
| organism_consistency | PASS | Homo sapiens 39/39 |
| source_tissue | WARN | liver-pattern source 25/39 |
| library_strategy | PASS | RNA-Seq 39/39 |
| library_source | PASS | transcriptomic 39/39 |
| library_selection | PASS | cDNA 39/39 |
| instrument_model | PASS | Illumina NovaSeq 6000 39/39 |
| metadata_completeness | PASS | reported consistently: disease, tissue; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (20 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: organoid (14/39 samples) |
| expression_data_availability | PASS | processed series-level file: GSE268518_CP20M_Biopsies_CTRL_and_MASH_excel_file_complete_expression_profile_14052024.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE268518_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX24727834, https://www.ncbi.nlm.nih.gov/sra?term=SRX24727835, https://www.ncbi.nlm.nih.gov/sra?term=SRX24727836, https://www.ncbi.nlm.nih.gov/sra?term=SRX24727837, https://www.ncbi.nlm.nih.gov/sra?term=SRX24727838, and 34 more (see sample_metadata.csv) |

## Canonical field distributions

- **disease**: Controls (19), MASH (20)
- **tissue**: Duodenum (25), Duodenum (epithelium) (14)

## Field presence

- cell type: 39/39
- disease state: 39/39 (canon: disease)
- tissue: 39/39 (canon: tissue)

## Evidence for WARN/FAIL checks

### source_tissue (WARN)
### material_type (WARN)
- GSM8292393 / Sample_characteristics_ch1: matched `organoid` in "cell type: organoids"
- GSM8292394 / Sample_characteristics_ch1: matched `organoid` in "cell type: organoids"
- GSM8292395 / Sample_characteristics_ch1: matched `organoid` in "cell type: organoids"
- GSM8292396 / Sample_characteristics_ch1: matched `organoid` in "cell type: organoids"
- GSM8292397 / Sample_characteristics_ch1: matched `organoid` in "cell type: organoids"
- GSM8292398 / Sample_characteristics_ch1: matched `organoid` in "cell type: organoids"
- GSM8292399 / Sample_characteristics_ch1: matched `organoid` in "cell type: organoids"
- GSM8292400 / Sample_characteristics_ch1: matched `organoid` in "cell type: organoids"
- GSM8292401 / Sample_characteristics_ch1: matched `organoid` in "cell type: organoids"
- GSM8292402 / Sample_characteristics_ch1: matched `organoid` in "cell type: organoids"
- GSM8292403 / Sample_characteristics_ch1: matched `organoid` in "cell type: organoids"
- GSM8292404 / Sample_characteristics_ch1: matched `organoid` in "cell type: organoids"
- GSM8292405 / Sample_characteristics_ch1: matched `organoid` in "cell type: organoids"
- GSM8292406 / Sample_characteristics_ch1: matched `organoid` in "cell type: organoids"

Decision: MANUAL_REVIEW

Reasons:
- source_tissue: liver-pattern source 25/39
- material_type: cell/culture terms in sample metadata: organoid (14/39 samples)
<!-- /computed -->