# Validation report: GSE241526

Mitochondrial GpC and CpG DNA hypermethylation cause metabolic stress induced mitophagy and cholestophagy [RNA-seq]

<!-- computed -->
Sample count: 23

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 23 samples |
| organism_consistency | PASS | Homo sapiens 23/23 |
| source_tissue | PASS | liver-pattern source 23/23 |
| library_strategy | PASS | RNA-Seq 23/23 |
| library_source | PASS | transcriptomic 23/23 |
| library_selection | PASS | cDNA 23/23 |
| instrument_model | PASS | Illumina NovaSeq 6000 23/23 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: HepG2, cell line (23/23 samples) |
| expression_data_availability | PASS | processed series-level file: GSE241526_table_input_gene_counts.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE241526_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX21466941, https://www.ncbi.nlm.nih.gov/sra?term=SRX21466942, https://www.ncbi.nlm.nih.gov/sra?term=SRX21466943, https://www.ncbi.nlm.nih.gov/sra?term=SRX21466944, https://www.ncbi.nlm.nih.gov/sra?term=SRX21466945, and 18 more (see sample_metadata.csv) |

## Canonical field distributions

- **treatment**: 1mM FFA (13), none (10)

## Field presence

- cell line: 23/23
- cell type: 23/23
- genotype: 23/23
- treatment: 23/23 (canon: treatment)

## Evidence for WARN/FAIL checks

### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE241526 / Series_summary: matched `MASLD` in "Metabolic dysfunction associated steatotic liver disease (MASLD) is characterized by a constant accumulation of lipids in the liver. This lipotoxicity in the liver is associated with dysregulation of "
### material_type (WARN)
- GSM7730197 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM7730198 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM7730199 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM7730200 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM7730201 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM7730202 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM7730203 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM7730204 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM7730205 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM7730206 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM7730207 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM7730208 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM7730209 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM7730210 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM7730211 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM7730212 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM7730213 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM7730214 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM7730215 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM7730216 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM7730217 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM7730218 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM7730219 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM7730197 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2 cells"
- GSM7730198 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2 cells"
- GSM7730199 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2 cells"
- GSM7730200 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2 cells"
- GSM7730201 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2 cells"
- GSM7730202 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2 cells"
- GSM7730203 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2 cells"
- GSM7730204 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2 cells"
- GSM7730205 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2 cells"
- GSM7730206 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2 cells"
- GSM7730207 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2 cells"
- GSM7730208 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2 cells"
- GSM7730209 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2 cells"
- GSM7730210 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2 cells"
- GSM7730211 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2 cells"
- GSM7730212 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2 cells"
- GSM7730213 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2 cells"
- GSM7730214 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2 cells"
- GSM7730215 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2 cells"
- GSM7730216 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2 cells"
- GSM7730217 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2 cells"
- GSM7730218 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2 cells"
- GSM7730219 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2 cells"

Decision: MANUAL_REVIEW

Reasons:
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: HepG2, cell line (23/23 samples)
<!-- /computed -->