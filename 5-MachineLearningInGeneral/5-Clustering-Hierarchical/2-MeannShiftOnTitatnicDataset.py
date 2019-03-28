# 2-MeanShiftOnTitanicDataset.py

# from 10th min in the video, Sentdex extracts knowledge from the dataframe, revisit this again and again

# copy large part from 2-HandlingNonNumericData.py and proceed

import numpy as np
import pandas as pd
import os
from sklearn import preprocessing, model_selection
from sklearn.cluster import MeanShift
pd.set_option('display.max_columns', 15)


path = "/home/varshalalapura/Desktop/datasets/Titanic"
filename = "titanic.xls"

my_file = os.path.join(path, filename)
print(my_file)

# read the excel sheet
df = pd.read_excel(my_file)


# copy the df as original_df for future use
original_df = pd.DataFrame.copy(df)
print(original_df.head())

df.drop(['body', 'name'], 1, inplace=True)
df.fillna(0, inplace=True)  # 0 means index of the df I had written dropna and 0 instead of fillna and 0 inside,
# 0 is put all na as 0

df.convert_objects(convert_numeric=True)
# print(df.head())


def handle_non_numeric_data(daf):
    # to print the columns values of the df
    columns = df.columns.values
    # print(columns)
    txt_to_int_dict = {}

    def convert_txt_int(txt):
        return txt_to_int_dict[txt]

    # columns = ['pclass', 'sex', 'cabin']
    for column in columns:  # for eac column in the df
        if df[column].dtype != np.int64 and df[column].dtype != np.float64:  # if it is non-numeric
            # convert to a list
            column_list = df[column].values.tolist()  # don't write df[column].to_list()
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


df = handle_non_numeric_data(daf=df)
df.drop(['ticket', 'home.dest'], axis=1, inplace=True)  # axis=1 is important
# print(df.head())
# # print()
#
# find the meaningful ref to compare and the remaining as data to interpret
X = np.array(df.drop(['survived'], 1).astype(np.float64))  # astype is important
X = preprocessing.scale(X)  # scale and not Scale
y = np.array(df['survived'])

clf = MeanShift()
clf.fit(X)

cluster_centers = clf.cluster_centers_
# print(cluster_centers)
labels = clf.labels_  # check check
# print(labels.shape)
# for label in labels:
#     print(label, type(label))

# iterate over labels and put those to a new col called cluster_group
original_df['cluster_group'] = np.nan
# print(df['cluster_group'].shape)
for i in range(len(X)):
    original_df['cluster_group'].iloc[i] = labels[i]  # place the corresponding labels of X in the corresponding
    # cluster_group column

# print(original_df['cluster_group'])  # 0-> 0.0 1-> 2.0 ... 29-> 1.0 ....

# calculating the survival rates and populating the dict if survival_rates
n_clusters = len(np.unique(labels))  # check check
survival_rates = {}
for i in range(n_clusters):
    temp_df = original_df[(original_df['cluster_group'] == float(i))] # conditional df,
    # all the rows where its not nan, labels are present
    survival = temp_df[(temp_df['survived'] == 1)]  # conditional df,
    # all the rows where survived col is true
    survival_rate = len(survival)/len(temp_df)
    survival_rates[i] = survival_rate

print(survival_rates)  # {0: 0.3534844668345928, 1: 1.0, 2: 0.6547619047619048, 3: 0.8888888888888888, 4: 1.0,
                       # 5: 0.1, 6: 1.0}
                       # 0 label cluster has 35% survival rate, 1 label survival rate 100%,  .........
# print(original_df[(original_df['cluster_group'] == 3)])  # pclass indicates 1, 1st class,
# sex indicate female in this cluster
# print((original_df[(original_df['cluster_group'] == 2)]).describe())
# prints ---->
#         pclass   survived       age      sibsp      parch        fare  \
# count    50.0  50.000000  50.000000  50.000000  50.000000   50.000000
# mean      1.0   0.660000  36.028334   0.820000   1.360000  198.790332
# std       0.0   0.478518  17.918778   0.873417   1.045105   55.808969
# min       1.0   0.000000   0.916700   0.000000   0.000000   83.158300
# 25%       1.0   0.000000  23.250000   0.000000   0.250000  151.550000
# 50%       1.0   1.000000  36.000000   1.000000   1.500000  211.500000
# 75%       1.0   1.000000  50.000000   1.000000   2.000000  258.661450
# max       1.0   1.000000  67.000000   3.000000   4.000000  263.000000
#           body       cluster_group
# count    6.000000           50.0
# mean   111.500000            2.0
# std     36.719205            0.0
# min     45.000000            2.0
# 25%    102.500000            2.0
# 50%    123.000000            2.0
# 75%    132.250000            2.0
# max    147.000000            2.0
# cluster_0 = original_df[(original_df['cluster_group'] == 0)]
# cluster_0_firstClass = cluster_0[(cluster_0['pclass'] == 1)]
# cluster_0_firstClass.describe()
