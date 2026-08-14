# Validation report: GSE313774

A Microphysiological Model of Human MASLD Reveals Paradoxical Response to Resmetirom

<!-- computed -->
Sample count: 33

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 33 samples |
| organism_consistency | PASS | Homo sapiens 33/33 |
| source_tissue | PASS | liver-pattern source 33/33 |
| library_strategy | PASS | RNA-Seq 33/33 |
| library_source | PASS | transcriptomic 33/33 |
| library_selection | PASS | cDNA 33/33 |
| instrument_model | PASS | Illumina HiSeq 4000 33/33 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (33/33 samples) |
| expression_data_availability | PASS | processed series-level file: GSE313774_RNA05000001_tpm.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE313774_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | no SRA/raw sequencing links found |

## Canonical field distributions

- **tissue**: liver (33)
- **treatment**: Condition 1 (7), Condition 1 + Ins (8), Condition 2 (9), Condition 2 + Ins (9)

## Field presence

- batch: 33/33
- cell line: 33/33
- cell type: 33/33
- tissue: 33/33 (canon: tissue)
- treatment: 33/33 (canon: treatment)

## Evidence for WARN/FAIL checks

### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE313774 / Series_title: matched `MASLD` in "A Microphysiological Model of Human MASLD Reveals Paradoxical Response to Resmetirom"
- GSE313774 / Series_summary: matched `Metabolic dysfunction-associated stea` in "Metabolic dysfunction-associated steatotic liver disease (MASLD) is a chronic disease with multiple etiologies, stemming from the interplay between local and systemic genetic, diet, and gene-environme"
- GSE313774 / Series_overall_design: matched `MASLD` in "Microphysiological modeling of MASLD with human hepatocytes in the CN-Bio LiverChip system."
### material_type (WARN)
- GSM9375169 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375170 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375171 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375172 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375173 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375174 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375175 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375176 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375177 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375178 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375179 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375180 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375181 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375182 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375183 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375184 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375185 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375186 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375187 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375188 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375189 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375190 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375191 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375192 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375193 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375194 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375195 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375196 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375197 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375198 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375199 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375200 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"
- GSM9375201 / Sample_characteristics_ch1: matched `cell line` in "cell line: primary"

Decision: MANUAL_REVIEW

Reasons:
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (33/33 samples)
<!-- /computed -->