# 1-KMeans.py

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
from sklearn import cluster

style.use('ggplot')

X = np.array([[1, 1.5],
             [2, 2.5],
             [5, 5.0],
             [6, 6.5],
             [2.4, 1.5],
             [8, 7.5],
             ])

clf = cluster.KMeans(n_clusters=2)
clf.fit(X)

centroids = clf.cluster_centers_
print(centroids)
labels = clf.labels_
print(labels)
# colours = ['r.', 'g.', 'b.', 'k.', 'y.', 'c.']
colors = ["g.", "r.", "c.", "y."]

# plt.scatter(X[:, 0], X[:, 1], linewidths=5, s=25)


# for row in range(len(X)):
#     plt.plot(X[row][0], X[row][1], colors[labels[row]], markersize=25)
#     print(colors[labels[row]])
# plt.show()

colors = ["g.", "r.", "c.", "y."]
for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=10)  # pay close attension to plot vs scatter
plt.scatter(centroids[:, 0], centroids[:, 1], marker="x", s=150, linewidths=5, zorder=10)
plt.show()