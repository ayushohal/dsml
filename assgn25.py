import pandas as pd

# Load dataset
df = pd.read_csv("sample_data_with_outliers.csv")

# ------------ DATA CLEANING ------------

# Fill missing values for Age & Gender
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])

# Convert JoinDate
df["JoinDate"] = pd.to_datetime(df["JoinDate"], errors="coerce")

# ---- Fill Income with mean WITHOUT outliers ----

# Step 1: Calculate IQR
Q1 = df["Income"].quantile(0.25)
Q3 = df["Income"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Step 2: Select only non-outlier income values
clean_income = df[(df["Income"] >= lower) & (df["Income"] <= upper)]["Income"]

# Step 3: Calculate clean mean
clean_mean_income = clean_income.mean()

# Step 4: Fill missing income values with clean mean
df["Income"] = df["Income"].fillna(clean_mean_income)

# Optional: Cap remaining outliers (you wanted threshold filling)
df["Income"] = df["Income"].clip(lower, upper)

# ------------ DATA TRANSFORMATION ------------

df["Income_Lakhs"] = df["Income"] / 100000

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0, 25, 35, 50, 100],
    labels=["Youth", "Young Adult", "Middle Age", "Senior"]
)

df["ID"] = df["ID"].astype(str)

print(df.head())