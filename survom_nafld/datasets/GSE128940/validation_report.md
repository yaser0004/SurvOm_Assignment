# Validation report: GSE128940

IL-11 neutralising therapies for the treatment of nonalcoholic steatohepatitis

<!-- computed -->
Sample count: 30

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 30 samples |
| organism_consistency | WARN | mixed organisms: Homo sapiens 6/30, Mus musculus 24/30 |
| source_tissue | PASS | liver-pattern source 30/30 |
| library_strategy | PASS | RNA-Seq 30/30 |
| library_source | PASS | transcriptomic 30/30 |
| library_selection | PASS | cDNA 30/30 |
| instrument_model | PASS | Illumina NextSeq 500 30/30 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | INFO | series prose mentions in vitro; sample metadata does not corroborate |
| expression_data_availability | PASS | processed series-level file: GSE128940_counts_human.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE128940-GPL18573_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX5581896, https://www.ncbi.nlm.nih.gov/sra?term=SRX5581897, https://www.ncbi.nlm.nih.gov/sra?term=SRX5581898, https://www.ncbi.nlm.nih.gov/sra?term=SRX5581899, https://www.ncbi.nlm.nih.gov/sra?term=SRX5581900, and 25 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: hepatic stellate cells (6), liver (24)
- **treatment**: IgG (6), TGFB1 + IgG (3), X203 (6), X209 (6), none (9)

## Field presence

- diet: 30/30
- rin: 30/30
- strain: 30/30
- time of treatment: 30/30
- tissue: 30/30 (canon: tissue)
- treatment: 30/30 (canon: treatment)

## Evidence for WARN/FAIL checks

### organism_consistency (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE128940 / Series_title: matched `steatohepatitis` in "IL-11 neutralising therapies for the treatment of nonalcoholic steatohepatitis"
- GSE128940 / Series_summary: matched `steatohepatitis` in "Background and aims: Here we investigate the role of IL-11 signalling in the pathogenesis of nonalcoholic steatohepatitis (NASH)."
- GSE128940 / Series_summary: matched `NASH` in "Methods: HSCs or hepatocytes were stimulated with IL-11 and effects assessed using cellular and high content imaging, immunoblotting, ELISA and invasion assays. Genetic and pharmacological IL-11 gain-"
- GSE128940 / Series_summary: matched `NASH` in "Results: When stimulated with NASH factors HSCs secrete IL-11, which drives an autocrine, ERK-dependent signaling loop required for the HSC-to-myofibroblast transformation. IL-11 is upregulated in hum"
- GSE128940 / Series_summary: matched `steatosis` in "Conclusion: We show an unappreciated and central role for IL-11 in liver pathobiology. Targeting IL-11 signalling with neutralizing antibodies reverses fibrosis, steatosis, hepatocyte death and inflam"

Decision: MANUAL_REVIEW

Reasons:
- organism_consistency: mixed organisms: Homo sapiens 6/30, Mus musculus 24/30
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
<!-- /computed -->