# Validation report: GSE270488

Antigen-driven CD8+ T cell clonal expansion is a prominent feature of MASH in humans and mice [human]

<!-- computed -->
Sample count: 18

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 18 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 18/18 |
| source_tissue | WARN | liver-pattern source 16/18; off-target tissue signal detected |
| library_strategy | WARN | mixed strategies: OTHER 9/18, RNA-Seq 9/18 |
| library_source | WARN | library_source: transcriptomic 9/18, transcriptomic single cell 9/18 |
| library_selection | WARN | mixed library_selection: cDNA 9/18, other 9/18 |
| instrument_model | PASS | Illumina NovaSeq 6000 18/18 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (6 sample(s)) |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: Cellranger, Chromium, Seurat, barcodes.tsv, features.tsv, matrix.mtx (19 sample(s)) |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | PASS | processed series-level file: GSE270488_human_normalized_rna_matrix.mtx.gz |
| series_matrix | INFO | present, metadata-only (GSE270488_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX25004155, https://www.ncbi.nlm.nih.gov/sra?term=SRX25004156, https://www.ncbi.nlm.nih.gov/sra?term=SRX25004157, https://www.ncbi.nlm.nih.gov/sra?term=SRX25004158, https://www.ncbi.nlm.nih.gov/sra?term=SRX25004159, and 13 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: liver (16), pbmc (2)
- **treatment**: disease - ALD (6), disease - MASH (6), no treatment (6)

## Field presence

- cell type: 18/18
- tissue: 18/18 (canon: tissue)
- treatment: 18/18 (canon: treatment)

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
- GSM8344695 / Sample_source_name_ch1: matched `pbmc` in "pbmc"
- GSM8344704 / Sample_source_name_ch1: matched `pbmc` in "pbmc"
- GSM8344695 / Sample_characteristics_ch1: matched `pbmc` in "tissue: pbmc"
- GSM8344704 / Sample_characteristics_ch1: matched `pbmc` in "tissue: pbmc"
### library_strategy (WARN)
### library_source (WARN)
### library_selection (WARN)
### metadata_completeness (WARN)
### single_cell_or_spatial (FAIL)
- GSM8344695 / Sample_extract_protocol_ch1: matched `Chromium` in "Library construction was preformed per manufacturers instructions with the Chromium Next GEM Single Cell 5' Kit V2 (GEX) or the Chromium Single Cell Human TCR Amplification Kit (TCR). cDNA libraries w"
- GSM8344696 / Sample_extract_protocol_ch1: matched `Chromium` in "Library construction was preformed per manufacturers instructions with the Chromium Next GEM Single Cell 5' Kit V2 (GEX) or the Chromium Single Cell Human TCR Amplification Kit (TCR). cDNA libraries w"
- GSM8344697 / Sample_extract_protocol_ch1: matched `Chromium` in "Library construction was preformed per manufacturers instructions with the Chromium Next GEM Single Cell 5' Kit V2 (GEX) or the Chromium Single Cell Human TCR Amplification Kit (TCR). cDNA libraries w"
- GSM8344698 / Sample_extract_protocol_ch1: matched `Chromium` in "Library construction was preformed per manufacturers instructions with the Chromium Next GEM Single Cell 5' Kit V2 (GEX) or the Chromium Single Cell Human TCR Amplification Kit (TCR). cDNA libraries w"
- GSM8344699 / Sample_extract_protocol_ch1: matched `Chromium` in "Library construction was preformed per manufacturers instructions with the Chromium Next GEM Single Cell 5' Kit V2 (GEX) or the Chromium Single Cell Human TCR Amplification Kit (TCR). cDNA libraries w"
- GSM8344700 / Sample_extract_protocol_ch1: matched `Chromium` in "Library construction was preformed per manufacturers instructions with the Chromium Next GEM Single Cell 5' Kit V2 (GEX) or the Chromium Single Cell Human TCR Amplification Kit (TCR). cDNA libraries w"
- GSM8344701 / Sample_extract_protocol_ch1: matched `Chromium` in "Library construction was preformed per manufacturers instructions with the Chromium Next GEM Single Cell 5' Kit V2 (GEX) or the Chromium Single Cell Human TCR Amplification Kit (TCR). cDNA libraries w"
- GSM8344702 / Sample_extract_protocol_ch1: matched `Chromium` in "Library construction was preformed per manufacturers instructions with the Chromium Next GEM Single Cell 5' Kit V2 (GEX) or the Chromium Single Cell Human TCR Amplification Kit (TCR). cDNA libraries w"
- GSM8344703 / Sample_extract_protocol_ch1: matched `Chromium` in "Library construction was preformed per manufacturers instructions with the Chromium Next GEM Single Cell 5' Kit V2 (GEX) or the Chromium Single Cell Human TCR Amplification Kit (TCR). cDNA libraries w"
- GSM8344704 / Sample_extract_protocol_ch1: matched `Chromium` in "Library construction was preformed per manufacturers instructions with the Chromium Next GEM Single Cell 5' Kit V2 (GEX) or the Chromium Single Cell Human TCR Amplification Kit (TCR). cDNA libraries w"
- GSM8344705 / Sample_extract_protocol_ch1: matched `Chromium` in "Library construction was preformed per manufacturers instructions with the Chromium Next GEM Single Cell 5' Kit V2 (GEX) or the Chromium Single Cell Human TCR Amplification Kit (TCR). cDNA libraries w"
- GSM8344706 / Sample_extract_protocol_ch1: matched `Chromium` in "Library construction was preformed per manufacturers instructions with the Chromium Next GEM Single Cell 5' Kit V2 (GEX) or the Chromium Single Cell Human TCR Amplification Kit (TCR). cDNA libraries w"
- GSM8344707 / Sample_extract_protocol_ch1: matched `Chromium` in "Library construction was preformed per manufacturers instructions with the Chromium Next GEM Single Cell 5' Kit V2 (GEX) or the Chromium Single Cell Human TCR Amplification Kit (TCR). cDNA libraries w"
- GSM8344708 / Sample_extract_protocol_ch1: matched `Chromium` in "Library construction was preformed per manufacturers instructions with the Chromium Next GEM Single Cell 5' Kit V2 (GEX) or the Chromium Single Cell Human TCR Amplification Kit (TCR). cDNA libraries w"
- GSM8344709 / Sample_extract_protocol_ch1: matched `Chromium` in "Library construction was preformed per manufacturers instructions with the Chromium Next GEM Single Cell 5' Kit V2 (GEX) or the Chromium Single Cell Human TCR Amplification Kit (TCR). cDNA libraries w"
- GSM8344710 / Sample_extract_protocol_ch1: matched `Chromium` in "Library construction was preformed per manufacturers instructions with the Chromium Next GEM Single Cell 5' Kit V2 (GEX) or the Chromium Single Cell Human TCR Amplification Kit (TCR). cDNA libraries w"
- GSM8344711 / Sample_extract_protocol_ch1: matched `Chromium` in "Library construction was preformed per manufacturers instructions with the Chromium Next GEM Single Cell 5' Kit V2 (GEX) or the Chromium Single Cell Human TCR Amplification Kit (TCR). cDNA libraries w"
- GSM8344712 / Sample_extract_protocol_ch1: matched `Chromium` in "Library construction was preformed per manufacturers instructions with the Chromium Next GEM Single Cell 5' Kit V2 (GEX) or the Chromium Single Cell Human TCR Amplification Kit (TCR). cDNA libraries w"
- GSM8344695 / Sample_data_processing: matched `Cellranger` in "Cellranger 7.1.0 (multi) for demultiplexing, barcode processing, and gene counting."
- GSM8344695 / Sample_data_processing: matched `Seurat` in "Cells were noramlized, corrected for batch, and integrated using Seurat(4.3.0)"
- GSM8344696 / Sample_data_processing: matched `Cellranger` in "Cellranger 7.1.0 (multi) for demultiplexing, barcode processing, and gene counting."
- GSM8344696 / Sample_data_processing: matched `Seurat` in "Cells were noramlized, corrected for batch, and integrated using Seurat(4.3.0)"
- GSM8344697 / Sample_data_processing: matched `Cellranger` in "Cellranger 7.1.0 (multi) for demultiplexing, barcode processing, and gene counting."
- GSM8344697 / Sample_data_processing: matched `Seurat` in "Cells were noramlized, corrected for batch, and integrated using Seurat(4.3.0)"
- GSM8344698 / Sample_data_processing: matched `Cellranger` in "Cellranger 7.1.0 (multi) for demultiplexing, barcode processing, and gene counting."
- GSM8344698 / Sample_data_processing: matched `Seurat` in "Cells were noramlized, corrected for batch, and integrated using Seurat(4.3.0)"
- GSM8344699 / Sample_data_processing: matched `Cellranger` in "Cellranger 7.1.0 (multi) for demultiplexing, barcode processing, and gene counting."
- GSM8344699 / Sample_data_processing: matched `Seurat` in "Cells were noramlized, corrected for batch, and integrated using Seurat(4.3.0)"
- GSM8344700 / Sample_data_processing: matched `Cellranger` in "Cellranger 7.1.0 (multi) for demultiplexing, barcode processing, and gene counting."
- GSM8344700 / Sample_data_processing: matched `Seurat` in "Cells were noramlized, corrected for batch, and integrated using Seurat(4.3.0)"
- GSM8344701 / Sample_data_processing: matched `Cellranger` in "Cellranger 7.1.0 (multi) for demultiplexing, barcode processing, and gene counting."
- GSM8344701 / Sample_data_processing: matched `Seurat` in "Cells were noramlized, corrected for batch, and integrated using Seurat(4.3.0)"
- GSM8344702 / Sample_data_processing: matched `Cellranger` in "Cellranger 7.1.0 (multi) for demultiplexing, barcode processing, and gene counting."
- GSM8344702 / Sample_data_processing: matched `Seurat` in "Cells were noramlized, corrected for batch, and integrated using Seurat(4.3.0)"
- GSM8344703 / Sample_data_processing: matched `Cellranger` in "Cellranger 7.1.0 (multi) for demultiplexing, barcode processing, and gene counting."
- GSM8344703 / Sample_data_processing: matched `Seurat` in "Cells were noramlized, corrected for batch, and integrated using Seurat(4.3.0)"
- GSM8344704 / Sample_data_processing: matched `Cellranger` in "Cellranger 7.1.0 (multi) for demultiplexing, barcode processing, and gene counting."
- GSM8344704 / Sample_data_processing: matched `Seurat` in "Cells were noramlized, corrected for batch, and integrated using Seurat(4.3.0)"
- GSM8344705 / Sample_data_processing: matched `Cellranger` in "Cellranger 7.1.0 (multi) for demultiplexing, barcode processing, and gene counting."
- GSM8344705 / Sample_data_processing: matched `Seurat` in "Cells were noramlized, corrected for batch, and integrated using Seurat(4.3.0)"
- GSM8344706 / Sample_data_processing: matched `Cellranger` in "Cellranger 7.1.0 (multi) for demultiplexing, barcode processing, and gene counting."
- GSM8344706 / Sample_data_processing: matched `Seurat` in "Cells were noramlized, corrected for batch, and integrated using Seurat(4.3.0)"
- GSM8344707 / Sample_data_processing: matched `Cellranger` in "Cellranger 7.1.0 (multi) for demultiplexing, barcode processing, and gene counting."
- GSM8344707 / Sample_data_processing: matched `Seurat` in "Cells were noramlized, corrected for batch, and integrated using Seurat(4.3.0)"
- GSM8344708 / Sample_data_processing: matched `Cellranger` in "Cellranger 7.1.0 (multi) for demultiplexing, barcode processing, and gene counting."
- GSM8344708 / Sample_data_processing: matched `Seurat` in "Cells were noramlized, corrected for batch, and integrated using Seurat(4.3.0)"
- GSM8344709 / Sample_data_processing: matched `Cellranger` in "Cellranger 7.1.0 (multi) for demultiplexing, barcode processing, and gene counting."
- GSM8344709 / Sample_data_processing: matched `Seurat` in "Cells were noramlized, corrected for batch, and integrated using Seurat(4.3.0)"
- GSM8344710 / Sample_data_processing: matched `Cellranger` in "Cellranger 7.1.0 (multi) for demultiplexing, barcode processing, and gene counting."
- GSM8344710 / Sample_data_processing: matched `Seurat` in "Cells were noramlized, corrected for batch, and integrated using Seurat(4.3.0)"
- GSM8344711 / Sample_data_processing: matched `Cellranger` in "Cellranger 7.1.0 (multi) for demultiplexing, barcode processing, and gene counting."
- GSM8344711 / Sample_data_processing: matched `Seurat` in "Cells were noramlized, corrected for batch, and integrated using Seurat(4.3.0)"
- GSM8344712 / Sample_data_processing: matched `Cellranger` in "Cellranger 7.1.0 (multi) for demultiplexing, barcode processing, and gene counting."
- GSM8344712 / Sample_data_processing: matched `Seurat` in "Cells were noramlized, corrected for batch, and integrated using Seurat(4.3.0)"
- GSE270488 / Series_supplementary_file: matched `barcodes.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE270nnn/GSE270488/suppl/GSE270488_human_cell_barcodes.tsv.gz"
- GSE270488 / Series_supplementary_file: matched `features.tsv` in "ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE270nnn/GSE270488/suppl/GSE270488_human_normalized_rna_features.tsv.gz"
- GSE270488 / Series_supplementary_file: matched `matrix.mtx` in "ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE270nnn/GSE270488/suppl/GSE270488_human_normalized_rna_matrix.mtx.gz"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: Cellranger, Chromium, Seurat, barcodes.tsv, features.tsv, matrix.mtx (19 sample(s)))
<!-- /computed -->