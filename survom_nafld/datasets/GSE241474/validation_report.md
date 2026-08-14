# Validation report: GSE241474

A genetically engineered mouse model (GEMM) of NUT carcinoma (RNA-Seq)

<!-- computed -->
Sample count: 21

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 21 samples |
| organism_consistency | WARN | mixed organisms: Homo sapiens 1/21, Mus musculus 20/21 |
| source_tissue | WARN | liver-pattern source 0/21 |
| library_strategy | PASS | RNA-Seq 21/21 |
| library_source | PASS | transcriptomic 21/21 |
| library_selection | PASS | cDNA 21/21 |
| instrument_model | PASS | Illumina NovaSeq 6000 21/21 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | FAIL | no NAFLD-spectrum term found in series or sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (21/21 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX21455953, https://www.ncbi.nlm.nih.gov/sra?term=SRX21455954, https://www.ncbi.nlm.nih.gov/sra?term=SRX21455955, https://www.ncbi.nlm.nih.gov/sra?term=SRX21455956, https://www.ncbi.nlm.nih.gov/sra?term=SRX21455957, and 16 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE241474-GPL24247_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX21455953, https://www.ncbi.nlm.nih.gov/sra?term=SRX21455954, https://www.ncbi.nlm.nih.gov/sra?term=SRX21455955, https://www.ncbi.nlm.nih.gov/sra?term=SRX21455956, https://www.ncbi.nlm.nih.gov/sra?term=SRX21455957, and 16 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: 311E cell line (12), 317E cell line (3), n/a (6)
- **treatment**: 96hr (12), n/a (9)

## Field presence

- cell line: 21/21
- cell type: 21/21
- genotype: 21/21
- tissue: 21/21 (canon: tissue)
- treatment: 21/21 (canon: treatment)

## Evidence for WARN/FAIL checks

### organism_consistency (WARN)
### source_tissue (WARN)
### metadata_completeness (WARN)
### disease_relevance (FAIL)
### material_type (WARN)
- GSM7729577 / Sample_source_name_ch1: matched `cell line` in "311E cell line"
- GSM7729578 / Sample_source_name_ch1: matched `cell line` in "311E cell line"
- GSM7729579 / Sample_source_name_ch1: matched `cell line` in "311E cell line"
- GSM7729580 / Sample_source_name_ch1: matched `cell line` in "311E cell line"
- GSM7729581 / Sample_source_name_ch1: matched `cell line` in "311E cell line"
- GSM7729582 / Sample_source_name_ch1: matched `cell line` in "311E cell line"
- GSM7729583 / Sample_source_name_ch1: matched `cell line` in "311E cell line"
- GSM7729584 / Sample_source_name_ch1: matched `cell line` in "311E cell line"
- GSM7729585 / Sample_source_name_ch1: matched `cell line` in "311E cell line"
- GSM7729586 / Sample_source_name_ch1: matched `cell line` in "311E cell line"
- GSM7729587 / Sample_source_name_ch1: matched `cell line` in "311E cell line"
- GSM7729588 / Sample_source_name_ch1: matched `cell line` in "311E cell line"
- GSM7729589 / Sample_source_name_ch1: matched `cell line` in "317E cell line"
- GSM7729590 / Sample_source_name_ch1: matched `cell line` in "317E cell line"
- GSM7729591 / Sample_source_name_ch1: matched `cell line` in "317E cell line"
- GSM7729589 / Sample_title: matched `cell line` in "317E cell line bio rep 1"
- GSM7729590 / Sample_title: matched `cell line` in "317E cell line bio rep 2"
- GSM7729591 / Sample_title: matched `cell line` in "317E cell line bio rep 3"
- GSM7729577 / Sample_characteristics_ch1: matched `cell line` in "tissue: 311E cell line"
- GSM7729577 / Sample_characteristics_ch1: matched `cell line` in "cell line: GEMM, esophagus mNC tumor"
- GSM7729578 / Sample_characteristics_ch1: matched `cell line` in "tissue: 311E cell line"
- GSM7729578 / Sample_characteristics_ch1: matched `cell line` in "cell line: GEMM, esophagus mNC tumor"
- GSM7729579 / Sample_characteristics_ch1: matched `cell line` in "tissue: 311E cell line"
- GSM7729579 / Sample_characteristics_ch1: matched `cell line` in "cell line: GEMM, esophagus mNC tumor"
- GSM7729580 / Sample_characteristics_ch1: matched `cell line` in "tissue: 311E cell line"
- GSM7729580 / Sample_characteristics_ch1: matched `cell line` in "cell line: GEMM, esophagus mNC tumor"
- GSM7729581 / Sample_characteristics_ch1: matched `cell line` in "tissue: 311E cell line"
- GSM7729581 / Sample_characteristics_ch1: matched `cell line` in "cell line: GEMM, esophagus mNC tumor"
- GSM7729582 / Sample_characteristics_ch1: matched `cell line` in "tissue: 311E cell line"
- GSM7729582 / Sample_characteristics_ch1: matched `cell line` in "cell line: GEMM, esophagus mNC tumor"
- GSM7729583 / Sample_characteristics_ch1: matched `cell line` in "tissue: 311E cell line"
- GSM7729583 / Sample_characteristics_ch1: matched `cell line` in "cell line: GEMM, esophagus mNC tumor"
- GSM7729584 / Sample_characteristics_ch1: matched `cell line` in "tissue: 311E cell line"
- GSM7729584 / Sample_characteristics_ch1: matched `cell line` in "cell line: GEMM, esophagus mNC tumor"
- GSM7729585 / Sample_characteristics_ch1: matched `cell line` in "tissue: 311E cell line"
- GSM7729585 / Sample_characteristics_ch1: matched `cell line` in "cell line: GEMM, esophagus mNC tumor"
- GSM7729586 / Sample_characteristics_ch1: matched `cell line` in "tissue: 311E cell line"
- GSM7729586 / Sample_characteristics_ch1: matched `cell line` in "cell line: GEMM, esophagus mNC tumor"
- GSM7729587 / Sample_characteristics_ch1: matched `cell line` in "tissue: 311E cell line"
- GSM7729587 / Sample_characteristics_ch1: matched `cell line` in "cell line: GEMM, esophagus mNC tumor"
- GSM7729588 / Sample_characteristics_ch1: matched `cell line` in "tissue: 311E cell line"
- GSM7729588 / Sample_characteristics_ch1: matched `cell line` in "cell line: GEMM, esophagus mNC tumor"
- GSM7729589 / Sample_characteristics_ch1: matched `cell line` in "tissue: 317E cell line"
- GSM7729589 / Sample_characteristics_ch1: matched `cell line` in "cell line: GEMM, esophagus mNC tumor"
- GSM7729590 / Sample_characteristics_ch1: matched `cell line` in "tissue: 317E cell line"
- GSM7729590 / Sample_characteristics_ch1: matched `cell line` in "cell line: GEMM, esophagus mNC tumor"
- GSM7729591 / Sample_characteristics_ch1: matched `cell line` in "tissue: 317E cell line"
- GSM7729591 / Sample_characteristics_ch1: matched `cell line` in "cell line: GEMM, esophagus mNC tumor"
- GSM7729592 / Sample_characteristics_ch1: matched `cell line` in "cell line: fresh GEMM tumor tissue from which 311E cell line was derived"
- GSM7729593 / Sample_characteristics_ch1: matched `cell line` in "cell line: fresh GEMM tumor tissue from which 317E cell line was derived"
- GSM7729594 / Sample_characteristics_ch1: matched `cell line` in "cell line: SOX2-/-BRD4-NUTM1+/- esophgeal mucosa fresh tissue"
- GSM7729595 / Sample_characteristics_ch1: matched `cell line` in "cell line: SOX2-/-BRD4-NUTM1+/- esophgeal mucosa fresh tissue"
- GSM7729596 / Sample_characteristics_ch1: matched `cell line` in "cell line: SOX2-/-BRD4-NUTM1+/- esophgeal mucosa fresh tissue"
- GSM7729597 / Sample_characteristics_ch1: matched `cell line` in "cell line: pleural fluid"

Decision: REJECT

Reasons:
- disease_relevance: no NAFLD-spectrum term in series or sample metadata (no NAFLD-spectrum term found in series or sample metadata)
<!-- /computed -->