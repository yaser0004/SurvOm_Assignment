# Validation report: GSE152091

Integrated Gut/Liver-on-a-Chip platform as in vitro human model of non-alcoholic fatty liver disease

<!-- computed -->
Sample count: 23

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 23 samples |
| organism_consistency | PASS | Homo sapiens 23/23 |
| source_tissue | WARN | liver-pattern source 0/23; off-target tissue signal detected |
| library_strategy | PASS | RNA-Seq 23/23 |
| library_source | PASS | transcriptomic 23/23 |
| library_selection | PASS | cDNA 23/23 |
| instrument_model | PASS | Illumina NovaSeq 6000 23/23 |
| metadata_completeness | PASS | reported consistently: disease; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade, tissue, treatment |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: SMART-seq (23 sample(s)) |
| material_type | WARN | cell/culture terms in sample metadata: Cell Line, HepG2, cell line (23/23 samples) |
| expression_data_availability | PASS | processed per-sample counts (23/23), packaged in GSE152091_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE152091_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX8508306, https://www.ncbi.nlm.nih.gov/sra?term=SRX8508307, https://www.ncbi.nlm.nih.gov/sra?term=SRX8508308, https://www.ncbi.nlm.nih.gov/sra?term=SRX8508309, https://www.ncbi.nlm.nih.gov/sra?term=SRX8508310, and 18 more (see sample_metadata.csv) |

## Canonical field distributions

- **disease**: Co-cultured with CaCO2 cells. No treatments with free fatty acid (3), Co-cultured with CaCO2 cells. Treatment with free fatty acid (1 mM) (3), Co-cultured with HepG2 cells. No treatments with free fatty acid (2), Co-cultured with HepG2 cells. Treatments with free fatty acid (1 mM) (3), No treatments with free fatty acid (6), Treatments with free fatty acid (1 mM) (6)

## Field presence

- cell line: 23/23
- condition: 23/23 (canon: disease)
- derived tissue: 23/23

## Evidence for WARN/FAIL checks

