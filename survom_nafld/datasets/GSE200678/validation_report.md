# Validation report: GSE200678

Hepatic senescence is associated with clinical progression of NAFLD/NASH: Role of BMP4 and its antagonist Gremlin1 (Visceral adipose cells)

<!-- computed -->
Sample count: 35

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 35 samples |
| organism_consistency | PASS | Homo sapiens 35/35 |
| source_tissue | WARN | liver-pattern source 0/35; off-target tissue signal detected |
| library_strategy | PASS | RNA-Seq 35/35 |
| library_source | PASS | transcriptomic 35/35 |
| library_selection | PASS | cDNA 35/35 |
| instrument_model | PASS | Illumina HiSeq 2500 35/35 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (35 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE200678_Kallisto_visceral_AT_tissue_TPM.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE200678_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX14833639, https://www.ncbi.nlm.nih.gov/sra?term=SRX14833640, https://www.ncbi.nlm.nih.gov/sra?term=SRX14833641, https://www.ncbi.nlm.nih.gov/sra?term=SRX14833642, https://www.ncbi.nlm.nih.gov/sra?term=SRX14833643, and 30 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 42 (1), 44 (1), 50 (2), 51 (1), 52 (1), 53 (1), 54 (1), 57 (1), 59 (1), 61 (1), 62 (1), 64 (2), 67 (2), 70 (1), 72 (4), 73 (3), 74 (2), 75 (1), 77 (2), 78 (2), 79 (1), 82 (2), 90 (1)
- **sex**: female (23), male (12)
- **tissue**: visceral adipose tissue (35)

## Field presence

- age: 35/35 (canon: age)
- bmi (kg/m2): 35/35
- cell type: 35/35
- diabetes: 35/35
- gender: 35/35 (canon: sex)
- nafld/nash: 35/35
- tissue: 35/35 (canon: tissue)

## Evidence for WARN/FAIL checks

### source_tissue (WARN)
- GSM6041898 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041899 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041900 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041901 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041902 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041903 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041904 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041905 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041906 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041907 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041908 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041909 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041910 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041911 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041912 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041913 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041914 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041915 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041916 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041917 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041918 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041919 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041920 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041921 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041922 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041923 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041924 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041925 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041926 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041927 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041928 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041929 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041930 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041931 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041932 / Sample_source_name_ch1: matched `adipose` in "visceral adipose tissue"
- GSM6041898 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041898 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041899 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041899 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041900 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041900 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041901 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041901 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041902 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041902 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041903 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041903 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041904 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041904 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041905 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041905 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041906 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041906 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041907 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041907 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041908 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041908 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041909 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041909 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041910 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041910 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041911 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041911 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041912 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041912 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041913 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041913 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041914 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041914 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041915 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041915 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041916 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041916 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041917 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041917 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041918 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041918 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041919 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041919 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041920 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041920 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041921 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041921 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041922 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041922 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041923 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041923 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041924 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041924 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041925 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041925 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041926 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041926 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041927 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041927 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041928 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041928 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041929 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041929 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041930 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041930 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041931 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041931 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
- GSM6041932 / Sample_characteristics_ch1: matched `adipose` in "tissue: visceral adipose tissue"
- GSM6041932 / Sample_characteristics_ch1: matched `adipose` in "cell type: visceral adipose cell"
### metadata_completeness (WARN)

Decision: MANUAL_REVIEW

Reasons:
- source_tissue: liver-pattern source 0/35; off-target tissue signal detected
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
<!-- /computed -->