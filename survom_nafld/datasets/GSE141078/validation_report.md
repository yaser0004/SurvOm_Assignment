# Validation report: GSE141078

The transcriptomic changes induced by NREP downregulation in HepG2 cells

<!-- computed -->
Sample count: 6

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 6 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 6/6 |
| source_tissue | WARN | liver-pattern source 0/6 |
| library_strategy | PASS | RNA-Seq 6/6 |
| library_source | PASS | transcriptomic 6/6 |
| library_selection | PASS | cDNA 6/6 |
| instrument_model | PASS | Illumina HiSeq 2500 6/6 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: HepG2 (6/6 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX7223715, https://www.ncbi.nlm.nih.gov/sra?term=SRX7223716, https://www.ncbi.nlm.nih.gov/sra?term=SRX7223717, https://www.ncbi.nlm.nih.gov/sra?term=SRX7223718, https://www.ncbi.nlm.nih.gov/sra?term=SRX7223719, and 1 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE141078_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX7223715, https://www.ncbi.nlm.nih.gov/sra?term=SRX7223716, https://www.ncbi.nlm.nih.gov/sra?term=SRX7223717, https://www.ncbi.nlm.nih.gov/sra?term=SRX7223718, https://www.ncbi.nlm.nih.gov/sra?term=SRX7223719, and 1 more (see sample_metadata.csv) |

## Field presence

- sirna: 6/6

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE141078 / Series_summary: matched `NAFLD` in "To evaluate the global transcriptomic changes induced by Neuronal Regeneration Related Protein (NREP) downregulation,  we employed RNA-sequencing in HepG2 cells lacking NREP. Enriched pathway analyses"
### material_type (WARN)
- GSM4194617 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4194618 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4194619 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4194620 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4194621 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4194622 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 6 samples (below 20)
- source_tissue: liver-pattern source 0/6
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: HepG2 (6/6 samples)
<!-- /computed -->