import pandas as pd
import math

df = pd.read_csv("Decision.csv")

# -------------------------------
# REMOVE ID COLUMN IF PRESENT
# -------------------------------
if "Id" in df.columns:
    df = df.drop(columns=["Id"])

print(df.head())

target = "Buys"
attributes = [col for col in df.columns if col != target]

def entropy(column):
    values = column.value_counts(normalize=True)
    return -sum(p * math.log2(p) for p in values)

def information_gain(df, attribute, target):
    total_entropy = entropy(df[target])
    vals = df[attribute].unique()

    weighted_entropy = 0
    for v in vals:
        subset = df[df[attribute] == v]
        weighted_entropy += (len(subset)/len(df)) * entropy(subset[target])

    return total_entropy - weighted_entropy

print("\nInformation Gain:")
gains = {}

for attr in attributes:
    gains[attr] = information_gain(df, attr, target)
    print(attr, ":", gains[attr])

root = max(gains, key=gains.get)
print("\nROOT NODE =", root)