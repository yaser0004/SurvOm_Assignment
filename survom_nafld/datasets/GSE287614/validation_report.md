# Validation report: GSE287614

The transcription factor ZNF469 regulates collagen production in liver fibrosis [RNA-Seq]

<!-- computed -->
Sample count: 28

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 28 samples |
| organism_consistency | PASS | Homo sapiens 28/28 |
| source_tissue | WARN | liver-pattern source 0/28 |
| library_strategy | PASS | RNA-Seq 28/28 |
| library_source | PASS | transcriptomic 28/28 |
| library_selection | PASS | cDNA 28/28 |
| instrument_model | PASS | Illumina NovaSeq 6000 28/28 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (28/28 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX27413751, https://www.ncbi.nlm.nih.gov/sra?term=SRX27413752, https://www.ncbi.nlm.nih.gov/sra?term=SRX27413753, https://www.ncbi.nlm.nih.gov/sra?term=SRX27413754, https://www.ncbi.nlm.nih.gov/sra?term=SRX27413755, and 23 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE287614_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX27413751, https://www.ncbi.nlm.nih.gov/sra?term=SRX27413752, https://www.ncbi.nlm.nih.gov/sra?term=SRX27413753, https://www.ncbi.nlm.nih.gov/sra?term=SRX27413754, https://www.ncbi.nlm.nih.gov/sra?term=SRX27413755, and 23 more (see sample_metadata.csv) |

## Field presence

- cell line: 28/28

## Evidence for WARN/FAIL checks

### source_tissue (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE287614 / Series_summary: matched `Non-alcoholic fatty liver` in "Non-alcoholic fatty liver disease (NAFLD) - characterized by excess accumulation of fat in the liver - now affects one third of the world’s population. As NAFLD progresses, extracellular matrix compon"
### material_type (WARN)
- GSM8748885 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748886 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748887 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748888 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748889 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748890 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748891 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748892 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748893 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748894 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748895 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748896 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748897 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748898 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748899 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748900 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748901 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748902 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748903 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748904 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748905 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748906 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748907 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748908 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748909 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748910 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748911 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748912 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"

Decision: MANUAL_REVIEW

Reasons:
- source_tissue: liver-pattern source 0/28
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (28/28 samples)
<!-- /computed -->