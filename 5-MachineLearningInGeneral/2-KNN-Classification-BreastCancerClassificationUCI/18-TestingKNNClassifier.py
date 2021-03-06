# write the knn classifier and apply it on the brest cancer data

import pandas as pd
import os
import random
import numpy as np
import warnings
from collections import Counter


def k_nearest_neighbors(dataset, predict, k=3):
    if len(dataset) >= k:
        warnings.warn('Check!')

    distances = []
    for egroup in dataset:
        for features in dataset[egroup]:
            euclid_dist = np.linalg.norm((np.array(features))-(np.array(predict)))
            distances.append([euclid_dist, egroup])

    votes = [i[1] for i in sorted(distances)[:k]]
    votes_result = Counter(votes).most_common(1)[0][0]

    return votes_result


path = "/home/varshalalapura/Desktop/datasets/UCI-BrestCancer_Orig"
filename = "breast-cancer-wisconsin.data"

my_data_file = os.path.join(path, filename)
print(my_data_file)

df = pd.read_csv(my_data_file)
# replace ? and drop id col
df.drop(["id"], 1, inplace=True)
df.replace('?', -99999, inplace=True)
# change to float list
full_data = df.astype(float).values.tolist()
# print(df.astype(float).values.tolist())
# shuffle
# print(full_data[:2])
random.shuffle(full_data)
# print(full_data[:2])

# test_size, train_set, test_set
test_size = 0.2
train_set = {2: [], 4: []}
test_set = {2: [], 4: []}

# get
train_data = full_data[:-int(test_size*len(full_data))]
test_data = full_data[-int(test_size*len(full_data)):]

# populate the sets from the list of lists
for i in train_data:
    # print(i)
    train_set[i[-1]].append(i[:-1]) # dictionary.append , extract the key as

for i in test_data:
    test_set[i[-1]].append(i[:-1])

# apply the k_nearest_neighbor algo to the train test data
correct = 0
total = 0
for group in test_set:
    for data in test_set[group]:
        vote_result = k_nearest_neighbors(dataset=train_set, predict=data, k=5)
        if group == vote_result:
            correct += 1

        total += 1
print('Accuracy:', correct/total)


