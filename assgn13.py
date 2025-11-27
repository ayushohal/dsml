import pandas as pd

# Load dataset
df=pd.read_csv("Covid Vaccine Statewise.csv")

pd.set_option('display.width', 200)   # increase width
pd.set_option('display.max_columns', None)  # show all columns
pd.set_option('display.float_format', '{:.2f}'.format)

print("Columns:", df.columns.tolist())
print("=== Dataset Description ===")
print(df.describe(include="all"))

# -----------------------------
# Statewise First Dose
# -----------------------------
print("\n=== Statewise First Dose ===")
first = df.groupby("State/UTs")["Dose 1"].sum()
print(first)

# -----------------------------
# Statewise Second Dose
# -----------------------------
print("\n=== Statewise Second Dose ===")
second = df.groupby("State/UTs")["Dose 2"].sum()
print(second)