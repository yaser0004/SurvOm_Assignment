# Validation report: GSE324401

Evaluation of the immortalized primary human hepatocyte cell line Fa2N-4 as a model for MASLD

<!-- computed -->
Sample count: 48

## Checks

| id | status | observed |
|---|---|---|
| sample_count | PASS | 48 samples |
| organism_consistency | PASS | Homo sapiens 48/48 |
| source_tissue | PASS | liver-pattern source 48/48 |
| library_strategy | PASS | RNA-Seq 48/48 |
| library_source | PASS | transcriptomic 48/48 |
| library_selection | PASS | cDNA 48/48 |
| instrument_model | PASS | Illumina NovaSeq 6000 48/48 |
| metadata_completeness | WARN | no disease/diagnosis/group/stage-type canonical field reported anywhere |
| disease_relevance | PASS | disease/fibrosis terms found in sample metadata (8 sample(s)) |
| single_cell_or_spatial | PASS | no single-cell/spatial signal detected |
| material_type | WARN | cell/culture terms in sample metadata: HepG2, cell line (48/48 samples) |
| expression_data_availability | INFO | raw sequencing only (https://www.ncbi.nlm.nih.gov/sra?term=SRX32438565, https://www.ncbi.nlm.nih.gov/sra?term=SRX32438566, https://www.ncbi.nlm.nih.gov/sra?term=SRX32438567, https://www.ncbi.nlm.nih.gov/sra?term=SRX32438568, https://www.ncbi.nlm.nih.gov/sra?term=SRX32438569, and 43 more (see sample_metadata.csv)) |
| series_matrix | INFO | present, metadata-only (GSE324401_series_matrix.txt.gz); samples are SRA-type with zero data rows |
| raw_sra_availability | INFO | SRA/BioProject links recorded, not downloaded: https://www.ncbi.nlm.nih.gov/sra?term=SRX32438565, https://www.ncbi.nlm.nih.gov/sra?term=SRX32438566, https://www.ncbi.nlm.nih.gov/sra?term=SRX32438567, https://www.ncbi.nlm.nih.gov/sra?term=SRX32438568, https://www.ncbi.nlm.nih.gov/sra?term=SRX32438569, and 43 more (see sample_metadata.csv) |

## Canonical field distributions

- **tissue**: Liver (48)
- **treatment**: MASLD (600 uM FFA) 1 (2), MASLD (600 uM FFA) 2 (2), MASLD (600 uM FFA) 3 (2), MASLD (600 uM FFA) 4 (2), Negative ctrl (BSA) 1 (2), Negative ctrl (BSA) 2 (2), Negative ctrl (BSA) 3 (2), Negative ctrl (BSA) 4 (2), SEQ Resmetirom 1 (2), SEQ Resmetirom 2 (2), SEQ Resmetirom 3 (2), SEQ Resmetirom 4 (2), SEQ Vehicle Resmetirom 1 (2), SEQ Vehicle Resmetirom 2 (2), SEQ Vehicle Resmetirom 3 (2), SEQ Vehicle Resmetirom 4 (2), SIM Resmetirom 1 (2), SIM Resmetirom 2 (2), SIM Resmetirom 3 (2), SIM Resmetirom 4 (2), SIM Vehicle Resmetirom 1 (2), SIM Vehicle Resmetirom 2 (2), SIM Vehicle Resmetirom 3 (2), SIM Vehicle Resmetirom 4 (2)

## Field presence

- batch: 48/48
- cell line: 48/48
- cell type: 48/48
- genotype: 48/48
- tissue: 48/48 (canon: tissue)
- treatment: 48/48 (canon: treatment)

## Evidence for WARN/FAIL checks

### metadata_completeness (WARN)
### material_type (WARN)
- GSM9575137 / Sample_title: matched `HepG2` in "HepG2_NT_1"
- GSM9575138 / Sample_title: matched `HepG2` in "HepG2_NT_2"
- GSM9575139 / Sample_title: matched `HepG2` in "HepG2_NT_3"
- GSM9575140 / Sample_title: matched `HepG2` in "HepG2_NT_4"
- GSM9575141 / Sample_title: matched `HepG2` in "HepG2_MASLD_1"
- GSM9575142 / Sample_title: matched `HepG2` in "HepG2_MASLD_2"
- GSM9575143 / Sample_title: matched `HepG2` in "HepG2_MASLD_3"
- GSM9575144 / Sample_title: matched `HepG2` in "HepG2_MASLD_4"
- GSM9575145 / Sample_title: matched `HepG2` in "HepG2_SIM_Veh_RSM1"
- GSM9575146 / Sample_title: matched `HepG2` in "HepG2_SIM_Veh_RSM2"
- GSM9575147 / Sample_title: matched `HepG2` in "HepG2_SIM_Veh_RSM3"
- GSM9575148 / Sample_title: matched `HepG2` in "HepG2_SIM_Veh_RSM4"
- GSM9575149 / Sample_title: matched `HepG2` in "HepG2_SIM_RSM1"
- GSM9575150 / Sample_title: matched `HepG2` in "HepG2_SIM_RSM2"
- GSM9575151 / Sample_title: matched `HepG2` in "HepG2_SIM_RSM3"
- GSM9575152 / Sample_title: matched `HepG2` in "HepG2_SIM_RSM4"
- GSM9575153 / Sample_title: matched `HepG2` in "HepG2_SEQ_Veh_RSM1"
- GSM9575154 / Sample_title: matched `HepG2` in "HepG2_SEQ_Veh_RSM2"
- GSM9575155 / Sample_title: matched `HepG2` in "HepG2_SEQ_Veh_RSM3"
- GSM9575156 / Sample_title: matched `HepG2` in "HepG2_SEQ_Veh_RSM4"
- GSM9575157 / Sample_title: matched `HepG2` in "HepG2_SEQ_RSM1"
- GSM9575158 / Sample_title: matched `HepG2` in "HepG2_SEQ_RSM2"
- GSM9575159 / Sample_title: matched `HepG2` in "HepG2_SEQ_RSM3"
- GSM9575160 / Sample_title: matched `HepG2` in "HepG2_SEQ_RSM4"
- GSM9575137 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9575138 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9575139 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9575140 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9575141 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9575142 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9575143 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9575144 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9575145 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9575146 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9575147 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9575148 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9575149 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9575150 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9575151 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9575152 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9575153 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9575154 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9575155 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9575156 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9575157 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9575158 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9575159 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9575160 / Sample_characteristics_ch1: matched `cell line` in "cell line: HepG2"
- GSM9575161 / Sample_characteristics_ch1: matched `cell line` in "cell line: Fa2N-4"
- GSM9575162 / Sample_characteristics_ch1: matched `cell line` in "cell line: Fa2N-4"
- GSM9575163 / Sample_characteristics_ch1: matched `cell line` in "cell line: Fa2N-4"
- GSM9575164 / Sample_characteristics_ch1: matched `cell line` in "cell line: Fa2N-4"
- GSM9575165 / Sample_characteristics_ch1: matched `cell line` in "cell line: Fa2N-4"
- GSM9575166 / Sample_characteristics_ch1: matched `cell line` in "cell line: Fa2N-4"
- GSM9575167 / Sample_characteristics_ch1: matched `cell line` in "cell line: Fa2N-4"
- GSM9575168 / Sample_characteristics_ch1: matched `cell line` in "cell line: Fa2N-4"
- GSM9575169 / Sample_characteristics_ch1: matched `cell line` in "cell line: Fa2N-4"
- GSM9575170 / Sample_characteristics_ch1: matched `cell line` in "cell line: Fa2N-4"
- GSM9575171 / Sample_characteristics_ch1: matched `cell line` in "cell line: Fa2N-4"
- GSM9575172 / Sample_characteristics_ch1: matched `cell line` in "cell line: Fa2N-4"
- GSM9575173 / Sample_characteristics_ch1: matched `cell line` in "cell line: Fa2N-4"
- GSM9575174 / Sample_characteristics_ch1: matched `cell line` in "cell line: Fa2N-4"
- GSM9575175 / Sample_characteristics_ch1: matched `cell line` in "cell line: Fa2N-4"
- GSM9575176 / Sample_characteristics_ch1: matched `cell line` in "cell line: Fa2N-4"
- GSM9575177 / Sample_characteristics_ch1: matched `cell line` in "cell line: Fa2N-4"
- GSM9575178 / Sample_characteristics_ch1: matched `cell line` in "cell line: Fa2N-4"
- GSM9575179 / Sample_characteristics_ch1: matched `cell line` in "cell line: Fa2N-4"
- GSM9575180 / Sample_characteristics_ch1: matched `cell line` in "cell line: Fa2N-4"
- GSM9575181 / Sample_characteristics_ch1: matched `cell line` in "cell line: Fa2N-4"
- GSM9575182 / Sample_characteristics_ch1: matched `cell line` in "cell line: Fa2N-4"
- GSM9575183 / Sample_characteristics_ch1: matched `cell line` in "cell line: Fa2N-4"
- GSM9575184 / Sample_characteristics_ch1: matched `cell line` in "cell line: Fa2N-4"

Decision: MANUAL_REVIEW

Reasons:
- metadata_completeness: no disease/diagnosis/group/stage-type canonical field reported anywhere
- material_type: cell/culture terms in sample metadata: HepG2, cell line (48/48 samples)
<!-- /computed -->