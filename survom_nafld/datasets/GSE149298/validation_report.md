# Validation report: GSE149298

Integrative molecular profiling of autoreactive CD4 T cells in autoimmune hepatitis

<!-- computed -->
Sample count: 14

## Checks

| id | status | observed |
|---|---|---|
| sample_count | WARN | 14 samples (below 20) |
| organism_consistency | PASS | Homo sapiens 14/14 |
| source_tissue | WARN | liver-pattern source 0/14 |
| library_strategy | PASS | RNA-Seq 14/14 |
| library_source | PASS | transcriptomic 14/14 |
| library_selection | PASS | cDNA 14/14 |
| instrument_model | PASS | NextSeq 550 14/14 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | FAIL | cell-resolved signal in sample metadata: Drop-seq, scRNA (14 sample(s)) |
| material_type | INFO | series prose mentions in vitro; sample metadata does not corroborate |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX8171801, https://www.ncbi.nlm.nih.gov/sra?term=SRX8171802, https://www.ncbi.nlm.nih.gov/sra?term=SRX8171803, https://www.ncbi.nlm.nih.gov/sra?term=SRX8171804, https://www.ncbi.nlm.nih.gov/sra?term=SRX8171805, and 9 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE149298_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX8171801, https://www.ncbi.nlm.nih.gov/sra?term=SRX8171802, https://www.ncbi.nlm.nih.gov/sra?term=SRX8171803, https://www.ncbi.nlm.nih.gov/sra?term=SRX8171804, https://www.ncbi.nlm.nih.gov/sra?term=SRX8171805, and 9 more (see sample_metadata.csv) |

## Field presence

- cell types: 14/14

## Evidence for WARN/FAIL checks

