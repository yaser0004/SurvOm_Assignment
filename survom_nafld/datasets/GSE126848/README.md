# GSE126848

**Title:** HEPATIC TRANSCRIPTOME SIGNATURES IN PATIENTS WITH VARYING DEGREES OF NON-ALCOHOLIC FATTY LIVER DISEASE COMPARED TO HEALTHY NORMAL-WEIGHT INDIVIDUALS
**Accession:** GSE126848
**GEO URL:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE126848
**Organism:** Homo sapiens
**Tissue:** Liver (biopsy)
**Disease/condition:** healthy normal-weight / obese / NAFL / NASH (four arms)
**Sample count:** 57
**Platform(s):** GPL18573
**PubMed:** 30653341
**Screening decision:** STRONG_CANDIDATE

## What this dataset is

Liver-biopsy RNA-seq across four groups — healthy normal-weight (14), obese without NAFLD (12), NAFL
(15) and NASH (16) — on Illumina NextSeq 500, with quantitative histomorphometry of liver fat,
inflammation and fibrosis performed alongside sequencing.

## Bulk vs. single-cell determination

`single_cell_or_spatial` = **PASS** — no single-cell or spatial signal in any sample record.

## Why it is in the collection

The only dataset here that reports a healthy normal-weight control arm and an obese-without-NAFLD
control arm as separate groups. Every other selected dataset compares severity within a
NAFLD-spectrum cohort, so this is the only one supporting an obese-without-NAFLD versus NAFLD/NASH
comparison — the comparison the assignment brief gives as its own first example. The study's finding
is that normal-weight and obese controls have comparable liver transcriptomes, both distinct from
NAFL and NASH.

It carries no fibrosis or NAS staging: it was selected for the four-arm design rather than for depth
of severity annotation.

## Sample metadata at a glance

- **disease**: NAFLD (15), NASH (16), healthy (14), obese (12)
- **sex**: Female (10), Male (47)
- **tissue**: Liver (57)

## Joining the expression matrix to the samples

The count matrix's sample columns are not GSM accessions — they are four-character numeric
identifiers (`0869`, `2683`, …). None of the 57 occurs anywhere in `sample_metadata.csv`, as a
field value or even as a substring, so the matrix cannot be joined to the sample table using the
files in this folder alone. The link lives in the series matrix, whose `!Sample_description` row
carries those identifiers alongside `!Sample_geo_accession`. `expression_sample_map.csv` makes
that link explicit:

| column | meaning |
|---|---|
| `gsm` | GEO `!Sample_geo_accession` — joins to `sample_metadata.csv` |
| `expression_sample_id` | the identifier as it appears in the matrix header |
| `raw__description` | GEO `!Sample_description`, unmodified |
| `title` | GEO `!Sample_title`, for a human-readable check |

`expression_sample_id` is `raw__description` left-padded with zeros to four characters. GEO
writes the low identifiers unpadded (`869`) while the matrix header pads them (`0869`); 26 of the
57 samples are affected and the other 31 are already four characters, which is why both forms are
kept rather than only the derived one. The 57 padded values reproduce the 57 matrix header
identifiers exactly, and the `gsm` ↔ `expression_sample_id` correspondence is one-to-one in both
directions.

The pairing comes from column position *within the series matrix* — `!Sample_geo_accession[i]`
with `!Sample_description[i]`, which is how a series matrix encodes per-sample fields — and the
join to the expression header is by value, not by column order.

The file is generated, not typed. It is not produced by `geo_screen` (which writes
`sample_metadata.csv` and would drop an added column on any re-run), so it is a dataset-local
artifact derived from two files that ship in this same folder. Run this from this directory to
re-derive the mapping; it writes to `expression_sample_map.regenerated.csv` so the shipped file
stays intact for the comparison on the last line:

```bash
python3 - <<'EOF'
import csv, gzip

def matrix_row(tag):
    with gzip.open("metadata/GSE126848_series_matrix.txt.gz", "rt") as fh:
        for line in fh:
            if line.startswith(tag + "\t"):
                return [v.strip('"') for v in line.rstrip("\n").split("\t")[1:]]
    raise SystemExit(f"{tag} not found in the series matrix")

with gzip.open("expression/GSE126848_Gene_counts_raw.txt.gz", "rt") as fh:
    columns = fh.readline().rstrip("\n").split("\t")[1:]

gsm = matrix_row("!Sample_geo_accession")
description = matrix_row("!Sample_description")
title = matrix_row("!Sample_title")
assert len(gsm) == len(description) == len(title) == len(columns), "sample counts disagree"

rows = [
    {"gsm": g, "expression_sample_id": d.zfill(4), "raw__description": d, "title": t}
    for g, d, t in zip(gsm, description, title)
]
ids = [row["expression_sample_id"] for row in rows]
assert len({row["gsm"] for row in rows}) == len(rows), "duplicate GSM"
assert len(set(ids)) == len(rows), "duplicate expression_sample_id"
assert set(ids) == set(columns), "mapping does not reproduce the expression header"

with open("expression_sample_map.regenerated.csv", "w", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=["gsm", "expression_sample_id", "raw__description", "title"])
    writer.writeheader()
    writer.writerows(rows)
print(f"{len(rows)} samples mapped")
EOF

diff expression_sample_map.csv expression_sample_map.regenerated.csv && echo "mapping reproduced"
```

It reads only the two shipped files named in it — the series matrix and the first line of the
count matrix — writes only the `.regenerated.csv` side file, and fails loudly rather than emitting
a partial mapping.

## Known GEO metadata inconsistency: Mus musculus in the processing description

One GEO processing-description field mentions mapping to the *Mus musculus* genome. This
conflicts with the sample organism being *Homo sapiens* and the stated GRCh38 build. The dataset
is retained as a human liver RNA-seq dataset; the conflicting statement is documented as a GEO
metadata inconsistency and no source expression data were altered.

What the shipped files actually say, measured across all 57 samples:

- `!Sample_data_processing` carries `Sequenced reads were mapped to Ensembl Mus musculus genome
  using whole genome using STAR v2.5.2a with default parameters` on 57/57 samples.
- The same field carries `Genome_build: Ensembl GRCh38 89` on 57/57 samples.
- `organism_consistency` is `PASS — Homo sapiens 57/57` (`validation_report.md`).
- All 19,786 data rows of the count matrix are keyed by human Ensembl gene accessions (`ENSG…`);
  no row uses a mouse `ENSMUSG` accession or any other identifier form.

The organism field, the genome-build line and the count matrix's own feature identifiers all say
human; a single sentence in the processing description says mouse. The dataset is therefore
treated as human, which is also how the screening checks scored it without intervention. Why
GEO's record contains the conflicting sentence is not something these files establish, and no
attempt was made to correct it upstream or locally — `metadata/GSE126848_series_matrix.txt.gz` is
shipped exactly as GEO serves it.

## Files in this folder

- `expression/GSE126848_Gene_counts_raw.txt.gz`
- `metadata/GSE126848_series_matrix.txt.gz`
- `expression_sample_map.csv` — matrix sample column ↔ GSM, see above

## Full checks and provenance

All 14 check results with their observed values: `validation_report.md`. Fetch provenance:
`source_manifest.json`. File sizes and sha256 digests: `download_manifest.json`. GEO submission date:
Feb 21 2019.
