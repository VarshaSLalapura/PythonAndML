from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

# X = np.array([[1, 1], [2, 2], [5, 5]],) # [6, 6], [2, 10], [2, 11], [3, 14]])
X = np.array([[1, 1], [2, 2], [5, 5], [6, 6], [2, 10], [2, 11], [3, 14]])
# plt this using plt.scatter
plt.scatter(X[:, 0], X[:, 1], s=150)
# plt.show()


class MeanShift:

    def __init__(self, radius=2):
        self.radius = radius

    def fit(self, data):
        centroids = {}

        # no. of centroids = no. of features/data points
        for i in range(len(data)):
            # print(X[i])
            centroids[i] = data[i]
        # print(centroids)  # if i declared centroids as an empty list and not a dict, this would fall out of index
        # range, caveat
        while True:
            new_centroids = []
            new_centroids1 = []

            for i in centroids:  # iterate through the centroids
                # pick one centroid
                centroid = centroids[i]
                # for that define a list that is populated with feature_sets w.r.to that centroid
                in_bandwidth = []

                for feature_set in data:  # through every feature in data
                    # check if the feature_set in X w.r.to the centroid is crossing the radius
                    if np.linalg.norm(feature_set - centroid) < self.radius:
                        print(feature_set, centroid, np.linalg.norm(feature_set - centroid), self.radius)
                        # if not , put it in in_bandwidth
                        in_bandwidth.append(feature_set)
                print('in_bandwidth: ', in_bandwidth)

                new_centroid = np.average(in_bandwidth, axis=0)
                print('new_centroid: ', new_centroid)

                # take these new centroid and append to new_centroids list
                new_centroids1.append(new_centroid)
                print('new_centroids: ', new_centroids1)
                new_centroids.append(tuple(new_centroid))
                print('new_centroids from tupled new_centroid: ', new_centroids)

            uniques = sorted(list(set(new_centroids)))
            print('unique centroids:', uniques)

            # now we want to compare the centroid with the prev centroid
            # so , dump this new centroid into a dict called prev_centroids

            previous_centroids = dict(centroids)

            centroids = {}
            # array version of unique ith element
            for i in range(len(uniques)):  # caveat the for loop indent
                centroids[i] = np.array(uniques[i])
            # print('centroids_dict: ', centroids)

            optimized = True
            for i in centroids:
                if not np.array_equal(centroids[i], previous_centroids[i]):
                    optimized = False
                if not optimized:
                    break
            if optimized:
                break

        self.centroids = centroids


clf = MeanShift()
clf.fit(data=X)  # cant pass X in the init method
centroids = clf.centroids
for c in centroids:
    # print(c)
    plt.scatter(centroids[c][0], centroids[c][1], color='k', marker='*', s=150)
    # plt.scatter(c[:, 0], c[:, 1], color='k', marker='*', s=150)
plt.show()

