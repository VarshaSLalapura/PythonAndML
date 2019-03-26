
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
from warnings import warn
from collections import Counter


style.use('fivethirtyeight') # 538


def k_nearest_neighbors(data, predict, k):
    if len(data) >= k:
        warnings.warn('K is set to a value greater than the total voting group, Check!')




dataset = {'r': [[1,1],[2,2]], 'k': [[4,4],[5,5]]}
newdata = [4.5,4.5]
[[plt.scatter(ii[0], ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]
plt.show()

k_nearest_neighbors()



























#     distances = []
#     # data is a dict, groups are r, k, within each group, there are features, which are list of lists, each list is
#     # one feature in one dimension
#
#     for group in data:
#         for features in data[group]:
#             print(features,predict)
#             # euclidian_dist = np.sqrt(np.sum(((np.array(features))-(np.array(predict)))**2))
#             euclidian_dist = np.linalg.norm(np.array(features)-np.array(predict))
#             print(euclidian_dist)
#             print(group)
#             # euclidean_distance = np.sqrt(np.sum((np.array(features)-np.array(predict))**2))
#             distances.append([euclidian_dist, group])
#     print('distances = ', distances)
#
#     # p = sorted(distances)[:k]
#     # print(p)
#     votes = [i[1] for i in sorted(distances)[:k]]
#     print(votes)
#     vote_result_at = Counter(votes).most_common(1)
#     print(vote_result_at)
#     vote_result = Counter(votes).most_common(1)[0][0]
#
#     return vote_result
#
#
# # make a dataset of the dictionary of atleast +1 k classes, now k = 1, so atleast 2 classes of data
# dataset = {'r': [[1, 1], [2, 2]], 'k': [[4, 4], [5, 5]]}
# new_data = [4.5, 4.5]
#
# # for i in dataset:
# #     for ii in dataset[i]:
# #         plt.scatter(ii[0], ii[1], s=100, color = i)
#
# [[plt.scatter(ii[0], ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]
# # [[plt.scatter(ii[0],ii[1],s=100,color=i) for ii in dataset[i]] for i in dataset]
# result = k_nearest_neighbors(data=dataset, predict=new_data, k=3)
# plt.scatter(new_data[0], new_data[1], s=100, color=result)
# plt.show()
