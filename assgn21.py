import pandas as pd
import numpy as np
import random

# Load dataset
df = pd.read_csv("IRIS.csv")

# Numeric features only
X = df[['sepal_length','sepal_width','petal_length','petal_width']].values

k = 4
iterations = 10

# Randomly select initial centroids
centroids = X[random.sample(range(len(X)), k)]

def euclidean(a, b):
    return np.sqrt(np.sum((a - b)**2))

# K-Means algorithm
for itr in range(iterations):
    clusters = [[] for _ in range(k)]

    for point in X:
        distances = [euclidean(point, c) for c in centroids]
        cluster_idx = np.argmin(distances)
        clusters[cluster_idx].append(point)

    new_centroids = []
    for cluster in clusters:
        new_centroids.append(np.mean(cluster, axis=0))
    centroids = new_centroids

# Print final centroids
print("\n=== Final Centroids for K=4 ===")
for i, c in enumerate(centroids):
    print(f"Cluster {i+1} centroid:", c)