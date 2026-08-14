# Validation report: GSE278008

Transcriptomic analysis of NAFLD model cells with the co-administration of pseudo-natural flavonol and copper

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
| instrument_model | PASS | Illumina NovaSeq X Plus 6/6 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: HepG2, cell line (6/6 samples) |
| expression_data_availability | PASS | processed series-level file: GSE278008_TPMs_allsamples.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE278008_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX26200133, https://www.ncbi.nlm.nih.gov/sra?term=SRX26200134, https://www.ncbi.nlm.nih.gov/sra?term=SRX26200135, https://www.ncbi.nlm.nih.gov/sra?term=SRX26200136, https://www.ncbi.nlm.nih.gov/sra?term=SRX26200137, and 1 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: liver (6)
- **treatment**: PA (3), PA_HQF_Cu (3)

## Field presence

- cell line: 6/6
- cell type: 6/6
- genotype: 6/6
- tissue: 6/6 (canon: tissue)
- treatment: 6/6 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE278008 / Series_title: matched `NAFLD` in "Transcriptomic analysis of NAFLD model cells with the co-administration of pseudo-natural flavonol and copper"
- GSE278008 / Series_summary: matched `non-alcoholic fatty liver` in "Copper deficiency is closely associated with non-alcoholic fatty liver disease (NAFLD). We developed pseudo-natural flavonol (HQF) as novel ionophore for rapid intracellular copper delivery. The co-ad"
- GSE278008 / Series_overall_design: matched `NAFLD` in "We performed gene expression profiling analysis using data obtained from mRNA-seq of NAFLD model cells, with or without the co-administration 0.5 µM HQF and 5 µM CuCl2 for 24 h. For the construction o"
### material_type (WARN)
- GSM8537407 / Sample_title: matched `HepG2` in "PA treated HepG2 cells_1"
- GSM8537408 / Sample_title: matched `HepG2` in "PA treated HepG2 cells_2"
- GSM8537409 / Sample_title: matched `HepG2` in "PA treated HepG2 cells_3"
- GSM8537410 / Sample_title: matched `HepG2` in "PA treated HepG2 cells for co-administration of HQF and copper_1"
- GSM8537411 / Sample_title: matched `HepG2` in "PA treated HepG2 cells for co-administration of HQF and copper_2"
- GSM8537412 / Sample_title: matched `HepG2` in "PA treated HepG2 cells for co-administration of HQF and copper_3"
- GSM8537407 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8537408 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8537409 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8537410 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8537411 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8537412 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 6 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: HepG2, cell line (6/6 samples)
<!-- /computed -->