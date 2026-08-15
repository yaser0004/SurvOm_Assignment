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

## What this dataset is

A multicenter cross-sectional cohort of 216 liver biopsies — 206 NAFLD, 10 control — profiled by
bulk RNA-seq on Illumina NextSeq 500. The study was designed to characterise how the liver
transcriptome changes as NAFLD progresses, and reports fibrosis stage, NAFLD Activity Score and a
severity group for every sample.

## Bulk vs. single-cell determination

`single_cell_or_spatial` = **PASS** — no single-cell or spatial signal in any sample record.

## Why it is in the collection

It was selected on the depth of what its records report: 216 samples with all five fibrosis stages
populated, NAS reported per sample, a severity group per sample, and a 10-sample control arm. Every
technical check passes at 216/216 — organism, tissue, library strategy, source, selection and
instrument — and processed per-sample gene counts are available rather than only raw reads.

## Sample metadata at a glance

- **disease**: Control (10), NAFLD (206)
- **fibrosis_stage**: 0 (46), 1 (48), 2 (54), 3 (54), 4 (14)
- **group**: NAFL (51), NASH_F0-F1 (34), NASH_F2 (53), NASH_F3 (54), NASH_F4 (14), control (10)
- **nas_score**: 0 (10), 1 (11), 2 (21), 3 (26), 4 (38), 5 (47), 6 (37), 7 (18), 8 (8)
- **stage**: control (10), early (138), moderate (68)

## Files in this folder

- `expression/` — 216 per-sample `GSM*.counts.txt.gz` files, one per GSM. GEO ships these inside
  `GSE135251_RAW.tar`; the archive was downloaded and only its processed count members extracted.
  **The tar itself is not included here.** Its entry in `download_manifest.json`, with the URL,
  45,854,720-byte size and sha256, is provenance for re-fetching it from GEO — not a claim that it
  ships in this folder. The adjacent `archive_extracted` entry lists all 216 members that do.
- `metadata/GSE135251_series_matrix.txt.gz`

## Full checks and provenance

All 14 check results with their observed values: `validation_report.md`. Fetch provenance:
`source_manifest.json`. File sizes and sha256 digests, including the extracted members:
`download_manifest.json`. GEO submission date: Aug 01 2019.
