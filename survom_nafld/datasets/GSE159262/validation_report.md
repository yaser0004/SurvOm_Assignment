# Validation report: GSE159262

Novel 3D Approach to Model Non-Alcoholic Fatty Liver Disease using human Pluripotent Stem Cells

<!-- computed -->
Sample count: 5

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 5 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 5/5 |
| source_tissue | WARN | liver-pattern source 0/5 |
| library_strategy | PASS | RNA-Seq 5/5 |
| library_source | PASS | transcriptomic 5/5 |
| library_selection | PASS | cDNA 5/5 |
| instrument_model | PASS | Illumina HiSeq 4000 5/5 |
| metadata_completeness | PASS | reported consistently: disease, treatment; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, sex, stage, steatosis_grade, tissue |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (4 sample(s)) |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: 10x, Chromium, Single cells were (5 sample(s)) |
| material_type | WARN | cell/culture terms in sample metadata: pluripotent stem cell (5/5 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX9266301, https://www.ncbi.nlm.nih.gov/sra?term=SRX9266302, https://www.ncbi.nlm.nih.gov/sra?term=SRX9266303, https://www.ncbi.nlm.nih.gov/sra?term=SRX9266304, https://www.ncbi.nlm.nih.gov/sra?term=SRX9266305) |
| series_matrix | INFO | present, metadata-only (GSE159262_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX9266301, https://www.ncbi.nlm.nih.gov/sra?term=SRX9266302, https://www.ncbi.nlm.nih.gov/sra?term=SRX9266303, https://www.ncbi.nlm.nih.gov/sra?term=SRX9266304, https://www.ncbi.nlm.nih.gov/sra?term=SRX9266305 |

## Canonical field distributions

- **disease**: Healthy (1), NAFLD (4)
- **treatment**: control sample (1), oleic acid 0.25uM (2), palmitic acid 0.25uM (2)

## Field presence

- disease state: 5/5 (canon: disease)
- time point: 5/5
- treatment: 5/5 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
### single_cell_or_spatial (FAIL)
- GSM4824487 / Sample_extract_protocol_ch1: matched `Chromium` in "The single cell solution from each sample was loaded onto the Chromium single cell controller by 10X genomics, a droplet-based single cell capture platform."
- GSM4824487 / Sample_extract_protocol_ch1: matched `Single cells were` in "Single cells were lysed and tagged by a bead containing unique molecular identifiers (UMIs), and encapsulated in an oil droplet.; this emulsion was amplified through reverse-transcription, and subsequ"
- GSM4824488 / Sample_extract_protocol_ch1: matched `Chromium` in "The single cell solution from each sample was loaded onto the Chromium single cell controller by 10X genomics, a droplet-based single cell capture platform."
- GSM4824488 / Sample_extract_protocol_ch1: matched `Single cells were` in "Single cells were lysed and tagged by a bead containing unique molecular identifiers (UMIs), and encapsulated in an oil droplet.; this emulsion was amplified through reverse-transcription, and subsequ"
- GSM4824489 / Sample_extract_protocol_ch1: matched `Chromium` in "The single cell solution from each sample was loaded onto the Chromium single cell controller by 10X genomics, a droplet-based single cell capture platform."
- GSM4824489 / Sample_extract_protocol_ch1: matched `Single cells were` in "Single cells were lysed and tagged by a bead containing unique molecular identifiers (UMIs), and encapsulated in an oil droplet.; this emulsion was amplified through reverse-transcription, and subsequ"
- GSM4824490 / Sample_extract_protocol_ch1: matched `Chromium` in "The single cell solution from each sample was loaded onto the Chromium single cell controller by 10X genomics, a droplet-based single cell capture platform."
- GSM4824490 / Sample_extract_protocol_ch1: matched `Single cells were` in "Single cells were lysed and tagged by a bead containing unique molecular identifiers (UMIs), and encapsulated in an oil droplet.; this emulsion was amplified through reverse-transcription, and subsequ"
- GSM4824491 / Sample_extract_protocol_ch1: matched `Chromium` in "The single cell solution from each sample was loaded onto the Chromium single cell controller by 10X genomics, a droplet-based single cell capture platform."
- GSM4824491 / Sample_extract_protocol_ch1: matched `Single cells were` in "Single cells were lysed and tagged by a bead containing unique molecular identifiers (UMIs), and encapsulated in an oil droplet.; this emulsion was amplified through reverse-transcription, and subsequ"
- GSM4824487 / Sample_data_processing: matched `10x` in "Alignment and protein-coding gene quantification was performed using 10x cellranger v3.1.0"
- GSM4824488 / Sample_data_processing: matched `10x` in "Alignment and protein-coding gene quantification was performed using 10x cellranger v3.1.0"
- GSM4824489 / Sample_data_processing: matched `10x` in "Alignment and protein-coding gene quantification was performed using 10x cellranger v3.1.0"
- GSM4824490 / Sample_data_processing: matched `10x` in "Alignment and protein-coding gene quantification was performed using 10x cellranger v3.1.0"
- GSM4824491 / Sample_data_processing: matched `10x` in "Alignment and protein-coding gene quantification was performed using 10x cellranger v3.1.0"
### material_type (WARN)
- GSM4824487 / Sample_source_name_ch1: matched `pluripotent stem cell` in "human induced pluripotent stem cells, primary human cholangiocytes, human immortalised stellate cells line"
- GSM4824488 / Sample_source_name_ch1: matched `pluripotent stem cell` in "human induced pluripotent stem cells, primary human cholangiocytes, human immortalised stellate cells line"
- GSM4824489 / Sample_source_name_ch1: matched `pluripotent stem cell` in "human induced pluripotent stem cells, primary human cholangiocytes, human immortalised stellate cells line"
- GSM4824490 / Sample_source_name_ch1: matched `pluripotent stem cell` in "human induced pluripotent stem cells, primary human cholangiocytes, human immortalised stellate cells line"
- GSM4824491 / Sample_source_name_ch1: matched `pluripotent stem cell` in "human induced pluripotent stem cells, primary human cholangiocytes, human immortalised stellate cells line"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: 10x, Chromium, Single cells were (5 sample(s)))
<!-- /computed -->