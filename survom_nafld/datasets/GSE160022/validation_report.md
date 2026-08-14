# Validation report: GSE160022

TREM2 sustains macrophage-hepatocyte metabolic coordination in NAFLD and sepsis

<!-- computed -->
Sample count: 31

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 31 samples |
| organism_consistency | WARN | mixed organisms: Homo sapiens 11/31, Mus musculus 20/31 |
| source_tissue | PASS | liver-pattern source 31/31 |
| library_strategy | WARN | mixed strategies: RNA-Seq 23/31, miRNA-Seq 8/31 |
| library_source | PASS | transcriptomic 31/31 |
| library_selection | WARN | mixed library_selection: cDNA 23/31, size fractionation 8/31 |
| instrument_model | WARN | mixed instruments: HiSeq X Ten 8/31, Illumina NovaSeq 6000 23/31 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (11 sample(s)) |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: snRNA (8 sample(s)) |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX9353386, https://www.ncbi.nlm.nih.gov/sra?term=SRX9353387, https://www.ncbi.nlm.nih.gov/sra?term=SRX9353388, https://www.ncbi.nlm.nih.gov/sra?term=SRX9353389, https://www.ncbi.nlm.nih.gov/sra?term=SRX9353390, and 26 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE160022-GPL21273_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX9353386, https://www.ncbi.nlm.nih.gov/sra?term=SRX9353387, https://www.ncbi.nlm.nih.gov/sra?term=SRX9353388, https://www.ncbi.nlm.nih.gov/sra?term=SRX9353389, https://www.ncbi.nlm.nih.gov/sra?term=SRX9353390, and 26 more (see sample_metadata.csv) |

## Canonical field distributions

- **age**: 16 (1), 18 (1), 33 (1), 37 (2), 40 (1), 46 (2), 50 (1), 51 (2)
- **sex**: Female (5), Male (26)
- **tissue**: Liver (31)
- **treatment**: High Fat Diet Model (20)

## Field presence

- Sex: 31/31 (canon: sex)
- age: 11/31 (canon: age)
- cell type: 14/31
- donor type: 11/31
- genotype: 20/31
- tissue: 31/31 (canon: tissue)
- treatment: 20/31 (canon: treatment)

## Evidence for WARN/FAIL checks

### organism_consistency (WARN)
### library_strategy (WARN)
### library_selection (WARN)
### instrument_model (WARN)
### metadata_completeness (WARN)
### single_cell_or_spatial (FAIL)
- GSM4852557 / Sample_data_processing: matched `snRNA` in "Raw reads were subjected to an in-house program, ACGT101-miR (LC Sciences, Houston, Texas, USA) to remove adapter dimers, junk, low complexity, common RNA families (rRNA, tRNA, snRNA, snoRNA) and repe"
- GSM4852558 / Sample_data_processing: matched `snRNA` in "Raw reads were subjected to an in-house program, ACGT101-miR (LC Sciences, Houston, Texas, USA) to remove adapter dimers, junk, low complexity, common RNA families (rRNA, tRNA, snRNA, snoRNA) and repe"
- GSM4852559 / Sample_data_processing: matched `snRNA` in "Raw reads were subjected to an in-house program, ACGT101-miR (LC Sciences, Houston, Texas, USA) to remove adapter dimers, junk, low complexity, common RNA families (rRNA, tRNA, snRNA, snoRNA) and repe"
- GSM4852560 / Sample_data_processing: matched `snRNA` in "Raw reads were subjected to an in-house program, ACGT101-miR (LC Sciences, Houston, Texas, USA) to remove adapter dimers, junk, low complexity, common RNA families (rRNA, tRNA, snRNA, snoRNA) and repe"
- GSM4852561 / Sample_data_processing: matched `snRNA` in "Raw reads were subjected to an in-house program, ACGT101-miR (LC Sciences, Houston, Texas, USA) to remove adapter dimers, junk, low complexity, common RNA families (rRNA, tRNA, snRNA, snoRNA) and repe"
- GSM4852562 / Sample_data_processing: matched `snRNA` in "Raw reads were subjected to an in-house program, ACGT101-miR (LC Sciences, Houston, Texas, USA) to remove adapter dimers, junk, low complexity, common RNA families (rRNA, tRNA, snRNA, snoRNA) and repe"
- GSM4852563 / Sample_data_processing: matched `snRNA` in "Raw reads were subjected to an in-house program, ACGT101-miR (LC Sciences, Houston, Texas, USA) to remove adapter dimers, junk, low complexity, common RNA families (rRNA, tRNA, snRNA, snoRNA) and repe"
- GSM4852564 / Sample_data_processing: matched `snRNA` in "Raw reads were subjected to an in-house program, ACGT101-miR (LC Sciences, Houston, Texas, USA) to remove adapter dimers, junk, low complexity, common RNA families (rRNA, tRNA, snRNA, snoRNA) and repe"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: snRNA (8 sample(s)))
<!-- /computed -->