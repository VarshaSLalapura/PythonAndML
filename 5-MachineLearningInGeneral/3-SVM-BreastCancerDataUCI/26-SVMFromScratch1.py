import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

# define a "class" called Support_Vector_Machine
# define the init method with visualization being True
# color
# while True, fig = plt.figure()
# .ax = plt.fig.add_subplot(1,1,1)
# define fit method
# define predict method
# it has decision boundary equation : W.X + b , np.sign(), np.dot, np.array
# return classification


class SupportVectorMachine:

    def __init__(self,visualization):
        self.visualization = visualization
        self.color = {'r': 1, 'k': -1}
        if visualization:
            self.fig = plt.figure()
            self.ax = plt.fig.add_subplot(1,1,1)

    # train
    def fit(self,data):
        pass

    # predict
    def predict(self, features):
        # sign (W.X + b)
        # classification = np.sign((np.dot(np.array(features),W )+b))
        classification = np.sign(np.dot(np.array(features), self.W) + self.b)
        return classification


# create the data dictionary in 2 D, one set for +1 and other set for -1

data_dict = {'r': [[1, 7], [2, 8], [3, 8]],
             'k': [[5, 1], [6, -1],  [7, 3]]}

# for group in data_dict:
#     for data in data_dict[group]:
#         print(data)

