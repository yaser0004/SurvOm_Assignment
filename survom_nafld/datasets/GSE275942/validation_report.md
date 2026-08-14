# Validation report: GSE275942

Estrogen Receptor 1 Signaling in Hepatic Stellate Cells Designates Resistance to Liver Fibrosis

<!-- computed -->
Sample count: 11

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 11 samples (below 20) |
| organism_consistency | WARN | mixed organisms: Homo sapiens 2/11, Mus musculus 9/11 |
| source_tissue | PASS | liver-pattern source 11/11 |
| library_strategy | WARN | mixed strategies: ChIP-Seq 1/11, RNA-Seq 10/11 |
| library_source | WARN | library_source: genomic 1/11, transcriptomic 10/11 |
| library_selection | WARN | mixed library_selection: ChIP 1/11, cDNA 10/11 |
| instrument_model | PASS | DNBSEQ-T7 11/11 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (1/11 samples) |
| expression_data_availability | PASS | processed series-level file: GSE275942_mHSC_female_estradiol_treatment_gene_expression.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE275942-GPL28330_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX25892640, https://www.ncbi.nlm.nih.gov/sra?term=SRX25892641, https://www.ncbi.nlm.nih.gov/sra?term=SRX25892642, https://www.ncbi.nlm.nih.gov/sra?term=SRX25892643, https://www.ncbi.nlm.nih.gov/sra?term=SRX25892644, and 6 more (see sample_metadata.csv) |

## Canonical field distributions

- **sex**: F (1), M (1)
- **tissue**: liver (10)
- **treatment**: 10μm 17β-estradiol (2), CCl4 i.p. for 3 weeks (4), Control (2)

## Field presence

- cell line: 1/11
- cell type: 11/11
- gender: 2/11 (canon: sex)
- genotype: 8/11
- tissue: 10/11 (canon: tissue)
- treatment: 8/11 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### organism_consistency (WARN)
### library_strategy (WARN)
### library_source (WARN)
### library_selection (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE275942 / Series_overall_design: matched `metabolic dysfunction-associated stea` in "First, we selected female C57/B6J mice and simulated menopause through ovariectomy, combined with methionine-choline deficient (MCD) diet to induce a metabolic dysfunction-associated steatohepatitis ("
### material_type (WARN)
- GSM8490658 / Sample_characteristics_ch1: matched `cell line` in "cell line: hepatic stellate cells"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 11 samples (below 20)
- organism_consistency: mixed organisms: Homo sapiens 2/11, Mus musculus 9/11
- library_strategy: mixed strategies: ChIP-Seq 1/11, RNA-Seq 10/11
- library_source: library_source: genomic 1/11, transcriptomic 10/11
- library_selection: mixed library_selection: ChIP 1/11, cDNA 10/11
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (1/11 samples)
<!-- /computed -->