### source_tissue (WARN)
- GSM4602968 / Sample_characteristics_ch1: matched `intestin` in "derived tissue: Human intestine"
- GSM4602969 / Sample_characteristics_ch1: matched `intestin` in "derived tissue: Human intestine"
- GSM4602970 / Sample_characteristics_ch1: matched `intestin` in "derived tissue: Human intestine"
- GSM4602971 / Sample_characteristics_ch1: matched `intestin` in "derived tissue: Human intestine"
- GSM4602972 / Sample_characteristics_ch1: matched `intestin` in "derived tissue: Human intestine"
- GSM4602973 / Sample_characteristics_ch1: matched `intestin` in "derived tissue: Human intestine"
- GSM4602974 / Sample_characteristics_ch1: matched `intestin` in "derived tissue: Human intestine"
- GSM4602975 / Sample_characteristics_ch1: matched `intestin` in "derived tissue: Human intestine"
- GSM4602976 / Sample_characteristics_ch1: matched `intestin` in "derived tissue: Human intestine"
- GSM4602977 / Sample_characteristics_ch1: matched `intestin` in "derived tissue: Human intestine"
- GSM4602978 / Sample_characteristics_ch1: matched `intestin` in "derived tissue: Human intestine"
### disease_relevance (WARN)
- GSE152091 / Series_title: matched `non-alcoholic fatty liver` in "Integrated Gut/Liver-on-a-Chip platform as in vitro human model of non-alcoholic fatty liver disease"
- GSE152091 / Series_summary: matched `Non-alcoholic fatty liver` in "Non-alcoholic fatty liver disease (NAFLD) influence one of third population around the world. Until now, no effective treatments have been established due to the improper in vitro assays and experimen"
### single_cell_or_spatial (FAIL)
- GSM4602968 / Sample_extract_protocol_ch1: matched `SMART-seq` in "SMART-seq (SMART-Seq v4 Ultra Low Input RNA Kit, Takara Bio)"
- GSM4602969 / Sample_extract_protocol_ch1: matched `SMART-seq` in "SMART-seq (SMART-Seq v4 Ultra Low Input RNA Kit, Takara Bio)"
- GSM4602970 / Sample_extract_protocol_ch1: matched `SMART-seq` in "SMART-seq (SMART-Seq v4 Ultra Low Input RNA Kit, Takara Bio)"
- GSM4602971 / Sample_extract_protocol_ch1: matched `SMART-seq` in "SMART-seq (SMART-Seq v4 Ultra Low Input RNA Kit, Takara Bio)"
- GSM4602972 / Sample_extract_protocol_ch1: matched `SMART-seq` in "SMART-seq (SMART-Seq v4 Ultra Low Input RNA Kit, Takara Bio)"
- GSM4602973 / Sample_extract_protocol_ch1: matched `SMART-seq` in "SMART-seq (SMART-Seq v4 Ultra Low Input RNA Kit, Takara Bio)"
- GSM4602974 / Sample_extract_protocol_ch1: matched `SMART-seq` in "SMART-seq (SMART-Seq v4 Ultra Low Input RNA Kit, Takara Bio)"
- GSM4602975 / Sample_extract_protocol_ch1: matched `SMART-seq` in "SMART-seq (SMART-Seq v4 Ultra Low Input RNA Kit, Takara Bio)"
- GSM4602976 / Sample_extract_protocol_ch1: matched `SMART-seq` in "SMART-seq (SMART-Seq v4 Ultra Low Input RNA Kit, Takara Bio)"
- GSM4602977 / Sample_extract_protocol_ch1: matched `SMART-seq` in "SMART-seq (SMART-Seq v4 Ultra Low Input RNA Kit, Takara Bio)"
- GSM4602978 / Sample_extract_protocol_ch1: matched `SMART-seq` in "SMART-seq (SMART-Seq v4 Ultra Low Input RNA Kit, Takara Bio)"
- GSM4602979 / Sample_extract_protocol_ch1: matched `SMART-seq` in "SMART-seq (SMART-Seq v4 Ultra Low Input RNA Kit, Takara Bio)"
- GSM4602980 / Sample_extract_protocol_ch1: matched `SMART-seq` in "SMART-seq (SMART-Seq v4 Ultra Low Input RNA Kit, Takara Bio)"
- GSM4602981 / Sample_extract_protocol_ch1: matched `SMART-seq` in "SMART-seq (SMART-Seq v4 Ultra Low Input RNA Kit, Takara Bio)"
- GSM4602982 / Sample_extract_protocol_ch1: matched `SMART-seq` in "SMART-seq (SMART-Seq v4 Ultra Low Input RNA Kit, Takara Bio)"
- GSM4602983 / Sample_extract_protocol_ch1: matched `SMART-seq` in "SMART-seq (SMART-Seq v4 Ultra Low Input RNA Kit, Takara Bio)"
- GSM4602984 / Sample_extract_protocol_ch1: matched `SMART-seq` in "SMART-seq (SMART-Seq v4 Ultra Low Input RNA Kit, Takara Bio)"
- GSM4602985 / Sample_extract_protocol_ch1: matched `SMART-seq` in "SMART-seq (SMART-Seq v4 Ultra Low Input RNA Kit, Takara Bio)"
- GSM4602986 / Sample_extract_protocol_ch1: matched `SMART-seq` in "SMART-seq (SMART-Seq v4 Ultra Low Input RNA Kit, Takara Bio)"
- GSM4602987 / Sample_extract_protocol_ch1: matched `SMART-seq` in "SMART-seq (SMART-Seq v4 Ultra Low Input RNA Kit, Takara Bio)"
- GSM4602988 / Sample_extract_protocol_ch1: matched `SMART-seq` in "SMART-seq (SMART-Seq v4 Ultra Low Input RNA Kit, Takara Bio)"
- GSM4602989 / Sample_extract_protocol_ch1: matched `SMART-seq` in "SMART-seq (SMART-Seq v4 Ultra Low Input RNA Kit, Takara Bio)"
- GSM4602990 / Sample_extract_protocol_ch1: matched `SMART-seq` in "SMART-seq (SMART-Seq v4 Ultra Low Input RNA Kit, Takara Bio)"
### material_type (WARN)
- GSM4602968 / Sample_source_name_ch1: matched `Cell Line` in "Caco-2  Cell Line"
- GSM4602969 / Sample_source_name_ch1: matched `Cell Line` in "Caco-2  Cell Line"
- GSM4602970 / Sample_source_name_ch1: matched `Cell Line` in "Caco-2  Cell Line"
- GSM4602971 / Sample_source_name_ch1: matched `Cell Line` in "Caco-2  Cell Line"
- GSM4602972 / Sample_source_name_ch1: matched `Cell Line` in "Caco-2  Cell Line"
- GSM4602973 / Sample_source_name_ch1: matched `Cell Line` in "Caco-2  Cell Line"
- GSM4602974 / Sample_source_name_ch1: matched `Cell Line` in "Caco-2  Cell Line"
- GSM4602975 / Sample_source_name_ch1: matched `Cell Line` in "Caco-2  Cell Line"
- GSM4602976 / Sample_source_name_ch1: matched `Cell Line` in "Caco-2  Cell Line"
- GSM4602977 / Sample_source_name_ch1: matched `Cell Line` in "Caco-2  Cell Line"
- GSM4602978 / Sample_source_name_ch1: matched `Cell Line` in "Caco-2  Cell Line"
- GSM4602979 / Sample_source_name_ch1: matched `Cell Line` in "Hep G2 Cell Line"
- GSM4602980 / Sample_source_name_ch1: matched `Cell Line` in "Hep G2 Cell Line"
- GSM4602981 / Sample_source_name_ch1: matched `Cell Line` in "Hep G2 Cell Line"
- GSM4602982 / Sample_source_name_ch1: matched `Cell Line` in "Hep G2 Cell Line"
- GSM4602983 / Sample_source_name_ch1: matched `Cell Line` in "Hep G2 Cell Line"
- GSM4602984 / Sample_source_name_ch1: matched `Cell Line` in "Hep G2 Cell Line"
- GSM4602985 / Sample_source_name_ch1: matched `Cell Line` in "Hep G2 Cell Line"
- GSM4602986 / Sample_source_name_ch1: matched `Cell Line` in "Hep G2 Cell Line"
- GSM4602987 / Sample_source_name_ch1: matched `Cell Line` in "Hep G2 Cell Line"
- GSM4602988 / Sample_source_name_ch1: matched `Cell Line` in "Hep G2 Cell Line"
- GSM4602989 / Sample_source_name_ch1: matched `Cell Line` in "Hep G2 Cell Line"
- GSM4602990 / Sample_source_name_ch1: matched `Cell Line` in "Hep G2 Cell Line"
- GSM4602979 / Sample_title: matched `HepG2` in "HepG2_CoCul_Cont.rep1"
- GSM4602980 / Sample_title: matched `HepG2` in "HepG2_CoCul_Cont.rep2"
- GSM4602981 / Sample_title: matched `HepG2` in "HepG2_CoCul_Cont.rep3"
- GSM4602982 / Sample_title: matched `HepG2` in "HepG2_CoCul_FA.rep1"
- GSM4602983 / Sample_title: matched `HepG2` in "HepG2_CoCul_FA.rep2"
- GSM4602984 / Sample_title: matched `HepG2` in "HepG2_CoCul_FA.rep3"
- GSM4602985 / Sample_title: matched `HepG2` in "HepG2_MonoCul_Cont.rep1"
- GSM4602986 / Sample_title: matched `HepG2` in "HepG2_MonoCul_Cont.rep2"
- GSM4602987 / Sample_title: matched `HepG2` in "HepG2_MonoCul_Cont.rep3"
- GSM4602988 / Sample_title: matched `HepG2` in "HepG2_MonoCul_FA.rep1"
- GSM4602989 / Sample_title: matched `HepG2` in "HepG2_MonoCul_FA.rep2"
- GSM4602990 / Sample_title: matched `HepG2` in "HepG2_MonoCul_FA.rep3"
- GSM4602968 / Sample_characteristics_ch1: matched `HepG2` in "condition: Co-cultured with HepG2 cells. No treatments with free fatty acid"
- GSM4602968 / Sample_characteristics_ch1: matched `cell line` in "cell line: Caco2"
- GSM4602969 / Sample_characteristics_ch1: matched `HepG2` in "condition: Co-cultured with HepG2 cells. No treatments with free fatty acid"
- GSM4602969 / Sample_characteristics_ch1: matched `cell line` in "cell line: Caco2"
- GSM4602970 / Sample_characteristics_ch1: matched `HepG2` in "condition: Co-cultured with HepG2 cells. Treatments with free fatty acid (1 mM)"
- GSM4602970 / Sample_characteristics_ch1: matched `cell line` in "cell line: Caco2"
- GSM4602971 / Sample_characteristics_ch1: matched `HepG2` in "condition: Co-cultured with HepG2 cells. Treatments with free fatty acid (1 mM)"
- GSM4602971 / Sample_characteristics_ch1: matched `cell line` in "cell line: Caco2"
- GSM4602972 / Sample_characteristics_ch1: matched `HepG2` in "condition: Co-cultured with HepG2 cells. Treatments with free fatty acid (1 mM)"
- GSM4602972 / Sample_characteristics_ch1: matched `cell line` in "cell line: Caco2"
- GSM4602973 / Sample_characteristics_ch1: matched `cell line` in "cell line: Caco2"
- GSM4602974 / Sample_characteristics_ch1: matched `cell line` in "cell line: Caco2"
- GSM4602975 / Sample_characteristics_ch1: matched `cell line` in "cell line: Caco2"
- GSM4602976 / Sample_characteristics_ch1: matched `cell line` in "cell line: Caco2"
- GSM4602977 / Sample_characteristics_ch1: matched `cell line` in "cell line: Caco2"
- GSM4602978 / Sample_characteristics_ch1: matched `cell line` in "cell line: Caco2"
- GSM4602979 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM4602980 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM4602981 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM4602982 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM4602983 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM4602984 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM4602985 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM4602986 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM4602987 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM4602988 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM4602989 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM4602990 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: SMART-seq (23 sample(s)))
<!-- /computed -->