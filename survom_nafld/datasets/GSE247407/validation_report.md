# Validation report: GSE247407

Induction ofsteatosis in primary human hepatocytes manifests into hepatic pathophysiology of metabolic dysfunction-associated liver disease

<!-- computed -->
Sample count: 30

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 30 samples |
| organism_consistency | PASS | Homo sapiens 30/30 |
| source_tissue | PASS | liver-pattern source 30/30 |
| library_strategy | PASS | RNA-Seq 30/30 |
| library_source | PASS | transcriptomic 30/30 |
| library_selection | PASS | cDNA 30/30 |
| instrument_model | PASS | Illumina NovaSeq 6000 30/30 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | INFO | series prose mentions in vitro; sample metadata does not corroborate |
| expression_data_availability | PASS | processed series-level file: GSE247407_gene_fpkm.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE247407_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX22478235, https://www.ncbi.nlm.nih.gov/sra?term=SRX22478236, https://www.ncbi.nlm.nih.gov/sra?term=SRX22478237, https://www.ncbi.nlm.nih.gov/sra?term=SRX22478238, https://www.ncbi.nlm.nih.gov/sra?term=SRX22478239, and 25 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Liver (30)
- **treatment**: Control (15), FFA (15)

## Field presence

- cell type: 30/30
- individual: 30/30
- tissue: 30/30 (canon: tissue)
- treatment: 30/30 (canon: treatment)

## Evidence for WARN/FAIL checks

### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE247407 / Series_title: matched `steatosis` in "Induction ofsteatosis in primary human hepatocytes manifests into hepatic pathophysiology of metabolic dysfunction-associated liver disease"
- GSE247407 / Series_summary: matched `MASLD` in "Background & Aims:The prevalence of metabolic dysfunction-associated liver disease (MASLD) has been strongly increasing over the last decades. As MASLD is often associated with more severe disease sta"

Decision: MANUAL_REVIEW

Reasons:
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
<!-- /computed -->