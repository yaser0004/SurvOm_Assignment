# GSE130970

**Title:** Gene expression predicts histological severity and reveals distinct molecular profiles of nonalcoholic fatty liver disease
**Accession:** GSE130970
**GEO URL:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE130970
**Organism:** Homo sapiens
**Tissue:** liver biopsy
**Disease/condition:** NAFLD spectrum, F0-F4 fibrosis, NAS 0-6
**Sample count:** 78
**Platform(s):** GPL16791
**PubMed:** 31467298
**Screening decision:** STRONG_CANDIDATE

## Experimental design

78 human liver biopsies: 6 histologically normal, 72 covering the full NAFLD spectrum (NAFLD Activity Score 0-6, fibrosis stage 0-4). Every sample carries all three individual NAS components (steatosis grade, lobular inflammation grade, cytological ballooning grade) as separate reported fields, in addition to the composite NAS and fibrosis stage.

## Bulk vs. single-cell determination

`single_cell_or_spatial` = **PASS** — no single-cell/spatial signal detected

## Technical checks

| check | status | observed |
|---|---|---|
| sample_count | PASS | 78 samples |
| organism_consistency | PASS | Homo sapiens 78/78 |
| source_tissue | PASS | liver-pattern source 78/78 |
| library_strategy | PASS | RNA-Seq 78/78 |
| library_source | PASS | transcriptomic 78/78 |
| library_selection | PASS | cDNA 78/78 |
| instrument_model | PASS | Illumina HiSeq 2500 78/78 |
| metadata_completeness | PASS | reported consistently: age, fibrosis_stage, nas_score, sex, steatosis_grade, tissue; not reported anywhere: bmi, diagnosis, disease, ethnicity, group, stage, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (78 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE130970_all_sample_salmon_tximport_TPM_entrez_gene_ID.csv.gz |
| series_matrix | INFO | present, metadata-only (GSE130970_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded (78 samples, see sample_metadata.csv) |

## Metadata summary (canonical field distributions)

- **age**: 39 distinct values, range 19-80
- **fibrosis_stage**: 0 (25), 1 (28), 2 (9), 3 (14), 4 (2)
- **nas_score**: 0 (4), 1 (5), 2 (9), 3 (18), 4 (16), 5 (18), 6 (8)
- **sex**: F (48), M (30)
- **steatosis_grade**: 0 (8), 1 (29), 2 (27), 3 (14)
- **tissue**: liver biopsy (78)

## Expression data files

| file | tier | bytes | sha256 |
|---|---|---|---|
| GSE130970_all_sample_salmon_tximport_TPM_entrez_gene_ID.csv.gz | expression | 6027512 | `db77ba7f60ab6e93...` |
| GSE130970_all_sample_salmon_tximport_counts_entrez_gene_ID.csv.gz | expression | 11482054 | `d33226c580f39f6d...` |
| GSE130970_series_matrix.txt.gz | metadata | 4840 | `add9a76443996d78...` |

## Selection rationale

Reports fibrosis stage, NAFLD Activity Score, and all three individual NAS components (steatosis, inflammation, ballooning) separately for every sample, alongside age and sex — a per-component breakdown that lets severity be modeled on its constituent parts rather than the composite score alone. (`GSE281797` reports the same set of per-component fields for its own, differently-focused cohort; the two are complementary rather than either being uniquely detailed.) Unlike GSE281797's obese, early-stage-weighted population, GSE130970 spans a general NAFLD cohort across the full severity range (6 histologically normal, 72 across fibrosis stage 0-4), matching the flagship GSE135251/GSE174478 cohorts in spectrum coverage while adding the per-component detail those two only report as composite scores. Its 48F/30M sex split also partially offsets the collection's existing male skew (e.g. GSE126848's 47M/10F). Its overall cohort design overlaps with GSE135251/GSE174478/GSE162694 (Western population, full fibrosis spectrum) at a smaller N, but that overlap is at the cohort-design level — its phenotype-annotation depth is a distinct contribution on its own.

## Provenance

Screened and downloaded via `geo_screen`. Full source manifest: `source_manifest.json`. Full download manifest: `download_manifest.json`. Submission date: May 09 2019.
