# 1-MeanShiftOnXData.py

from sklearn.cluster import MeanShift
from sklearn.datasets.samples_generator import make_blobs
from mpl_toolkits.mplot3d import Axes3D   # this is a part of matplotlib package, so noprobs
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')

centers = [[1, 1, 1], [5, 5, 5], [3, 10, 10]]
X, _ = make_blobs(n_samples=100, centers=centers, cluster_std=1)
# print(X)  # given theses centers, create 100 points around them in 3D space

ms = MeanShift()
ms.fit(X)
labels = ms.labels_
print(labels)  # to the cluster it belonged, [1, 1, 0, 0, 2 so on............]
cluster_centers = ms.cluster_centers_
print(cluster_centers)  # should be close to the defined centres
n_clusters_ = range(len(cluster_centers))
print(n_clusters_)


# plotting
colors = 10*['r', 'g', 'b', 'k', 'y', 'c', 'm']  # 70 different colors
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
print(ax)  #Axes3DSubplot(0.125,0.11;0.775x0.77)

for i in range(len(X)):
    ax.scatter(X[i][0], X[i][1], X[i][2], c=colors[labels[i]], marker = 'o')  # i indicates it has x,y in data

ax.scatter(cluster_centers[:, 0], cluster_centers[:, 1], cluster_centers[:, 2], marker='*', linewidths=5, s=150,
           color='k')
plt.show()
