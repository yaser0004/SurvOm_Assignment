# GSE162694

**Title:** Molecular Characterization and Cell Type Composition Deconvolution of Fibrosis in NAFLD
**Accession:** GSE162694
**GEO URL:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE162694
**Organism:** Homo sapiens
**Tissue:** liver
**Disease/condition:** NASH, fibrosis staged F0-F4 (plus an explicit 'normal liver histology' group)
**Sample count:** 143
**Platform(s):** GPL21290
**PubMed:** 34508113
**Screening decision:** STRONG_CANDIDATE

## Experimental design

143-sample cross-sectional NASH cohort built specifically for cell-type composition deconvolution of fibrosis; bulk RNA-seq.

## Bulk vs. single-cell determination

`single_cell_or_spatial` = **PASS** — no single-cell/spatial signal detected

## Technical checks

| check | status | observed |
|---|---|---|
| sample_count | PASS | 143 samples |
| organism_consistency | PASS | Homo sapiens 143/143 |
| source_tissue | PASS | liver-pattern source 143/143 |
| library_strategy | PASS | RNA-Seq 143/143 |
| library_source | PASS | transcriptomic 143/143 |
| library_selection | PASS | cDNA 143/143 |
| instrument_model | PASS | Illumina HiSeq 3000 143/143 |
| metadata_completeness | PASS | reported consistently: age, fibrosis_stage, nas_score, sex, tissue; not reported anywhere: bmi, diagnosis, disease, ethnicity, group, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (143 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE162694_raw_counts.csv.gz |
| series_matrix | INFO | present, metadata-only (GSE162694_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX9633405, https://www.ncbi.nlm.nih.gov/sra?term=SRX9633406, https://www.ncbi.nlm.nih.gov/sra?term=SRX9633407, https://www.ncbi.nlm.nih.gov/sra?term=SRX9633408, https://www.ncbi.nlm.nih.gov/sra?term=SRX9633409, and 138 more (see sample_metadata.csv) |

## Metadata summary (canonical field distributions)

- **age**: 18 (1), 20 (3), 21 (1), 22 (3), 25 (5), 26 (1), 28 (4), 29 (1), 30 (2), 32 (5), 33 (3), 34 (5), 35 (3), 36 (2), 37 (4), 39 (2), 40 (2), 41 (3), 42 (4), 43 (1), 44 (4), 45 (3), 46 (4), 47 (3), 48 (5), 49 (5), 50 (3), 51 (4), 52 (4), 53 (4), 54 (6), 55 (5), 56 (3), 57 (5), 58 (3), 59 (4), 60 (4), 61 (4), 62 (3), 64 (4), 65 (3), 66 (1), 68 (2), 69 (1), 72 (1)
- **fibrosis_stage**: 0 (35), 1 (30), 2 (27), 3 (8), 4 (12), normal liver histology (31)
- **nas_score**: 0 (32), 1 (12), 2 (9), 3 (11), 4 (13), 5 (19), 6 (12), 7 (9), NA (26)
- **sex**: Female (103), Male (40)
- **tissue**: Liver (143)

## Expression data files

| file | tier | bytes | sha256 |
|---|---|---|---|
| GSE162694_raw_counts.csv.gz | expression | 6228026 | `c8c882e477dcd8a5...` |
| GSE162694_series_matrix.txt.gz | metadata | 6860 | `d5e84d5044021d78...` |

## Selection rationale

The third-largest cohort in the collection, after GSE213621 and GSE135251, and the only one whose stated purpose is a distinct analytical angle - deconvolving bulk expression into cell-type composition changes across fibrosis stages, rather than a straightforward case-control comparison. Adds methodological diversity to the collection.

## Provenance

Screened and downloaded via `geo_screen`. Full source manifest: `source_manifest.json`. Full download manifest: `download_manifest.json`. Submission date: Dec 04 2020.
