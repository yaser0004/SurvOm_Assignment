# Validation report: GSE295362

Hepatocyte-derived Pumilio1-enriched exosomes inhibit HSC activation by suppressing tropomyosin-4 translation

<!-- computed -->
Sample count: 6

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 6 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 6/6 |
| source_tissue | PASS | liver-pattern source 6/6 |
| library_strategy | PASS | RNA-Seq 6/6 |
| library_source | PASS | transcriptomic 6/6 |
| library_selection | PASS | cDNA 6/6 |
| instrument_model | PASS | Illumina HiSeq 2500 6/6 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: LX-2, cell line (6/6 samples) |
| expression_data_availability | PASS | processed series-level file: GSE295362_All_gene_expression_TPM.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE295362_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX28505028, https://www.ncbi.nlm.nih.gov/sra?term=SRX28505029, https://www.ncbi.nlm.nih.gov/sra?term=SRX28505030, https://www.ncbi.nlm.nih.gov/sra?term=SRX28505031, https://www.ncbi.nlm.nih.gov/sra?term=SRX28505032, and 1 more (see sample_metadata.csv) |

## Canonical field distributions

- **treatment**: siRNA Control (3), siRNA PUM1 (3)

## Field presence

- batch: 6/6
- cell line: 6/6
- cell type: 6/6
- genotype: 6/6
- treatment: 6/6 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE295362 / Series_summary: matched `Metabolic dysfunction-associated stea` in "Metabolic dysfunction-associated steatotic liver disease (MASLD) has become the most common chronic liver disease globally. Abnormal crosstalk between hepatocytes and hepatic stellate cells (HSCs) lea"
### material_type (WARN)
- GSM8946544 / Sample_source_name_ch1: matched `LX-2` in "LX-2 cells"
- GSM8946545 / Sample_source_name_ch1: matched `LX-2` in "LX-2 cells"
- GSM8946546 / Sample_source_name_ch1: matched `LX-2` in "LX-2 cells"
- GSM8946547 / Sample_source_name_ch1: matched `LX-2` in "LX-2 cells"
- GSM8946548 / Sample_source_name_ch1: matched `LX-2` in "LX-2 cells"
- GSM8946549 / Sample_source_name_ch1: matched `LX-2` in "LX-2 cells"
- GSM8946544 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2 cells"
- GSM8946545 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2 cells"
- GSM8946546 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2 cells"
- GSM8946547 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2 cells"
- GSM8946548 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2 cells"
- GSM8946549 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2 cells"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 6 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: LX-2, cell line (6/6 samples)
<!-- /computed -->