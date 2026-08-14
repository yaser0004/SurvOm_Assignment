# Validation report: GSE240729

Development of a novel non-invasive biomarker panel for hepatic fibrosis in individuals with MASLD

<!-- computed -->
Sample count: 67

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 67 samples |
| organism_consistency | PASS | Homo sapiens 67/67 |
| source_tissue | PASS | liver-pattern source 67/67 |
| library_strategy | PASS | RNA-Seq 67/67 |
| library_source | PASS | transcriptomic 67/67 |
| library_selection | PASS | cDNA 67/67 |
| instrument_model | PASS | Illumina NovaSeq 6000 67/67 |
| metadata_completeness | PASS | reported consistently: fibrosis_stage, tissue; not reported anywhere: age, bmi, diagnosis, disease, ethnicity, group, nas_score, sex, stage, steatosis_grade, treatment |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed per-sample counts (67/67), packaged in GSE240729_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE240729_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX21357014, https://www.ncbi.nlm.nih.gov/sra?term=SRX21357015, https://www.ncbi.nlm.nih.gov/sra?term=SRX21357016, https://www.ncbi.nlm.nih.gov/sra?term=SRX21357017, https://www.ncbi.nlm.nih.gov/sra?term=SRX21357018, and 62 more (see sample_metadata.csv) |

## Canonical field distributions

- **fibrosis_stage**: F0 (9), F1 (17), F2 (25), F3 (10), F4 (6)
- **tissue**: liver (FFPE = Formalin Fixed Paraffin Embedded) (67)

## Field presence

- fibrosisscore: 67/67 (canon: fibrosis_stage)
- tissue: 67/67 (canon: tissue)

## Evidence for WARN/FAIL checks

### disease_relevance (WARN)
- GSE240729 / Series_title: matched `MASLD` in "Development of a novel non-invasive biomarker panel for hepatic fibrosis in individuals with MASLD"
- GSE240729 / Series_summary: matched `metabolic dysfunction-associated stea` in "- Background & Aims: Considering the escalating prevalence of metabolic dysfunction-associated steatotic liver disease (MASLD) and MASLD-related fibrosis, accurate non-invasive biomarkers for diagnosi"
- GSE240729 / Series_summary: matched `MASLD` in "- Approach & Results: Using a translational diet-induced LDLr-/-.Leiden MASLD mouse model, candidate biomarkers were identified focused on the mechanism of collagen deposition, by integrating hepatic "
- GSE240729 / Series_summary: matched `MASLD` in "- Conclusion & Discussion: Using a translational Approach to identify collagen turnover related proteins indicative of fibrosis, we developed an accurate blood-based biomarker panel to detect and stag"
- GSE240729 / Series_overall_design: matched `MASLD` in "To translate the murine findings to humans, 74  individuals with MASLD were selected of whom stored liver biopsy material was available at the pathology department of the Erasmus Medical Center and Ut"

Decision: MANUAL_REVIEW

Reasons:
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
<!-- /computed -->