# Validation report: GSE158884

RNA-seq in HepG2 cells with YY1 knockdown

<!-- computed -->
Sample count: 22

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 22 samples |
| organism_consistency | PASS | Homo sapiens 22/22 |
| source_tissue | PASS | liver-pattern source 22/22 |
| library_strategy | PASS | RNA-Seq 22/22 |
| library_source | PASS | transcriptomic 22/22 |
| library_selection | PASS | cDNA 22/22 |
| instrument_model | PASS | Illumina HiSeq 2500 22/22 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: HepG2 (22/22 samples) |
| expression_data_availability | PASS | processed series-level file: GSE158884_YY1_KD_feature_counts.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE158884_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX9230547, https://www.ncbi.nlm.nih.gov/sra?term=SRX9230548, https://www.ncbi.nlm.nih.gov/sra?term=SRX9230549, https://www.ncbi.nlm.nih.gov/sra?term=SRX9230550, https://www.ncbi.nlm.nih.gov/sra?term=SRX9230551, and 17 more (see sample_metadata.csv) |

## Canonical field distributions

- **treatment**: YY1-KD (8), control (14)

## Field presence

- cell type: 22/22
- strain: 22/22
- treatment: 22/22 (canon: treatment)

## Evidence for WARN/FAIL checks

### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE158884 / Series_summary: matched `nonalcoholic fatty liver` in "Dysregulation of YY1 has been observed in many human cancers. Recent studies have shown that overexpression of YY1 plays a pivotal role in the initiation and progression of nonalcoholic fatty liver di"
### material_type (WARN)
- GSM4813878 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4813879 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4813880 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4813881 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4813882 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4813883 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4813884 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4813885 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4813886 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4813887 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4813888 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4813889 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4813890 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4813891 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4813892 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4813893 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4813894 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4813895 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4813896 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4813897 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4813898 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4813899 / Sample_source_name_ch1: matched `HepG2` in "HepG2 cells"
- GSM4813878 / Sample_title: matched `HepG2` in "HepG2-control-rep1"
- GSM4813879 / Sample_title: matched `HepG2` in "HepG2-control-rep2"
- GSM4813880 / Sample_title: matched `HepG2` in "HepG2-control-rep3"
- GSM4813881 / Sample_title: matched `HepG2` in "HepG2-control-rep4"
- GSM4813882 / Sample_title: matched `HepG2` in "HepG2-control-rep5"
- GSM4813883 / Sample_title: matched `HepG2` in "HepG2-control-rep6"
- GSM4813884 / Sample_title: matched `HepG2` in "HepG2-control-rep7"
- GSM4813885 / Sample_title: matched `HepG2` in "HepG2-YY-KD-rep1"
- GSM4813886 / Sample_title: matched `HepG2` in "HepG2-YY-KD-rep2"
- GSM4813887 / Sample_title: matched `HepG2` in "HepG2-YY-KD-rep3"
- GSM4813888 / Sample_title: matched `HepG2` in "HepG2-YY-KD-rep4"
- GSM4813889 / Sample_title: matched `HepG2` in "HepG2-YY-KD-rep5"
- GSM4813890 / Sample_title: matched `HepG2` in "HepG2-YY-KD-rep6"
- GSM4813891 / Sample_title: matched `HepG2` in "HepG2-YY-KD-rep7"
- GSM4813892 / Sample_title: matched `HepG2` in "HepG2-YY-KD-rep8"
- GSM4813893 / Sample_title: matched `HepG2` in "HepG2-control-rep8"
- GSM4813894 / Sample_title: matched `HepG2` in "HepG2-control-rep9"
- GSM4813895 / Sample_title: matched `HepG2` in "HepG2-control-rep10"
- GSM4813896 / Sample_title: matched `HepG2` in "HepG2-control-rep11"
- GSM4813897 / Sample_title: matched `HepG2` in "HepG2-control-rep12"
- GSM4813898 / Sample_title: matched `HepG2` in "HepG2-control-rep13"
- GSM4813899 / Sample_title: matched `HepG2` in "HepG2-control-rep14"
- GSM4813878 / Sample_characteristics_ch1: matched `HepG2` in "strain: HepG2 cells"
- GSM4813879 / Sample_characteristics_ch1: matched `HepG2` in "strain: HepG2 cells"
- GSM4813880 / Sample_characteristics_ch1: matched `HepG2` in "strain: HepG2 cells"
- GSM4813881 / Sample_characteristics_ch1: matched `HepG2` in "strain: HepG2 cells"
- GSM4813882 / Sample_characteristics_ch1: matched `HepG2` in "strain: HepG2 cells"
- GSM4813883 / Sample_characteristics_ch1: matched `HepG2` in "strain: HepG2 cells"
- GSM4813884 / Sample_characteristics_ch1: matched `HepG2` in "strain: HepG2 cells"
- GSM4813885 / Sample_characteristics_ch1: matched `HepG2` in "strain: HepG2 cells"
- GSM4813886 / Sample_characteristics_ch1: matched `HepG2` in "strain: HepG2 cells"
- GSM4813887 / Sample_characteristics_ch1: matched `HepG2` in "strain: HepG2 cells"
- GSM4813888 / Sample_characteristics_ch1: matched `HepG2` in "strain: HepG2 cells"
- GSM4813889 / Sample_characteristics_ch1: matched `HepG2` in "strain: HepG2 cells"
- GSM4813890 / Sample_characteristics_ch1: matched `HepG2` in "strain: HepG2 cells"
- GSM4813891 / Sample_characteristics_ch1: matched `HepG2` in "strain: HepG2 cells"
- GSM4813892 / Sample_characteristics_ch1: matched `HepG2` in "strain: HepG2 cells"
- GSM4813893 / Sample_characteristics_ch1: matched `HepG2` in "strain: HepG2 cells"
- GSM4813894 / Sample_characteristics_ch1: matched `HepG2` in "strain: HepG2 cells"
- GSM4813895 / Sample_characteristics_ch1: matched `HepG2` in "strain: HepG2 cells"
- GSM4813896 / Sample_characteristics_ch1: matched `HepG2` in "strain: HepG2 cells"
- GSM4813897 / Sample_characteristics_ch1: matched `HepG2` in "strain: HepG2 cells"
- GSM4813898 / Sample_characteristics_ch1: matched `HepG2` in "strain: HepG2 cells"
- GSM4813899 / Sample_characteristics_ch1: matched `HepG2` in "strain: HepG2 cells"

Decision: MANUAL_REVIEW

Reasons:
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: HepG2 (22/22 samples)
<!-- /computed -->