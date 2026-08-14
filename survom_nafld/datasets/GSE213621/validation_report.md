# Validation report: GSE213621

Hepatocyte Smoothened Activity Controls Susceptibility to Insulin Resistance and Nonalcoholic Fatty Liver Disease [RNA-Seq]

<!-- computed -->
Sample count: 368

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 368 samples |
| organism_consistency | PASS | Homo sapiens 368/368 |
| source_tissue | PASS | liver-pattern source 368/368 |
| library_strategy | PASS | RNA-Seq 368/368 |
| library_source | PASS | transcriptomic 368/368 |
| library_selection | PASS | cDNA 368/368 |
| instrument_model | PASS | Illumina HiSeq 2500 368/368 |
| metadata_completeness | PASS | reported consistently: fibrosis_stage; not reported anywhere: age, bmi, diagnosis, disease, ethnicity, group, nas_score, sex, stage, steatosis_grade, tissue, treatment |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | WARN | series prose mentions single-cell; sample metadata does not corroborate |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE213621_FPKMs_allsamples.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE213621_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX17623649, https://www.ncbi.nlm.nih.gov/sra?term=SRX17623650, https://www.ncbi.nlm.nih.gov/sra?term=SRX17623651, https://www.ncbi.nlm.nih.gov/sra?term=SRX17623652, https://www.ncbi.nlm.nih.gov/sra?term=SRX17623653, and 363 more (see sample_metadata.csv) |

## Canonical field distributions

- **fibrosis_stage**: Control (69), F0F1 (97), F2 (107), F3F4 (95)

## Field presence

- cell type: 368/368
- fibrotic stage: 368/368 (canon: fibrosis_stage)

## Evidence for WARN/FAIL checks

### disease_relevance (WARN)
- GSE213621 / Series_title: matched `Nonalcoholic Fatty Liver` in "Hepatocyte Smoothened Activity Controls Susceptibility to Insulin Resistance and Nonalcoholic Fatty Liver Disease [RNA-Seq]"
- GSE213621 / Series_summary: matched `Nonalcoholic fatty liver` in "Nonalcoholic fatty liver disease (NAFLD) is strongly associated with insulin resistance (IR), but little is known about the key genetic driver that links these two disorders."
- GSE213621 / Series_summary: matched `NAFLD` in "We aimed to elucidate the mechanism by which Smoothened (Smo), a G-protein coupled receptor, contributes to pathogenesis of NAFLD and IR."
- GSE213621 / Series_overall_design: matched `NAFLD` in "We used Smoflox/flox mice in combination with AAV8-TBG-Cre which enables genetic disruption of Smo in mature hepatocytes selectively. Adult Smoflox/flox mice were treated with AAV vectors for 7 days. "
### single_cell_or_spatial (WARN)
- GSE213621 / Series_overall_design: matched `single-cell` in "We used Smoflox/flox mice in combination with AAV8-TBG-Cre which enables genetic disruption of Smo in mature hepatocytes selectively. Adult Smoflox/flox mice were treated with AAV vectors for 7 days. "

Decision: MANUAL_REVIEW

Reasons:
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- single_cell_or_spatial: series prose mentions single-cell; sample metadata does not corroborate
<!-- /computed -->