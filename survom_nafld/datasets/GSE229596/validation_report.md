# Validation report: GSE229596

Multicellular liver organoid model for recapitulating hepatitis C virus infection and non-alcoholic fatty liver disease progression [RNA-Seq]

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
| material_type | WARN | cell/culture terms in sample metadata: organoid (12/12 samples) |
| expression_data_availability | PASS | processed series-level file: GSE229596_merged.expression_Profile.GRCh38.gene.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE229596_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX19950672, https://www.ncbi.nlm.nih.gov/sra?term=SRX19950673, https://www.ncbi.nlm.nih.gov/sra?term=SRX19950674, https://www.ncbi.nlm.nih.gov/sra?term=SRX19950675, https://www.ncbi.nlm.nih.gov/sra?term=SRX19950676, and 7 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Liver organoid (12)
- **treatment**: iMAC (2), iMAC-FA (2), iMAC-FAHCV (2), iMAC-HCV (2), mono (2), mono-HCV (2)

## Field presence

- agent: 12/12 (canon: treatment)
- tissue: 12/12 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE229596 / Series_title: matched `non-alcoholic fatty liver` in "Multicellular liver organoid model for recapitulating hepatitis C virus infection and non-alcoholic fatty liver disease progression [RNA-Seq]"
- GSE229596 / Series_summary: matched `non-alcoholic fatty liver` in "Hepatitis C virus (HCV) infection has been successfully managed by anti-viral therapies, however, high prevalence to severe chronic liver disease state including non-alcoholic fatty liver disease (NAF"
### material_type (WARN)
- GSM7165936 / Sample_source_name_ch1: matched `organoid` in "Liver organoid"
- GSM7165937 / Sample_source_name_ch1: matched `organoid` in "Liver organoid"
- GSM7165938 / Sample_source_name_ch1: matched `organoid` in "Liver organoid"
- GSM7165939 / Sample_source_name_ch1: matched `organoid` in "Liver organoid"
- GSM7165940 / Sample_source_name_ch1: matched `organoid` in "Liver organoid"
- GSM7165941 / Sample_source_name_ch1: matched `organoid` in "Liver organoid"
- GSM7165942 / Sample_source_name_ch1: matched `organoid` in "Liver organoid"
- GSM7165943 / Sample_source_name_ch1: matched `organoid` in "Liver organoid"
- GSM7165944 / Sample_source_name_ch1: matched `organoid` in "Liver organoid"
- GSM7165945 / Sample_source_name_ch1: matched `organoid` in "Liver organoid"
- GSM7165946 / Sample_source_name_ch1: matched `organoid` in "Liver organoid"
- GSM7165947 / Sample_source_name_ch1: matched `organoid` in "Liver organoid"
- GSM7165936 / Sample_characteristics_ch1: matched `organoid` in "tissue: Liver organoid"
- GSM7165937 / Sample_characteristics_ch1: matched `organoid` in "tissue: Liver organoid"
- GSM7165938 / Sample_characteristics_ch1: matched `organoid` in "tissue: Liver organoid"
- GSM7165939 / Sample_characteristics_ch1: matched `organoid` in "tissue: Liver organoid"
- GSM7165940 / Sample_characteristics_ch1: matched `organoid` in "tissue: Liver organoid"
- GSM7165941 / Sample_characteristics_ch1: matched `organoid` in "tissue: Liver organoid"
- GSM7165942 / Sample_characteristics_ch1: matched `organoid` in "tissue: Liver organoid"
- GSM7165943 / Sample_characteristics_ch1: matched `organoid` in "tissue: Liver organoid"
- GSM7165944 / Sample_characteristics_ch1: matched `organoid` in "tissue: Liver organoid"
- GSM7165945 / Sample_characteristics_ch1: matched `organoid` in "tissue: Liver organoid"
- GSM7165946 / Sample_characteristics_ch1: matched `organoid` in "tissue: Liver organoid"
- GSM7165947 / Sample_characteristics_ch1: matched `organoid` in "tissue: Liver organoid"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 12 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: organoid (12/12 samples)
<!-- /computed -->