# Validation report: GSE206417

Integrated Gut/Liver-on-a-Chip platform as in vitro human model of non-alcoholic fatty liver disease

<!-- computed -->
Sample count: 16

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 16 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 16/16 |
| source_tissue | WARN | liver-pattern source 0/16; off-target tissue signal detected |
| library_strategy | PASS | RNA-Seq 16/16 |
| library_source | PASS | transcriptomic 16/16 |
| library_selection | PASS | cDNA 16/16 |
| instrument_model | PASS | MinION 16/16 |
| metadata_completeness | PASS | reported consistently: disease; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade, tissue, treatment |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: Cell Line, HepG2, cell line (16/16 samples) |
| expression_data_availability | PASS | processed per-sample counts (16/16), packaged in GSE206417_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE206417_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX15790170, https://www.ncbi.nlm.nih.gov/sra?term=SRX15790171, https://www.ncbi.nlm.nih.gov/sra?term=SRX15790172, https://www.ncbi.nlm.nih.gov/sra?term=SRX15790173, https://www.ncbi.nlm.nih.gov/sra?term=SRX15790174, and 11 more (see sample_metadata.csv) |

## Canonical field distributions

- **disease**: Co-cultured with CaCO2 cells. No treatments with free fatty acid (2), Co-cultured with CaCO2 cells. Treatment with free fatty acid (1 mM) (2), Co-cultured with HepG2 cells. No treatments with free fatty acid (2), Co-cultured with HepG2 cells. Treatments with free fatty acid (1 mM) (2), No treatments with free fatty acid (4), Treatments with free fatty acid (1 mM) (4)

## Field presence

- cell line: 16/16
- condition: 16/16 (canon: disease)
- derived tissue: 16/16

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
- GSM6253326 / Sample_characteristics_ch1: matched `intestin` in "derived tissue: Human intestine"
- GSM6253327 / Sample_characteristics_ch1: matched `intestin` in "derived tissue: Human intestine"
- GSM6253328 / Sample_characteristics_ch1: matched `intestin` in "derived tissue: Human intestine"
- GSM6253329 / Sample_characteristics_ch1: matched `intestin` in "derived tissue: Human intestine"
- GSM6253330 / Sample_characteristics_ch1: matched `intestin` in "derived tissue: Human intestine"
- GSM6253331 / Sample_characteristics_ch1: matched `intestin` in "derived tissue: Human intestine"
- GSM6253332 / Sample_characteristics_ch1: matched `intestin` in "derived tissue: Human intestine"
- GSM6253333 / Sample_characteristics_ch1: matched `intestin` in "derived tissue: Human intestine"
### disease_relevance (WARN)
- GSE206417 / Series_title: matched `non-alcoholic fatty liver` in "Integrated Gut/Liver-on-a-Chip platform as in vitro human model of non-alcoholic fatty liver disease"
- GSE206417 / Series_summary: matched `Non-alcoholic fatty liver` in "Non-alcoholic fatty liver disease (NAFLD) influence one of third population around the world. Until now, no effective treatments have been established due to the improper in vitro assays and experimen"
### material_type (WARN)
- GSM6253326 / Sample_source_name_ch1: matched `Cell Line` in "Caco-2  Cell Line"
- GSM6253327 / Sample_source_name_ch1: matched `Cell Line` in "Caco-2  Cell Line"
- GSM6253328 / Sample_source_name_ch1: matched `Cell Line` in "Caco-2  Cell Line"
- GSM6253329 / Sample_source_name_ch1: matched `Cell Line` in "Caco-2  Cell Line"
- GSM6253330 / Sample_source_name_ch1: matched `Cell Line` in "Caco-2  Cell Line"
- GSM6253331 / Sample_source_name_ch1: matched `Cell Line` in "Caco-2  Cell Line"
- GSM6253332 / Sample_source_name_ch1: matched `Cell Line` in "Caco-2  Cell Line"
- GSM6253333 / Sample_source_name_ch1: matched `Cell Line` in "Caco-2  Cell Line"
- GSM6253334 / Sample_source_name_ch1: matched `Cell Line` in "Hep G2 Cell Line"
- GSM6253335 / Sample_source_name_ch1: matched `Cell Line` in "Hep G2 Cell Line"
- GSM6253336 / Sample_source_name_ch1: matched `Cell Line` in "Hep G2 Cell Line"
- GSM6253337 / Sample_source_name_ch1: matched `Cell Line` in "Hep G2 Cell Line"
- GSM6253338 / Sample_source_name_ch1: matched `Cell Line` in "Hep G2 Cell Line"
- GSM6253339 / Sample_source_name_ch1: matched `Cell Line` in "Hep G2 Cell Line"
- GSM6253340 / Sample_source_name_ch1: matched `Cell Line` in "Hep G2 Cell Line"
- GSM6253341 / Sample_source_name_ch1: matched `Cell Line` in "Hep G2 Cell Line"
- GSM6253334 / Sample_title: matched `HepG2` in "LTC_HepG2_CoCal_Cont.rep1"
- GSM6253335 / Sample_title: matched `HepG2` in "LTC_HepG2_CoCal_Cont.rep2"
- GSM6253336 / Sample_title: matched `HepG2` in "LTC_HepG2_CoCal_FA.rep1"
- GSM6253337 / Sample_title: matched `HepG2` in "LTC_HepG2_CoCal_FA.rep2"
- GSM6253338 / Sample_title: matched `HepG2` in "LTC_HepG2_MonoCal_Cont.rep1"
- GSM6253339 / Sample_title: matched `HepG2` in "LTC_HepG2_MonoCal_Cont.rep2"
- GSM6253340 / Sample_title: matched `HepG2` in "LTC_HepG2_MonoCal_FA.rep1"
- GSM6253341 / Sample_title: matched `HepG2` in "LTC_HepG2_MonoCal_FA.rep2"
- GSM6253326 / Sample_characteristics_ch1: matched `HepG2` in "condition: Co-cultured with HepG2 cells. No treatments with free fatty acid"
- GSM6253326 / Sample_characteristics_ch1: matched `cell line` in "cell line: Caco-2"
- GSM6253327 / Sample_characteristics_ch1: matched `HepG2` in "condition: Co-cultured with HepG2 cells. No treatments with free fatty acid"
- GSM6253327 / Sample_characteristics_ch1: matched `cell line` in "cell line: Caco-2"
- GSM6253328 / Sample_characteristics_ch1: matched `HepG2` in "condition: Co-cultured with HepG2 cells. Treatments with free fatty acid (1 mM)"
- GSM6253328 / Sample_characteristics_ch1: matched `cell line` in "cell line: Caco-2"
- GSM6253329 / Sample_characteristics_ch1: matched `HepG2` in "condition: Co-cultured with HepG2 cells. Treatments with free fatty acid (1 mM)"
- GSM6253329 / Sample_characteristics_ch1: matched `cell line` in "cell line: Caco-2"
- GSM6253330 / Sample_characteristics_ch1: matched `cell line` in "cell line: Caco-2"
- GSM6253331 / Sample_characteristics_ch1: matched `cell line` in "cell line: Caco-2"
- GSM6253332 / Sample_characteristics_ch1: matched `cell line` in "cell line: Caco-2"
- GSM6253333 / Sample_characteristics_ch1: matched `cell line` in "cell line: Caco-2"
- GSM6253334 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM6253335 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM6253336 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM6253337 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM6253338 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM6253339 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM6253340 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM6253341 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 16 samples (below 20)
- source_tissue: liver-pattern source 0/16; off-target tissue signal detected
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: Cell Line, HepG2, cell line (16/16 samples)
<!-- /computed -->