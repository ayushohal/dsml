import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("IRIS.csv")

numeric_cols = ['sepal_length','sepal_width','petal_length','petal_width']

# 1. Boxplots
df[numeric_cols].plot(kind='box', figsize=(8,6))
plt.title("Box Plot of Iris Features")
plt.show()

# 2. Identify outliers using IQR
print("\n=== Outlier Detection (IQR Method) ===")
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR

    outliers = df[(df[col] < lower) | (df[col] > upper)][col]
    print(f"{col} outliers:")
    print(outliers.values)
    print()