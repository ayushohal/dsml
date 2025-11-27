import pandas as pd

# Load dataset
df = pd.read_csv("winequality-red (3).csv")

# 1. Count unique values of each column
print("=== UNIQUE VALUES COUNT ===")
print(df.nunique(), "\n")

# 2. Format (data type) of each column
print("=== DATA TYPES OF COLUMNS ===")
print(df.dtypes, "\n")

# 3. Convert variable data types
# Example: convert 'quality' to float then back to int
df['quality_float'] = df['quality'].astype(float)
df['quality_int'] = df['quality_float'].astype(int)

print("=== DATA TYPES AFTER CONVERSION ===")
print(df[['quality', 'quality_float', 'quality_int']].dtypes, "\n")

# 4. Identify missing values
print("=== MISSING VALUES IN EACH COLUMN ===")
print(df.isnull().sum(), "\n")

# 5. Fill missing values (numeric columns → mean)
df_filled = df.fillna(df.mean(numeric_only=True))

print("=== FIRST 5 ROWS AFTER FILLING MISSING VALUES ===")
print(df_filled.head())