# Validation report: GSE303090

Mature Polarized Hepatocyte Organoids Derived from Human Embryonic Stem Cells for Modeling the Pathogenesis and Progression of Metabolic Dysfunction-Associated Steatotic Liver Disease and Therapeutic Drug Screening

<!-- computed -->
Sample count: 12

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 12 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 12/12 |
| source_tissue | PASS | liver-pattern source 12/12 |
| library_strategy | PASS | RNA-Seq 12/12 |
| library_source | PASS | transcriptomic 12/12 |
| library_selection | PASS | cDNA 12/12 |
| instrument_model | PASS | Illumina NovaSeq 6000 12/12 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: Organoid (12/12 samples) |
| expression_data_availability | PASS | processed series-level file: GSE303090_Day10_counts_matrix.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE303090_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX29770291, https://www.ncbi.nlm.nih.gov/sra?term=SRX29770292, https://www.ncbi.nlm.nih.gov/sra?term=SRX29770293, https://www.ncbi.nlm.nih.gov/sra?term=SRX29770294, https://www.ncbi.nlm.nih.gov/sra?term=SRX29770295, and 7 more (see sample_metadata.csv) |

## Canonical field distributions

- **treatment**: Control, Day10 (3), Control, Day2 (3), FFAs, Day10 (3), FFAs, Day2 (3)

## Field presence

- cell type: 12/12
- treatment: 12/12 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE303090 / Series_title: matched `Metabolic Dysfunction-Associated Stea` in "Mature Polarized Hepatocyte Organoids Derived from Human Embryonic Stem Cells for Modeling the Pathogenesis and Progression of Metabolic Dysfunction-Associated Steatotic Liver Disease and Therapeutic "
- GSE303090 / Series_summary: matched `Metabolic dysfunction-associated stea` in "Metabolic dysfunction-associated steatotic liver disease (MASLD), the most prevalent chronic liver disorder worldwide, exhibits complex pathogenesis and lacks effective targeted therapeutics. Existing"
### material_type (WARN)
- GSM9117745 / Sample_source_name_ch1: matched `Organoid` in "Polarized Hepatocyte Organoids"
- GSM9117746 / Sample_source_name_ch1: matched `Organoid` in "Polarized Hepatocyte Organoids"
- GSM9117747 / Sample_source_name_ch1: matched `Organoid` in "Polarized Hepatocyte Organoids"
- GSM9117748 / Sample_source_name_ch1: matched `Organoid` in "Polarized Hepatocyte Organoids"
- GSM9117749 / Sample_source_name_ch1: matched `Organoid` in "Polarized Hepatocyte Organoids"
- GSM9117750 / Sample_source_name_ch1: matched `Organoid` in "Polarized Hepatocyte Organoids"
- GSM9117751 / Sample_source_name_ch1: matched `Organoid` in "Polarized Hepatocyte Organoids"
- GSM9117752 / Sample_source_name_ch1: matched `Organoid` in "Polarized Hepatocyte Organoids"
- GSM9117753 / Sample_source_name_ch1: matched `Organoid` in "Polarized Hepatocyte Organoids"
- GSM9117754 / Sample_source_name_ch1: matched `Organoid` in "Polarized Hepatocyte Organoids"
- GSM9117755 / Sample_source_name_ch1: matched `Organoid` in "Polarized Hepatocyte Organoids"
- GSM9117756 / Sample_source_name_ch1: matched `Organoid` in "Polarized Hepatocyte Organoids"
- GSM9117745 / Sample_characteristics_ch1: matched `Organoid` in "cell type: Polarized Hepatocyte Organoids"
- GSM9117746 / Sample_characteristics_ch1: matched `Organoid` in "cell type: Polarized Hepatocyte Organoids"
- GSM9117747 / Sample_characteristics_ch1: matched `Organoid` in "cell type: Polarized Hepatocyte Organoids"
- GSM9117748 / Sample_characteristics_ch1: matched `Organoid` in "cell type: Polarized Hepatocyte Organoids"
- GSM9117749 / Sample_characteristics_ch1: matched `Organoid` in "cell type: Polarized Hepatocyte Organoids"
- GSM9117750 / Sample_characteristics_ch1: matched `Organoid` in "cell type: Polarized Hepatocyte Organoids"
- GSM9117751 / Sample_characteristics_ch1: matched `Organoid` in "cell type: Polarized Hepatocyte Organoids"
- GSM9117752 / Sample_characteristics_ch1: matched `Organoid` in "cell type: Polarized Hepatocyte Organoids"
- GSM9117753 / Sample_characteristics_ch1: matched `Organoid` in "cell type: Polarized Hepatocyte Organoids"
- GSM9117754 / Sample_characteristics_ch1: matched `Organoid` in "cell type: Polarized Hepatocyte Organoids"
- GSM9117755 / Sample_characteristics_ch1: matched `Organoid` in "cell type: Polarized Hepatocyte Organoids"
- GSM9117756 / Sample_characteristics_ch1: matched `Organoid` in "cell type: Polarized Hepatocyte Organoids"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 12 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: Organoid (12/12 samples)
<!-- /computed -->