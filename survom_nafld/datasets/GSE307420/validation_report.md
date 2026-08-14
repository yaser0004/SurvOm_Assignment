# Validation report: GSE307420

Inhibition of Acetyl-CoA metabolic enzymes by EVT0185 impairs hepatic stellate cell activation and reverses MASH and fibrosis in mouse models.

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
| instrument_model | PASS | Illumina HiSeq 2000 12/12 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | WARN | series prose mentions Spatial transcriptom; sample metadata does not corroborate |
| material_type | WARN | cell/culture terms in sample metadata: LX-2, cell line (12/12 samples) |
| expression_data_availability | PASS | processed series-level file: GSE307420_LX2_featurecounts.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE307420_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX30399312, https://www.ncbi.nlm.nih.gov/sra?term=SRX30399313, https://www.ncbi.nlm.nih.gov/sra?term=SRX30399314, https://www.ncbi.nlm.nih.gov/sra?term=SRX30399315, https://www.ncbi.nlm.nih.gov/sra?term=SRX30399316, and 7 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: HSC immortalized cells (12)

## Field presence

- cell line: 12/12
- cell type: 12/12
- plasmid condition: 12/12
- tgfb1 dose: 12/12
- tissue: 12/12 (canon: tissue)
- treatment dose: 12/12
- treatment time: 12/12

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE307420 / Series_title: matched `MASH` in "Inhibition of Acetyl-CoA metabolic enzymes by EVT0185 impairs hepatic stellate cell activation and reverses MASH and fibrosis in mouse models."
- GSE307420 / Series_summary: matched `Metabolic Dysfunction-Associated Stea` in "Metabolic Dysfunction-Associated Steatohepatitis (MASH) is characterized by liver steatosis and inflammation which lead to fibrosis following hepatic stellate cell (HSC) activation. Acetyl-CoA is fund"
### single_cell_or_spatial (WARN)
- GSE307420 / Series_summary: matched `Spatial transcriptom` in "Metabolic Dysfunction-Associated Steatohepatitis (MASH) is characterized by liver steatosis and inflammation which lead to fibrosis following hepatic stellate cell (HSC) activation. Acetyl-CoA is fund"
### material_type (WARN)
- GSM9223734 / Sample_title: matched `LX-2` in "LX-2 cells, PRP-empty, TGFb1, DMSO, biol rep 1"
- GSM9223735 / Sample_title: matched `LX-2` in "LX-2 cells, PRP-empty, TGFb1, DMSO, biol rep 2"
- GSM9223736 / Sample_title: matched `LX-2` in "LX-2 cells, PRP-empty, TGFb1, DMSO, biol rep 3"
- GSM9223737 / Sample_title: matched `LX-2` in "LX-2 cells, PRP-empty, TGFb1, EVT0185, biol rep 1"
- GSM9223738 / Sample_title: matched `LX-2` in "LX-2 cells, PRP-empty, TGFb1, EVT0185, biol rep 2"
- GSM9223739 / Sample_title: matched `LX-2` in "LX-2 cells, PRP-empty, TGFb1, EVT0185, biol rep 3"
- GSM9223740 / Sample_title: matched `LX-2` in "LX-2 cells, PRP-SLC27A2, TGFb1, DMSO, biol rep 1"
- GSM9223741 / Sample_title: matched `LX-2` in "LX-2 cells, PRP-SLC27A2, TGFb1, DMSO, biol rep 2"
- GSM9223742 / Sample_title: matched `LX-2` in "LX-2 cells, PRP-SLC27A2, TGFb1, DMSO, biol rep 3"
- GSM9223743 / Sample_title: matched `LX-2` in "LX-2 cells, PRP-SLC27A2, TGFb1, EVT0185, biol rep 1"
- GSM9223744 / Sample_title: matched `LX-2` in "LX-2 cells, PRP-SLC27A2, TGFb1, EVT0185, biol rep 2"
- GSM9223745 / Sample_title: matched `LX-2` in "LX-2 cells, PRP-SLC27A2, TGFb1, EVT0185, biol rep 3"
- GSM9223734 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM9223735 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM9223736 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM9223737 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM9223738 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM9223739 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM9223740 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM9223741 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM9223742 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM9223743 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM9223744 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"
- GSM9223745 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX-2"

Decision: MANUAL_REVIEW

Reasons:
- sample_count: 12 samples (below 20)
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- single_cell_or_spatial: series prose mentions Spatial transcriptom; sample metadata does not corroborate
- material_type: cell/culture terms in sample metadata: LX-2, cell line (12/12 samples)
<!-- /computed -->