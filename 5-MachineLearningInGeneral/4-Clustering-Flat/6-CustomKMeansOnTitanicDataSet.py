# 6-CustomKMeansOnTitanicDataSet.py
# apply KMeans made from scratch to titanic dataset and compare with sklearn KMeans with Titanic Dataset

# 5-KMeansFromScratch.py

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd
import os
from sklearn import preprocessing
pd.set_option('display.max_columns', 15)

style.use('ggplot')


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
                distances = [np.linalg.norm(featureset - self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)
                # print(featureset, self.centroids, distances, classification, self.classifications)
            # print()
            prev_centroids = dict(self.centroids)
            # at that particular index of min distance, find the mean to get the new centroid in that index
            for classification in self.classifications:
                # self.centroids[classification] = np.mean(self.classifications[classification], axis=0)
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)
            # print(self.centroids)
            # print()
            optimized = True

            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                if np.sum((current_centroid - original_centroid) / original_centroid * 100.0) > self.tol:
                    print(np.sum((current_centroid - original_centroid) / original_centroid * 100.0))
                    optimized = False

            if optimized:
                break

    def predict(self, data):
        for featureset in data:
            distances = [np.linalg.norm(featureset - self.centroids[centroid]) for centroid in self.centroids]
            classification = distances.index(min(distances))
            self.classifications[classification].append(featureset)

            return classification


path = "/home/varshalalapura/Desktop/datasets/Titanic"
filename = "titanic.xls"

my_file = os.path.join(path, filename)
print(my_file)

# read the excel sheet
df = pd.read_excel(my_file)

df.drop(['body', 'name'], 1, inplace=True)
df.dropna(0, inplace=True)  # 0 means index of the df

df.convert_objects(convert_numeric=True)
print(df.head())


def handle_non_numeric_data(daf):
    # to print the columns of the df
    columns = df.columns.values
    print(columns)
    txt_to_int_dict = {}

    def convert_txt_int(txt):
        return txt_to_int_dict[txt]

    # columns = ['pclass', 'sex', 'cabin']
    for column in columns:  # for eac column in the df
        if df[column].dtype != np.int64 and df[column].dtype != np.float64:  # if it is non-numeric
            # convert to a list
            column_list = df[column].values.tolist()
            # find the unique elements
            unique_elements = set(column_list)
            # not iterate over the unique elements and put to the dict with value starting from 0
            x = 0
            for unique in unique_elements:
                if unique not in txt_to_int_dict:
                    txt_to_int_dict[unique] = x
                    x += 1

            print('txt_to_int_dict', txt_to_int_dict)

            df[column] = list(map(convert_txt_int, df[column]))
            print(df[column])
    return df


handle_non_numeric_data(daf=df)
print(df.head())
# df.drop(['ticket'], 1, inplace=True)
# df.drop(['boat'], 1, inplace=True)
# find the meaningful ref to compare and the remaining as data to interpret
X = np.array(df.drop(['survived'], 1).astype(np.float64))
y = np.array(df['survived'])

# print(X)
# print(range(len(X)))

X = preprocessing.scale(X)
# X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)
# this doesnot matter here itseems??????????
# clf = cluster.KMeans(n_clusters=2)
clf = KMeans()
clf.fit(X)
# centroids = clf.cluster_centers_
# label = clf.labels_
correct = 0
for i in range(len(X)):
    predict_me = np.array(X[i])
    predict_me = predict_me.reshape(-1, len(predict_me))
    print(predict_me)
    prediction = clf.predict(data=predict_me)
    if prediction == y[i]:
        correct += 1
print('accuracy:', correct/len(X))

# data = X  # this X can be placed anywhere outside of the class
# clf = KMeans()
# clf.fit(data)
# for centroid in clf.centroids:
#     plt.scatter(clf.centroids[centroid][0], clf.centroids[centroid][1], color='k', linewidths=5, s=150, marker='o')
#
# colors = 10 * ["g", "r", "c", "b", "k"]
# for classification in clf.classifications:
#     color = colors[classification]
#     for featureset in clf.classifications[classification]:
#         plt.scatter(featureset[0], featureset[1], color=color, s=150, linewidths=5, marker='x')

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

