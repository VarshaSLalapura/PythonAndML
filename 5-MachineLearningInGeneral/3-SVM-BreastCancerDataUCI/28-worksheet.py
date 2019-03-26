import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')


class SupportVectorMachine:

    def __init__(self, visualization):
        self.visualization = visualization
        self.color = {'r': 1, 'k': -1}
        if visualization:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(1, 1, 1)

    # train
    def fit(self, data):
        self.data = data
        # ||w|| = [w, b]
        opt_dict = []
        transforms = [[1, 1], [-1, 1], [-1, -1], [1, -1]]

        # make a list of the data
        all_data = []
        for classes in self.data:
            for feature_set in self.data[classes]:
                for feature in feature_set:
                    all_data.append(feature)

        print(all_data)

        # find the min and max feature values from the list and clear the list
        self.max_feature_value = max(all_data)
        self.min_feature_value = min(all_data)
        all_data = None
        print(self.max_feature_value)
        print(self.min_feature_value)

        # step_size for w
        step_size = [self.max_feature_value * 0.1,
                     self.max_feature_value * 0.01,
                     self.max_feature_value * 0.001]  # this size will be expensive
        # step size for b
        b_range_multiple = 5
        b_multiple = 5

        # define the latest_optimum to be the max value scaled up 10
        latest_optimum = self.max_feature_value * 10
        print(latest_optimum)

        # iterate over steps, b, transforms, data or the other way condition on data range-> transformed range-> steps
        # of b range -> steps of w
        for step in np.arange(step_size):  # step_size
            w = np.array([latest_optimum, latest_optimum])
            optimized = False
            while not optimized:
                for b in np.arange(-1 * (self.max_feaute_value * self.b_range_multiple),
                                   self.max_feaute_value * b_range_multiple, step * b_multiple):
                    for transformation in transforms:
                        w_t = w * transformation
                        found_option = True
                        for i in self.data:
                            for xi in self.data[i]:
                                yi = i

                                if not (yi * (np.dot(w_t, xi) + b) >= 0):
                                    found_option = False
                        if found_option:
                                opt_dict[np.linalg.norm(w_t)] = [w_t, b]

                if w[0] < 0:
                    optimized = True
                    print('One step optimized')
                else:
                    w = w - step

            norm = sorted([n for n in opt_dict])
            opt_choice = opt_dict[norm]
            opt_w = opt_choice[0]
            opt_b = opt_choice[1]
            latest_optimum = opt_choice[0][0] + step * 2


    # predict
    def predict(self, features):
        # sign (W.X + b)
        # classification = np.sign((np.dot(np.array(features),W )+b))
        classification = np.sign(np.dot(np.array(features), self.W) + self.b)

        return classification


# create the data dictionary in 2 D, one set for +1 and other set for -1

data_dict = {'r': [[1, 7], [2, 8], [3, 8]],
             'k': [[5, 1], [6, -1],  [7, 3]]}

svm = SupportVectorMachine(visualization=False)
svm.fit(data=data_dict)

# for group in data_dict:
#     for data in data_dict[group]:
#         print(data)
#
