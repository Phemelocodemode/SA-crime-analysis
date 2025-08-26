import pandas as pd
import matplotlib.pyplot as plt

crime = pd.read_csv("SouthAfricaCrimeStats_v2.csv")
pop = pd.read_csv("ProvincePopulation.csv")

pop.rename(columns={pop.columns[0]:'Province', pop.columns[1]:'Population'}, inplace=True)
pop['Province'] = pop['Province'].str.strip()

year_cols = [c for c in crime.columns if "-" in str(c)]
year_cols_sorted = sorted(year_cols, key=lambda x: int(x.split("-")[0]))
latest_year = year_cols_sorted[-1]

province_totals = crime.groupby("Province")[latest_year].sum().reset_index()
province_totals.to_csv("outputs/province_totals_2015-2016.csv", index=False)

merged = province_totals.merge(pop, on="Province", how="left")
merged["Crime Rate per 100k"] = merged[latest_year] / merged["Population"] * 100000
merged.to_csv("outputs/province_per_capita_2015-2016.csv", index=False)

top10 = crime.groupby("Category")[latest_year].sum().reset_index().sort_values(latest_year, ascending=False).head(10)
top10.to_csv("outputs/top10_categories_2015-2016.csv", index=False)

plt.figure(figsize=(10,6))
plt.bar(province_totals["Province"], province_totals[latest_year])
plt.title("Total Crimes by Province (2015-2016)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("figures/total_crimes_by_province_2015-2016.png")
plt.close()

plt.figure(figsize=(10,6))
plt.bar(merged["Province"], merged["Crime Rate per 100k"])
plt.title("Crime Rate per 100k Population (2015-2016)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("figures/crime_rate_per_100k_2015-2016.png")
plt.close()

plt.figure(figsize=(10,6))
plt.bar(top10["Category"], top10[latest_year])
plt.title("Top 10 Crime Categories (2015-2016)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("figures/top10_categories_2015-2016.png")
plt.close()
