# Validation report: GSE270357

Transcriptome sequencing of palmitic acid-treated HepG2 cells upon intervention of curcumin or curcumin-copper complex

<!-- computed -->
Sample count: 9

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 9 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 9/9 |
| source_tissue | PASS | liver-pattern source 9/9 |
| library_strategy | PASS | RNA-Seq 9/9 |
| library_source | PASS | transcriptomic 9/9 |
| library_selection | PASS | cDNA 9/9 |
| instrument_model | PASS | Illumina NovaSeq X Plus 9/9 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: HepG2, cell line (9/9 samples) |
| expression_data_availability | PASS | processed series-level file: GSE270357_TPMs_allsamples.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE270357_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX24993464, https://www.ncbi.nlm.nih.gov/sra?term=SRX24993465, https://www.ncbi.nlm.nih.gov/sra?term=SRX24993466, https://www.ncbi.nlm.nih.gov/sra?term=SRX24993467, https://www.ncbi.nlm.nih.gov/sra?term=SRX24993468, and 4 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: liver (9)
- **treatment**: Cur + PA (3), Cur-Cu + PA (3), PA (3)

## Field presence

- cell line: 9/9
- cell type: 9/9
- genotype: 9/9
- tissue: 9/9 (canon: tissue)
- treatment: 9/9 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE270357 / Series_summary: matched `non-alcoholic fatty liver` in "Globally, non-alcoholic fatty liver disease (NAFLD) poses a major risk to human health. The natural polyphenol curcumin (Cur) can act as a copper (Cu) transporter in a Cur-Cu complex for enhanced Cu c"
### material_type (WARN)
- GSM8340242 / Sample_title: matched `HepG2` in "PA treated HepG2 cells_1"
- GSM8340243 / Sample_title: matched `HepG2` in "PA treated HepG2 cells_2"
- GSM8340244 / Sample_title: matched `HepG2` in "PA treated HepG2 cells_3"
- GSM8340245 / Sample_title: matched `HepG2` in "PA treated HepG2 cells for Cur incubation_1"
- GSM8340246 / Sample_title: matched `HepG2` in "PA treated HepG2 cells for Cur incubation_2"
- GSM8340247 / Sample_title: matched `HepG2` in "PA treated HepG2 cells for Cur incubation_3"
- GSM8340248 / Sample_title: matched `HepG2` in "PA treated HepG2 cells for Cur and copper incubation_1"
- GSM8340249 / Sample_title: matched `HepG2` in "PA treated HepG2 cells for Cur and copper incubation_2"
- GSM8340250 / Sample_title: matched `HepG2` in "PA treated HepG2 cells for Cur and copper incubation_3"
- GSM8340242 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8340243 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8340244 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8340245 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8340246 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8340247 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8340248 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8340249 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM8340250 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 9 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: HepG2, cell line (9/9 samples)
<!-- /computed -->