# Validation report: GSE164441

A selective HDAC8 inhibitor potentiates antitumor immunity and efficacy of immune checkpoint blockade in hepatocellular carcinoma [RNA-seq]

<!-- computed -->
Sample count: 20

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 20 samples |
| organism_consistency | PASS | Homo sapiens 20/20 |
| source_tissue | WARN | liver-pattern source 10/20 |
| library_strategy | PASS | RNA-Seq 20/20 |
| library_source | PASS | transcriptomic 20/20 |
| library_selection | PASS | cDNA 20/20 |
| instrument_model | PASS | Illumina HiSeq 4000 20/20 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (20 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE164441_RNAseq_10Tvs10NT_cuffdiff_FPKM.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE164441_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | no SRA/raw sequencing links found |

## Canonical field distributions

- **tissue**: Adjacent non-tumor liver tissue (10), Tumor tissue (10)

## Field presence

- ajcc stage: 10/20
- tissue: 20/20 (canon: tissue)

## Evidence for WARN/FAIL checks

### source_tissue (WARN)
### metadata_completeness (WARN)

Decision: MANUAL_REVIEW

Reasons:
- source_tissue: liver-pattern source 10/20
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
<!-- /computed -->