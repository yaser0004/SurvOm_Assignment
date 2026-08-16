# GSE130970

**Title:** Gene expression predicts histological severity and reveals distinct molecular profiles of nonalcoholic fatty liver disease
**Accession:** GSE130970
**GEO URL:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE130970
**Organism:** Homo sapiens
**Tissue:** liver biopsy
**Disease/condition:** NAFLD spectrum, fibrosis F0-F4, NAS 0-6
**Sample count:** 78
**Platform(s):** GPL16791
**PubMed:** 31467298
**Screening decision:** STRONG_CANDIDATE
**Experimental design:** 78 distinct liver biopsies, 6 histologically normal and 72 covering NAFLD activity score 0-6 and fibrosis stage 0-4. Steatosis, lobular inflammation and ballooning grades are reported separately per sample.

## What this dataset is

78 human liver biopsies — 6 histologically normal, 72 spanning the NAFLD severity range — profiled
by bulk RNA-seq on Illumina HiSeq 2500. Alongside the composite NAS and fibrosis stage, every sample
carries the three individual NAS components (steatosis grade, lobular inflammation grade, cytological
ballooning grade) as separately reported fields.

## Bulk vs. single-cell determination

`single_cell_or_spatial` = **PASS** — no single-cell or spatial signal in any sample record.

## Why it is in the collection

It reports steatosis, lobular inflammation and ballooning as separate per-sample fields rather than
only the composite NAS, so severity can be modelled on the individual components. GSE281797 reports
the same set of per-component fields for its own, early-stage obese cohort; this cohort covers the
general NAFLD severity range instead. Its 48F/30M split also partly offsets the male skew elsewhere
in the collection (GSE126848 is 47M/10F).

Its cohort design does overlap with GSE135251, GSE174478 and GSE162694 — Western population, full
fibrosis spectrum — at a smaller N. The overlap is at the design level; the per-component annotation
is what distinguishes it.

## Sample metadata at a glance

- **age**: 39 distinct values, range 19-80
- **fibrosis_stage**: 0 (25), 1 (28), 2 (9), 3 (14), 4 (2)
- **nas_score**: 0 (4), 1 (5), 2 (9), 3 (18), 4 (16), 5 (18), 6 (8)
- **sex**: F (48), M (30)
- **steatosis_grade**: 0 (8), 1 (29), 2 (27), 3 (14)
- **tissue**: liver biopsy (78)

## Files in this folder

- `expression/GSE130970_all_sample_salmon_tximport_TPM_entrez_gene_ID.csv.gz`
- `expression/GSE130970_all_sample_salmon_tximport_counts_entrez_gene_ID.csv.gz`
- `metadata/GSE130970_series_matrix.txt.gz`

## Full checks and provenance

All 14 check results with their observed values: `validation_report.md`. Fetch provenance:
`source_manifest.json`. File sizes and sha256 digests: `download_manifest.json`. GEO submission date:
May 09 2019.
