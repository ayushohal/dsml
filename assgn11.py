import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris dataset
df=pd.read_csv("IRIS.csv")

# 1. LIST FEATURES AND THEIR TYPES
print("=== Feature Types in Iris Dataset ===")
for col in df.columns:
    if df[col].dtype in ['float64', 'int64']:
        print(f"{col}  --> Numeric")
    else:
        print(f"{col}  --> Nominal")

# 2. HISTOGRAMS FOR EACH FEATURE
df.iloc[:, :4].hist(figsize=(10, 8), bins=15)
plt.suptitle("Histograms of All Numerical Features in Iris Dataset", fontsize=14)
plt.show()