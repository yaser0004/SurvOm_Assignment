# Validation report: GSE261297

The fatty liver disease-causing protein PNPLA3-I148M alters lipid droplet-Golgi dynamics

<!-- computed -->
Sample count: 60

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 60 samples |
| organism_consistency | PASS | Homo sapiens 60/60 |
| source_tissue | PASS | liver-pattern source 60/60 |
| library_strategy | PASS | RNA-Seq 60/60 |
| library_source | PASS | transcriptomic 60/60 |
| library_selection | PASS | cDNA 60/60 |
| instrument_model | PASS | Illumina HiSeq 2500 60/60 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | WARN | disease term found only in series-level text, not corroborated by sample metadata |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (60/60 samples) |
| expression_data_availability | PASS | processed series-level file: GSE261297_primary_count_gene.Counts.Table.txt.gz |
| series_matrix | INFO | present, metadata-only (GSE261297_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX23898157, https://www.ncbi.nlm.nih.gov/sra?term=SRX23898158, https://www.ncbi.nlm.nih.gov/sra?term=SRX23898159, https://www.ncbi.nlm.nih.gov/sra?term=SRX23898160, https://www.ncbi.nlm.nih.gov/sra?term=SRX23898161, and 55 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Human liver cancer cell line (60)
- **treatment**: oleic acid,0.5h (10), oleic acid,1h (10), oleic acid,24h (10), oleic acid,2h (10), oleic acid,4h (10), untreated (10)

## Field presence

- cell line: 60/60
- cell type: 60/60
- genotype: 60/60
- tissue: 60/60 (canon: tissue)
- treatment: 60/60 (canon: treatment)

## Evidence for WARN/FAIL checks

### metadata_completeness (WARN)
### disease_relevance (WARN)
- GSE261297 / Series_title: matched `fatty liver` in "The fatty liver disease-causing protein PNPLA3-I148M alters lipid droplet-Golgi dynamics"
- GSE261297 / Series_summary: matched `Non-alcoholic fatty liver` in "Non-alcoholic fatty liver disease (NAFLD), recently renamed metabolic dysfunction-associated steatotic liver disease (MASLD), is a progressive metabolic disorder that begins with aberrant triglyceride"
### material_type (WARN)
- GSM8139622 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139623 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139624 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139625 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139626 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139627 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139628 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139629 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139630 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139631 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139632 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139633 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139634 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139635 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139636 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139637 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139638 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139639 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139640 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139641 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139642 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139643 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139644 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139645 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139646 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139647 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139648 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139649 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139650 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139651 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139652 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139653 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139654 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139655 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139656 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139657 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139658 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139659 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139660 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139661 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139662 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139663 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139664 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139665 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139666 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139667 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139668 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139669 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139670 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139671 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139672 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139673 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139674 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139675 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139676 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139677 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139678 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139679 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139680 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139681 / Sample_source_name_ch1: matched `cell line` in "Human liver cancer cell line"
- GSM8139622 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139622 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139623 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139623 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139624 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139624 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139625 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139625 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139626 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139626 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139627 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139627 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139628 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139628 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139629 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139629 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139630 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139630 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139631 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139631 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139632 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139632 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139633 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139633 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139634 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139634 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139635 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139635 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139636 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139636 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139637 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139637 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139638 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139638 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139639 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139639 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139640 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139640 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139641 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139641 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139642 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139642 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139643 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139643 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139644 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139644 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139645 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139645 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139646 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139646 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139647 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139647 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139648 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139648 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139649 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139649 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139650 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139650 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139651 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139651 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139652 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139652 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139653 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139653 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139654 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139654 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139655 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139655 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139656 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139656 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139657 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139657 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139658 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139658 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139659 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139659 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139660 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139660 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139661 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139661 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139662 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139662 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139663 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139663 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139664 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139664 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139665 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139665 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139666 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139666 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139667 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139667 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139668 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139668 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139669 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139669 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139670 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139670 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139671 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139671 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139672 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139672 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139673 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139673 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139674 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139674 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139675 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139675 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139676 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139676 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139677 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139677 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139678 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139678 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139679 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139679 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139680 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139680 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"
- GSM8139681 / Sample_characteristics_ch1: matched `cell line` in "tissue: Human liver cancer cell line"
- GSM8139681 / Sample_characteristics_ch1: matched `cell line` in "cell line: Hep3B217"

Decision: MANUAL_REVIEW

Reasons:
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- disease_relevance: disease term found only in series-level text, not corroborated by sample metadata
- material_type: cell/culture terms in sample metadata: cell line (60/60 samples)
<!-- /computed -->