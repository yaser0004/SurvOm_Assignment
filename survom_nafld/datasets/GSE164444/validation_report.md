# Validation report: GSE164444

A selective HDAC8 inhibitor potentiates antitumor immunity and efficacy of immune checkpoint blockade in hepatocellular carcinoma

<!-- computed -->
Sample count: 37

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 37 samples |
| organism_consistency | PASS | Homo sapiens 37/37 |
| source_tissue | WARN | liver-pattern source 20/37 |
| library_strategy | WARN | mixed strategies: ChIP-Seq 17/37, RNA-Seq 20/37 |
| library_source | WARN | library_source: genomic 17/37, transcriptomic 20/37 |
| library_selection | WARN | mixed library_selection: ChIP 17/37, cDNA 20/37 |
| instrument_model | PASS | Illumina HiSeq 4000 37/37 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (37 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | FAIL | no downloadable expression data or sequencing reads found |
| series_matrix | INFO | present, metadata-only (GSE164444_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | no SRA/raw sequencing links found |

## Canonical field distributions

- **tissue**: Adjacent non-tumor liver tissue (20), Tumor tissue (17)

## Field presence

- ajcc stage: 10/37
- genotype: 7/37
- tissue: 37/37 (canon: tissue)

## Evidence for WARN/FAIL checks

### source_tissue (WARN)
### library_strategy (WARN)
### library_source (WARN)
### library_selection (WARN)
### metadata_completeness (WARN)
### expression_data_availability (FAIL)

Decision: REJECT

Reasons:
- expression_data_availability: no downloadable expression data (no downloadable expression data or sequencing reads found)
<!-- /computed -->