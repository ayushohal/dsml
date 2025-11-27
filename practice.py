import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns
from numpy.ma.extras import unique

df=pd.read_csv("sample_data_with_outliers.csv")

df["Age"]=df["Age"].fillna(df["Age"].median())
df["JoinDate"]=pd.to_datetime(df["JoinDate"], errors="coerce")

Q1=df["Income"].quantile(0.25)
Q3=df["Income"].quantile(0.75)
IQR=Q3-Q1
lower=Q1-1.5*IQR
upper=Q3+1.5*IQR

income_without_outliers=df[(df["Income"] >= lower) & (df["Income"] <= upper)]["Income"]
clean_mean=income_without_outliers.mean()

df["Income"]=df["Income"].fillna(clean_mean)


df["Income"]=df["Income"].clip(lower,upper)
df["Income in Lakhs"]=df["Income"]/100000
df["Age_group"]=pd.cut(
    df["Age"],
    bins=(0, 18, 25, 50, 80),
    labels=("Underage", "Young Adults", "Adults", "Old")
)

print(df.head(30))

