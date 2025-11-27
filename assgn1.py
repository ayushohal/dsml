import pandas as pd
df = pd.read_csv("titanic.csv")

print(df.head())
print(df[['survived', 'age']])

print(df.sort_values(by="age"))

print(df.describe())
print("\n",df.dtypes)