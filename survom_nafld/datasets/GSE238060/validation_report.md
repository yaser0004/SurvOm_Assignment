# Validation report: GSE238060

HSD17B13 liquid-liquid phase separation activates autocrine platelet-activating factor signaling in NASH

<!-- computed -->
Sample count: 12

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 12 samples (below 20) |
| organism_consistency | WARN | mixed organisms: Homo sapiens 6/12, Mus musculus 6/12 |
| source_tissue | PASS | liver-pattern source 12/12 |
| library_strategy | PASS | RNA-Seq 12/12 |
| library_source | PASS | transcriptomic 12/12 |
| library_selection | PASS | cDNA 12/12 |
| instrument_model | PASS | Illumina NovaSeq 6000 12/12 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: HepaRG, cell line (6/12 samples) |
| expression_data_availability | PASS | processed series-level file: GSE238060_AAV_KO_FPKM.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE238060-GPL24247_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX21134301, https://www.ncbi.nlm.nih.gov/sra?term=SRX21134302, https://www.ncbi.nlm.nih.gov/sra?term=SRX21134303, https://www.ncbi.nlm.nih.gov/sra?term=SRX21134304, https://www.ncbi.nlm.nih.gov/sra?term=SRX21134305, and 7 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: liver (12)
- **treatment**: AAV control (3), AAV human HSD17B13 (3), lentivirus HepaRG-HSD17B13 (3), lentivirus HepaRG-NC (3)

## Field presence

- cell line: 6/12
- cell type: 12/12
- genotype: 12/12
- tissue: 12/12 (canon: tissue)
- treatment: 12/12 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### organism_consistency (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE238060 / Series_title: matched `NASH` in "HSD17B13 liquid-liquid phase separation activates autocrine platelet-activating factor signaling in NASH"
- GSE238060 / Series_summary: matched `NASH` in "Loss-of-function variants in 17-beta hydroxysteroid dehydrogenase 13 (HSD17B13) are associated with decreased inflammation in human chronic liver disease. The underlying mechanism by which HSD17B13 pr"
### material_type (WARN)
- GSM7658117 / Sample_title: matched `HepaRG` in "HepaRG cells, HSD17B13, rep1"
- GSM7658118 / Sample_title: matched `HepaRG` in "HepaRG cells, HSD17B13, rep2"
- GSM7658119 / Sample_title: matched `HepaRG` in "HepaRG cells, HSD17B13, rep3"
- GSM7658120 / Sample_title: matched `HepaRG` in "HepaRG cells, Control, rep1"
- GSM7658121 / Sample_title: matched `HepaRG` in "HepaRG cells, Control, rep2"
- GSM7658122 / Sample_title: matched `HepaRG` in "HepaRG cells, Control, rep3"
- GSM7658117 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG"
- GSM7658117 / Sample_characteristics_ch1: matched `HepaRG` in "treatment: lentivirus HepaRG-HSD17B13"
- GSM7658118 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG"
- GSM7658118 / Sample_characteristics_ch1: matched `HepaRG` in "treatment: lentivirus HepaRG-HSD17B13"
- GSM7658119 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG"
- GSM7658119 / Sample_characteristics_ch1: matched `HepaRG` in "treatment: lentivirus HepaRG-HSD17B13"
- GSM7658120 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG"
- GSM7658120 / Sample_characteristics_ch1: matched `HepaRG` in "treatment: lentivirus HepaRG-NC"
- GSM7658121 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG"
- GSM7658121 / Sample_characteristics_ch1: matched `HepaRG` in "treatment: lentivirus HepaRG-NC"
- GSM7658122 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepaRG"
- GSM7658122 / Sample_characteristics_ch1: matched `HepaRG` in "treatment: lentivirus HepaRG-NC"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 12 samples (below 20)
- organism_consistency: mixed organisms: Homo sapiens 6/12, Mus musculus 6/12
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: HepaRG, cell line (6/12 samples)
<!-- /computed -->