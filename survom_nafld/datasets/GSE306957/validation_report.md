# Validation report: GSE306957

Mitochondrial RNA cytosolic leakage drives the SASP [CRISPR/Cas9]

<!-- computed -->
Sample count: 34

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 34 samples |
| organism_consistency | WARN | mixed organisms: Homo sapiens 27/34, Mus musculus 7/34 |
| source_tissue | WARN | liver-pattern source 7/34 |
| library_strategy | PASS | RNA-Seq 34/34 |
| library_source | PASS | transcriptomic 34/34 |
| library_selection | PASS | cDNA 34/34 |
| instrument_model | PASS | Illumina NovaSeq X Plus 34/34 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: 10X (34 sample(s)) |
| material_type | WARN | cell/culture terms in sample metadata: cell line (27/34 samples) |
| expression_data_availability | PASS | processed per-sample counts (34/34), packaged in GSE306957_RAW.tar |
| series_matrix | INFO | present, metadata-only (GSE306957-GPL34284_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX30335518, https://www.ncbi.nlm.nih.gov/sra?term=SRX30335519, https://www.ncbi.nlm.nih.gov/sra?term=SRX30335520, https://www.ncbi.nlm.nih.gov/sra?term=SRX30335521, https://www.ncbi.nlm.nih.gov/sra?term=SRX30335522, and 29 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Fibroblast (27), Liver (7)
- **treatment**: 20Gy X-ray irradiation (15), FFC diet (7), Proliferating (12)

## Field presence

- cell line: 27/34
- cell type: 27/34
- genotype: 34/34
- tissue: 34/34 (canon: tissue)
- treatment: 34/34 (canon: treatment)

## Evidence for WARN/FAIL checks

### organism_consistency (WARN)
### source_tissue (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE306957 / Series_summary: matched `Steatohepatitis` in "Senescent cells secrete proinflammatory factors known as the senescence-associated secretory phenotype (SASP), contributing to tissue dysfunction and aging. Mitochondrial dysfunction is a key feature "
- GSE306957 / Series_overall_design: matched `metabolic dysfunction-associated stea` in "RNA-seq profiling of proliferating and senescent fibroblasts lacking proteins associated with cytosolic RNA signaling, including DDX58 (RIG-I), IFIH1 (MDA5) and MAVS. Moreover, RNA-seq was also perfor"
### single_cell_or_spatial (FAIL)
- GSM9213050 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213051 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213052 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213053 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213054 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213055 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213056 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213057 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213058 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213059 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213060 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213061 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213062 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213063 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213064 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213065 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213066 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213067 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213068 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213069 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213070 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213071 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213072 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213073 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213074 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213075 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213076 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213077 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213078 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213079 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213080 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213081 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213082 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
- GSM9213083 / Sample_data_processing: matched `10X` in "Assembly: Data were aligned and quantified using the 10X Genomics Cell Ranger Software Suite (v6.1.1) against the murine reference genome (mm10) and human genome (hg38)."
### material_type (WARN)
- GSM9213050 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213051 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213052 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213053 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213054 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213055 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213056 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213057 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213058 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213059 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213060 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213061 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213062 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213063 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213064 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213065 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213066 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213067 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213068 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213069 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213070 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213071 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213072 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213073 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213074 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213075 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"
- GSM9213076 / Sample_characteristics_ch1: matched `cell line` in "cell line: MRC5"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: 10X (34 sample(s)))
<!-- /computed -->