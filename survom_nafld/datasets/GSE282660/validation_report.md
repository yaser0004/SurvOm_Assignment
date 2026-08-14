# Validation report: GSE282660

Salsalate improves the anti-tumor efficacy of Lenvatinib in MASH-driven hepatocellular carcinoma.

<!-- computed -->
Sample count: 36

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 36 samples |
| organism_consistency | WARN | mixed organisms: Homo sapiens 12/36, Mus musculus 24/36 |
| source_tissue | WARN | liver-pattern source 24/36 |
| library_strategy | PASS | RNA-Seq 36/36 |
| library_source | PASS | transcriptomic 36/36 |
| library_selection | PASS | cDNA 36/36 |
| instrument_model | WARN | mixed instruments: Illumina HiSeq 1500 12/36, NextSeq 2000 24/36 |
| metadata_completeness | PASS | reported consistently: disease, tissue; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade, treatment |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: Hep3B (12/36 samples) |
| expression_data_availability | PASS | processed series-level file: GSE282660_cells_VST_normalized_counts.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE282660-GPL18460_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX26827382, https://www.ncbi.nlm.nih.gov/sra?term=SRX26827383, https://www.ncbi.nlm.nih.gov/sra?term=SRX26827384, https://www.ncbi.nlm.nih.gov/sra?term=SRX26827385, https://www.ncbi.nlm.nih.gov/sra?term=SRX26827386, and 31 more (see sample_metadata.csv) |

## Canonical field distributions

- **disease**: Combination-treated (9), DMSO control (3), Lenvatinib-mesylate-treated (3), Lenvatinib-treated (6), Salicylic acid-treated (3), Salsalate-treated (6), vehicle control (6)
- **tissue**: HCC immortalized cells (12), non-tumor liver (24)

## Field presence

- age at_sacrifice_(mice): 36/36
- ccl4 model_diet_(mice): 36/36
- ccl4 model_dosage_(mice): 36/36
- cell type: 36/36
- cell/mouse line: 36/36
- condition: 36/36 (canon: disease)
- tissue: 36/36 (canon: tissue)
- treatment dose: 36/36

## Evidence for WARN/FAIL checks

### organism_consistency (WARN)
### source_tissue (WARN)
### instrument_model (WARN)
### disease_relevance (WARN)
- GSE282660 / Series_title: matched `MASH` in "Salsalate improves the anti-tumor efficacy of Lenvatinib in MASH-driven hepatocellular carcinoma."
- GSE282660 / Series_summary: matched `metabolic dysfunction-associated stea` in "Rates of hepatocellular carcinoma (HCC) are increasing rapidly due to the epidemic of metabolic dysfunction-associated steatohepatitis (MASH). In addition to increased incidence, emerging evidence sug"
- GSE282660 / Series_overall_design: matched `NASH` in "To investigate transcriptomic effects of Lenvatinib-mesylate, Salsalate, or combination treatment in vivo, bulk RNA-seq data was obtained from  non-tumoral liver tissue from a FAT-NASH murine model (W"
### material_type (WARN)
- GSM8648415 / Sample_title: matched `Hep3B` in "Hep3B cells, DMSO control, biol rep 1"
- GSM8648416 / Sample_title: matched `Hep3B` in "Hep3B cells, DMSO control, biol rep 2"
- GSM8648417 / Sample_title: matched `Hep3B` in "Hep3B cells, DMSO control, biol rep 3"
- GSM8648418 / Sample_title: matched `Hep3B` in "Hep3B cells, Salsalate-treated, biol rep 1"
- GSM8648419 / Sample_title: matched `Hep3B` in "Hep3B cells, Salsalate-treated, biol rep 2"
- GSM8648420 / Sample_title: matched `Hep3B` in "Hep3B cells, Salsalate-treated, biol rep 3"
- GSM8648421 / Sample_title: matched `Hep3B` in "Hep3B cells, Lenvatinib-treated, biol rep 1"
- GSM8648422 / Sample_title: matched `Hep3B` in "Hep3B cells, Lenvatinib-treated, biol rep 2"
- GSM8648423 / Sample_title: matched `Hep3B` in "Hep3B cells, Lenvatinib-treated, biol rep 3"
- GSM8648424 / Sample_title: matched `Hep3B` in "Hep3B cells, Combination-treated, biol rep 1"
- GSM8648425 / Sample_title: matched `Hep3B` in "Hep3B cells, Combination-treated, biol rep 2"
- GSM8648426 / Sample_title: matched `Hep3B` in "Hep3B cells, Combination-treated, biol rep 3"
- GSM8648415 / Sample_characteristics_ch1: matched `Hep3B` in "cell/mouse line: Hep3B"
- GSM8648416 / Sample_characteristics_ch1: matched `Hep3B` in "cell/mouse line: Hep3B"
- GSM8648417 / Sample_characteristics_ch1: matched `Hep3B` in "cell/mouse line: Hep3B"
- GSM8648418 / Sample_characteristics_ch1: matched `Hep3B` in "cell/mouse line: Hep3B"
- GSM8648419 / Sample_characteristics_ch1: matched `Hep3B` in "cell/mouse line: Hep3B"
- GSM8648420 / Sample_characteristics_ch1: matched `Hep3B` in "cell/mouse line: Hep3B"
- GSM8648421 / Sample_characteristics_ch1: matched `Hep3B` in "cell/mouse line: Hep3B"
- GSM8648422 / Sample_characteristics_ch1: matched `Hep3B` in "cell/mouse line: Hep3B"
- GSM8648423 / Sample_characteristics_ch1: matched `Hep3B` in "cell/mouse line: Hep3B"
- GSM8648424 / Sample_characteristics_ch1: matched `Hep3B` in "cell/mouse line: Hep3B"
- GSM8648425 / Sample_characteristics_ch1: matched `Hep3B` in "cell/mouse line: Hep3B"
- GSM8648426 / Sample_characteristics_ch1: matched `Hep3B` in "cell/mouse line: Hep3B"

Decision: MANUAL_REVIEW

Reasons:
- organism_consistency: mixed organisms: Homo sapiens 12/36, Mus musculus 24/36
- source_tissue: liver-pattern source 24/36
- instrument_model: mixed instruments: Illumina HiSeq 1500 12/36, NextSeq 2000 24/36
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: Hep3B (12/36 samples)
<!-- /computed -->