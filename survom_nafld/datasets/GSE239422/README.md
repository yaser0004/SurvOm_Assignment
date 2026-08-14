# GSE239422 — reviewed, not selected

**Title:** A functional interaction between hepatic Estrogen Receptor-a and PNPLA3 p.I148M variant drives fatty liver diseases susceptibility in women
**Accession:** GSE239422
**GEO URL:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE239422
**Organism:** Homo sapiens
**Tissue:** Liver
**Disease/condition:** Obese, graded steatosis, PNPLA3 rs738409 genotype
**Sample count:** 125
**Platform(s):** GPL20301
**PubMed:** 37749332, 40501083
**Screening decision:** STRONG_CANDIDATE

## What this dataset is

Hepatic transcriptomes of 125 obese individuals biopsied at bariatric surgery, stratified by sex and
PNPLA3 rs738409 (I148M) genotype (CC 60 / CG 56 / GG 9). The study examines how estrogen
receptor-alpha interacts with the PNPLA3 risk variant to drive fatty liver disease susceptibility in
women. Bulk RNA-seq, Illumina HiSeq 4000, 125/125 samples.

## Bulk vs. single-cell determination

`single_cell_or_spatial` = **PASS** — no single-cell/spatial signal in any sample record.

## Why it is not in the final collection

The screening tool rates this dataset `STRONG_CANDIDATE` (see `reports/summary.csv`), and that
verdict stands: it is human, liver, bulk RNA-seq, with graded steatosis reported per sample. It was
dropped at the final scientific review, not by the classifier.

The reason is study design rather than data quality. Every sample's `disease` field reads `Obese`;
the cohort is not organised as control → NAFL → NASH → fibrosis, and the transcriptomic component
exists to test a sex × PNPLA3-genotype interaction. That is a mechanistic susceptibility study, and
the nine selected datasets already cover the disease spectrum (GSE135251, GSE130970, GSE174478,
GSE162694), early disease (GSE281797), NAFL-vs-NASH contrasts (GSE126848, GSE167523), a large
independent fibrosis cohort (GSE213621) and an intervention arm (GSE150026). Including it would have
invited a fair question — why an obese cohort stratified by genotype counts as a core NAFLD dataset —
without extending the collection's coverage.

The downloaded files stay here because they were fetched before that review; the accession is no
longer listed in `selected.txt`.

## Sample metadata at a glance

- **age**: 39 distinct values, range 21-68
- **disease**: Obese (125)
- **sex**: F (107), M (18)
- **steatosis_grade**: 0 (20), 1 (48), 2 (29), 3 (28)
- **tissue**: Liver (125)
- **pnpla3 rs738409** (raw field, not canonicalized): CC (60), CG (56), GG (9)

## Files in this folder

- `expression/GSE239422_Normalized_Counts.txt.gz`, `expression/GSE239422_RAW_Counts.txt.gz`
- `metadata/GSE239422_series_matrix.txt.gz`

## Full checks and provenance

All 14 check results with their observed values: `validation_report.md`. Fetch provenance:
`source_manifest.json`. File sizes and sha256 digests: `download_manifest.json`. GEO submission date:
Jul 27 2023.
