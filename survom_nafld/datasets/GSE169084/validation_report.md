# Validation report: GSE169084

A human liver cell-based system modeling a clinical prognostic liver signature combined with single-cell RNA-Seq for discovery of liver disease therapeutics

<!-- computed -->
Sample count: 12

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 12 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 12/12 |
| source_tissue | WARN | liver-pattern source 0/12 |
| library_strategy | PASS | RNA-Seq 12/12 |
| library_source | PASS | transcriptomic 12/12 |
| library_selection | PASS | cDNA 12/12 |
| instrument_model | PASS | NextSeq 550 12/12 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | WARN | series prose mentions single-cell; sample metadata does not corroborate |
| material_type | WARN | cell/culture terms in sample metadata: Huh7, cell line (12/12 samples) |
| expression_data_availability | PASS | processed series-level file: GSE169084_Huh7dif_rawReadCounts.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE169084_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX10366595, https://www.ncbi.nlm.nih.gov/sra?term=SRX10366596, https://www.ncbi.nlm.nih.gov/sra?term=SRX10366597, https://www.ncbi.nlm.nih.gov/sra?term=SRX10366598, https://www.ncbi.nlm.nih.gov/sra?term=SRX10366599, and 7 more (see sample_metadata.csv) |

## Field presence

- cell line: 12/12
- objective response: 12/12

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE169084 / Series_summary: matched `NASH` in "Abstract: Chronic liver disease and hepatocellular carcinoma (HCC) are life-threatening with limited treatment options. The lack of clinically relevant/tractable experimental models hampers therapeuti"
### single_cell_or_spatial (WARN)
- GSE169084 / Series_title: matched `single-cell` in "A human liver cell-based system modeling a clinical prognostic liver signature combined with single-cell RNA-Seq for discovery of liver disease therapeutics"
### material_type (WARN)
- GSM5176220 / Sample_source_name_ch1: matched `Huh7` in "Huh751_D0_1"
- GSM5176221 / Sample_source_name_ch1: matched `Huh7` in "Huh751_D0_2"
- GSM5176222 / Sample_source_name_ch1: matched `Huh7` in "Huh751_D0_3"
- GSM5176223 / Sample_source_name_ch1: matched `Huh7` in "Huh751_D3_1"
- GSM5176224 / Sample_source_name_ch1: matched `Huh7` in "Huh751_D3_2"
- GSM5176225 / Sample_source_name_ch1: matched `Huh7` in "Huh751_D3_3"
- GSM5176226 / Sample_source_name_ch1: matched `Huh7` in "Huh751_D7_1"
- GSM5176227 / Sample_source_name_ch1: matched `Huh7` in "Huh751_D7_2"
- GSM5176228 / Sample_source_name_ch1: matched `Huh7` in "Huh751_D7_3"
- GSM5176229 / Sample_source_name_ch1: matched `Huh7` in "Huh751_D10_1"
- GSM5176230 / Sample_source_name_ch1: matched `Huh7` in "Huh751_D10_2"
- GSM5176231 / Sample_source_name_ch1: matched `Huh7` in "Huh751_D10_3"
- GSM5176220 / Sample_title: matched `Huh7` in "Huh751_D0_1"
- GSM5176221 / Sample_title: matched `Huh7` in "Huh751_D0_2"
- GSM5176222 / Sample_title: matched `Huh7` in "Huh751_D0_3"
- GSM5176223 / Sample_title: matched `Huh7` in "Huh751_D3_1"
- GSM5176224 / Sample_title: matched `Huh7` in "Huh751_D3_2"
- GSM5176225 / Sample_title: matched `Huh7` in "Huh751_D3_3"
- GSM5176226 / Sample_title: matched `Huh7` in "Huh751_D7_1"
- GSM5176227 / Sample_title: matched `Huh7` in "Huh751_D7_2"
- GSM5176228 / Sample_title: matched `Huh7` in "Huh751_D7_3"
- GSM5176229 / Sample_title: matched `Huh7` in "Huh751_D10_1"
- GSM5176230 / Sample_title: matched `Huh7` in "Huh751_D10_2"
- GSM5176231 / Sample_title: matched `Huh7` in "Huh751_D10_3"
- GSM5176220 / Sample_characteristics_ch1: matched `Huh7` in "objective response: Huh751 DMSO differentiation Day 0 Replicate 1"
- GSM5176220 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh751"
- GSM5176221 / Sample_characteristics_ch1: matched `Huh7` in "objective response: Huh751 DMSO differentiation Day 0 Replicate 2"
- GSM5176221 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh751"
- GSM5176222 / Sample_characteristics_ch1: matched `Huh7` in "objective response: Huh751 DMSO differentiation Day 0 Replicate 3"
- GSM5176222 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh751"
- GSM5176223 / Sample_characteristics_ch1: matched `Huh7` in "objective response: Huh751 DMSO differentiation Day 3 Replicate 1"
- GSM5176223 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh751"
- GSM5176224 / Sample_characteristics_ch1: matched `Huh7` in "objective response: Huh751 DMSO differentiation Day 3 Replicate 2"
- GSM5176224 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh751"
- GSM5176225 / Sample_characteristics_ch1: matched `Huh7` in "objective response: Huh751 DMSO differentiation Day 3 Replicate 3"
- GSM5176225 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh751"
- GSM5176226 / Sample_characteristics_ch1: matched `Huh7` in "objective response: Huh751 DMSO differentiation Day 7 Replicate 1"
- GSM5176226 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh751"
- GSM5176227 / Sample_characteristics_ch1: matched `Huh7` in "objective response: Huh751 DMSO differentiation Day 7 Replicate 2"
- GSM5176227 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh751"
- GSM5176228 / Sample_characteristics_ch1: matched `Huh7` in "objective response: Huh751 DMSO differentiation Day 7 Replicate 3"
- GSM5176228 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh751"
- GSM5176229 / Sample_characteristics_ch1: matched `Huh7` in "objective response: Huh751 DMSO differentiation Day 10 Replicate 1"
- GSM5176229 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh751"
- GSM5176230 / Sample_characteristics_ch1: matched `Huh7` in "objective response: Huh751 DMSO differentiation Day 10 Replicate 2"
- GSM5176230 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh751"
- GSM5176231 / Sample_characteristics_ch1: matched `Huh7` in "objective response: Huh751 DMSO differentiation Day 10 Replicate 3"
- GSM5176231 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh751"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 12 samples (below 20)
- source_tissue: liver-pattern source 0/12
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- single_cell_or_spatial: series prose mentions single-cell; sample metadata does not corroborate
- material_type: cell/culture terms in sample metadata: Huh7, cell line (12/12 samples)
<!-- /computed -->