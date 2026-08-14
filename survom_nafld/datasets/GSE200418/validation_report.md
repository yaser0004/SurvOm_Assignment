# Validation report: GSE200418

Transcriptomic profiling of induced steatosis in human precision-cut liver slices

<!-- computed -->
Sample count: 99

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 99 samples |
| organism_consistency | PASS | Homo sapiens 99/99 |
| source_tissue | PASS | liver-pattern source 99/99 |
| library_strategy | PASS | RNA-Seq 99/99 |
| library_source | PASS | transcriptomic 99/99 |
| library_selection | PASS | cDNA 99/99 |
| instrument_model | PASS | Illumina NovaSeq 6000 99/99 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE200418_1047_uTPM.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE200418_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX14778800, https://www.ncbi.nlm.nih.gov/sra?term=SRX14778801, https://www.ncbi.nlm.nih.gov/sra?term=SRX14778802, https://www.ncbi.nlm.nih.gov/sra?term=SRX14778803, https://www.ncbi.nlm.nih.gov/sra?term=SRX14778804, and 94 more (see sample_metadata.csv) |

## Canonical field distributions

- **sex**: Male (15), Unknown (84)
- **tissue**: Liver (99)
- **treatment**: CTRh (13), Fh (13), GFIOh (11), GFIPOh (10), GFIPh (14), GFIh (13), GFh (13), Gh (12)

## Field presence

- donor id: 99/99
- gender: 99/99 (canon: sex)
- sampling: 99/99
- timepoint: 99/99
- tissue: 99/99 (canon: tissue)
- treatment: 99/99 (canon: treatment)

## Evidence for WARN/FAIL checks

### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE200418 / Series_title: matched `steatosis` in "Transcriptomic profiling of induced steatosis in human precision-cut liver slices"
- GSE200418 / Series_summary: matched `non-alcoholic fatty liver` in "Progression of non-alcoholic fatty liver disease (NAFLD) to non-alcoholic steatohepatitis (NASH) is a major cause of end-stage liver diseases. There is a high need for predictive human ex vivo models "

Decision: MANUAL_REVIEW

Reasons:
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
<!-- /computed -->