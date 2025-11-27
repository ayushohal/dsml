import pandas as pd

df = pd.read_csv("telecom_churn.csv")
df['churn'] = df['churn'].astype(int)

print(df.dtypes)
print("Minimum : \n",df.min())
print("Maximum : \n",df.max())
print("Mean : \n",df.mean(numeric_only=True))
print("Range : \n", df.max(numeric_only=True) - df.min(numeric_only=True))
print("Standard Dev : \n",df.std(numeric_only=True))
print("Variance : \n",df.var(numeric_only=True))
print("Percentile : \n",df.describe(percentiles=[0.25, 0.5, 0.75]))