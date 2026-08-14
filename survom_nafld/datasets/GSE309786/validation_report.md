# Validation report: GSE309786

PNPLA3-I148M genetic variant rewires lipid metabolism to drive programmed cell death in human hepatocytes

<!-- computed -->
Sample count: 8

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 8 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 8/8 |
| source_tissue | PASS | liver-pattern source 8/8 |
| library_strategy | PASS | RNA-Seq 8/8 |
| library_source | PASS | transcriptomic 8/8 |
| library_selection | PASS | cDNA 8/8 |
| instrument_model | PASS | Illumina NextSeq 500 8/8 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: SMART-Seq (8 sample(s)) |
| material_type | INFO | series prose mentions iPSC; sample metadata does not corroborate |
| expression_data_availability | PASS | processed series-level file: GSE309786_Normalized_Counts_All_Samples.csv.gz |
| series_matrix | INFO | present, metadata-only (GSE309786_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX31058564, https://www.ncbi.nlm.nih.gov/sra?term=SRX31058565, https://www.ncbi.nlm.nih.gov/sra?term=SRX31058566, https://www.ncbi.nlm.nih.gov/sra?term=SRX31058567, https://www.ncbi.nlm.nih.gov/sra?term=SRX31058568, and 3 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Liver (8)

## Field presence

- genotype: 8/8
- tissue: 8/8 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE309786 / Series_summary: matched `metabolic dysfunction-associated stea` in "Genetic variants in lipid metabolism influence the risk of developing metabolic dysfunction-associated steatotic liver disease (MASLD), cirrhosis, and end-stage liver disease (ESLD). The mechanisms by"
### single_cell_or_spatial (FAIL)
- GSM9279097 / Sample_extract_protocol_ch1: matched `SMART-Seq` in "total RNA was extracted from isolated primary human hepatocytes using RNeasy Plus Micro Kit (Qiagen). RNA integrity was assessed using the High Sensitivity RNA ScreenTape system on an Agilent 2200 Tap"
- GSM9279098 / Sample_extract_protocol_ch1: matched `SMART-Seq` in "total RNA was extracted from isolated primary human hepatocytes using RNeasy Plus Micro Kit (Qiagen). RNA integrity was assessed using the High Sensitivity RNA ScreenTape system on an Agilent 2200 Tap"
- GSM9279099 / Sample_extract_protocol_ch1: matched `SMART-Seq` in "total RNA was extracted from isolated primary human hepatocytes using RNeasy Plus Micro Kit (Qiagen). RNA integrity was assessed using the High Sensitivity RNA ScreenTape system on an Agilent 2200 Tap"
- GSM9279100 / Sample_extract_protocol_ch1: matched `SMART-Seq` in "total RNA was extracted from isolated primary human hepatocytes using RNeasy Plus Micro Kit (Qiagen). RNA integrity was assessed using the High Sensitivity RNA ScreenTape system on an Agilent 2200 Tap"
- GSM9279101 / Sample_extract_protocol_ch1: matched `SMART-Seq` in "total RNA was extracted from isolated primary human hepatocytes using RNeasy Plus Micro Kit (Qiagen). RNA integrity was assessed using the High Sensitivity RNA ScreenTape system on an Agilent 2200 Tap"
- GSM9279102 / Sample_extract_protocol_ch1: matched `SMART-Seq` in "total RNA was extracted from isolated primary human hepatocytes using RNeasy Plus Micro Kit (Qiagen). RNA integrity was assessed using the High Sensitivity RNA ScreenTape system on an Agilent 2200 Tap"
- GSM9279103 / Sample_extract_protocol_ch1: matched `SMART-Seq` in "total RNA was extracted from isolated primary human hepatocytes using RNeasy Plus Micro Kit (Qiagen). RNA integrity was assessed using the High Sensitivity RNA ScreenTape system on an Agilent 2200 Tap"
- GSM9279104 / Sample_extract_protocol_ch1: matched `SMART-Seq` in "total RNA was extracted from isolated primary human hepatocytes using RNeasy Plus Micro Kit (Qiagen). RNA integrity was assessed using the High Sensitivity RNA ScreenTape system on an Agilent 2200 Tap"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: SMART-Seq (8 sample(s)))
<!-- /computed -->