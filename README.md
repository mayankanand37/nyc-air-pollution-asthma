# NYC Air Pollution & Childhood Asthma — Showcase

This repository contains notebooks and data used to analyze links between NYC air pollution (NYCCAS/NYC sensors) and childhood asthma hospitalizations.

Overview
- **Notebooks:**
  - [acs_yearly_data.ipynb](acs_yearly_data.ipynb)
  - [asthma_incidence.ipynb](asthma_incidence.ipynb)
  - [download_NYCCAS.ipynb](download_NYCCAS.ipynb)
  - [nyccas_analytics.ipynb](nyccas_analytics.ipynb)
  - [poverty_income.ipynb](poverty_income.ipynb)
  - [sparcs_aggregation.ipynb](sparcs_aggregation.ipynb)
  - [sparcs_fetch_columns.ipynb](sparcs_fetch_columns.ipynb)

Open notebooks in Google Colab

- Click any badge to open the corresponding notebook in Colab. Replace `GITHUB_USER/REPO` with your GitHub username and repository name.

- acs_yearly_data.ipynb:  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mayankanand3007/nyc-air-pollution-asthma/blob/main/acs_yearly_data.ipynb)

- asthma_incidence.ipynb:  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mayankanand3007/nyc-air-pollution-asthma/blob/main/asthma_incidence.ipynb)

- download_NYCCAS.ipynb:  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mayankanand3007/nyc-air-pollution-asthma/blob/main/download_NYCCAS.ipynb)

- nyccas_analytics.ipynb:  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mayankanand3007/nyc-air-pollution-asthma/blob/main/nyccas_analytics.ipynb)

- poverty_income.ipynb:  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mayankanand3007/nyc-air-pollution-asthma/blob/main/poverty_income.ipynb)

- sparcs_aggregation.ipynb:  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mayankanand3007/nyc-air-pollution-asthma/blob/main/sparcs_aggregation.ipynb)

- sparcs_fetch_columns.ipynb:  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mayankanand3007/nyc-air-pollution-asthma/blob/main/sparcs_fetch_columns.ipynb)

- **Data:** see [data_csv/SPARCS_asthma_hospitalizations_by_zip3_2010-2024.csv](data_csv/SPARCS_asthma_hospitalizations_by_zip3_2010-2024.csv)

Reproducibility
- Using conda (recommended):

```bash
conda env create -f environment.yml
conda activate nyc-asthma
jupyter lab
```

- Using pip/venv:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

Run on Colab
- Use the following template to open a notebook in Google Colab (replace `GITHUB_USER` and `REPO`):

```
https://colab.research.google.com/github/mayankanand3007/nyc-air-pollution-asthma/blob/main/path/to/notebook.ipynb
```

- Quick Colab setup (in a Colab cell):

```python
!pip install -r https://raw.githubusercontent.com/mayankanand3007/nyc-air-pollution-asthma/main/colab/colab_requirements.txt
from google.colab import drive
drive.mount('/content/drive')
```

- If you host the data in the repository, download raw CSVs using the raw GitHub URL (example):

```bash
wget https://raw.githubusercontent.com/mayankanand3007/nyc-air-pollution-asthma/main/data_csv/SPARCS_asthma_hospitalizations_by_zip3_2010-2024.csv
```

- See `colab/README.md` for notes and troubleshooting (geospatial packages may require extra system libraries on Colab).

How to cite
- If you use this repository in research, please cite the repository and include a statement referencing the original data sources (SPARCS, NYCCAS) used in the analysis.

Notes for reviewers
- Each notebook is self-contained and includes narrative, code, and figures suitable for a reproducible methods appendix.
- Consider running notebooks interactively or converting to HTML/PDF for inclusion in appendices.

Contact
- Repository owner: Mayank Anand (local workspace user)

