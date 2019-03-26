# 2-MeanShiftOnTitanicDataset.py

# copy large part from 2-HandlingNonNumericData.py and proceed

import numpy as np
import pandas as pd
import os
from sklearn import preprocessing, model_selection, cluster
pd.set_option('display.max_columns', 15)


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
df.drop(['boat', 'sex'], 1, inplace=True)


def handle_non_numeric_data(daf):
    # to print the columns of the df
    columns = df.columns.values
    # print(columns)
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

            # print('txt_to_int_dict', txt_to_int_dict)

            df[column] = list(map(convert_txt_int, df[column]))
            # print(df[column])
    return df


handle_non_numeric_data(daf=df)
# print(df.head())
# print()

# find the meaningful ref to compare and the remaining as data to interpret
X = np.array(df.drop(['survived'], 1).astype(np.float64))
y = np.array(df['survived'])

# print(X)
# print(range(len(X)))

X = preprocessing.scale(X)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)
clf = cluster.KMeans(n_clusters=2)
clf.fit(X)
centroids = clf.cluster_centers_
label = clf.labels_
correct = 0
for i in range(len(X)):
    predict_me = np.array(X[i])
    predict_me = predict_me.reshape(-1, len(predict_me))
    print(predict_me)
    prediction = clf.predict(predict_me)
    if prediction == y[i]:
        correct += 1
print('accuracy:', correct/len(X))