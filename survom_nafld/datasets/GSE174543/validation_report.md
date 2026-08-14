# Validation report: GSE174543

Genome-wide RNAseq of liver tissue derived from humanized mice fed by CDA-HFD and treated with CLDN1 mAb or vehicle Control

<!-- computed -->
Sample count: 10

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 10 samples (below 20) |
| organism_consistency | PASS | Homo sapiens | Mus musculus 10/10 |
| source_tissue | PASS | liver-pattern source 10/10 |
| library_strategy | PASS | RNA-Seq 10/10 |
| library_source | PASS | transcriptomic 10/10 |
| library_selection | PASS | cDNA 10/10 |
| instrument_model | PASS | Illumina HiSeq 4000 10/10 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE174543_DESeq2-normalized_counts.tsv.gz |
| series_matrix | INFO | present, metadata-only (GSE174543_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX10910833, https://www.ncbi.nlm.nih.gov/sra?term=SRX10910834, https://www.ncbi.nlm.nih.gov/sra?term=SRX10910835, https://www.ncbi.nlm.nih.gov/sra?term=SRX10910836, https://www.ncbi.nlm.nih.gov/sra?term=SRX10910837, and 5 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 38 weeks (10)
- **tissue**: non-tumorous liver (10)
- **treatment**: CLDN1 mAb (500ug) i.p. 1/w for 8 weeks (4), No treatment (3), Vehicle Control (PBS)  i.p. 1/w for 8 weeks (3)

## Field presence

- age: 10/10 (canon: age)
- diet: 10/10
- strain: 10/10
- tissue: 10/10 (canon: tissue)
- treatment: 10/10 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE174543 / Series_summary: matched `NASH` in "Six-week old Fah−/−/Rag2−/−/Il2rg −/− (FRG) –NOD breeding mice were intravenously injected with 1.5 x 10^9 plaque forming units (pfu) of an adenoviral vector encoding the secreted form of the human ur"
- GSE174543 / Series_overall_design: matched `NASH` in "mRNA profiles of humanized mice fed a regular diet, humanized NASH fibrosis mice treated with vehicle control and humanized NASH fibrosis mice treated with CLDN1 mAb"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 10 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
<!-- /computed -->