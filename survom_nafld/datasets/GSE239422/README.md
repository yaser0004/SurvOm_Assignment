# GSE239422

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

## Experimental design

Hepatic transcriptome of 125 obese individuals, percutaneous liver biopsy at bariatric surgery, stratified by sex and PNPLA3 rs738409 (I148M) genotype (CC 60 / CG 56 / GG 9). Studies the interaction between estrogen receptor-alpha and the PNPLA3 risk variant in driving fatty liver disease susceptibility, with an ERalpha binding site identified within the PNPLA3 enhancer.

## Bulk vs. single-cell determination

`single_cell_or_spatial` = **PASS** — no single-cell/spatial signal detected

## Technical checks

| check | status | observed |
|---|---|---|
| sample_count | PASS | 125 samples |
| organism_consistency | PASS | Homo sapiens 125/125 |
| source_tissue | PASS | liver-pattern source 125/125 |
| library_strategy | PASS | RNA-Seq 125/125 |
| library_source | PASS | transcriptomic 125/125 |
| library_selection | PASS | cDNA 125/125 |
| instrument_model | PASS | Illumina HiSeq 4000 125/125 |
| metadata_completeness | PASS | reported consistently: age, disease, sex, steatosis_grade, tissue; not reported anywhere: bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, stage, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (125 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE239422_Normalized_Counts.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE239422_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded (125 samples, see sample_metadata.csv) |

## Metadata summary (canonical field distributions)

- **age**: 39 distinct values, range 21-68
- **disease**: Obese (125)
- **sex**: F (107), M (18)
- **steatosis_grade**: 0 (20), 1 (48), 2 (29), 3 (28)
- **tissue**: Liver (125)
- **pnpla3 rs738409** (raw field, not canonicalized): CC (60), CG (56), GG (9)

## Expression data files

| file | tier | bytes | sha256 |
|---|---|---|---|
| GSE239422_Normalized_Counts.txt.gz | expression | 11287168 | `86850b8b47f1b527...` |
| GSE239422_RAW_Counts.txt.gz | expression | 3132721 | `edcb770e5f0d335f...` |
| GSE239422_series_matrix.txt.gz | metadata | 6581 | `a499b9f8900b8d21...` |

## Selection rationale

Adds a host-genetic dimension through PNPLA3 I148M variation and a graded steatosis phenotype, rather than another NAFLD-severity cohort. PNPLA3 rs738409 is the most-replicated NAFLD risk variant, and this is the only dataset in the collection reporting genotype per sample; steatosis is graded (0-3 across 20/48/29/28 samples), giving a severity axis independent of the separate `nash: yes/no` field also present in the metadata. Fourth-largest cohort in the collection (125), and the only female-dominant one (107F/18M), which fits the paper's own focus on sex-specific FLD susceptibility.

## Provenance

Screened and downloaded via `geo_screen`. Full source manifest: `source_manifest.json`. Full download manifest: `download_manifest.json`. Submission date: Jul 27 2023.
