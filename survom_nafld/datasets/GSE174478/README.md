# GSE174478

**Title:** Whole transcriptome profiling of Japanese  nonalcoholic fatty liver disease cohort.
**Accession:** GSE174478
**GEO URL:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE174478
**Organism:** Homo sapiens
**Tissue:** liver biopsy
**Disease/condition:** NAFLD, full fibrosis spectrum F0-F4
**Sample count:** 94
**Platform(s):** GPL24676
**PubMed:** 35380992, 40262132
**Screening decision:** STRONG_CANDIDATE

## Experimental design

Japanese NAFLD cohort, 94 liver biopsies with fibrosis stage and NAS score per sample; bulk RNA-seq.

## Bulk vs. single-cell determination

`single_cell_or_spatial` = **PASS** — no single-cell/spatial signal detected

## Technical checks

| check | status | observed |
|---|---|---|
| sample_count | PASS | 94 samples |
| organism_consistency | PASS | Homo sapiens 94/94 |
| source_tissue | PASS | liver-pattern source 94/94 |
| library_strategy | PASS | RNA-Seq 94/94 |
| library_source | PASS | transcriptomic 94/94 |
| library_selection | PASS | cDNA 94/94 |
| instrument_model | PASS | Illumina NovaSeq 6000 94/94 |
| metadata_completeness | PASS | reported consistently: age, disease, fibrosis_stage, nas_score, sex, tissue; not reported anywhere: bmi, diagnosis, ethnicity, group, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (94 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE174478_raw_gene_counts_matrix.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE174478_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX10894433, https://www.ncbi.nlm.nih.gov/sra?term=SRX10894434, https://www.ncbi.nlm.nih.gov/sra?term=SRX10894435, https://www.ncbi.nlm.nih.gov/sra?term=SRX10894436, https://www.ncbi.nlm.nih.gov/sra?term=SRX10894437, and 89 more (see sample_metadata.csv) |

## Metadata summary (canonical field distributions)

- **age**: 19 (1), 25 (2), 27 (2), 31 (1), 32 (1), 33 (1), 34 (2), 35 (4), 36 (1), 37 (1), 38 (1), 40 (1), 42 (3), 44 (4), 45 (1), 46 (1), 47 (2), 48 (2), 49 (2), 50 (2), 51 (6), 52 (1), 53 (3), 54 (3), 56 (1), 57 (2), 58 (3), 59 (2), 60 (2), 61 (2), 63 (1), 64 (1), 65 (1), 66 (4), 67 (2), 68 (8), 69 (1), 70 (2), 71 (1), 72 (1), 73 (1), 74 (1), 75 (2), 76 (2), 77 (1), 83 (2), 85 (1), 87 (1), 92 (1)
- **disease**: NAFLD (94)
- **fibrosis_stage**: 0 (7), 1 (29), 2 (23), 3 (24), 4 (11)
- **nas_score**: 1 (1), 2 (11), 3 (9), 4 (17), 5 (36), 6 (17), 7 (3)
- **sex**: F (45), M (49)
- **tissue**: liver (94)

## Expression data files

| file | tier | bytes | sha256 |
|---|---|---|---|
| GSE174478_raw_gene_counts_matrix.txt.gz | expression | 4143552 | `9c3e67b931255017...` |
| GSE174478_series_matrix.txt.gz | metadata | 4696 | `2aa5318b0b7b13aa...` |

## Selection rationale

Every other STRONG_CANDIDATE cohort in this collection is Western; this is the only non-Western population, and it independently reports the same F0-F4 fibrosis staging as the flagship dataset. Included for population/ethnic diversity rather than as a near-duplicate of GSE135251's design - the assignment brief warns against downloading as many datasets as possible, which favors a dataset like this one that adds a distinct population over one that would only repeat an existing design.

## Provenance

Screened and downloaded via `geo_screen`. Full source manifest: `source_manifest.json`. Full download manifest: `download_manifest.json`. Submission date: May 14 2021.
