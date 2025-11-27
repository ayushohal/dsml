import pandas as pd

df = pd.read_csv("Covid Vaccine Statewise.csv")

# A. Describe dataset
print("=== Dataset Description ===")
print(df.describe(include='all'))

# B. Total males vaccinated
print("\n=== Total Males Vaccinated ===")
print(df["Male(Individuals Vaccinated)"].sum())

# C. Total females vaccinated
print("\n=== Total Females Vaccinated ===")
print(df["Female(Individuals Vaccinated)"].sum())