# GSE135251

**Title:** TRANSCRIPTOMIC PROFILING ACROSS THE SPECTRUM OF NON-ALCOHOLIC FATTY LIVER DISEASE
**Accession:** GSE135251
**GEO URL:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE135251
**Organism:** Homo sapiens
**Tissue:** liver biopsy (snap-frozen)
**Disease/condition:** NAFLD across the full severity spectrum (NAFL through NASH F0-F4) vs. control
**Sample count:** 216
**Platform(s):** GPL18573
**PubMed:** 33268509, 33762733, 39566466
**Screening decision:** STRONG_CANDIDATE

## Experimental design

Multicenter cross-sectional cohort; 216 liver biopsies (206 NAFLD, 10 control), bulk RNA-seq on Illumina NextSeq 500.

## Bulk vs. single-cell determination

`single_cell_or_spatial` = **PASS** — no single-cell/spatial signal detected

## Technical checks

| check | status | observed |
|---|---|---|
| sample_count | PASS | 216 samples |
| organism_consistency | PASS | Homo sapiens 216/216 |
| source_tissue | PASS | liver-pattern source 216/216 |
| library_strategy | PASS | RNA-Seq 216/216 |
| library_source | PASS | transcriptomic 216/216 |
| library_selection | PASS | cDNA 216/216 |
| instrument_model | PASS | Illumina NextSeq 500 216/216 |
| metadata_completeness | PASS | reported consistently: disease, fibrosis_stage, group, nas_score, stage; not reported anywhere: age, bmi, diagnosis, ethnicity, sex, steatosis_grade, tissue, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (216 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (216/216), packaged in GSE135251_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE135251_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX6635477, https://www.ncbi.nlm.nih.gov/sra?term=SRX6635478, https://www.ncbi.nlm.nih.gov/sra?term=SRX6635479, https://www.ncbi.nlm.nih.gov/sra?term=SRX6635480, https://www.ncbi.nlm.nih.gov/sra?term=SRX6635481, and 211 more (see sample_metadata.csv) |

## Metadata summary (canonical field distributions)

- **disease**: Control (10), NAFLD (206)
- **fibrosis_stage**: 0 (46), 1 (48), 2 (54), 3 (54), 4 (14)
- **group**: NAFL (51), NASH_F0-F1 (34), NASH_F2 (53), NASH_F3 (54), NASH_F4 (14), control (10)
- **nas_score**: 0 (10), 1 (11), 2 (21), 3 (26), 4 (38), 5 (47), 6 (37), 7 (18), 8 (8)
- **stage**: control (10), early (138), moderate (68)

## Expression data files

| file | tier | bytes | sha256 |
|---|---|---|---|
| GSE135251_series_matrix.txt.gz | metadata | 11529 | `3987ef627abe9468...` |
| GSE135251_RAW.tar | archive | 45854720 | `0f4527224ad66cfa...` |
| GSE135251_RAW.tar (extracted) | 216 member files -> expression/ | - | - |

## Selection rationale

The flagship dataset for this collection: the largest classic case-control design in the pool with the fullest fibrosis-stage spectrum (F0-F4) and NAS scoring reported per sample, from a multicenter study specifically designed to characterize transcriptional change across NAFLD progression. Every technical check passes at 100% (organism, tissue, library strategy, source, selection, instrument), and processed per-sample gene counts are available (packaged inside GSE135251_RAW.tar, extracted to expression/).

## Provenance

Screened and downloaded via `geo_screen`. Full source manifest: `source_manifest.json`. Full download manifest: `download_manifest.json`. Submission date: Aug 01 2019.