### sample_count (WARN)
### source_tissue (WARN)
### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE149298 / Series_summary: matched `steatohepatitis` in "Background & Aims: In most autoimmune disorders, crosstalk of B cells and CD4 T cells results in the accumulation of autoantibodies targeting specific self-antigen like the Soluble Liver Antigen (SLA "
### single_cell_or_spatial (FAIL)
- GSM4495738 / Sample_extract_protocol_ch1: matched `scRNA` in "First, CD154+ memory CD4 T cells were sorted on BD FACSAriaII, one cell per well, in 96-well plates containing specific lysis buffer at the CRTI, Nantes. Plates were immediately frozen for storage at "
- GSM4495738 / Sample_extract_protocol_ch1: matched `scRNA` in "For each plate, an Illumina sequencing library targeting the 5’-end of barcoded cDNA was prepared by a modified transposase-based method incorporating a plate-associated i7 barcode (Attaf et al., DOI:"
- GSM4495738 / Sample_extract_protocol_ch1: matched `scRNA` in "Cells were analyzed in three distinct scRNAseq experiments (scRNAseqMetrics_SupplementaryTable_Geo.docx). Libraries prepared with the FB5P-seq protocol were sequenced on Illumina NextSeq550 platform w"
- GSM4495739 / Sample_extract_protocol_ch1: matched `scRNA` in "First, CD154+ memory CD4 T cells were sorted on BD FACSAriaII, one cell per well, in 96-well plates containing specific lysis buffer at the CRTI, Nantes. Plates were immediately frozen for storage at "
- GSM4495739 / Sample_extract_protocol_ch1: matched `scRNA` in "For each plate, an Illumina sequencing library targeting the 5’-end of barcoded cDNA was prepared by a modified transposase-based method incorporating a plate-associated i7 barcode (Attaf et al., DOI:"
- GSM4495739 / Sample_extract_protocol_ch1: matched `scRNA` in "Cells were analyzed in three distinct scRNAseq experiments (scRNAseqMetrics_SupplementaryTable_Geo.docx). Libraries prepared with the FB5P-seq protocol were sequenced on Illumina NextSeq550 platform w"
- GSM4495740 / Sample_extract_protocol_ch1: matched `scRNA` in "First, CD154+ memory CD4 T cells were sorted on BD FACSAriaII, one cell per well, in 96-well plates containing specific lysis buffer at the CRTI, Nantes. Plates were immediately frozen for storage at "
- GSM4495740 / Sample_extract_protocol_ch1: matched `scRNA` in "For each plate, an Illumina sequencing library targeting the 5’-end of barcoded cDNA was prepared by a modified transposase-based method incorporating a plate-associated i7 barcode (Attaf et al., DOI:"
- GSM4495740 / Sample_extract_protocol_ch1: matched `scRNA` in "Cells were analyzed in three distinct scRNAseq experiments (scRNAseqMetrics_SupplementaryTable_Geo.docx). Libraries prepared with the FB5P-seq protocol were sequenced on Illumina NextSeq550 platform w"
- GSM4495741 / Sample_extract_protocol_ch1: matched `scRNA` in "First, CD154+ memory CD4 T cells were sorted on BD FACSAriaII, one cell per well, in 96-well plates containing specific lysis buffer at the CRTI, Nantes. Plates were immediately frozen for storage at "
- GSM4495741 / Sample_extract_protocol_ch1: matched `scRNA` in "For each plate, an Illumina sequencing library targeting the 5’-end of barcoded cDNA was prepared by a modified transposase-based method incorporating a plate-associated i7 barcode (Attaf et al., DOI:"
- GSM4495741 / Sample_extract_protocol_ch1: matched `scRNA` in "Cells were analyzed in three distinct scRNAseq experiments (scRNAseqMetrics_SupplementaryTable_Geo.docx). Libraries prepared with the FB5P-seq protocol were sequenced on Illumina NextSeq550 platform w"
- GSM4495742 / Sample_extract_protocol_ch1: matched `scRNA` in "First, CD154+ memory CD4 T cells were sorted on BD FACSAriaII, one cell per well, in 96-well plates containing specific lysis buffer at the CRTI, Nantes. Plates were immediately frozen for storage at "
- GSM4495742 / Sample_extract_protocol_ch1: matched `scRNA` in "For each plate, an Illumina sequencing library targeting the 5’-end of barcoded cDNA was prepared by a modified transposase-based method incorporating a plate-associated i7 barcode (Attaf et al., DOI:"
- GSM4495742 / Sample_extract_protocol_ch1: matched `scRNA` in "Cells were analyzed in three distinct scRNAseq experiments (scRNAseqMetrics_SupplementaryTable_Geo.docx). Libraries prepared with the FB5P-seq protocol were sequenced on Illumina NextSeq550 platform w"
- GSM4495743 / Sample_extract_protocol_ch1: matched `scRNA` in "First, CD154+ memory CD4 T cells were sorted on BD FACSAriaII, one cell per well, in 96-well plates containing specific lysis buffer at the CRTI, Nantes. Plates were immediately frozen for storage at "
- GSM4495743 / Sample_extract_protocol_ch1: matched `scRNA` in "For each plate, an Illumina sequencing library targeting the 5’-end of barcoded cDNA was prepared by a modified transposase-based method incorporating a plate-associated i7 barcode (Attaf et al., DOI:"
- GSM4495743 / Sample_extract_protocol_ch1: matched `scRNA` in "Cells were analyzed in three distinct scRNAseq experiments (scRNAseqMetrics_SupplementaryTable_Geo.docx). Libraries prepared with the FB5P-seq protocol were sequenced on Illumina NextSeq550 platform w"
- GSM4495744 / Sample_extract_protocol_ch1: matched `scRNA` in "First, CD154+ memory CD4 T cells were sorted on BD FACSAriaII, one cell per well, in 96-well plates containing specific lysis buffer at the CRTI, Nantes. Plates were immediately frozen for storage at "
- GSM4495744 / Sample_extract_protocol_ch1: matched `scRNA` in "For each plate, an Illumina sequencing library targeting the 5’-end of barcoded cDNA was prepared by a modified transposase-based method incorporating a plate-associated i7 barcode (Attaf et al., DOI:"
- GSM4495744 / Sample_extract_protocol_ch1: matched `scRNA` in "Cells were analyzed in three distinct scRNAseq experiments (scRNAseqMetrics_SupplementaryTable_Geo.docx). Libraries prepared with the FB5P-seq protocol were sequenced on Illumina NextSeq550 platform w"
- GSM4495745 / Sample_extract_protocol_ch1: matched `scRNA` in "First, CD154+ memory CD4 T cells were sorted on BD FACSAriaII, one cell per well, in 96-well plates containing specific lysis buffer at the CRTI, Nantes. Plates were immediately frozen for storage at "
- GSM4495745 / Sample_extract_protocol_ch1: matched `scRNA` in "For each plate, an Illumina sequencing library targeting the 5’-end of barcoded cDNA was prepared by a modified transposase-based method incorporating a plate-associated i7 barcode (Attaf et al., DOI:"
- GSM4495745 / Sample_extract_protocol_ch1: matched `scRNA` in "Cells were analyzed in three distinct scRNAseq experiments (scRNAseqMetrics_SupplementaryTable_Geo.docx). Libraries prepared with the FB5P-seq protocol were sequenced on Illumina NextSeq550 platform w"
- GSM4495746 / Sample_extract_protocol_ch1: matched `scRNA` in "First, CD154+ memory CD4 T cells were sorted on BD FACSAriaII, one cell per well, in 96-well plates containing specific lysis buffer at the CRTI, Nantes. Plates were immediately frozen for storage at "
- GSM4495746 / Sample_extract_protocol_ch1: matched `scRNA` in "For each plate, an Illumina sequencing library targeting the 5’-end of barcoded cDNA was prepared by a modified transposase-based method incorporating a plate-associated i7 barcode (Attaf et al., DOI:"
- GSM4495746 / Sample_extract_protocol_ch1: matched `scRNA` in "Cells were analyzed in three distinct scRNAseq experiments (scRNAseqMetrics_SupplementaryTable_Geo.docx). Libraries prepared with the FB5P-seq protocol were sequenced on Illumina NextSeq550 platform w"
- GSM4495747 / Sample_extract_protocol_ch1: matched `scRNA` in "First, CD154+ memory CD4 T cells were sorted on BD FACSAriaII, one cell per well, in 96-well plates containing specific lysis buffer at the CRTI, Nantes. Plates were immediately frozen for storage at "
- GSM4495747 / Sample_extract_protocol_ch1: matched `scRNA` in "For each plate, an Illumina sequencing library targeting the 5’-end of barcoded cDNA was prepared by a modified transposase-based method incorporating a plate-associated i7 barcode (Attaf et al., DOI:"
- GSM4495747 / Sample_extract_protocol_ch1: matched `scRNA` in "Cells were analyzed in three distinct scRNAseq experiments (scRNAseqMetrics_SupplementaryTable_Geo.docx). Libraries prepared with the FB5P-seq protocol were sequenced on Illumina NextSeq550 platform w"
- GSM4495748 / Sample_extract_protocol_ch1: matched `scRNA` in "First, CD154+ memory CD4 T cells were sorted on BD FACSAriaII, one cell per well, in 96-well plates containing specific lysis buffer at the CRTI, Nantes. Plates were immediately frozen for storage at "
- GSM4495748 / Sample_extract_protocol_ch1: matched `scRNA` in "For each plate, an Illumina sequencing library targeting the 5’-end of barcoded cDNA was prepared by a modified transposase-based method incorporating a plate-associated i7 barcode (Attaf et al., DOI:"
- GSM4495748 / Sample_extract_protocol_ch1: matched `scRNA` in "Cells were analyzed in three distinct scRNAseq experiments (scRNAseqMetrics_SupplementaryTable_Geo.docx). Libraries prepared with the FB5P-seq protocol were sequenced on Illumina NextSeq550 platform w"
- GSM4495749 / Sample_extract_protocol_ch1: matched `scRNA` in "First, CD154+ memory CD4 T cells were sorted on BD FACSAriaII, one cell per well, in 96-well plates containing specific lysis buffer at the CRTI, Nantes. Plates were immediately frozen for storage at "
- GSM4495749 / Sample_extract_protocol_ch1: matched `scRNA` in "For each plate, an Illumina sequencing library targeting the 5’-end of barcoded cDNA was prepared by a modified transposase-based method incorporating a plate-associated i7 barcode (Attaf et al., DOI:"
- GSM4495749 / Sample_extract_protocol_ch1: matched `scRNA` in "Cells were analyzed in three distinct scRNAseq experiments (scRNAseqMetrics_SupplementaryTable_Geo.docx). Libraries prepared with the FB5P-seq protocol were sequenced on Illumina NextSeq550 platform w"
- GSM4495750 / Sample_extract_protocol_ch1: matched `scRNA` in "First, CD154+ memory CD4 T cells were sorted on BD FACSAriaII, one cell per well, in 96-well plates containing specific lysis buffer at the CRTI, Nantes. Plates were immediately frozen for storage at "
- GSM4495750 / Sample_extract_protocol_ch1: matched `scRNA` in "For each plate, an Illumina sequencing library targeting the 5’-end of barcoded cDNA was prepared by a modified transposase-based method incorporating a plate-associated i7 barcode (Attaf et al., DOI:"
- GSM4495750 / Sample_extract_protocol_ch1: matched `scRNA` in "Cells were analyzed in three distinct scRNAseq experiments (scRNAseqMetrics_SupplementaryTable_Geo.docx). Libraries prepared with the FB5P-seq protocol were sequenced on Illumina NextSeq550 platform w"
- GSM4495751 / Sample_extract_protocol_ch1: matched `scRNA` in "First, CD154+ memory CD4 T cells were sorted on BD FACSAriaII, one cell per well, in 96-well plates containing specific lysis buffer at the CRTI, Nantes. Plates were immediately frozen for storage at "
- GSM4495751 / Sample_extract_protocol_ch1: matched `scRNA` in "For each plate, an Illumina sequencing library targeting the 5’-end of barcoded cDNA was prepared by a modified transposase-based method incorporating a plate-associated i7 barcode (Attaf et al., DOI:"
- GSM4495751 / Sample_extract_protocol_ch1: matched `scRNA` in "Cells were analyzed in three distinct scRNAseq experiments (scRNAseqMetrics_SupplementaryTable_Geo.docx). Libraries prepared with the FB5P-seq protocol were sequenced on Illumina NextSeq550 platform w"
- GSM4495738 / Sample_data_processing: matched `Drop-seq` in "To generate single-cell UMI count matrices, we used a custom bioinformatics pipeline as described (Attaf et al. 10.3389/fimmu.2020.00216), relying on Drop-seq-tools v1.12 running STAR v2.5.3a and HTSe"
- GSM4495738 / Sample_data_processing: matched `scRNA` in "Quality control was performed on each scRNA-seq batch independently to remove poor quality cells. Cells with less than 250 genes detected were removed. We further excluded cells with values below 3 me"
- GSM4495739 / Sample_data_processing: matched `Drop-seq` in "To generate single-cell UMI count matrices, we used a custom bioinformatics pipeline as described (Attaf et al. 10.3389/fimmu.2020.00216), relying on Drop-seq-tools v1.12 running STAR v2.5.3a and HTSe"
- GSM4495739 / Sample_data_processing: matched `scRNA` in "Quality control was performed on each scRNA-seq batch independently to remove poor quality cells. Cells with less than 250 genes detected were removed. We further excluded cells with values below 3 me"
- GSM4495740 / Sample_data_processing: matched `Drop-seq` in "To generate single-cell UMI count matrices, we used a custom bioinformatics pipeline as described (Attaf et al. 10.3389/fimmu.2020.00216), relying on Drop-seq-tools v1.12 running STAR v2.5.3a and HTSe"
- GSM4495740 / Sample_data_processing: matched `scRNA` in "Quality control was performed on each scRNA-seq batch independently to remove poor quality cells. Cells with less than 250 genes detected were removed. We further excluded cells with values below 3 me"
- GSM4495741 / Sample_data_processing: matched `Drop-seq` in "To generate single-cell UMI count matrices, we used a custom bioinformatics pipeline as described (Attaf et al. 10.3389/fimmu.2020.00216), relying on Drop-seq-tools v1.12 running STAR v2.5.3a and HTSe"
- GSM4495741 / Sample_data_processing: matched `scRNA` in "Quality control was performed on each scRNA-seq batch independently to remove poor quality cells. Cells with less than 250 genes detected were removed. We further excluded cells with values below 3 me"
- GSM4495742 / Sample_data_processing: matched `Drop-seq` in "To generate single-cell UMI count matrices, we used a custom bioinformatics pipeline as described (Attaf et al. 10.3389/fimmu.2020.00216), relying on Drop-seq-tools v1.12 running STAR v2.5.3a and HTSe"
- GSM4495742 / Sample_data_processing: matched `scRNA` in "Quality control was performed on each scRNA-seq batch independently to remove poor quality cells. Cells with less than 250 genes detected were removed. We further excluded cells with values below 3 me"
- GSM4495743 / Sample_data_processing: matched `Drop-seq` in "To generate single-cell UMI count matrices, we used a custom bioinformatics pipeline as described (Attaf et al. 10.3389/fimmu.2020.00216), relying on Drop-seq-tools v1.12 running STAR v2.5.3a and HTSe"
- GSM4495743 / Sample_data_processing: matched `scRNA` in "Quality control was performed on each scRNA-seq batch independently to remove poor quality cells. Cells with less than 250 genes detected were removed. We further excluded cells with values below 3 me"
- GSM4495744 / Sample_data_processing: matched `Drop-seq` in "To generate single-cell UMI count matrices, we used a custom bioinformatics pipeline as described (Attaf et al. 10.3389/fimmu.2020.00216), relying on Drop-seq-tools v1.12 running STAR v2.5.3a and HTSe"
- GSM4495744 / Sample_data_processing: matched `scRNA` in "Quality control was performed on each scRNA-seq batch independently to remove poor quality cells. Cells with less than 250 genes detected were removed. We further excluded cells with values below 3 me"
- GSM4495745 / Sample_data_processing: matched `Drop-seq` in "To generate single-cell UMI count matrices, we used a custom bioinformatics pipeline as described (Attaf et al. 10.3389/fimmu.2020.00216), relying on Drop-seq-tools v1.12 running STAR v2.5.3a and HTSe"
- GSM4495745 / Sample_data_processing: matched `scRNA` in "Quality control was performed on each scRNA-seq batch independently to remove poor quality cells. Cells with less than 250 genes detected were removed. We further excluded cells with values below 3 me"
- GSM4495746 / Sample_data_processing: matched `Drop-seq` in "To generate single-cell UMI count matrices, we used a custom bioinformatics pipeline as described (Attaf et al. 10.3389/fimmu.2020.00216), relying on Drop-seq-tools v1.12 running STAR v2.5.3a and HTSe"
- GSM4495746 / Sample_data_processing: matched `scRNA` in "Quality control was performed on each scRNA-seq batch independently to remove poor quality cells. Cells with less than 250 genes detected were removed. We further excluded cells with values below 3 me"
- GSM4495747 / Sample_data_processing: matched `Drop-seq` in "To generate single-cell UMI count matrices, we used a custom bioinformatics pipeline as described (Attaf et al. 10.3389/fimmu.2020.00216), relying on Drop-seq-tools v1.12 running STAR v2.5.3a and HTSe"
- GSM4495747 / Sample_data_processing: matched `scRNA` in "Quality control was performed on each scRNA-seq batch independently to remove poor quality cells. Cells with less than 250 genes detected were removed. We further excluded cells with values below 3 me"
- GSM4495748 / Sample_data_processing: matched `Drop-seq` in "To generate single-cell UMI count matrices, we used a custom bioinformatics pipeline as described (Attaf et al. 10.3389/fimmu.2020.00216), relying on Drop-seq-tools v1.12 running STAR v2.5.3a and HTSe"
- GSM4495748 / Sample_data_processing: matched `scRNA` in "Quality control was performed on each scRNA-seq batch independently to remove poor quality cells. Cells with less than 250 genes detected were removed. We further excluded cells with values below 3 me"
- GSM4495749 / Sample_data_processing: matched `Drop-seq` in "To generate single-cell UMI count matrices, we used a custom bioinformatics pipeline as described (Attaf et al. 10.3389/fimmu.2020.00216), relying on Drop-seq-tools v1.12 running STAR v2.5.3a and HTSe"
- GSM4495749 / Sample_data_processing: matched `scRNA` in "Quality control was performed on each scRNA-seq batch independently to remove poor quality cells. Cells with less than 250 genes detected were removed. We further excluded cells with values below 3 me"
- GSM4495750 / Sample_data_processing: matched `Drop-seq` in "To generate single-cell UMI count matrices, we used a custom bioinformatics pipeline as described (Attaf et al. 10.3389/fimmu.2020.00216), relying on Drop-seq-tools v1.12 running STAR v2.5.3a and HTSe"
- GSM4495750 / Sample_data_processing: matched `scRNA` in "Quality control was performed on each scRNA-seq batch independently to remove poor quality cells. Cells with less than 250 genes detected were removed. We further excluded cells with values below 3 me"
- GSM4495751 / Sample_data_processing: matched `Drop-seq` in "To generate single-cell UMI count matrices, we used a custom bioinformatics pipeline as described (Attaf et al. 10.3389/fimmu.2020.00216), relying on Drop-seq-tools v1.12 running STAR v2.5.3a and HTSe"
- GSM4495751 / Sample_data_processing: matched `scRNA` in "Quality control was performed on each scRNA-seq batch independently to remove poor quality cells. Cells with less than 250 genes detected were removed. We further excluded cells with values below 3 me"

Decision: REJECT

Reasons:
- single_cell_or_spatial: cell-resolved assay; not bulk transcriptomics (cell-resolved signal in sample metadata: Drop-seq, scRNA (14 sample(s)))
<!-- /computed -->