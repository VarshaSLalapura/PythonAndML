# Custom KMeans upto distance between points and centroids, correct

import numpy as np


X = np.array([[1, 1], [2, 2], [3, 3], [7, 7], [8, 8]])
# for elem in X:
#     print(elem)


class KMeans:
    def __init__(self, k=2, tol=0.001, max_iter=2):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter

    def fit(self, data):

        self.centroids = {}

        for i in range(self.k):
            self.centroids[i] = data[i]

        # calculate the distance from a centroids to a particular featureset
        for i in range(self.max_iter):

            print('Iter no. {}'.format(i))
            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []  # these two lines are for clearing the clusters before the next iteration
                # begins

            for featureset in data: # caveat, had put it inside the for loop above, this forloop for iterating over
                # featureset over one iteration
                distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)
                print(featureset, self.centroids, distances, classification, self.classifications)


# Iter no.0
# [1 1] {0: array([1, 1]), 1: array([2, 2])}[0.0, 1.4142135623730951] 0 {0: [array([1, 1])], 1: []}
# [2 2] {0: array([1, 1]), 1: array([2, 2])} [1.4142135623730951, 0.0] 1 {0: [array([1, 1])], 1: [array([2, 2])]}
# 3 3] {0: array([1, 1]), 1: array([2, 2])} [2.8284271247461903, 1.4142135623730951] 1 {0: [array([1, 1])], 1: [array([2, 2]), array([3, 3])]}
# [7 7] {0: array([1, 1]), 1: array([2, 2])} [8.48528137423857, 7.0710678118654755] 1 {0: [array([1, 1])], 1: [array([2, 2]), array([3, 3]), array([7, 7])]}
# [8 8] {0: array([1, 1]), 1: array([2, 2])} [9.899494936611665, 8.48528137423857] 1 {0: [array([1, 1])], 1: [array([2, 2]), array([3, 3]), array([7, 7]), array([8, 8])]}
# Iter no. 1
# [1 1] {0: array([1, 1]), 1: array([2, 2])} [0.0, 1.4142135623730951] 0 {0: [array([1, 1])], 1: []}
# [2 2] {0: array([1, 1]), 1: array([2, 2])} [1.4142135623730951, 0.0] 1 {0: [array([1, 1])], 1: [array([2, 2])]}
# [3 3] {0: array([1, 1]), 1: array([2, 2])} [2.8284271247461903, 1.4142135623730951] 1 {0: [array([1, 1])], 1: [array([2, 2]), array([3, 3])]}
# [7 7] {0: array([1, 1]), 1: array([2, 2])} [8.48528137423857, 7.0710678118654755] 1 {0: [array([1, 1])], 1: [array([2, 2]), array([3, 3]), array([7, 7])]}
# [8 8] {0: array([1, 1]), 1: array([2, 2])} [9.899494936611665, 8.48528137423857] 1 {0: [array([1, 1])], 1: [array([2, 2]), array([3, 3]), array([7, 7]), array([8, 8])]}

clf = KMeans()
clf.fit(data=X)  # X is passed into data


