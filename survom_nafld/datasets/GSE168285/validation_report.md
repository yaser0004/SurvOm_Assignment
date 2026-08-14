# Validation report: GSE168285

Transcriptomal profiling of liver microphysiological system (MPS) co-culture NASH model under varying culture conditions

<!-- computed -->
Sample count: 179

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 179 samples |
| organism_consistency | PASS | Homo sapiens 179/179 |
| source_tissue | PASS | liver-pattern source 179/179 |
| library_strategy | PASS | RNA-Seq 179/179 |
| library_source | PASS | transcriptomic 179/179 |
| library_selection | PASS | cDNA 179/179 |
| instrument_model | PASS | Illumina NextSeq 500 179/179 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE168285_raw_counts.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE168285_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | no SRA/raw sequencing links found |

## Canonical field distributions

- **tissue**: Liver MPS co-culture tissue (179)
- **treatment**: Fat (12), Fat_Cholesterol (3), Fat_Fructose (3), Fat_Fructose_Cholesterol (3), Fat_Fructose_TGF-B (3), Fat_LPS (3), Fat_LPS_Cholesterol (3), Fat_LPS_Fructose (3), Fat_LPS_TGF-B (3), Fat_LPS_TGF-B_Fructose_Cholesterol (3), Fat_TGF-B (3), Fat_TGF-B_Cholesterol (3), Lean (12), Lean_Cholesterol (3), Lean_Fructose (3), Lean_Fructose_Cholesterol (3), Lean_Fructose_TGF-B (3), Lean_LPS (3), Lean_LPS_Cholesterol (3), Lean_LPS_Fructose (3), Lean_LPS_TGF-B (3), Lean_LPS_TGF-B_Fructose_Cholesterol (3), Lean_TGF-B (3), Lean_TGF-B_Cholesterol (3), Reduced_Lean_LPS_Fructose (3), Reduced_NPC_Fat (12), Reduced_NPC_Fat_Cholesterol (3), Reduced_NPC_Fat_Fructose (3), Reduced_NPC_Fat_Fructose_Cholesterol (3), Reduced_NPC_Fat_Fructose_TGF-B (3), Reduced_NPC_Fat_LPS (3), Reduced_NPC_Fat_LPS_Cholesterol (3), Reduced_NPC_Fat_LPS_Fructose (3), Reduced_NPC_Fat_LPS_TGF-B (3), Reduced_NPC_Fat_LPS_TGF-B_Fructose_Cholesterol (3), Reduced_NPC_Fat_TGF-B (3), Reduced_NPC_Fat_TGF-B_Cholesterol (3), Reduced_NPC_Lean (12), Reduced_NPC_Lean_Cholesterol (3), Reduced_NPC_Lean_Fructose (3), Reduced_NPC_Lean_Fructose_Cholesterol (3), Reduced_NPC_Lean_Fructose_TGF-B (3), Reduced_NPC_Lean_LPS (3), Reduced_NPC_Lean_LPS_Cholesterol (3), Reduced_NPC_Lean_LPS_TGF-B (2), Reduced_NPC_Lean_LPS_TGF-B_Fructose_Cholesterol (3), Reduced_NPC_Lean_TGF-B (3), Reduced_NPC_Lean_TGF-B_Cholesterol (3)

## Field presence

- tissue: 179/179 (canon: tissue)
- treatment: 179/179 (canon: treatment)

## Evidence for WARN/FAIL checks

### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE168285 / Series_title: matched `NASH` in "Transcriptomal profiling of liver microphysiological system (MPS) co-culture NASH model under varying culture conditions"
- GSE168285 / Series_summary: matched `NASH` in "Purpose: Liver MPS NASH model was cultured in the presence or absence of six independent cues to identify the culture conditions that produce a model of NAFLD/NASH that most closely represents the hum"

Decision: MANUAL_REVIEW

Reasons:
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
<!-- /computed -->