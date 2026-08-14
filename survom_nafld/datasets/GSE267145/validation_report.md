# Validation report: GSE267145

The transcription factor ZNF469 regulates collagen production in liver fibrosis

<!-- computed -->
Sample count: 508

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 508 samples |
| organism_consistency | WARN | mixed organisms: Homo sapiens 448/508, Mus musculus 60/508 |
| source_tissue | WARN | liver-pattern source 432/508 |
| library_strategy | WARN | mixed strategies: Hi-C 2/508, OTHER 120/508, RNA-Seq 386/508 |
| library_source | WARN | library_source: genomic 122/508, transcriptomic 386/508 |
| library_selection | WARN | mixed library_selection: cDNA 386/508, other 122/508 |
| instrument_model | PASS | Illumina NovaSeq 6000 508/508 |
| metadata_completeness | WARN | patchy fields: sex 99/508, stage 99/508, steatosis_grade 99/508, tissue 432/508, treatment 71/508. not reported anywhere: age, bmi, diagnosis, disease, ethnicity, fibrosis_stage, group, nas_score |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (99 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: cell line (87/508 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX24462696, https://www.ncbi.nlm.nih.gov/sra?term=SRX24462697, https://www.ncbi.nlm.nih.gov/sra?term=SRX24488324, https://www.ncbi.nlm.nih.gov/sra?term=SRX24488325, https://www.ncbi.nlm.nih.gov/sra?term=SRX24488326, and 503 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE267145-GPL24247_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX24462696, https://www.ncbi.nlm.nih.gov/sra?term=SRX24462697, https://www.ncbi.nlm.nih.gov/sra?term=SRX24488324, https://www.ncbi.nlm.nih.gov/sra?term=SRX24488325, https://www.ncbi.nlm.nih.gov/sra?term=SRX24488326, and 503 more (see sample_metadata.csv) |

## Canonical field distributions

- **sex**: F (85), M (14)
- **stage**: NAFL (28), NASH_F0 (19), NASH_F1 (15), NASH_F23 (13), NOR (24)
- **steatosis_grade**: 0 (24), 1 (43), 2 (19), 3 (13)
- **tissue**: Liver (421), liver (11)
- **treatment**: HSC electroporated with a pooled set of guide RNAs targeting ZNF469 gene (3), HSC electroporoated with non-targeting gRNA (3), control diet (24), high fat diet (12), methionine-choline deficient diet (12), no treatment (3), resting (2), standard chow diet (6), standard chow diet along with addition of 0.165% DL Ethionine (6)

## Field presence

- Sex: 99/508 (canon: sex)
- Stage: 99/508 (canon: stage)
- balloning: 99/508
- cell line: 87/508
- cell type: 2/508
- chip antibody: 120/508
- fibrosis nas_tidy: 99/508
- genotype: 2/508
- lobular inflammation: 99/508
- lobular necrosis: 99/508
- steatosis: 99/508 (canon: steatosis_grade)
- tissue: 432/508 (canon: tissue)
- treatment: 71/508 (canon: treatment)

## Evidence for WARN/FAIL checks

### organism_consistency (WARN)
### source_tissue (WARN)
### library_strategy (WARN)
### library_source (WARN)
### library_selection (WARN)
### metadata_completeness (WARN)
### material_type (WARN)
- GSM8253036 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8253037 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257189 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257190 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257191 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257192 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257193 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257194 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257195 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257196 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257197 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257198 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257199 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257200 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257201 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257202 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257203 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257204 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257205 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257206 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257207 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257208 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257209 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257210 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257211 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257212 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257213 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257214 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257215 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257216 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257217 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257218 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257219 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257220 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257221 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257222 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257223 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8257224 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8260313 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8260314 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8260315 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8260316 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8260317 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8260318 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8260319 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8260320 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8260321 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8260322 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8260323 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8260324 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8260325 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8260326 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8260327 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8260328 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX2"
- GSM8260329 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX2"
- GSM8260330 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX2"
- GSM8260331 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX2"
- GSM8260332 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX2"
- GSM8260333 / Sample_characteristics_ch1: matched `cell line` in "cell line: LX2"
- GSM8748885 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748886 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748887 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748888 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748889 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748890 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748891 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748892 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748893 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748894 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748895 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748896 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748897 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748898 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748899 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748900 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748901 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748902 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748903 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748904 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748905 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748906 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748907 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748908 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748909 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748910 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748911 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"
- GSM8748912 / Sample_characteristics_ch1: matched `cell line` in "cell line: HSC"

Decision: MANUAL_REVIEW

Reasons:
- organism_consistency: mixed organisms: Homo sapiens 448/508, Mus musculus 60/508
- source_tissue: liver-pattern source 432/508
- library_strategy: mixed strategies: Hi-C 2/508, OTHER 120/508, RNA-Seq 386/508
- library_source: library_source: genomic 122/508, transcriptomic 386/508
- library_selection: mixed library_selection: cDNA 386/508, other 122/508
- metadata_completeness: patchy fields: sex 99/508, stage 99/508, steatosis_grade 99/508, tissue 432/508, treatment 71/508. not reported anywhere: age, bmi, diagnosis, disease, ethnicity, fibrosis_stage, group, nas_score
- material_type: cell/culture terms in sample metadata: cell line (87/508 samples)
<!-- /computed -->