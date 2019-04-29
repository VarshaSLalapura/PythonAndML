import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

# nparray_data = [[1, 1], [3, 3], [7, 7], [8, 8], [9, 9]]
# data = [[1, 1], [3, 3], [7, 7], [8, 8], [9, 9]]
# for elem in nparray_data:
#     print(elem)
X = np.array([[1, 1], [3, 3], [7, 7], [8, 8], [9, 9]])


class KMeans:

    def __init__(self, k=2, tol=0.001, max_iter=4):

        self.k = k
        self.tol = tol
        self.max_iter = max_iter
        # print(self.k)

    def fit(self, data):

        self.centroids = {}

        for i in range(self.k):
            self.centroids[i] = data[i]
        print(self.centroids)


        for i in range(self.max_iter):
            self.classification = {}

            for i in range(self.k):
                self.classification[i] = []
            print(self.classification)

            for featureset in data:
                distances = [np.linalg.norm(featureset - self.centroids[centroid]) for centroid in self.centroids]
            print(distances)





    # def fit(self, data):
    #     self.centroids = {}
    #
    #     for i in range(self.k):
    #         self.centroids[i] = data[i]
    #
    #     for i in range(self.max_iter):
    #                self.classifications = {}
    #
    #         for j in range(self.k):
    #             print('j:', j)
    #             self.classifications[i] = []
    #
    #         for featureset in data:
    #             print(featureset)
    #             distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
    #             print(distances)
    #             classification = distances.index(min(distances))
    #             print(classification)
                # self.classifications[classification].append(featureset)
                # print(self.classifications[classification])
                # self.classifications[classification].append(featureset)

    # def fit(self, data):
    #     self.centroids = {}
    #
    #     for i in range(self.k):
    #         self.centroids[i] = data[i]
    #
    #     for i in range(self.max_iter):
    #         self.classifications = {}
    #
    #         for i in range(self.k):
    #             self.classifications[i] = []
    #
    #         for featureset in data:
    #             distances = [np.linalg.norm(featureset - self.centroids[centroid]) for centroid in self.centroids]
    #             classification = distances.index(min(distances))
    #             self.classifications[classification].append(featureset)
    # def fit(self, data):
    #     # an empty dict of centroids
    #     self.centroids = {}  # {0: [1,1], 1 : [2,2]}
    #
    #     for i in range(self.k):
    #         # place the initial centroid points
    #         self.centroids[i] = data[i] # {0: [1,1], 1 : [2,2]}
    #     print(self.centroids)
    #
    #     for i in range(self.max_iter):
    #         # a dict for cluster points
    #         self.classifications = {}
    #         for j in range(self.k):
    #             self.classifications[i] = {}   # before you start, clear the cluster points
    #                                       # zero the dict vals at every key
    #             for featureset in data:     # for elem in the list/np.array
    #                 distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
    #             # print(distances)
    #                 classification = distances.index(min(distances))
    #             # print(i, classification)
    #                 self.classifications[classification].append(featureset)  # dict[key].append(elemOfDataList)
    #                 # classification = distances.index(min(distances))
    #                 # classifications[classification].append(featureset) # populating the dic[key] with elem in the list
    #         print(self.classifications)




    # def predict(self, data):
    #
    #     distances = [np.linalg.norm(features - centroids[centroid] for centroid in centroids)]
    #     classification = distances.index(min(distances))
    #
    #     return classification

data = X  # this X can be placed anywhere outside of the class
KMeans()
clf = KMeans()
clf.fit(data)
