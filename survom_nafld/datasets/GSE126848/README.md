# GSE126848

**Title:** HEPATIC TRANSCRIPTOME SIGNATURES IN PATIENTS WITH VARYING DEGREES OF NON-ALCOHOLIC FATTY LIVER DISEASE COMPARED TO HEALTHY NORMAL-WEIGHT INDIVIDUALS
**Accession:** GSE126848
**GEO URL:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE126848
**Organism:** Homo sapiens
**Tissue:** Liver (biopsy)
**Disease/condition:** healthy normal-weight / obese / NAFL / NASH (4-arm)
**Sample count:** 57
**Platform(s):** GPL18573
**PubMed:** 30653341
**Screening decision:** STRONG_CANDIDATE

## Experimental design

RNA-seq on liver biopsies from four groups: healthy normal-weight (n=14), obese without NAFLD (n=12), NAFL (n=15), NASH (n=16). Quantitative histomorphometry of liver fat, inflammation, and fibrosis was performed alongside sequencing.

## Bulk vs. single-cell determination

`single_cell_or_spatial` = **PASS** — no single-cell/spatial signal detected

## Technical checks

| check | status | observed |
|---|---|---|
| sample_count | PASS | 57 samples |
| organism_consistency | PASS | Homo sapiens 57/57 |
| source_tissue | PASS | liver-pattern source 57/57 |
| library_strategy | PASS | RNA-Seq 57/57 |
| library_source | PASS | transcriptomic 57/57 |
| library_selection | PASS | cDNA 57/57 |
| instrument_model | PASS | Illumina NextSeq 500 57/57 |
| metadata_completeness | PASS | reported consistently: disease, sex, tissue; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, stage, steatosis_grade, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (31 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE126848_Gene_counts_raw.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE126848_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded (57 samples, see sample_metadata.csv) |

## Metadata summary (canonical field distributions)

- **disease**: NAFLD (15), NASH (16), healthy (14), obese (12)
- **sex**: Female (10), Male (47)
- **tissue**: Liver (57)

## Expression data files

| file | tier | bytes | sha256 |
|---|---|---|---|
| GSE126848_Gene_counts_raw.txt.gz | expression | 1399252 | `8208defed61d1eb6...` |
| GSE126848_series_matrix.txt.gz | metadata | 3891 | `f6c8602249bf321b...` |

## Selection rationale

The only dataset in the collection with a **healthy normal-weight** control arm and an **obese-without-NAFLD** control arm reported as distinct groups (14 and 12 subjects respectively), alongside NAFL (15) and NASH (16). Every other selected dataset compares disease severity within a NAFLD-spectrum cohort; this one is the only way to separate the effect of obesity itself from the effect of NAFLD/NASH — the paper's own finding is that normal-weight and obese controls have comparable liver transcriptomes, clearly distinct from NAFL/NASH. Directly matches the assignment email's first two example comparisons ("healthy/control liver samples" vs. "NAFLD/NASH liver samples"). Has no fibrosis/NAS staging, unlike the flagship spectrum cohorts — its value is the control-arm design, not depth of severity annotation.

## Provenance

Screened and downloaded via `geo_screen`. Full source manifest: `source_manifest.json`. Full download manifest: `download_manifest.json`. Submission date: Feb 21 2019.
