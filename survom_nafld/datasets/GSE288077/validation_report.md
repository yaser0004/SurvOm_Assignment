# Validation report: GSE288077

Metabolic dysfunction-associated steatotic liver disease may increase intrahepatic interferon gene signatures in patients with chronic hepatitis B

<!-- computed -->
Sample count: 35

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 35 samples |
| organism_consistency | WARN | mixed organisms: Homo sapiens 18/35, Mus musculus 17/35 |
| source_tissue | PASS | liver-pattern source 35/35 |
| library_strategy | PASS | RNA-Seq 35/35 |
| library_source | PASS | transcriptomic 35/35 |
| library_selection | PASS | cDNA 35/35 |
| instrument_model | PASS | Illumina NovaSeq X Plus 35/35 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (19 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE288077_Human_FPKMs.csv.gz |
| series_matrix | INFO | present, metadata-only (GSE288077-GPL34284_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX27479602, https://www.ncbi.nlm.nih.gov/sra?term=SRX27479603, https://www.ncbi.nlm.nih.gov/sra?term=SRX27479604, https://www.ncbi.nlm.nih.gov/sra?term=SRX27479605, https://www.ncbi.nlm.nih.gov/sra?term=SRX27479606, and 30 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: liver (35)
- **treatment**: Treatment naïve (18), chow diet (4), high fat diet (4), rAAV8-1.3 HBV injection + chow diet (5), rAAV8-1.3 HBV injection + high fat diet (1), rAAV8-1.4 HBV injection + high fat diet (1), rAAV8-1.5 HBV injection + high fat diet (1), rAAV8-1.6 HBV injection + high fat diet (1)

## Field presence

- batch: 35/35
- strain: 17/35
- subject status: 18/35
- tissue: 35/35 (canon: tissue)
- treatment: 35/35 (canon: treatment)

## Evidence for WARN/FAIL checks

### organism_consistency (WARN)
### metadata_completeness (WARN)

Decision: MANUAL_REVIEW

Reasons:
- organism_consistency: mixed organisms: Homo sapiens 18/35, Mus musculus 17/35
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
<!-- /computed -->