# Validation report: GSE269926

Single nucleus RNA-sequencing integrated into risk variant colocalization discovers 17 cell-type-specific abdominal obesity genes for metabolic dysfunction-associated steatotic liver disease [scRNA-seq]

<!-- computed -->
Sample count: 8

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 8 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 8/8 |
| source_tissue | WARN | liver-pattern source 0/8; off-target tissue signal detected |
| library_strategy | PASS | RNA-Seq 8/8 |
| library_source | WARN | library_source: transcriptomic single cell 8/8 |
| library_selection | PASS | cDNA 8/8 |
| instrument_model | PASS | Illumina NovaSeq 6000 8/8 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: 10x, STARSolo, barcodes.tsv, features.tsv, matrix.mtx (9 sample(s)) |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE269926_matrix.mtx.gz |
| series_matrix | INFO | present, metadata-only (GSE269926_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | no SRA/raw sequencing links found |

## Canonical field distributions

- **tissue**: subcutaneous adipose tissue (8)

## Field presence

- tissue: 8/8 (canon: tissue)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
- GSM8330444 / Sample_source_name_ch1: matched `adipose` in "subcutaneous adipose tissue"
- GSM8330445 / Sample_source_name_ch1: matched `adipose` in "subcutaneous adipose tissue"
- GSM8330446 / Sample_source_name_ch1: matched `adipose` in "subcutaneous adipose tissue"
- GSM8330447 / Sample_source_name_ch1: matched `adipose` in "subcutaneous adipose tissue"
- GSM8330448 / Sample_source_name_ch1: matched `adipose` in "subcutaneous adipose tissue"
- GSM8330449 / Sample_source_name_ch1: matched `adipose` in "subcutaneous adipose tissue"
- GSM8330450 / Sample_source_name_ch1: matched `adipose` in "subcutaneous adipose tissue"
- GSM8330452 / Sample_source_name_ch1: matched `adipose` in "subcutaneous adipose tissue"
- GSM8330444 / Sample_characteristics_ch1: matched `adipose` in "tissue: subcutaneous adipose tissue"
- GSM8330445 / Sample_characteristics_ch1: matched `adipose` in "tissue: subcutaneous adipose tissue"
- GSM8330446 / Sample_characteristics_ch1: matched `adipose` in "tissue: subcutaneous adipose tissue"
- GSM8330447 / Sample_characteristics_ch1: matched `adipose` in "tissue: subcutaneous adipose tissue"
- GSM8330448 / Sample_characteristics_ch1: matched `adipose` in "tissue: subcutaneous adipose tissue"
- GSM8330449 / Sample_characteristics_ch1: matched `adipose` in "tissue: subcutaneous adipose tissue"
- GSM8330450 / Sample_characteristics_ch1: matched `adipose` in "tissue: subcutaneous adipose tissue"
- GSM8330452 / Sample_characteristics_ch1: matched `adipose` in "tissue: subcutaneous adipose tissue"
### library_source (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE269926 / Series_title: matched `metabolic dysfunction-associated stea` in "Single nucleus RNA-sequencing integrated into risk variant colocalization discovers 17 cell-type-specific abdominal obesity genes for metabolic dysfunction-associated steatotic liver disease [scRNA-se"
- GSE269926 / Series_summary: matched `non-alcoholic fatty liver` in "Abdominal obesity increases the risk for non-alcoholic fatty liver disease (NAFLD), now known as metabolic dysfunction-associated steatotic liver disease (MASLD). To elucidate the directional cell-typ"
### single_cell_or_spatial (FAIL)
- GSM8330444 / Sample_extract_protocol_ch1: matched `10x` in "Libraries were prepared using the 10x Single Cell 3’ Reagent Kit v3.1"
- GSM8330445 / Sample_extract_protocol_ch1: matched `10x` in "Libraries were prepared using the 10x Single Cell 3’ Reagent Kit v3.1"
- GSM8330446 / Sample_extract_protocol_ch1: matched `10x` in "Libraries were prepared using the 10x Single Cell 3’ Reagent Kit v3.1"
- GSM8330447 / Sample_extract_protocol_ch1: matched `10x` in "Libraries were prepared using the 10x Single Cell 3’ Reagent Kit v3.1"
- GSM8330448 / Sample_extract_protocol_ch1: matched `10x` in "Libraries were prepared using the 10x Single Cell 3’ Reagent Kit v3.1"
- GSM8330449 / Sample_extract_protocol_ch1: matched `10x` in "Libraries were prepared using the 10x Single Cell 3’ Reagent Kit v3.1"
- GSM8330450 / Sample_extract_protocol_ch1: matched `10x` in "Libraries were prepared using the 10x Single Cell 3’ Reagent Kit v3.1"
- GSM8330452 / Sample_extract_protocol_ch1: matched `10x` in "Libraries were prepared using the 10x Single Cell 3’ Reagent Kit v3.1"
- GSM8330444 / Sample_data_processing: matched `STARSolo` in "Sequence reads were aligned to the GRCh37 human genome reference using STARSolo in STAR v2.7.5a with the the ‘--soloFeatures GeneFull’ parameter to account for full pre-mRNA transcripts"
- GSM8330445 / Sample_data_processing: matched `STARSolo` in "Sequence reads were aligned to the GRCh37 human genome reference using STARSolo in STAR v2.7.5a with the the ‘--soloFeatures GeneFull’ parameter to account for full pre-mRNA transcripts"
- GSM8330446 / Sample_data_processing: matched `STARSolo` in "Sequence reads were aligned to the GRCh37 human genome reference using STARSolo in STAR v2.7.5a with the the ‘--soloFeatures GeneFull’ parameter to account for full pre-mRNA transcripts"
- GSM8330447 / Sample_data_processing: matched `STARSolo` in "Sequence reads were aligned to the GRCh37 human genome reference using STARSolo in STAR v2.7.5a with the the ‘--soloFeatures GeneFull’ parameter to account for full pre-mRNA transcripts"
- GSM8330448 / Sample_data_processing: matched `STARSolo` in "Sequence reads were aligned to the GRCh37 human genome reference using STARSolo in STAR v2.7.5a with the the ‘--soloFeatures GeneFull’ parameter to account for full pre-mRNA transcripts"
- GSM8330449 / Sample_data_processing: matched `STARSolo` in "Sequence reads were aligned to the GRCh37 human genome reference using STARSolo in STAR v2.7.5a with the the ‘--soloFeatures GeneFull’ parameter to account for full pre-mRNA transcripts"
- GSM8330450 / Sample_data_processing: matched `STARSolo` in "Sequence reads were aligned to the GRCh37 human genome reference using STARSolo in STAR v2.7.5a with the the ‘--soloFeatures GeneFull’ parameter to account for full pre-mRNA transcripts"
- GSM8330452 / Sample_data_processing: matched `STARSolo` in "Sequence reads were aligned to the GRCh37 human genome reference using STARSolo in STAR v2.7.5a with the the ‘--soloFeatures GeneFull’ parameter to account for full pre-mRNA transcripts"
- GSE269926 / Series_supplementary_file: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE269nnn/GSE269926/suppl/GSE269926_barcodes.tsv.gz"
- GSE269926 / Series_supplementary_file: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE269nnn/GSE269926/suppl/GSE269926_features.tsv.gz"
- GSE269926 / Series_supplementary_file: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE269nnn/GSE269926/suppl/GSE269926_matrix.mtx.gz"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: 10x, STARSolo, barcodes.tsv, features.tsv, matrix.mtx (9 sample(s)))
<!-- /computed -->