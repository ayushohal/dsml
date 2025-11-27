import pandas as pd

# Load dataset
df = pd.read_csv("IRIS.csv")

# Display unique species
print("Species present:", df['species'].unique())

# Filter by each species
setosa = df[df['species'] == 'Iris-setosa']
versicolor = df[df['species'] == 'Iris-versicolor']
virginica = df[df['species'] == 'Iris-virginica']

# Function to print stats
def print_stats(name, data):
    print(f"\n=== Statistics for {name} ===")
    print("Mean:\n", data.mean())
    print("\nStandard Deviation:\n", data.std())
    print("\n25th Percentile:\n", data.quantile(0.25))
    print("\n50th Percentile (Median):\n", data.quantile(0.50))
    print("\n75th Percentile:\n", data.quantile(0.75))

# Exclude species column
numeric_cols = ['sepal_length','sepal_width','petal_length','petal_width']

print_stats("Iris-setosa", setosa[numeric_cols])
print_stats("Iris-versicolor", versicolor[numeric_cols])
print_stats("Iris-virginica", virginica[numeric_cols])