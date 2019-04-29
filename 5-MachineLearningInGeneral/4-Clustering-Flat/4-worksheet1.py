import numpy as np


X = np.array([[1, 1], [2, 2], [3, 3], [7, 7], [8, 8]])
# for elem in X:
#     print(elem)


class KMeans:
    def __init__(self, k=2, tol=0.001, max_iter=3):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter

    def fit(self, data):

        self.centroids = {}

        for i in range(self.k):
            self.centroids[i] = data[i]

        for i in range(self.max_iter):
            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []

            for featureset in data:
                distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)
            print(self.classifications)


clf = KMeans()
clf.fit(data=X)  # X is passed into data