# GSE174478

**Title:** Whole transcriptome profiling of Japanese nonalcoholic fatty liver disease cohort.
**Accession:** GSE174478
**GEO URL:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE174478
**Organism:** Homo sapiens
**Tissue:** liver biopsy
**Disease/condition:** NAFLD, full fibrosis spectrum F0-F4
**Sample count:** 94
**Platform(s):** GPL24676
**PubMed:** 35380992, 40262132
**Screening decision:** STRONG_CANDIDATE

## What this dataset is

94 liver biopsies from a Japanese biopsy-proven NAFLD cohort, bulk RNA-seq on Illumina NovaSeq 6000,
with fibrosis stage, NAS, age and sex reported for every sample.

## Bulk vs. single-cell determination

`single_cell_or_spatial` = **PASS** — no single-cell or spatial signal in any sample record.

## Why it is in the collection

The only non-Western cohort among the nine, and it stages fibrosis F0-F4 on the same scale as
GSE135251, so the two can be compared directly rather than one being a near-duplicate of the other.
It was selected on the population it covers, not on its size — the brief warns against collecting
datasets for volume alone.

## Sample metadata at a glance

- **age**: 49 distinct values, range 19-92
- **disease**: NAFLD (94)
- **fibrosis_stage**: 0 (7), 1 (29), 2 (23), 3 (24), 4 (11)
- **nas_score**: 1 (1), 2 (11), 3 (9), 4 (17), 5 (36), 6 (17), 7 (3)
- **sex**: F (45), M (49)
- **tissue**: liver (94)

## Known data quirk: duplicate feature identifiers

The matrix has 60,651 data rows but 60,607 distinct Ensembl gene IDs — 44 IDs appear twice. In all
44 cases the two rows are byte-identical across every one of the 94 sample columns, so
deduplication is lossless: keeping either row preserves the values exactly. The file is shipped as
GEO serves it. Tooling that requires unique row IDs should drop the repeats, not sum them — summing
would double the affected genes.

## Files in this folder

- `expression/GSE174478_raw_gene_counts_matrix.txt.gz`
- `metadata/GSE174478_series_matrix.txt.gz`

## Full checks and provenance

All 14 check results with their observed values: `validation_report.md`. Fetch provenance:
`source_manifest.json`. File sizes and sha256 digests: `download_manifest.json`. GEO submission date:
May 14 2021.
