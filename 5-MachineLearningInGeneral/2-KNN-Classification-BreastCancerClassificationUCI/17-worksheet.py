from math import sqrt
import numpy as np
from matplotlib import pyplot as plt

# to fing the Euclidian distance between 2 points in 2d space

plot0 = [2, 2]
plot1 = [3, 3]
euclidean_dist = sqrt( ( ( ( plot0[0])-(plot1[0]) )**2 ) + ( ( ( plot0[1]) - (  plot0[1]) )**2 ) )
print(euclidean_dist)

# to find the distance between 2 arrays of n dimensions
# 1 set is features, 1 more is predict, we want to find the distance between them

features = [[1, 1], [3, 3], [4, 4]]
predict = [2, 2]
eucl_dist = np.sqrt(np.sum(((np.array(features) - np.array(predict))**2)))
print(eucl_dist)

# same thing using np.linalg.norm
eucl_dist = np.linalg.norm((np.array(features))-(np.array(predict)))
print(eucl_dist)

# create a dataset of dictionary, with 2 classes, 4 datapoints each, 2 dimensional in nature

dataset = {'r': [[1, 1], [2, 2], [3, 3], [4, 4]], 'k': [[6, 6], [7, 7], [8, 8]]}

# plot the dataset:
# for group in dataset:
#     for data in dataset[group]:
#         plt.scatter(data[0], data[1], s=100, color=group)
#
#
# plt.show()

# or one liner
[[plt.scatter(data[0], data[1], s=100, color=group) for data in dataset[group]] for group in dataset]
plt.show()

