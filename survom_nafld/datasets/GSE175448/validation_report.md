# Validation report: GSE175448

Transcriptome profiles of liver biopsy tissues before and after cenicriviroc treatment in patients with non-alcoholic steatohepatitis

<!-- computed -->
Sample count: 38

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 38 samples |
| organism_consistency | PASS | Homo sapiens 38/38 |
| source_tissue | PASS | liver-pattern source 38/38 |
| library_strategy | PASS | RNA-Seq 38/38 |
| library_source | PASS | transcriptomic 38/38 |
| library_selection | PASS | cDNA 38/38 |
| instrument_model | PASS | NextSeq 550 38/38 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX10973778, https://www.ncbi.nlm.nih.gov/sra?term=SRX10973779, https://www.ncbi.nlm.nih.gov/sra?term=SRX10973780, https://www.ncbi.nlm.nih.gov/sra?term=SRX10973781, https://www.ncbi.nlm.nih.gov/sra?term=SRX10973782, and 33 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE175448_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX10973778, https://www.ncbi.nlm.nih.gov/sra?term=SRX10973779, https://www.ncbi.nlm.nih.gov/sra?term=SRX10973780, https://www.ncbi.nlm.nih.gov/sra?term=SRX10973781, https://www.ncbi.nlm.nih.gov/sra?term=SRX10973782, and 33 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: liver (38)

## Field presence

- fibrosis improvement: 38/38
- timing of biopsy: 38/38
- tissue: 38/38 (canon: tissue)

## Evidence for WARN/FAIL checks

### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE175448 / Series_title: matched `steatohepatitis` in "Transcriptome profiles of liver biopsy tissues before and after cenicriviroc treatment in patients with non-alcoholic steatohepatitis"
- GSE175448 / Series_summary: matched `steatohepatitis` in "Non-alcoholic steatohepatitis (NASH) is a sharpy emerging cause of liver fibrosis and cancer that leads to poor prognosis of the patients. A dual CCR2/CCR5 inhibitor, cenicriviroc, was tested in a pha"
- GSE175448 / Series_overall_design: matched `NASH` in "Liver biopsy tissues were obtained before and after 1-year treatment with cenicriviroc 150mg once daily from fibrotic NASH patients who showed improvement (n=10) or no improvement (n=9) of fibrosis af"

Decision: MANUAL_REVIEW

Reasons:
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
<!-- /computed -->