# Validation report: GSE233808

RNA N6-methyladenosine methyltransferase METTL3 drives NAFLD-HCC and is a therapeutic target for boosting immunotherapy

<!-- computed -->
Sample count: 12

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 12 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 12/12 |
| source_tissue | WARN | liver-pattern source 0/12 |
| library_strategy | WARN | mixed strategies: OTHER 8/12, RNA-Seq 4/12 |
| library_source | PASS | transcriptomic 12/12 |
| library_selection | WARN | mixed library_selection: cDNA 4/12, other 8/12 |
| instrument_model | WARN | mixed instruments: Illumina HiSeq 4000 4/12, Illumina NovaSeq 6000 8/12 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (12 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (12/12 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX20550764, https://www.ncbi.nlm.nih.gov/sra?term=SRX20550765, https://www.ncbi.nlm.nih.gov/sra?term=SRX20550766, https://www.ncbi.nlm.nih.gov/sra?term=SRX20550767, https://www.ncbi.nlm.nih.gov/sra?term=SRX20550768, and 7 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE233808-GPL20301_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX20550764, https://www.ncbi.nlm.nih.gov/sra?term=SRX20550765, https://www.ncbi.nlm.nih.gov/sra?term=SRX20550766, https://www.ncbi.nlm.nih.gov/sra?term=SRX20550767, https://www.ncbi.nlm.nih.gov/sra?term=SRX20550768, and 7 more (see sample_metadata.csv) |

## Field presence

- cell line: 12/12
- cell type: 12/12

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
### library_strategy (WARN)
### library_selection (WARN)
### instrument_model (WARN)
### metadata_completeness (WARN)
### material_type (WARN)
- GSM7437129 / Sample_source_name_ch1: matched `cell line` in "HKCI2 cell line"
- GSM7437131 / Sample_source_name_ch1: matched `cell line` in "HKCI2 cell line"
- GSM7437132 / Sample_source_name_ch1: matched `cell line` in "HKCI2 cell line"
- GSM7437134 / Sample_source_name_ch1: matched `cell line` in "HKCI2 cell line"
- GSM7437135 / Sample_source_name_ch1: matched `cell line` in "HKCI2 cell line"
- GSM7437136 / Sample_source_name_ch1: matched `cell line` in "HKCI2 cell line"
- GSM7437137 / Sample_source_name_ch1: matched `cell line` in "HKCI2 cell line"
- GSM7437138 / Sample_source_name_ch1: matched `cell line` in "HKCI2 cell line"
- GSM7437139 / Sample_source_name_ch1: matched `cell line` in "HKCI2 cell line"
- GSM7437140 / Sample_source_name_ch1: matched `cell line` in "HKCI2 cell line"
- GSM7437141 / Sample_source_name_ch1: matched `cell line` in "HKCI2 cell line"
- GSM7437142 / Sample_source_name_ch1: matched `cell line` in "HKCI2 cell line"
- GSM7437129 / Sample_characteristics_ch1: matched `cell line` in "cell line: HKCI2 cell line"
- GSM7437131 / Sample_characteristics_ch1: matched `cell line` in "cell line: HKCI2 cell line"
- GSM7437132 / Sample_characteristics_ch1: matched `cell line` in "cell line: HKCI2 cell line"
- GSM7437134 / Sample_characteristics_ch1: matched `cell line` in "cell line: HKCI2 cell line"
- GSM7437135 / Sample_characteristics_ch1: matched `cell line` in "cell line: HKCI2 cell line"
- GSM7437136 / Sample_characteristics_ch1: matched `cell line` in "cell line: HKCI2 cell line"
- GSM7437137 / Sample_characteristics_ch1: matched `cell line` in "cell line: HKCI2 cell line"
- GSM7437138 / Sample_characteristics_ch1: matched `cell line` in "cell line: HKCI2 cell line"
- GSM7437139 / Sample_characteristics_ch1: matched `cell line` in "cell line: HKCI2 cell line"
- GSM7437140 / Sample_characteristics_ch1: matched `cell line` in "cell line: HKCI2 cell line"
- GSM7437141 / Sample_characteristics_ch1: matched `cell line` in "cell line: HKCI2 cell line"
- GSM7437142 / Sample_characteristics_ch1: matched `cell line` in "cell line: HKCI2 cell line"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 12 samples (below 20)
- source_tissue: liver-pattern source 0/12
- library_strategy: mixed strategies: OTHER 8/12, RNA-Seq 4/12
- library_selection: mixed library_selection: cDNA 4/12, other 8/12
- instrument_model: mixed instruments: Illumina HiSeq 4000 4/12, Illumina NovaSeq 6000 8/12
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- material_type: cell/culture terms in sample metadata: cell line (12/12 samples)
<!-- /computed -->