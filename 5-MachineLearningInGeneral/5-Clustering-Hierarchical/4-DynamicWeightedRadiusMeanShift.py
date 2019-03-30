# 4-DynamicWeightedRadiusMeanshift.py

import numpy as np
from matplotlib import style

style.use('ggplot')
X = np.array([[1, 1], [2, 2], [5, 5], [6, 6], [2, 10], [2, 11], [3, 14]])


class MeanShift:

    def __init__(self, radius=None, radius_norm_step=100):
        self.radius = radius
        self.radius_norm_step = radius_norm_step

    def fit(self, data):
        # print(data)

        # if self.radius == None:
        if self.radius is None:
            all_data_centroid = np.average(data, axis=0)
            all_data_norm = np.linalg.norm(all_data_centroid)
            print(all_data_norm)
            self.radius = all_data_norm/self.radius_norm_step
            print(self.radius)

        centroids = {}

        for i in range(len(data)):   # unhashable type: 'numpy.ndarray' if i wrote data and not range(len(data))
            centroids[i] = data[i]
        print(centroids)

        weights = [i for i in reversed(range(self.radius_norm_step))]  #[::-1]  # to reverse it
        print(weights)

        while True:
            new_centroids = []
            for i in centroids:
                in_bandwidth = []
                centroid = centroids[i]
                print()
                for feature_set in data:
                    distances = np.linalg.norm(feature_set-centroid)
                    print(feature_set, centroid, distances)
                    if distances == 0:
                        distances = 0.0000000001
                    weight_index = int(distances/self.radius)
                    print(weight_index)

                    if weight_index > self.radius_norm_step-1:
                        print(weight_index, self.radius_norm_step-1)
                        weight_index = self.radius_norm_step-1
                    to_add = (weights[weight_index]**2)*[feature_set]
                    print(len(to_add))
                    in_bandwidth += to_add

                new_centroid = np.average(in_bandwidth, axis=0)
                new_centroids.append(tuple(new_centroid))

            print(new_centroids)
            uniques = sorted(list(set(new_centroids)))
            print(uniques)

        previous_centroids = dict(centroids)
        centroids = {}
        for i in range(len(uniques)):
            centroids[i] = np.array(uniques[i])
        print(centroids)

        optimized = True
        for j in centroids:
            if not np.array_equal(np.linalg.norm(previous_centroids[j], centroids[j])):
                optimized = False
            if not optimized:
                break
        if optimized:
            break

    self.centroids = centroids


clf = MeanShift()
clf.fit(data=X)
