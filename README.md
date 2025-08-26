# South Africa Crime Analysis (2015-2016)

This project analyzes South African crime statistics by province and category, and normalizes by population to compute per-capita rates.

## What I did
- Loaded raw SAPS crime statistics (CSV) and a province population table.
- Aggregated **total incidents by province** for **2015-2016**.
- Calculated **crime rates per 100k residents** using province populations.
- Identified the **Top 10 crime categories** nationally.
- Produced three charts and exported clean CSVs for recruiters to quickly review.

## Files
- `SouthAfricaCrimeStats_v2.csv` — raw crime dataset (from Kaggle).
- `ProvincePopulation.csv` — province population reference.
- `analyze_sa_crime.py` — one-click script to reproduce outputs.
- `province_totals_2015-2016.csv` — total incidents by province.
- `province_per_capita_2015-2016.csv` — incidents and rate per 100k by province.
- `top10_categories_2015-2016.csv` — top crime categories (national).
- `total_crimes_by_province_2015-2016.png` — bar chart.
- `crime_rate_per_100k_2015-2016.png` — bar chart.
- `top10_categories_2015-2016.png` — horizontal bar chart.

## How to run locally
1. Place `SouthAfricaCrimeStats_v2.csv` and `ProvincePopulation.csv` in the project root.
2. Run:
   ```bash
   python analyze_sa_crime.py
   ```
3. Outputs will appear in `sa-crime-analysis-output/`.


  ## Visualizations

### Total Crimes by Province (2015–2016)
![Total Crimes by Province](figures/total_crimes_by_province_2015-2016.png)

### Crime Rate per 100k Population
![Crime Rate per 100k](figures/crime_rate_per_100k_2015-2016.png)

### Top 10 Crime Categories
![Top 10 Categories](figures/top10_categories_2015-2016.png)

## Notes
- The latest available year in this dataset is **2015-2016**.
- Population is a single snapshot, so per-capita rates are indicative rather than exact for that year.


![Total Crimes](total_crimes_by_province_2015-2016.png)


