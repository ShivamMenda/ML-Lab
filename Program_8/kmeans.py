import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class KMeans:
    def __init__(self, n_clusters, max_iterations=200):
        self.n_clusters = n_clusters
        self.max_iterations = max_iterations

    def fit(self, X):
        self.centroids = X[np.random.choice(range(X.shape[0]), self.n_clusters, replace=False)]

        for _ in range(self.max_iterations):
            # Assign points to the nearest centroid
            distances = self.calculate_distances(X)
            labels = np.argmin(distances, axis=1)

            # Update centroids
            new_centroids = np.array([X[labels == k].mean(axis=0) for k in range(self.n_clusters)])

            if np.all(self.centroids == new_centroids):
                break

            self.centroids = new_centroids

            return labels

    def calculate_distances(self, X):
        distances = np.sqrt(((X[:, np.newaxis] - self.centroids) ** 2).sum(axis=2))
        return distances

# Set the random seed for reproducibility
np.random.seed(42)

# Load the data from iris.csv
data = pd.read_csv('iris.csv')
X = data.iloc[:, :-1].values

kmeans = KMeans(n_clusters=3)
labels = kmeans.fit(X)

# Plot the results
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], marker='x', color='red')
plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
