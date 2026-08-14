# Validation report: GSE173671

A human liver cell-based system modeling a clinical prognostic liver signature combined with single-cell RNA-Seq for discovery of liver disease therapeutics

<!-- computed -->
Sample count: 2

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 2 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 2/2 |
| source_tissue | PASS | liver-pattern source 2/2 |
| library_strategy | PASS | RNA-Seq 2/2 |
| library_source | PASS | transcriptomic 2/2 |
| library_selection | PASS | cDNA 2/2 |
| instrument_model | PASS | Illumina NextSeq 500 2/2 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: scRNA (2 sample(s)) |
| material_type | INFO | series prose mentions spheroid; sample metadata does not corroborate |
| expression_data_availability | PASS | processed series-level file: GSE173671_gene_counts_matrix.tsv.gz |
| series_matrix | INFO | present, metadata-only (GSE173671_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX10723954, https://www.ncbi.nlm.nih.gov/sra?term=SRX10723955 |

## Canonical field distributions

- **tissue**: Liver tissues from patients with advanced liver disease and HCC (2)
- **treatment**: DMSO (1), Nizatidine (1)

## Field presence

- cell type: 2/2
- tissue: 2/2 (canon: tissue)
- treatment: 2/2 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE173671 / Series_summary: matched `NASH` in "Abstract: Chronic liver disease and hepatocellular carcinoma (HCC) are life-threatening with limited treatment options. The lack of clinically relevant/tractable experimental models hampers therapeuti"
### single_cell_or_spatial (FAIL)
- GSM5273490 / Sample_extract_protocol_ch1: matched `scRNA` in "scRNA-Seq was performed by Single-Cell Discoveries B.V. using SORT-seq protocol."
- GSM5273491 / Sample_extract_protocol_ch1: matched `scRNA` in "scRNA-Seq was performed by Single-Cell Discoveries B.V. using SORT-seq protocol."

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: scRNA (2 sample(s)))
<!-- /computed -->