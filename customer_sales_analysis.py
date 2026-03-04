import pandas as pd

# Dataset: Online Retail (public sample hosted on GitHub)
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url, encoding="ISO-8859-1")

print("First 5 rows:")
print(df.head())

print("\nDataset info:")
print(df.info())

# Create a revenue column
df["Revenue"] = df["total_bill"]

# --- SQL-style analysis ---
# 1) Total revenue
total_revenue = df["Revenue"].sum()
print("\nTotal Revenue:", round(total_revenue, 2))

# 2) Top 10 customers by revenue
top_customers = (
    df.groupby("sex")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Customers by Revenue:")
print(top_customers)

# 3) Top 10 products by revenue
top_products = (
    df.groupby("day")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products by Revenue:")
print(top_products)

# 4) Revenue by country (Top 10)
top_countries = (
    df.groupby("time")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Countries by Revenue:")
print(top_countries)

import matplotlib.pyplot as plt

# Revenue by day chart
revenue_by_day = df.groupby("day")["Revenue"].sum()

plt.bar(revenue_by_day.index, revenue_by_day.values)
plt.title("Total Revenue by Day")
plt.xlabel("Day")
plt.ylabel("Revenue")
plt.show()