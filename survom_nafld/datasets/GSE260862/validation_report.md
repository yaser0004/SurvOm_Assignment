# Validation report: GSE260862

Cell-permeated peptide P-T3H2 inhibits malignancy on hepatocarcinoma through stabilizing HNF4α protein

<!-- computed -->
Sample count: 6

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 6 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 6/6 |
| source_tissue | WARN | liver-pattern source 0/6 |
| library_strategy | PASS | RNA-Seq 6/6 |
| library_source | PASS | transcriptomic 6/6 |
| library_selection | PASS | cDNA 6/6 |
| instrument_model | PASS | Illumina NovaSeq 6000 6/6 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: Cell line, cell line (6/6 samples) |
| expression_data_availability | PASS | processed series-level file: GSE260862_gene_expression.xls.gz |
| series_matrix | INFO | present, metadata-only (GSE260862_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX23839130, https://www.ncbi.nlm.nih.gov/sra?term=SRX23839131, https://www.ncbi.nlm.nih.gov/sra?term=SRX23839132, https://www.ncbi.nlm.nih.gov/sra?term=SRX23839133, https://www.ncbi.nlm.nih.gov/sra?term=SRX23839134, and 1 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Cell line (6)
- **treatment**: control peptide P-T3H2-2A (3), peptide P-T3H2 (3)

## Field presence

- cell line: 6/6
- cell type: 6/6
- genotype: 6/6
- tissue: 6/6 (canon: tissue)
- treatment: 6/6 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE260862 / Series_summary: matched `non-alcoholic fatty liver` in "Objectives: Hepatocyte nuclear factor 4α (HNF4α) is a key regulator of hepatocyte function and has a strong therapeutic effect on hepatocellular carcinoma (HCC) by inducing  the differentiation of hep"
### material_type (WARN)
- GSM8125776 / Sample_source_name_ch1: matched `Cell line` in "Cell line"
- GSM8125777 / Sample_source_name_ch1: matched `Cell line` in "Cell line"
- GSM8125778 / Sample_source_name_ch1: matched `Cell line` in "Cell line"
- GSM8125779 / Sample_source_name_ch1: matched `Cell line` in "Cell line"
- GSM8125780 / Sample_source_name_ch1: matched `Cell line` in "Cell line"
- GSM8125781 / Sample_source_name_ch1: matched `Cell line` in "Cell line"
- GSM8125776 / Sample_characteristics_ch1: matched `Cell line` in "tissue: Cell line"
- GSM8125776 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh-7"
- GSM8125777 / Sample_characteristics_ch1: matched `Cell line` in "tissue: Cell line"
- GSM8125777 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh-7"
- GSM8125778 / Sample_characteristics_ch1: matched `Cell line` in "tissue: Cell line"
- GSM8125778 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh-7"
- GSM8125779 / Sample_characteristics_ch1: matched `Cell line` in "tissue: Cell line"
- GSM8125779 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh-7"
- GSM8125780 / Sample_characteristics_ch1: matched `Cell line` in "tissue: Cell line"
- GSM8125780 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh-7"
- GSM8125781 / Sample_characteristics_ch1: matched `Cell line` in "tissue: Cell line"
- GSM8125781 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh-7"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 6 samples (below 20)
- source_tissue: liver-pattern source 0/6
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: Cell line, cell line (6/6 samples)
<!-- /computed -->