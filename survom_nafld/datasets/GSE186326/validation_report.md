# Validation report: GSE186326

Activation of GPR3-b-Arrestin2-PKM2 by DPI enhanced glycolysis in kupffer cells [Human KC]

<!-- computed -->
Sample count: 4

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 4 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 4/4 |
| source_tissue | PASS | liver-pattern source 4/4 |
| library_strategy | PASS | RNA-Seq 4/4 |
| library_source | PASS | transcriptomic 4/4 |
| library_selection | PASS | cDNA 4/4 |
| instrument_model | PASS | Illumina NovaSeq 6000 4/4 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | WARN | series prose mentions Single cell; sample metadata does not corroborate |
| material_type | INFO | series prose mentions in vitro; sample metadata does not corroborate |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX12724906, https://www.ncbi.nlm.nih.gov/sra?term=SRX12724907, https://www.ncbi.nlm.nih.gov/sra?term=SRX12724908, https://www.ncbi.nlm.nih.gov/sra?term=SRX12724909) |
| series_matrix | INFO | present, metadata-only (GSE186326_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX12724906, https://www.ncbi.nlm.nih.gov/sra?term=SRX12724907, https://www.ncbi.nlm.nih.gov/sra?term=SRX12724908, https://www.ncbi.nlm.nih.gov/sra?term=SRX12724909 |

## Canonical field distributions

- **tissue**: liver (4)
- **treatment**: DMSO (2), DPI (2)

## Field presence

- cell type: 4/4
- donor: 4/4
- tissue: 4/4 (canon: tissue)
- treatment: 4/4 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE186326 / Series_summary: matched `NAFLD` in "To investigate the human primary Kupffer cells from NAFLD patients response to DPI in vitro."
- GSE186326 / Series_overall_design: matched `NAFLD` in "Single cells were prepared from human liver biopsies from NAFLD patiehts. Kupffer cells were FAC-sorted by CD14+ and treated with 500nM DPI for 24hrs.  RNA was isolated and purified by Qiagen Rneasy m"
### single_cell_or_spatial (WARN)
- GSE186326 / Series_overall_design: matched `Single cell` in "Single cells were prepared from human liver biopsies from NAFLD patiehts. Kupffer cells were FAC-sorted by CD14+ and treated with 500nM DPI for 24hrs.  RNA was isolated and purified by Qiagen Rneasy m"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 4 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- single_cell_or_spatial: series prose mentions Single cell; sample metadata does not corroborate
<!-- /computed -->