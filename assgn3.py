import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("HousePrice.csv")

print(df.std(numeric_only=True))
print(df.var(numeric_only=True))
print(df.describe(percentiles=[0.25, 0.5, 0.75]))

df.hist(figsize=(12,12))
plt.show()