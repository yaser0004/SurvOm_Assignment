# Validation report: GSE319635

Methionine and choline deficiency rewires transcriptional programs to recapitulate molecular features of human MASH

<!-- computed -->
Sample count: 8

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 8 samples (below 20) |
| organism_consistency | WARN | mixed organisms: Homo sapiens 6/8, Mus musculus 2/8 |
| source_tissue | WARN | liver-pattern source 4/8 |
| library_strategy | PASS | RNA-Seq 8/8 |
| library_source | PASS | transcriptomic 8/8 |
| library_selection | PASS | cDNA 8/8 |
| instrument_model | PASS | NextSeq 2000 8/8 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | WARN | series prose mentions single nucle; sample metadata does not corroborate |
| material_type | WARN | cell/culture terms in sample metadata: HepG2, cell line (8/8 samples) |
| expression_data_availability | PASS | processed series-level file: GSE319635_Raw_counts_BMDM.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE319635-GPL30172_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX32195191, https://www.ncbi.nlm.nih.gov/sra?term=SRX32195192, https://www.ncbi.nlm.nih.gov/sra?term=SRX32195193, https://www.ncbi.nlm.nih.gov/sra?term=SRX32195194, https://www.ncbi.nlm.nih.gov/sra?term=SRX32195195, and 3 more (see sample_metadata.csv) |

## Canonical field distributions

- **treatment**: MCD (4), vehicle (4)

## Field presence

- cell line: 8/8
- cell type: 8/8
- genotype: 8/8
- treatment: 8/8 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### organism_consistency (WARN)
### source_tissue (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE319635 / Series_title: matched `MASH` in "Methionine and choline deficiency rewires transcriptional programs to recapitulate molecular features of human MASH"
- GSE319635 / Series_summary: matched `Metabolic dysfunction-associated stea` in "Metabolic dysfunction-associated steatohepatitis (MASH) is a leading cause of cirrhosis and liver related mortality, but it remains unclear how nutrient stresses drive coordinated transcriptional remo"
### single_cell_or_spatial (WARN)
- GSE319635 / Series_summary: matched `single nucle` in "Metabolic dysfunction-associated steatohepatitis (MASH) is a leading cause of cirrhosis and liver related mortality, but it remains unclear how nutrient stresses drive coordinated transcriptional remo"
### material_type (WARN)
- GSM9521867 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM9521868 / Sample_source_name_ch1: matched `HepG2` in "HepG2"
- GSM9521867 / Sample_title: matched `HepG2` in "HepG2,Ctrl"
- GSM9521868 / Sample_title: matched `HepG2` in "HepG2, MCD"
- GSM9521867 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9521868 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9521869 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized BMDM"
- GSM9521870 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized BMDM"
- GSM9521871 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human aortic endothelial cells"
- GSM9521872 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized human aortic endothelial cells"
- GSM9521873 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized hepatic stellate cells"
- GSM9521874 / Sample_characteristics_ch1: matched `cell line` in "cell line: immortalized hepatic stellate cells"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 8 samples (below 20)
- organism_consistency: mixed organisms: Homo sapiens 6/8, Mus musculus 2/8
- source_tissue: liver-pattern source 4/8
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- single_cell_or_spatial: series prose mentions single nucle; sample metadata does not corroborate
- material_type: cell/culture terms in sample metadata: HepG2, cell line (8/8 samples)
<!-- /computed -->