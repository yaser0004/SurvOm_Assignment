# Validation report: GSE316562

Cyanidin-3-rutinoside(C3R) Attenuates Free Fatty Acid-Induced Hepatic Lipid Accumulation in HepG2 Cells

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
| instrument_model | PASS | Illumina NovaSeq X Plus 15/15 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (15/15 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX31822212, https://www.ncbi.nlm.nih.gov/sra?term=SRX31822213, https://www.ncbi.nlm.nih.gov/sra?term=SRX31822214, https://www.ncbi.nlm.nih.gov/sra?term=SRX31822215, https://www.ncbi.nlm.nih.gov/sra?term=SRX31822216, and 10 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE316562_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX31822212, https://www.ncbi.nlm.nih.gov/sra?term=SRX31822213, https://www.ncbi.nlm.nih.gov/sra?term=SRX31822214, https://www.ncbi.nlm.nih.gov/sra?term=SRX31822215, https://www.ncbi.nlm.nih.gov/sra?term=SRX31822216, and 10 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: liver (15)

## Field presence

- cell line: 15/15
- cell type: 15/15
- tissue: 15/15 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE316562 / Series_summary: matched `Non-alcoholic fatty liver` in "Non-alcoholic fatty liver disease (NAFLD) is characteristic by pathological lipid accumulation in hepatocytes. This study investigates how Cyanidin-3-rutinoside(C3R), a natural anthocyanin with antiox"
### material_type (WARN)
- GSM9456068 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9456069 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9456070 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9456071 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9456072 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9456073 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9456074 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9456075 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9456076 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9456077 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9456078 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9456079 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9456080 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9456081 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9456082 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 15 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (15/15 samples)
<!-- /computed -->