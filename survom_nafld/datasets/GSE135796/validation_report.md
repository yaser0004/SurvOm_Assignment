# Validation report: GSE135796

Growth Differentiation Factor 11 exacerbates non-alcoholic fatty liver disease in vitro and in vivo

<!-- computed -->
Sample count: 6

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 6 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 6/6 |
| source_tissue | PASS | liver-pattern source 6/6 |
| library_strategy | PASS | RNA-Seq 6/6 |
| library_source | PASS | transcriptomic 6/6 |
| library_selection | PASS | cDNA 6/6 |
| instrument_model | PASS | Illumina MiSeq 6/6 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: HepG2 (6/6 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX6709588, https://www.ncbi.nlm.nih.gov/sra?term=SRX6709589, https://www.ncbi.nlm.nih.gov/sra?term=SRX6709590, https://www.ncbi.nlm.nih.gov/sra?term=SRX6709591, https://www.ncbi.nlm.nih.gov/sra?term=SRX6709592, and 1 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE135796_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX6709588, https://www.ncbi.nlm.nih.gov/sra?term=SRX6709589, https://www.ncbi.nlm.nih.gov/sra?term=SRX6709590, https://www.ncbi.nlm.nih.gov/sra?term=SRX6709591, https://www.ncbi.nlm.nih.gov/sra?term=SRX6709592, and 1 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 15-year-old Caucasian American male (6)
- **tissue**: Liver (6)

## Field presence

- age: 6/6 (canon: age)
- cell type: 6/6
- tissue: 6/6 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE135796 / Series_title: matched `non-alcoholic fatty liver` in "Growth Differentiation Factor 11 exacerbates non-alcoholic fatty liver disease in vitro and in vivo"
- GSE135796 / Series_summary: matched `NAFLD` in "Growth differentiation factor 11 (GDF11), also known as bone morphogenetic protein 11 (BMP11) is a member of the Growth differentiation factors (GDFs), a subfamily of proteins belonging to the transfo"
### material_type (WARN)
- GSM4030315 / Sample_source_name_ch1: matched `HepG2` in "HepG2 - immortalized cell line"
- GSM4030316 / Sample_source_name_ch1: matched `HepG2` in "HepG2 - immortalized cell line"
- GSM4030317 / Sample_source_name_ch1: matched `HepG2` in "HepG2 - immortalized cell line"
- GSM4030318 / Sample_source_name_ch1: matched `HepG2` in "HepG2 - immortalized cell line"
- GSM4030319 / Sample_source_name_ch1: matched `HepG2` in "HepG2 - immortalized cell line"
- GSM4030320 / Sample_source_name_ch1: matched `HepG2` in "HepG2 - immortalized cell line"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 6 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: HepG2 (6/6 samples)
<!-- /computed -->