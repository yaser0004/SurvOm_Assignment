# Validation report: GSE333851

Spatial Glyco-Codes Define Human Liver Pathology and Progression

<!-- computed -->
Sample count: 32

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 32 samples |
| organism_consistency | PASS | Homo sapiens 32/32 |
| source_tissue | PASS | liver-pattern source 32/32 |
| library_strategy | FAIL | no expression-profiling strategy found (OTHER) |
| library_source | WARN | library_source: other 16/32, transcriptomic 16/32 |
| library_selection | PASS | other 32/32 |
| instrument_model | PASS | Illumina NovaSeq 6000 32/32 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (24 sample(s)) |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: CITE-seq, Seurat, Spatial Transcriptom (32 sample(s)) |
| material_type | PASS | no cell-line/culture signal detected |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX33671159, https://www.ncbi.nlm.nih.gov/sra?term=SRX33671160, https://www.ncbi.nlm.nih.gov/sra?term=SRX33671161, https://www.ncbi.nlm.nih.gov/sra?term=SRX33671162, https://www.ncbi.nlm.nih.gov/sra?term=SRX33671163, and 27 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE333851_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX33671159, https://www.ncbi.nlm.nih.gov/sra?term=SRX33671160, https://www.ncbi.nlm.nih.gov/sra?term=SRX33671161, https://www.ncbi.nlm.nih.gov/sra?term=SRX33671162, https://www.ncbi.nlm.nih.gov/sra?term=SRX33671163, and 27 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Liver (32)

## Field presence

- tissue: 32/32 (canon: tissue)

## Evidence for WARN/FAIL checks

### library_strategy (FAIL)
### library_source (WARN)
### metadata_completeness (WARN)
### single_cell_or_spatial (FAIL)
- GSM9775937 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775938 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775939 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775940 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775941 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775942 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775943 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775944 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775945 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775946 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775947 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775948 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775949 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775950 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775951 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775952 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775953 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775954 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775955 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775956 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775957 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775958 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775959 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775960 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775961 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775962 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775963 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775964 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775965 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775966 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775967 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775968 / Sample_extract_protocol_ch1: matched `CITE-seq` in "Spatial glycomics and protein libraries, corresponding to DNA-barcoded lectin-derived tags and antibody-derived tags (LDTs and ADTs), were prepared following the spatial CITE-seq library preparation p"
- GSM9775937 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775937 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775937 / Sample_data_processing: matched `CITE-seq` in "Library strategy: CITE-seq"
- GSM9775938 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775938 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775938 / Sample_data_processing: matched `Spatial Transcriptom` in "Library strategy: Spatial Transcriptomics"
- GSM9775939 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775939 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775939 / Sample_data_processing: matched `CITE-seq` in "Library strategy: CITE-seq"
- GSM9775940 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775940 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775940 / Sample_data_processing: matched `Spatial Transcriptom` in "Library strategy: Spatial Transcriptomics"
- GSM9775941 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775941 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775941 / Sample_data_processing: matched `CITE-seq` in "Library strategy: CITE-seq"
- GSM9775942 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775942 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775942 / Sample_data_processing: matched `Spatial Transcriptom` in "Library strategy: Spatial Transcriptomics"
- GSM9775943 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775943 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775943 / Sample_data_processing: matched `CITE-seq` in "Library strategy: CITE-seq"
- GSM9775944 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775944 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775944 / Sample_data_processing: matched `Spatial Transcriptom` in "Library strategy: Spatial Transcriptomics"
- GSM9775945 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775945 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775945 / Sample_data_processing: matched `CITE-seq` in "Library strategy: CITE-seq"
- GSM9775946 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775946 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775946 / Sample_data_processing: matched `Spatial Transcriptom` in "Library strategy: Spatial Transcriptomics"
- GSM9775947 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775947 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775947 / Sample_data_processing: matched `CITE-seq` in "Library strategy: CITE-seq"
- GSM9775948 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775948 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775948 / Sample_data_processing: matched `Spatial Transcriptom` in "Library strategy: Spatial Transcriptomics"
- GSM9775949 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775949 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775949 / Sample_data_processing: matched `CITE-seq` in "Library strategy: CITE-seq"
- GSM9775950 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775950 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775950 / Sample_data_processing: matched `Spatial Transcriptom` in "Library strategy: Spatial Transcriptomics"
- GSM9775951 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775951 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775951 / Sample_data_processing: matched `CITE-seq` in "Library strategy: CITE-seq"
- GSM9775952 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775952 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775952 / Sample_data_processing: matched `Spatial Transcriptom` in "Library strategy: Spatial Transcriptomics"
- GSM9775953 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775953 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775953 / Sample_data_processing: matched `CITE-seq` in "Library strategy: CITE-seq"
- GSM9775954 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775954 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775954 / Sample_data_processing: matched `Spatial Transcriptom` in "Library strategy: Spatial Transcriptomics"
- GSM9775955 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775955 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775955 / Sample_data_processing: matched `CITE-seq` in "Library strategy: CITE-seq"
- GSM9775956 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775956 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775956 / Sample_data_processing: matched `Spatial Transcriptom` in "Library strategy: Spatial Transcriptomics"
- GSM9775957 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775957 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775957 / Sample_data_processing: matched `CITE-seq` in "Library strategy: CITE-seq"
- GSM9775958 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775958 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775958 / Sample_data_processing: matched `Spatial Transcriptom` in "Library strategy: Spatial Transcriptomics"
- GSM9775959 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775959 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775959 / Sample_data_processing: matched `CITE-seq` in "Library strategy: CITE-seq"
- GSM9775960 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775960 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775960 / Sample_data_processing: matched `Spatial Transcriptom` in "Library strategy: Spatial Transcriptomics"
- GSM9775961 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775961 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775961 / Sample_data_processing: matched `CITE-seq` in "Library strategy: CITE-seq"
- GSM9775962 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775962 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775962 / Sample_data_processing: matched `Spatial Transcriptom` in "Library strategy: Spatial Transcriptomics"
- GSM9775963 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775963 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775963 / Sample_data_processing: matched `CITE-seq` in "Library strategy: CITE-seq"
- GSM9775964 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775964 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775964 / Sample_data_processing: matched `Spatial Transcriptom` in "Library strategy: Spatial Transcriptomics"
- GSM9775965 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775965 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775965 / Sample_data_processing: matched `CITE-seq` in "Library strategy: CITE-seq"
- GSM9775966 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775966 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775966 / Sample_data_processing: matched `Spatial Transcriptom` in "Library strategy: Spatial Transcriptomics"
- GSM9775967 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775967 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775967 / Sample_data_processing: matched `CITE-seq` in "Library strategy: CITE-seq"
- GSM9775968 / Sample_data_processing: matched `CITE-seq` in "LDT and ADT UMI counts were quantified at each spatial pixel using CITE-seq-Count version 1.4.5 with default settings. A whole-transcriptome count matrix was additionally generated using the recommend"
- GSM9775968 / Sample_data_processing: matched `Seurat` in "DBiT-GPT glycan, protein, and transcript count matrices were processed in Seurat using modality-specific SCT normalization, PCA, graph-based clustering, UMAP visualization, and differential feature an"
- GSM9775968 / Sample_data_processing: matched `Spatial Transcriptom` in "Library strategy: Spatial Transcriptomics"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: CITE-seq, Seurat, Spatial Transcriptom (32 sample(s)))
<!-- /computed -->