# Validation report: GSE214432

Transcriptome profile of hepatocellular carcinoma from non-alcoholic fatty liver.

<!-- computed -->
Sample count: 45

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 45 samples |
| organism_consistency | PASS | Homo sapiens 45/45 |
| source_tissue | PASS | liver-pattern source 45/45 |
| library_strategy | PASS | RNA-Seq 45/45 |
| library_source | PASS | transcriptomic 45/45 |
| library_selection | PASS | cDNA 45/45 |
| instrument_model | PASS | Illumina NextSeq 500 45/45 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX21026420, https://www.ncbi.nlm.nih.gov/sra?term=SRX21026421, https://www.ncbi.nlm.nih.gov/sra?term=SRX21026422, https://www.ncbi.nlm.nih.gov/sra?term=SRX21026423, https://www.ncbi.nlm.nih.gov/sra?term=SRX21026424, and 40 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE214432_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX21026420, https://www.ncbi.nlm.nih.gov/sra?term=SRX21026421, https://www.ncbi.nlm.nih.gov/sra?term=SRX21026422, https://www.ncbi.nlm.nih.gov/sra?term=SRX21026423, https://www.ncbi.nlm.nih.gov/sra?term=SRX21026424, and 40 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 57 (2), 58 (1), 59 (2), 63 (2), 64 (1), 65 (4), 67 (1), 68 (2), 69 (3), 70 (1), 72 (2), 74 (1), 75 (3), 76 (2), 77 (6), 78 (1), 79 (5), 80 (1), 81 (1), 82 (3), 84 (1)
- **sex**: Female (9), Male (36)
- **tissue**: Liver (45)

## Field presence

- Sex: 45/45 (canon: sex)
- age: 45/45 (canon: age)
- recurrence: 45/45
- tissue: 45/45 (canon: tissue)

## Evidence for WARN/FAIL checks

### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE214432 / Series_title: matched `non-alcoholic fatty liver` in "Transcriptome profile of hepatocellular carcinoma from non-alcoholic fatty liver."
- GSE214432 / Series_summary: matched `Non-alcoholic fatty liver` in "Non-alcoholic fatty liver disease (NAFLD) is a major global health problem with its high prevalence and risk of developing lethal complications, progressive liver fibrosis and hepatocellular carcinoma"

Decision: MANUAL_REVIEW

Reasons:
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
<!-- /computed -->