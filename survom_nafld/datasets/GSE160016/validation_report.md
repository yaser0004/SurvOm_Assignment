# Validation report: GSE160016

TREM2 sustains macrophage-hepatocyte metabolic coordination in NAFLD and sepsis [Human_liver_RNA_seq]

<!-- computed -->
Sample count: 11

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 11 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 11/11 |
| source_tissue | PASS | liver-pattern source 11/11 |
| library_strategy | PASS | RNA-Seq 11/11 |
| library_source | PASS | transcriptomic 11/11 |
| library_selection | PASS | cDNA 11/11 |
| instrument_model | PASS | Illumina NovaSeq 6000 11/11 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (11 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE160016_gene_fpkm.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE160016_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX9353386, https://www.ncbi.nlm.nih.gov/sra?term=SRX9353387, https://www.ncbi.nlm.nih.gov/sra?term=SRX9353388, https://www.ncbi.nlm.nih.gov/sra?term=SRX9353389, https://www.ncbi.nlm.nih.gov/sra?term=SRX9353390, and 6 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 16 (1), 18 (1), 33 (1), 37 (2), 40 (1), 46 (2), 50 (1), 51 (2)
- **sex**: Female (5), Male (6)
- **tissue**: Liver (11)

## Field presence

- Sex: 11/11 (canon: sex)
- age: 11/11 (canon: age)
- donor type: 11/11
- tissue: 11/11 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 11 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
<!-- /computed -->