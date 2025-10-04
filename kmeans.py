import numpy as np
import csv
import matplotlib.pyplot as plt 

class KMeansClustering:

    def __init__(self, k):
        self.k = k  # initialise the number of clusters
        self.centroids = None  # make an empty variable for centroids to be stored

    @staticmethod
    def euclidean_distance(data_points, centroids):
        # this function calculates the Euclidean distance from each data point to each centroid using broadcasting
        return np.linalg.norm(data_points[:, np.newaxis] - centroids, axis=2)

    def fit(self, X, max_iterations=200):
        # this function randomly initialises centroids within the dataset points
        self.centroids = np.random.uniform(np.amin(X, axis=0), np.amax(X, axis=0), size=(self.k, X.shape[1]))

        for _ in range(max_iterations): # this loop calculates the distance from each data point to each centroid           
            distances = KMeansClustering.euclidean_distance(X, self.centroids)
            y = np.argmin(distances, axis=1) # this line assigns each data point to the nearest centroid (cluster)

            cluster_centers = []
            for i in range(self.k): # in this loop if there are points assigned to the cluster, new centroid is computed
                if np.any(y == i):
                    cluster_centers.append(X[y == i].mean(axis=0))
                else:
                    cluster_centers.append(np.random.uniform(np.amin(X, axis=0), np.amax(X, axis=0)))

            if np.all(np.linalg.norm(self.centroids - cluster_centers, axis=1) < 0.0001): 
                break

            self.centroids = np.array(cluster_centers)  # update centroids

        return y 

    def silhouette_score(self, X, labels):
        unique_labels = np.unique(labels)  # initialise unique cluster labels
        silhouette_scores = []

        for i in range(len(X)):
            same_cluster = X[labels == labels[i]]
            other_clusters = X[labels != labels[i]]

            a = np.mean([np.linalg.norm(X[i] - point) for point in same_cluster if not np.array_equal(X[i], point)]) if len(same_cluster) > 1 else 0
            
            b = np.min([np.mean([np.linalg.norm(X[i] - point) for point in X[labels == label]]) for label in unique_labels if label != labels[i]]) if len(other_clusters) > 0 else 0

            silhouette_scores.append((b - a) / max(a, b) if max(a, b) > 0 else 0)

        return np.mean(silhouette_scores)  

def read_csv(csv_file):
    csv_list = []
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.reader(file)

        next(reader)
        for row in reader:
            print(row.__getitem__(0)," ",row.__getitem__(1)," ",row.__getitem__(2)," ",row.__getitem__(3)," ",row.__getitem__(4))
            csv_list.append([float(row[-2]), float(row[-1])])
    return np.array(csv_list)  

data_points = read_csv('inc_vs_rent.csv')
annual_rent_Data =[]
average_SEK_Data=[]

for data in data_points:
    annual_rent_Data.append(float(data[0]))
    average_SEK_Data.append(float(data[1]))


plt.scatter(annual_rent_Data, average_SEK_Data, color='orange')
plt.xlabel('Annual rent sqm')  # Label for x-axis
plt.ylabel('Avg yearly inc SEK')
plt.show()



list_of_k = range(2, 12)  # Start from 2 to avoid 1-cluster case
silhouette_list = []

for k in list_of_k:
    kmeans = KMeansClustering(k)
    labels = kmeans.fit(data_points)
    silhouette_avg = kmeans.silhouette_score(data_points, labels)
    silhouette_list.append(silhouette_avg)
    print(f"k={k}, Silhouette Score: {silhouette_avg:.4f}")
    # Plotting the results
    plt.scatter(data_points[:, 0], data_points[:, 1], c=labels, cmap='viridis', marker='o', edgecolor='k')
    plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], c='red', marker="*", s=200, label='Centroids')
    plt.title('KMeans Clustering')  # Title for the plot
    plt.xlabel('Independent Variable')  # Label for x-axis
    plt.ylabel('Dependent Variable')  # Label for y-axis
    plt.legend()  # Show legend
    plt.show()  # Display the plot




