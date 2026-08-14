# Validation report: GSE156906

Adipose tissue immunology, inflammation and exosomes in regulating insulin sensitivity in people with obesity and nonalcoholic fatty liver disease

<!-- computed -->
Sample count: 66

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 66 samples |
| organism_consistency | PASS | Homo sapiens 66/66 |
| source_tissue | WARN | liver-pattern source 0/66; off-target tissue signal detected |
| library_strategy | PASS | RNA-Seq 66/66 |
| library_source | PASS | transcriptomic 66/66 |
| library_selection | PASS | cDNA 66/66 |
| instrument_model | PASS | Illumina NovaSeq 6000 66/66 |
| metadata_completeness | PASS | reported consistently: disease, tissue; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade, treatment |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE156906_PSQ_inflammation_all.gene_moderated_log2cpm.xlsx |
| series_matrix | INFO | present, metadata-only (GSE156906_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX9013178, https://www.ncbi.nlm.nih.gov/sra?term=SRX9013179, https://www.ncbi.nlm.nih.gov/sra?term=SRX9013180, https://www.ncbi.nlm.nih.gov/sra?term=SRX9013181, https://www.ncbi.nlm.nih.gov/sra?term=SRX9013182, and 61 more (see sample_metadata.csv) |

## Canonical field distributions

- **disease**: MHL (14), MHO (25), MUO (27)
- **tissue**: Subcutaneous adipose tissue (66)

## Field presence

- condition: 66/66 (canon: disease)
- time point: 66/66
- tissue: 66/66 (canon: tissue)

## Evidence for WARN/FAIL checks

### source_tissue (WARN)
- GSM4748450 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748451 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748452 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748453 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748454 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748455 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748456 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748457 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748458 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748459 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748460 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748461 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748462 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748463 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748464 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748465 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748466 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748467 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748468 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748469 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748470 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748471 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748472 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748473 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748474 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748475 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748476 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748477 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748478 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748479 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748480 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748481 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748482 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748483 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748484 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748485 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748486 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748487 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748488 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748489 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748490 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748491 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748492 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748493 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748494 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748495 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748496 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748497 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748498 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748499 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748500 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748501 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748502 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748503 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748504 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748505 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748506 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748507 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748508 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748509 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748510 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748511 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748512 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748513 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748514 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748515 / Sample_source_name_ch1: matched `adipose` in "Subcutaneous adipose tissue"
- GSM4748450 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748451 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748452 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748453 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748454 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748455 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748456 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748457 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748458 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748459 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748460 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748461 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748462 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748463 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748464 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748465 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748466 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748467 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748468 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748469 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748470 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748471 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748472 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748473 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748474 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748475 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748476 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748477 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748478 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748479 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748480 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748481 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748482 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748483 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748484 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748485 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748486 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748487 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748488 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748489 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748490 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748491 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748492 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748493 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748494 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748495 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748496 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748497 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748498 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748499 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748500 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748501 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748502 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748503 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748504 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748505 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748506 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748507 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748508 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748509 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748510 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748511 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748512 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748513 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748514 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
- GSM4748515 / Sample_characteristics_ch1: matched `adipose` in "tissue: Subcutaneous adipose tissue"
### disease_relevance (WARN)
- GSE156906 / Series_title: matched `nonalcoholic fatty liver` in "Adipose tissue immunology, inflammation and exosomes in regulating insulin sensitivity in people with obesity and nonalcoholic fatty liver disease"
- GSE156906 / Series_summary: matched `NAFLD` in "Background and Aims: Insulin resistance is a key factor in the pathogenesis of NAFLD. We evaluated the importance of subcutaneous abdominal adipose tissue (SAAT) inflammation and both plasma and SAAT-"
- GSE156906 / Series_summary: matched `NAFLD` in "Methods: Adipose tissue inflammation (macrophage and T cell content and gene expression of proinflammatory cytokines), liver and whole-body insulin sensitivity (assessed by a hyperinsulinemic-euglycem"
- GSE156906 / Series_summary: matched `NAFLD` in "Results: Proinflammatory macrophages, proinflammatory CD4 and CD8 T cell populations, and gene expression of several cytokines in SAAT were greater in the OB-NAFLD than the OB-NL and LEAN groups. Howe"
- GSE156906 / Series_summary: matched `NAFLD` in "Conclusion: These results suggest SAAT-derived exosomes and PAI-1 are involved in the pathogenesis of systemic insulin resistance in people with obesity and NAFLD. ClinicalTrials.gov number: NCT027062"

Decision: MANUAL_REVIEW

Reasons:
- source_tissue: liver-pattern source 0/66; off-target tissue signal detected
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
<!-- /computed -->