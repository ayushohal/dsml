import pandas as pd

# Load dataset
df = pd.read_csv("HousePrice.csv")

# Identify categorical and quantitative variables
categorical_cols = df.select_dtypes(include=['object']).columns
quantitative_cols = df.select_dtypes(include=['int64', 'float64']).columns

print("=== Categorical Columns ===")
print(list(categorical_cols))
print("\n=== Quantitative Columns ===")
print(list(quantitative_cols))

# Summary statistics: grouped by each categorical variable
for cat in categorical_cols:
    print(f"\n\n==============================")
    print(f"Summary statistics grouped by: {cat}")
    print(f"==============================\n")

    for num in quantitative_cols:
        print(f"\n--- {num} grouped by {cat} ---")
        stats = df.groupby(cat)[num].agg(
            Mean='mean',
            Median='median',
            Minimum='min',
            Maximum='max',
            Std_Dev='std'
        )
        print(stats)