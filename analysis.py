import pandas as pd
import requests

# API URL
url = "https://api.worldbank.org/v2/country/all/indicator/NE.CON.PRVT.CD?format=json&per_page=20000"

# Fetch data
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
response.raise_for_status()

data = response.json()

# Convert to DataFrame
records = pd.DataFrame(data[1])

# Select columns
df = records[["country", "countryiso3code", "date", "value"]].copy()

# Extract country name
df["country_name"] = df["country"].apply(
    lambda x: x["value"] if isinstance(x, dict) and "value" in x else None
)
# Rename
df = df.rename(columns={
    "countryiso3code": "country_code",
    "date": "year",
    "value": "consumption_usd"
})

# Clean
df = df.dropna(subset=["consumption_usd"])
df["year"] = df["year"].astype(int)

# Output
# Output
print(df[["country_name", "country_code", "year", "consumption_usd"]].head())
print(df.shape)

# Make numbers easier to read
pd.set_option("display.float_format", "{:,.0f}".format)

# Top 10 countries by consumption (latest year)
latest_year = df["year"].max()
latest_data = df[df["year"] == latest_year]

top10 = latest_data.sort_values(by="consumption_usd", ascending=False).head(10)

print("\nTop 10 countries by consumption:")
print(top10[["country_name", "consumption_usd"]])

# Global consumption trend over time
trend = df.groupby("year")["consumption_usd"].sum()

print("\nGlobal consumption over time:")
print(trend.tail(10))
# UK vs Global comparison
uk = df[df["country_code"] == "GBR"]

uk_trend = uk.groupby("year")["consumption_usd"].sum()

print("\nUK consumption over time:")
print(uk_trend.tail(10))

import matplotlib.pyplot as plt

# Plot global vs UK
plt.figure()

plt.plot(trend.index, trend.values, label="Global")
plt.plot(uk_trend.index, uk_trend.values, label="UK")

plt.yscale("log")  # ✅ THIS is the key line

plt.title("Consumption Over Time (Log Scale)")
plt.xlabel("Year")
plt.ylabel("Consumption (USD - log scale)")
plt.legend()

plt.show()
