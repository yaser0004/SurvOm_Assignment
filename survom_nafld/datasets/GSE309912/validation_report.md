# Validation report: GSE309912

Bulk RNA-seq Toxic Lipid-induced Epigenetic Activation of ICAM1 in Liver Sinusoidal Endothelium Regulates Myeloid-Driven Fibro-inflammatory Response in MASH

<!-- computed -->
Sample count: 12

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 12 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 12/12 |
| source_tissue | PASS | liver-pattern source 12/12 |
| library_strategy | PASS | RNA-Seq 12/12 |
| library_source | PASS | transcriptomic 12/12 |
| library_selection | PASS | cDNA 12/12 |
| instrument_model | PASS | Illumina HiSeq 4000 12/12 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | INFO | series prose mentions in vitro; sample metadata does not corroborate |
| expression_data_availability | PASS | processed series-level file: GSE309912_PA.800_vs_PA.LY_DE_statAll_normCPM.xlsx |
| series_matrix | INFO | present, metadata-only (GSE309912_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX31067785, https://www.ncbi.nlm.nih.gov/sra?term=SRX31067786, https://www.ncbi.nlm.nih.gov/sra?term=SRX31067787, https://www.ncbi.nlm.nih.gov/sra?term=SRX31067788, https://www.ncbi.nlm.nih.gov/sra?term=SRX31067789, and 7 more (see sample_metadata.csv) |

## Canonical field distributions

- **treatment**: PA 500uM (3), PA 500uM+LY (3), PA 800uM (3), Vehicle (3)

## Field presence

- batch: 12/12
- cell type: 12/12
- treatment: 12/12 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE309912 / Series_title: matched `MASH` in "Bulk RNA-seq Toxic Lipid-induced Epigenetic Activation of ICAM1 in Liver Sinusoidal Endothelium Regulates Myeloid-Driven Fibro-inflammatory Response in MASH"
- GSE309912 / Series_summary: matched `metabolic dysfunction-associated stea` in "Background: Liver sinusoidal endothelial cells (LSECs) acquire a proinflammatory phenotype in metabolic dysfunction-associated steatohepatitis (MASH), characterized by elevated adhesion molecules and "

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 12 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
<!-- /computed -->