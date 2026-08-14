# Validation report: GSE233806

RNA N6-methyladenosine methyltransferase METTL3 drives NAFLD-HCC and is a therapeutic target for boosting immunotherapy [RNA-Seq]

<!-- computed -->
Sample count: 4

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 4 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 4/4 |
| source_tissue | WARN | liver-pattern source 0/4 |
| library_strategy | PASS | RNA-Seq 4/4 |
| library_source | PASS | transcriptomic 4/4 |
| library_selection | PASS | cDNA 4/4 |
| instrument_model | PASS | Illumina HiSeq 4000 4/4 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (4 sample(s)) |
| single_cell_or_spatial | WARN | series prose mentions Single-cell; sample metadata does not corroborate |
| material_type | WARN | cell/culture terms in sample metadata: cell line (4/4 samples) |
| expression_data_availability | PASS | processed series-level file: GSE233806_Raw_counts_txt.csv.gz |
| series_matrix | INFO | present, metadata-only (GSE233806_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX20550764, https://www.ncbi.nlm.nih.gov/sra?term=SRX20550765, https://www.ncbi.nlm.nih.gov/sra?term=SRX20550766, https://www.ncbi.nlm.nih.gov/sra?term=SRX20550767 |

## Field presence

- cell line: 4/4
- cell type: 4/4

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
### metadata_completeness (WARN)
### single_cell_or_spatial (WARN)
- GSE233806 / Series_summary: matched `Single-cell` in "Non-alcoholic fatty liver disease (NAFLD) is an emerging risk factor of hepatocellular carcinoma (HCC). However, the mechanism and target therapy on NAFLD-HCC are still unclear. Here, we identify that"
### material_type (WARN)
- GSM7437129 / Sample_source_name_ch1: matched `cell line` in "HKCI2 cell line"
- GSM7437131 / Sample_source_name_ch1: matched `cell line` in "HKCI2 cell line"
- GSM7437132 / Sample_source_name_ch1: matched `cell line` in "HKCI2 cell line"
- GSM7437134 / Sample_source_name_ch1: matched `cell line` in "HKCI2 cell line"
- GSM7437129 / Sample_characteristics_ch1: matched `cell line` in "cell line: HKCI2 cell line"
- GSM7437131 / Sample_characteristics_ch1: matched `cell line` in "cell line: HKCI2 cell line"
- GSM7437132 / Sample_characteristics_ch1: matched `cell line` in "cell line: HKCI2 cell line"
- GSM7437134 / Sample_characteristics_ch1: matched `cell line` in "cell line: HKCI2 cell line"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 4 samples (below 20)
- source_tissue: liver-pattern source 0/4
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- single_cell_or_spatial: series prose mentions Single-cell; sample metadata does not corroborate
- material_type: cell/culture terms in sample metadata: cell line (4/4 samples)
<!-- /computed -->