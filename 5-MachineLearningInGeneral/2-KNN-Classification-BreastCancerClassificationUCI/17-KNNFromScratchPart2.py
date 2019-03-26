# KNN to Breast Cancer Dataset

# 1. Acquire Breast Cancer Dataframe
# 2. Remove the unwanted cols, and replace missing data, important : convert to float type
# 3. Find the appropriate features and labels
# 4. Convert df to np
# 5. Preprocess the train set features
# 5. Use sklearn to do train test split with a good test size
# 6. Define the classifier - KNN
# 7. Run the training
# 8. Run the testing and find the accuracy of train-test phase



import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing, model_selection, neighbors
import pandas as pd
import os


path = "/home/varshalalapura/Desktop/datasets/UCI-BrestCancer_Orig"
filename = "breast-cancer-wisconsin.data"

my_data_file = os.path.join(path, filename)
print(my_data_file)

df = pd.read_csv(my_data_file)
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True)
# Acquired the df and did the necessary changes

# Now want to find the features and labels
X = df.drop(['class'], 1)
y = df['class']
# print(len(X), len(y))

# make them into np arrays for sklearn to accept it
X = np.array(X)
y = np.array(y)

# preprocessing
X = preprocessing.scale(X) # not always a must

# train test split
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

# clf
clf = neighbors.KNeighborsClassifier() # closed braces  was not there, so error in next line when executed

# train
clf.fit(X_train, y_train)

# test
accuracy = clf.score(X_test, y_test)
print(accuracy)




