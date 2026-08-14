# Validation report: GSE266939

The transcription factor ZNF469 regulates collagen production in liver fibrosis [RNAseq_HSC]

<!-- computed -->
Sample count: 36

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 36 samples |
| organism_consistency | PASS | Homo sapiens 36/36 |
| source_tissue | WARN | liver-pattern source 0/36 |
| library_strategy | PASS | RNA-Seq 36/36 |
| library_source | PASS | transcriptomic 36/36 |
| library_selection | PASS | cDNA 36/36 |
| instrument_model | PASS | Illumina NovaSeq 6000 36/36 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (36/36 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX24488324, https://www.ncbi.nlm.nih.gov/sra?term=SRX24488325, https://www.ncbi.nlm.nih.gov/sra?term=SRX24488326, https://www.ncbi.nlm.nih.gov/sra?term=SRX24488327, https://www.ncbi.nlm.nih.gov/sra?term=SRX24488328, and 31 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE266939_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX24488324, https://www.ncbi.nlm.nih.gov/sra?term=SRX24488325, https://www.ncbi.nlm.nih.gov/sra?term=SRX24488326, https://www.ncbi.nlm.nih.gov/sra?term=SRX24488327, https://www.ncbi.nlm.nih.gov/sra?term=SRX24488328, and 31 more (see sample_metadata.csv) |

## Field presence

- cell line: 36/36

## Evidence for WARN/FAIL checks

### source_tissue (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE266939 / Series_summary: matched `Non-alcoholic fatty liver` in "Non-alcoholic fatty liver disease (NAFLD)—characterized by excess accumulation of fat in the liver—now affects one third of the world’s population. As NAFLD progresses, extracellular matrix components"
### material_type (WARN)
- GSM8257189 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257190 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257191 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257192 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257193 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257194 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257195 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257196 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257197 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257198 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257199 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257200 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257201 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257202 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257203 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257204 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257205 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257206 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257207 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257208 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257209 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257210 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257211 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257212 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257213 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257214 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257215 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257216 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257217 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257218 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257219 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257220 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257221 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257222 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257223 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257224 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"

Decision: MANUAL_REVIEW

Reasons:
- source_tissue: liver-pattern source 0/36
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (36/36 samples)
<!-- /computed -->