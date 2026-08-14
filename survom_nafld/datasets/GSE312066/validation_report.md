# Validation report: GSE312066

A genetically encoded bifunctional enzyme that mitigates redox imbalance and lipotoxicity via engineered Gro3P-Glycerol shunt

<!-- computed -->
Sample count: 8

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 8 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 8/8 |
| source_tissue | WARN | liver-pattern source 0/8 |
| library_strategy | PASS | RNA-Seq 8/8 |
| library_source | PASS | transcriptomic 8/8 |
| library_selection | PASS | cDNA 8/8 |
| instrument_model | PASS | HiSeq X Ten 8/8 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (8/8 samples) |
| expression_data_availability | PASS | processed per-sample counts (8/8), packaged in GSE312066_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE312066_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX31176594, https://www.ncbi.nlm.nih.gov/sra?term=SRX31176595, https://www.ncbi.nlm.nih.gov/sra?term=SRX31176596, https://www.ncbi.nlm.nih.gov/sra?term=SRX31176597, https://www.ncbi.nlm.nih.gov/sra?term=SRX31176598, and 3 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Uterus; Cervix (8)
- **treatment**: 24h doxycycline (8)

## Field presence

- cell line: 8/8
- cell type: 8/8
- genotype: 8/8
- tissue: 8/8 (canon: tissue)
- treatment: 8/8 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE312066 / Series_summary: matched `metabolic dysfunction-associated stea` in "Dihydroxyacetone phosphate (DHAP), glycerol-3-phosphate (Gro3P) and reduced/oxidized nicotinamide adenine dinucleotide (NADH/NAD+) are key metabolites of the Gro3P shuttle system that forms a redox ci"
### material_type (WARN)
- GSM9337216 / Sample_characteristics_ch1: matched `cell line` in "cell line: HeLa"
- GSM9337217 / Sample_characteristics_ch1: matched `cell line` in "cell line: HeLa"
- GSM9337218 / Sample_characteristics_ch1: matched `cell line` in "cell line: HeLa"
- GSM9337219 / Sample_characteristics_ch1: matched `cell line` in "cell line: HeLa"
- GSM9337220 / Sample_characteristics_ch1: matched `cell line` in "cell line: HeLa"
- GSM9337221 / Sample_characteristics_ch1: matched `cell line` in "cell line: HeLa"
- GSM9337222 / Sample_characteristics_ch1: matched `cell line` in "cell line: HeLa"
- GSM9337223 / Sample_characteristics_ch1: matched `cell line` in "cell line: HeLa"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 8 samples (below 20)
- source_tissue: liver-pattern source 0/8
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (8/8 samples)
<!-- /computed -->