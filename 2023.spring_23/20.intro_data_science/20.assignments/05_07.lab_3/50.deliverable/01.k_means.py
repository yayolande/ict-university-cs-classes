# May 07, 2023
# K-Means Classification

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.cluster as KMeans
import sklearn.cluster as cluster
import os

project_dir = os.path.dirname(__file__)
os.chdir(project_dir)

file = '01.data.csv'
fd = pd.read_csv(file)

inertias = []
column_list = fd.columns.values
height = fd[column_list[1]] # height columns only
weight = fd[column_list[2]] # weight columns only
data = list(zip(height, weight))

# scaler = StandardScaler()
# scaled_features = scaler.fit_transform(features)
# from sklearn.metrics import silhouette_score
# kmeans_silhouette = silhouette_score(scaled_features, kmeans.labels).round(2)
# fd.values[0]

# # Ways 1 - Plot all Kmeans inorder to find the best K
# for n in range(1, 10):
#     # kmeans = KMeans(n_clusters=n)
#     # kmeans.fit(fd)
#     kmeans = cluster.KMeans(n_clusters=n)
#     kmeans.fit(data)
#     inertias.append(kmeans.inertia_)

# plt.plot(range(1, 10), inertias, marker = 'o')
# plt.show()

# # Ways 2
# x = fd['Height (Cm)']
# y = fd['Weight (Kg)']

# plt.scatter(x, y)
# plt.show()

# Ways 3 - Plot K-Means around K=n_clusters
k_value = 2
kmeans = cluster.KMeans(n_clusters=k_value, n_init=10)
kmeans.fit(data)
centers = kmeans.cluster_centers_

# TODO: UNCOMMENT below code once testing done !!!
plt.scatter(height, weight, c=kmeans.labels_)
plt.scatter(centers[:, 0], centers[:, 1], c='blue', s=100, alpha=0.9)
plt.grid(True)
plt.xlabel('Weight (Kg)')
plt.ylabel('Height (Cm)')
plt.title(f'Fitness Club Members K-Means (K = {k_value})')
plt.show()

print(f"""
Legend: Cluster label for each data (ordering according to data index)
0 ==> cluster 1 
1 ==> cluster 2 

{kmeans.labels_}
""")

# ---------------------- Training & Experimental Zone ----------------------
# List data points available in a cluster -- way 1
cluster_label_for_every_data = kmeans.labels_
count = kmeans.n_clusters
data_in_cluster = [[] for i in range(count)]

for index, label in enumerate(cluster_label_for_every_data):
    data_in_cluster[label].append(list(fd.values[index]))

data_index_in_clusters = [np.where(kmeans.labels_ == i)[0] for i in range(count)]

# List data points available in a cluster -- way 2
# data_points_in_cluster_0 = fd[kmeans.labels_ == 0]
# data_points_in_cluster_1 = fd[kmeans.labels_ == 1]
# data_points_in_cluster_2 = fd[kmeans.labels_ == 2]
# output = data_points_in_cluster_0

# print(output)
# print(data_in_cluster)
# print(fd.to_string())
