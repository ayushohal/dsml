import pandas as pd

# Load dataset
df = pd.read_csv("Covid Vaccine Statewise.csv")

# Clean column names (remove extra spaces)
df.columns = df.columns.str.strip()


print("Columns:", df.columns.tolist())
print("=== Dataset Description ===")
print(df.describe(include="all"))

# -----------------------------
# Statewise First Dose
# -----------------------------
print("\n=== Statewise First Dose ===")
first = df.groupby("State")["First Dose Administered"].sum()
print(first)

# -----------------------------
# Statewise Second Dose
# -----------------------------
print("\n=== Statewise Second Dose ===")
second = df.groupby("State")["Second Dose Administered"].sum()
print(second)
