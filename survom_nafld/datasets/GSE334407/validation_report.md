# Validation report: GSE334407

Physiologically relevant media are associated with overlapping metabolic responses in primary human hepatocytes and Huh7 cells

<!-- computed -->
Sample count: 30

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 30 samples |
| organism_consistency | PASS | Homo sapiens 30/30 |
| source_tissue | PASS | liver-pattern source 30/30 |
| library_strategy | PASS | RNA-Seq 30/30 |
| library_source | PASS | transcriptomic 30/30 |
| library_selection | PASS | cDNA 30/30 |
| instrument_model | PASS | Illumina NovaSeq 6000 30/30 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: Huh7, cell line (30/30 samples) |
| expression_data_availability | PASS | processed series-level file: GSE334407_Huh7_raw_counts.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE334407_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX33758232, https://www.ncbi.nlm.nih.gov/sra?term=SRX33758233, https://www.ncbi.nlm.nih.gov/sra?term=SRX33758234, https://www.ncbi.nlm.nih.gov/sra?term=SRX33758235, https://www.ncbi.nlm.nih.gov/sra?term=SRX33758236, and 25 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Liver (30)
- **treatment**: Control (10), OPLA (10), POLA (10)

## Field presence

- batch: 30/30
- cell line: 30/30
- cell type: 30/30
- tissue: 30/30 (canon: tissue)
- treatment: 30/30 (canon: treatment)

## Evidence for WARN/FAIL checks

### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE334407 / Series_summary: matched `metabolic dysfunction-associated stea` in "Background and aims: The initiation and progression of metabolic dysfunction-associated steatotic liver disease (MASLD) is challenging to study in vivo in humans and robust in vitro high-fidelity dise"
### material_type (WARN)
- GSM9788165 / Sample_title: matched `Huh7` in "Huh7 cells Control 1"
- GSM9788166 / Sample_title: matched `Huh7` in "Huh7 cells Control 2"
- GSM9788167 / Sample_title: matched `Huh7` in "Huh7 cells Control 3"
- GSM9788168 / Sample_title: matched `Huh7` in "Huh7 cells Control 4"
- GSM9788169 / Sample_title: matched `Huh7` in "Huh7 cells Control 5"
- GSM9788170 / Sample_title: matched `Huh7` in "Huh7 cells OPLA 1"
- GSM9788171 / Sample_title: matched `Huh7` in "Huh7 cells OPLA 2"
- GSM9788172 / Sample_title: matched `Huh7` in "Huh7 cells OPLA 3"
- GSM9788173 / Sample_title: matched `Huh7` in "Huh7 cells OPLA 4"
- GSM9788174 / Sample_title: matched `Huh7` in "Huh7 cells OPLA 5"
- GSM9788175 / Sample_title: matched `Huh7` in "Huh7 cells POLA 1"
- GSM9788176 / Sample_title: matched `Huh7` in "Huh7 cells POLA 2"
- GSM9788177 / Sample_title: matched `Huh7` in "Huh7 cells POLA 3"
- GSM9788178 / Sample_title: matched `Huh7` in "Huh7 cells POLA 4"
- GSM9788179 / Sample_title: matched `Huh7` in "Huh7 cells POLA 5"
- GSM9788165 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM9788166 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM9788167 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM9788168 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM9788169 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM9788170 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM9788171 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM9788172 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM9788173 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM9788174 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM9788175 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM9788176 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM9788177 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM9788178 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM9788179 / Sample_characteristics_ch1: matched `cell line` in "cell line: Huh7"
- GSM9788180 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM9788181 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM9788182 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM9788183 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM9788184 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM9788185 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM9788186 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM9788187 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM9788188 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM9788189 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM9788190 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM9788191 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM9788192 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM9788193 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"
- GSM9788194 / Sample_characteristics_ch1: matched `cell line` in "cell line: PHH"

Decision: MANUAL_REVIEW

Reasons:
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: Huh7, cell line (30/30 samples)
<!-- /computed -->