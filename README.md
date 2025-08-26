# South Africa Crime Analysis (2015–2016)

An analysis of South African crime statistics by province and category, normalized by population to compute per-capita rates.

## Highlights

* Processed raw **SAPS crime statistics** and province population data.
* Aggregated **total incidents by province** for 2015–2016.
* Calculated **crime rates per 100k residents**.
* Identified the **Top 10 national crime categories**.
* Exported clean CSVs and visualizations for quick insights.

## Repository Contents

* `SouthAfricaCrimeStats_v2.csv` — raw dataset (Kaggle).
* `ProvincePopulation.csv` — reference population data.
* `analyze_sa_crime.py` — script to reproduce analysis.
* `province_totals_2015-2016.csv` — incidents by province.
* `province_per_capita_2015-2016.csv` — incidents + rate per 100k.
* `top10_categories_2015-2016.csv` — national top crime categories.
* Charts:

  * `total_crimes_by_province_2015-2016.jpg`
  * `crime_rate_per_100k_2015-2016.jpg`
  * `top10_categories_2015-2016.jpg`

## Running Locally

1. Place `SouthAfricaCrimeStats_v2.csv` and `ProvincePopulation.csv` in the project root.
2. Run the script:

   ```bash
   python analyze_sa_crime.py
   ```
3. Outputs will be generated in `sa-crime-analysis-output/`.

## Visualizations

### Total Crimes by Province (2015–2016)

![Total Crimes by Province](figures/total_crimes_by_province_2015-2016.jpg)

### Crime Rate per 100k Population

![Crime Rate per 100k](figures/crime_rate_per_100k_2015-2016.jpg)

### Top 10 Crime Categories

![Top 10 Categories](figures/top10_categories_2015-2016.jpg)

## Notes

* Dataset covers **2015–2016**, the latest available year.
* Population is a single snapshot, so per-capita rates are approximate.

