# Validation report: GSE292999

Peroxisome Proliferator-activated Receptor Agonist IVA337 Alleviates Inflammation

<!-- computed -->
Sample count: 14

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 14 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 14/14 |
| source_tissue | PASS | liver-pattern source 14/14 |
| library_strategy | PASS | RNA-Seq 14/14 |
| library_source | PASS | transcriptomic 14/14 |
| library_selection | PASS | cDNA 14/14 |
| instrument_model | PASS | DNBSEQ-T7 14/14 |
| metadata_completeness | PASS | reported consistently: disease; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade, tissue, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (10 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: Spheroid, spheroid (6/14 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX28151104, https://www.ncbi.nlm.nih.gov/sra?term=SRX28151105, https://www.ncbi.nlm.nih.gov/sra?term=SRX28151106, https://www.ncbi.nlm.nih.gov/sra?term=SRX28151107, https://www.ncbi.nlm.nih.gov/sra?term=SRX28151108, and 9 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE292999_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX28151104, https://www.ncbi.nlm.nih.gov/sra?term=SRX28151105, https://www.ncbi.nlm.nih.gov/sra?term=SRX28151106, https://www.ncbi.nlm.nih.gov/sra?term=SRX28151107, https://www.ncbi.nlm.nih.gov/sra?term=SRX28151108, and 9 more (see sample_metadata.csv) |

## Canonical field distributions

- **disease**: NAFL donor (4), NASH donor (10)

## Field presence

- cell type: 14/14
- disease state: 14/14 (canon: disease)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### material_type (WARN)
- GSM8873327 / Sample_source_name_ch1: matched `spheroid` in "Human liver spheroid"
- GSM8873328 / Sample_source_name_ch1: matched `spheroid` in "Human liver spheroid"
- GSM8873329 / Sample_source_name_ch1: matched `spheroid` in "Human liver spheroid"
- GSM8873330 / Sample_source_name_ch1: matched `spheroid` in "Human liver spheroid"
- GSM8873331 / Sample_source_name_ch1: matched `spheroid` in "Human liver spheroid"
- GSM8873332 / Sample_source_name_ch1: matched `spheroid` in "Human liver spheroid"
- GSM8873327 / Sample_title: matched `Spheroid` in "Spheroid-CTRL-1"
- GSM8873328 / Sample_title: matched `Spheroid` in "Spheroid-CTRL-2"
- GSM8873329 / Sample_title: matched `Spheroid` in "Spheroid-NASH-1"
- GSM8873330 / Sample_title: matched `Spheroid` in "Spheroid-NASH-2"
- GSM8873331 / Sample_title: matched `Spheroid` in "Spheroid-IVA-1"
- GSM8873332 / Sample_title: matched `Spheroid` in "Spheroid-IVA-2"
- GSM8873327 / Sample_characteristics_ch1: matched `spheroid` in "cell type: Human liver spheroid"
- GSM8873328 / Sample_characteristics_ch1: matched `spheroid` in "cell type: Human liver spheroid"
- GSM8873329 / Sample_characteristics_ch1: matched `spheroid` in "cell type: Human liver spheroid"
- GSM8873330 / Sample_characteristics_ch1: matched `spheroid` in "cell type: Human liver spheroid"
- GSM8873331 / Sample_characteristics_ch1: matched `spheroid` in "cell type: Human liver spheroid"
- GSM8873332 / Sample_characteristics_ch1: matched `spheroid` in "cell type: Human liver spheroid"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 14 samples (below 20)
- material_type: cell/culture terms in sample metadata: Spheroid, spheroid (6/14 samples)
<!-- /computed -->