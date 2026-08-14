# Validation report: GSE180882

Transcriptome characterization of organoids derived from healthy and irreversibly damaged NASH patient liver

<!-- computed -->
Sample count: 45

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 45 samples |
| organism_consistency | PASS | Homo sapiens 45/45 |
| source_tissue | PASS | liver-pattern source 45/45 |
| library_strategy | PASS | RNA-Seq 45/45 |
| library_source | PASS | transcriptomic 45/45 |
| library_selection | PASS | cDNA 45/45 |
| instrument_model | PASS | Illumina NovaSeq 6000 45/45 |
| metadata_completeness | PASS | reported consistently: disease, sex; not reported anywhere: age, bmi, diagnosis, ethnicity, fibrosis_stage, group, nas_score, stage, steatosis_grade, tissue, treatment |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (24 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: organoid (39/45 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX11559697, https://www.ncbi.nlm.nih.gov/sra?term=SRX11559698, https://www.ncbi.nlm.nih.gov/sra?term=SRX11559699, https://www.ncbi.nlm.nih.gov/sra?term=SRX11559700, https://www.ncbi.nlm.nih.gov/sra?term=SRX11559701, and 40 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE180882_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX11559697, https://www.ncbi.nlm.nih.gov/sra?term=SRX11559698, https://www.ncbi.nlm.nih.gov/sra?term=SRX11559699, https://www.ncbi.nlm.nih.gov/sra?term=SRX11559700, https://www.ncbi.nlm.nih.gov/sra?term=SRX11559701, and 40 more (see sample_metadata.csv) |

## Canonical field distributions

- **disease**: alcoholic cirrhosis  human liver (3), cirrhotic NASH human liver (24), cystic fibropsis human liver (3), healthy human liver (15)
- **sex**: female (24), male (21)

## Field presence

- Sex: 45/45 (canon: sex)
- cell type: 45/45
- differentiation status: 45/45
- disease state: 45/45 (canon: disease)
- rna isolation method: 45/45

## Evidence for WARN/FAIL checks

### material_type (WARN)
- GSM5474274 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474274 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474275 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474275 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474276 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474276 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474277 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474277 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474278 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474278 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474279 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474279 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474280 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474280 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474281 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474281 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474282 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474282 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474283 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474283 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474284 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474284 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474285 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474285 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474286 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474286 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474287 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474287 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474288 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474288 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474289 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474289 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474290 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474290 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474291 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474291 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474292 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474292 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474293 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474293 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474294 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474294 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474295 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474295 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474296 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474296 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474297 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474297 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474298 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474298 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474299 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474299 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474300 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474300 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474301 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474301 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474302 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474302 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474303 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474303 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474304 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474304 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474305 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474305 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474306 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474306 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474307 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474307 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474308 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474308 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474309 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474309 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474310 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474310 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474311 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474311 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"
- GSM5474312 / Sample_characteristics_ch1: matched `organoid` in "cell type: hepatic organoids"
- GSM5474312 / Sample_characteristics_ch1: matched `organoid` in "differentiation status: 12d hepatic differentiation of biliary organoids"

Decision: MANUAL_REVIEW

Reasons:
- material_type: cell/culture terms in sample metadata: organoid (39/45 samples)
<!-- /computed -->