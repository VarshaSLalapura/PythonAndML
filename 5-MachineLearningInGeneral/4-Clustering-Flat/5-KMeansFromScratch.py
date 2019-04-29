# 5-KMeansFromScratch.py

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

# X = np.array([[1, 1], [2, 2], [3, 3], [7, 7], [8, 8]])

X = np.array([[1, 2],
              [1.5, 1.8],
              [5, 8],
              [8, 8],
              [1, 0.6],
              [9, 11],
              [1, 3],
              [8, 9],
              [0, 3],
              [5, 4],
              [6, 4]])

# unknowns = np.array([[1, 3],
#                      [8, 9],
#                      [0, 3],
#                      [5, 4],
#                      [6, 4]])

# for elem in X:
#     print(elem)


class KMeans:
    def __init__(self, k=2, tol=0.001, max_iter=500):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter
        self.centroids = {}
        self.classifications = {}

    def fit(self, data):

        # self.centroids = {}

        for i in range(self.k):
            self.centroids[i] = data[i]

        # calculate the distance from a centroids to a particular featureset
        for i in range(self.max_iter):

            print('Iter no. {}'.format(i))
            # self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []  # these two lines are for clearing the clusters before the next iteration
                # begins

            for featureset in data:  # caveat, had put it inside the for loop above, this forloop for iterating over
                # featureset over one iteration
                distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)
                # print(featureset, self.centroids, distances, classification, self.classifications)
            # print()
            prev_centroids = dict(self.centroids)
            # at that particular index of min distance, find the mean to get the new centroid in that index
            for classification in self.classifications:
                # self.centroids[classification] = np.mean(self.classifications[classification], axis=0)
                self.centroids[classification] = np.average(self.classifications[classification],axis=0)
            # print(self.centroids)
            # print()
            optimized = True

            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                if np.sum((current_centroid-original_centroid)/original_centroid*100.0) > self.tol:
                    print(np.sum((current_centroid-original_centroid)/original_centroid*100.0))
                    optimized = False

            if optimized:
                break

    def predict(self, data):
        for features in data:
            distances = [np.linalg.norm(features-self.centroids[centroid]) for centroid in self.centroids]
            classification = distances.index(min(distances))
            self.classifications[classification].append(featureset)

            return classification

    
data = X  # this X can be placed anywhere outside of the class
clf = KMeans()
clf.fit(data)
for centroid in clf.centroids:
    plt.scatter(clf.centroids[centroid][0], clf.centroids[centroid][1], color='k', linewidths=5, s=150, marker='o')

colors = 10*["g","r","c","b","k"]
for classification in clf.classifications:
    color = colors[classification]
    for featureset in clf.classifications[classification]:
        plt.scatter(featureset[0], featureset[1], color=color, s=150, linewidths=5, marker='x')

# unknowns = np.array([[1, 3],
#                      [8, 9],
#                      [0, 3],
#                      [5, 4],
#                      [6, 4]])

# for unknown in unknowns:
#     classification = clf.predict(unknown) # he put this to classification, the index, will be used for
#     # color
#     plt.scatter(unknown[0], unknown[1], color=colors[classification], s=150, linewidths=5, marker='*')

plt.show()