# GSE167523

**Title:** Transcriptome profiling of human non-alcoholic fatty liver disease
**Accession:** GSE167523
**GEO URL:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE167523
**Organism:** Homo sapiens
**Tissue:** liver biopsy
**Disease/condition:** NAFLD
**Sample count:** 98
**Platform(s):** GPL21290
**PubMed:** 34105780
**Screening decision:** STRONG_CANDIDATE

## Experimental design

98-sample human NAFLD cohort; bulk RNA-seq, with a separate phenotype-correspondence spreadsheet linking samples to clinical data.

## Bulk vs. single-cell determination

`single_cell_or_spatial` = **PASS** — no single-cell/spatial signal detected

## Technical checks

| check | status | observed |
|---|---|---|
| sample_count | PASS | 98 samples |
| organism_consistency | PASS | Homo sapiens 98/98 |
| source_tissue | PASS | liver-pattern source 98/98 |
| library_strategy | PASS | RNA-Seq 98/98 |
| library_source | PASS | transcriptomic 98/98 |
| library_selection | PASS | cDNA 98/98 |
| instrument_model | PASS | Illumina HiSeq 3000 98/98 |
| metadata_completeness | PASS | reported consistently: age, disease, sex, tissue; not reported anywhere: bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (98 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (98/98), packaged in GSE167523_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE167523_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX10181356, https://www.ncbi.nlm.nih.gov/sra?term=SRX10181357, https://www.ncbi.nlm.nih.gov/sra?term=SRX10181358, https://www.ncbi.nlm.nih.gov/sra?term=SRX10181359, https://www.ncbi.nlm.nih.gov/sra?term=SRX10181360, and 93 more (see sample_metadata.csv) |

## Metadata summary (canonical field distributions)

- **age**: 18 (1), 19 (1), 24 (1), 29 (1), 30 (2), 31 (1), 36 (3), 37 (1), 38 (1), 40 (3), 43 (1), 44 (1), 45 (5), 46 (4), 47 (4), 48 (4), 49 (3), 50 (5), 51 (3), 53 (2), 54 (4), 55 (2), 56 (2), 57 (2), 58 (2), 59 (1), 60 (1), 61 (2), 62 (5), 63 (5), 64 (3), 65 (1), 66 (5), 67 (3), 69 (2), 70 (1), 71 (2), 73 (1), 74 (2), 76 (1), 77 (2), 78 (1), 81 (1)
- **disease**: NAFLD (98)
- **sex**: F (34), M (64)
- **tissue**: liver biopsy (98)

## Expression data files

| file | tier | bytes | sha256 |
|---|---|---|---|
| GSE167523_Raw_gene_counts_matrix.txt.gz | expression | 2652007 | `7714aa32816f4a37...` |
| GSE167523_Sample_phenotype_correspondence.xlsx | metadata | 11131 | `bee26e98858fc8f9...` |
| GSE167523_series_matrix.txt.gz | metadata | 6226 | `746d69b44f1124c8...` |

## Selection rationale

An independent, previously-vetted NAFLD cohort (evaluated manually before this tool existed) that reports disease status and tissue type but not fibrosis/NAS staging - useful as an independent validation cohort with a genuinely different metadata shape from the staged cohorts above, rather than as another fibrosis-spectrum dataset.

## Provenance

Screened and downloaded via `geo_screen`. Full source manifest: `source_manifest.json`. Full download manifest: `download_manifest.json`. Submission date: Feb 25 2021.
