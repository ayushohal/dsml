import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

# Survival count by gender
sns.countplot(x='survived', hue='sex', data=df)
plt.title("Survival Based on Gender")
plt.show()

# Survival count by passenger class
sns.countplot(x='survived', hue="pclass",data=df)
plt.title("Survival Based on Passenger Class")
plt.show()

# Age distribution by survival
sns.boxplot(x='survived', y='age', data=df)
plt.title("Age Distribution vs Survival")
plt.show()

numeric_df = df.select_dtypes(include="number")
sns.heatmap(numeric_df.corr(), annot=True)
plt.show()
