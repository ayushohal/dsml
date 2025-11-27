import pandas as pd
import math

data = [
    ["Young","High","No","Fair","No"],
    ["Young","High","No","Good","No"],
    ["Middle","High","No","Fair","Yes"],
    ["Old","Medium","No","Fair","Yes"],
    ["Old","Low","Yes","Fair","Yes"],
    ["Old","Low","Yes","Good","No"],
    ["Middle","Low","Yes","Good","Yes"],
    ["Young","Medium","No","Fair","No"],
    ["Young","Low","Yes","Fair","Yes"],
    ["Old","Medium","Yes","Fair","Yes"],
    ["Young","Medium","Yes","Good","Yes"],
    ["Middle","Medium","No","Good","Yes"],
    ["Middle","High","Yes","Fair","Yes"],
    ["Old","Medium","No","Good","No"]
]

cols = ["Age","Income","Married","Health","Class"]
df = pd.DataFrame(data, columns=cols)
df['Age'] = df['Age'].str.capitalize()

# Frequency table
freq_table = df['Age'].value_counts().rename_axis('Age').reset_index(name='Frequency')
freq_table['Proportion'] = freq_table['Frequency'] / len(df)
print(freq_table)

# Class distribution per age
print(df.groupby(['Age','Class']).size().unstack(fill_value=0))

# Entropy function
def entropy(counts):
    total = sum(counts)
    ent = 0.0
    for c in counts:
        if c == 0: continue
        p = c / total
        ent -= p * math.log2(p)
    return ent

# Parent entropy
class_counts = df['Class'].value_counts()
H_parent = entropy(class_counts.tolist())

# Conditional entropy and info gain
cond_entropy = 0.0
for age, group in df.groupby('Age'):
    counts = group['Class'].value_counts()
    h = entropy(counts.tolist())
    weight = len(group) / len(df)
    cond_entropy += weight * h

info_gain = H_parent - cond_entropy

print("H_parent =", H_parent)
print("H_conditional =", cond_entropy)
print("Information Gain =", info_gain)