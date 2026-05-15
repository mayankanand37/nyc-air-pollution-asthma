Colab support notes

- Open any notebook from this repo in Colab by replacing `GITHUB_USER/REPO` in the URL:

```
https://colab.research.google.com/github/mayankanand3007/nyc-air-pollution-asthma/blob/main/path/to/notebook.ipynb
```

- Quick steps inside Colab:
  1. Install pip requirements from the repo:

```python
!pip install -r https://raw.githubusercontent.com/mayankanand3007/nyc-air-pollution-asthma/main/colab/colab_requirements.txt
```

  2. Mount Google Drive (optional) to persist outputs:

```python
from google.colab import drive
drive.mount('/content/drive')
```

  3. Download data directly from the repository (if present):

```bash
!wget https://raw.githubusercontent.com/mayankanand3007/nyc-air-pollution-asthma/main/data_csv/SPARCS_asthma_hospitalizations_by_zip3_2010-2024.csv
```

- Notes:
  - Some geospatial packages (e.g., `geopandas`, `rasterio`) may require system libraries. If installation fails, try installing a lightweight subset (pandas, numpy, matplotlib, seaborn) or use a hosted runtime that supports conda.
  - Replace `GITHUB_USER/REPO` with your GitHub username and repository name (or use the provided `mayankanand3007/nyc-air-pollution-asthma` example).
