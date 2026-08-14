# Validation report: GSE255384

RNA-sequencing of alpha beta hydrolase domain 6 (ABHD6) wild type (WT) versus knockout (KO) Huh7 hepatoma cells with or without palmitic acid treatment.

<!-- computed -->
Sample count: 24

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 24 samples |
| organism_consistency | PASS | Homo sapiens 24/24 |
| source_tissue | WARN | liver-pattern source 0/24 |
| library_strategy | PASS | RNA-Seq 24/24 |
| library_source | PASS | transcriptomic 24/24 |
| library_selection | PASS | cDNA 24/24 |
| instrument_model | PASS | Illumina NovaSeq 6000 24/24 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: Huh7, cell line (24/24 samples) |
| expression_data_availability | PASS | processed series-level file: GSE255384_FPKMMatrix.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE255384_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX23579306, https://www.ncbi.nlm.nih.gov/sra?term=SRX23579307, https://www.ncbi.nlm.nih.gov/sra?term=SRX23579308, https://www.ncbi.nlm.nih.gov/sra?term=SRX23579309, https://www.ncbi.nlm.nih.gov/sra?term=SRX23579310, and 19 more (see sample_metadata.csv) |

## Canonical field distributions

- **treatment**: 800 microM palmitic acid (16), basal media (8)

## Field presence

- cell line: 24/24
- cell type: 24/24
- genotype: 24/24
- treatment: 24/24 (canon: treatment)

## Evidence for WARN/FAIL checks

### source_tissue (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE255384 / Series_summary: matched `non-alcoholic fatty liver` in "Primary liver cancer accounts for approximately 700,000 deaths worldwide annually ranking third in cancer-related mortality, with hepatocellular carcinoma (HCC) comprising the great majority of these "
### material_type (WARN)
- GSM8070882 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8070883 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8070884 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8070885 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8070886 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8070887 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8070888 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8070889 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8070890 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8070891 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8070892 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8070893 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8070894 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8070895 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8070896 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8070897 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8070898 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8070899 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8070900 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8070901 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8070902 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8070903 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8070904 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8070905 / Sample_source_name_ch1: matched `Huh7` in "Huh7"
- GSM8070882 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8070883 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8070884 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8070885 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8070886 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8070887 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8070888 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8070889 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8070890 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8070891 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8070892 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8070893 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8070894 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8070895 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8070896 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8070897 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8070898 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8070899 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8070900 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8070901 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8070902 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8070903 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8070904 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM8070905 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"

Decision: MANUAL_REVIEW

Reasons:
- source_tissue: liver-pattern source 0/24
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: Huh7, cell line (24/24 samples)
<!-- /computed -->