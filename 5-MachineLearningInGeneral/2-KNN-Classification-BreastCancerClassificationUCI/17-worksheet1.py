import numpy as np
import warnings
from collections import Counter
from matplotlib import pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')


def k_nearest_neighbor(data, predict, k):

    if len(data) >= k:
        warnings.warn('Chosen k is l, check!')

    distances = []
    for group in data:
        for features in data[group]:
            euclid_dist = np.linalg.norm((np.array(features))-(np.array(predict)))
            distances.append([euclid_dist, group])

    # print(distances)
    votes = [i[1] for i in sorted(distances)[:k]]
    print(votes)
    vote_tuple = Counter(votes).most_common(1)
    print(vote_tuple)
    vote_result = Counter(votes).most_common(1)[0][0]
    print(vote_result)
    confidence = Counter(votes).most_common(1)[0][1] / k
    print(confidence)
    # for i in data:
    #     dataset.append(data[i])
    # print(dataset)

    return vote_result


dataset = {'r': [[1, 1], [2, 2], [3, 3], [4, 4]], 'g': [[6, 6], [7, 7], [8, 8], [10, 10]]}
new_feature = [9, 9]
result = k_nearest_neighbor(data=dataset, predict=new_feature, k=3)
[[plt.scatter(data[0], data[1], s=100, color=group) for data in dataset[group]] for group in dataset]
plt.scatter(new_feature[0], new_feature[1], s=100, color=result)
plt.show()