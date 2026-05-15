Data provenance and notes

- File: [data_csv/SPARCS_asthma_hospitalizations_by_zip3_2010-2024.csv](data_csv/SPARCS_asthma_hospitalizations_by_zip3_2010-2024.csv)

- Description: aggregated SPARCS counts of asthma hospitalizations for children by ZIP3 from 2010–2024. Columns include year, zip3, count, and any demographic or age stratifiers extracted for analysis.

- Original sources: New York State SPARCS (hospitalization records) and NYCCAS / local air-quality monitoring for pollutant exposure data.

- Privacy: This dataset is aggregated to 3-digit ZIP level to protect individual privacy. Do not attempt to re-identify individuals.

- Reproducibility: `sparcs_aggregation.ipynb` and `sparcs_fetch_columns.ipynb` contain the code used to produce the aggregated CSV from raw SPARCS extracts. If you need the raw SPARCS files, consult the NY State SPARCS data portal and follow their terms of use.

