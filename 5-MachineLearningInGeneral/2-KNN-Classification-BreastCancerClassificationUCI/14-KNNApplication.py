# 14-KNNApplication.py
# https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29
# https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Original%29 - Sentdex uses this


# 1. ID
# 2. Clump thickness
# 3. Uniformity of cell size
# 4. Uniformity of cell shape
# 5. Margin of adhesion
# 6. Single epith cell size
# 7. Bare nuclie
# 8. Bland chromatin
# 9. Normal nucleolie
# 10. Mitosis
# 11. Class (2- Benign, 4 - Malignant)


import numpy as np
from sklearn import preprocessing, model_selection, neighbors
import pandas as pd
import os

path = '/home/varshalalapura/Desktop/datasets/UCI-BrestCancer_Orig'
file_name = 'breast-cancer-wisconsin.data'


my_file = os.path.join(path, file_name)
# print(my_file)
accuracies = []
for i in range(25):
    df = pd.read_csv(my_file)
    df.replace('?', -99999, inplace=True)
    df.drop(['id'], 1, inplace=True)

    X = np.array(df.drop(['class'], 1))  # there was a space after class in the .data file, so it was throwing error
    y = np.array(df['class'])

    X = preprocessing.scale(X)

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2) # without giving the test_size
    # the order of X_train, X_test, y_train, y_test matters
    # print(len(X_train), len(y_train))
    clf = neighbors.KNeighborsClassifier()
    clf.fit(X_train, y_train)
    accuracy = clf.score(X_test, y_test)
    # print(accuracy)

    # example_measure = np.array([[4, 2, 2, 1, 1, 1, 2, 1, 1], [8, 2, 2, 1, 1, 1, 2, 1, 1]]) # two braces
    # for list of lists,
    # # and then to np.array
    # example_measure = example_measure.reshape(len(example_measure), -1)
    # prediction = clf.predict(example_measure)
    # print(prediction)

    accuracies.append(accuracy)

print(sum(accuracies)/len(accuracies))
