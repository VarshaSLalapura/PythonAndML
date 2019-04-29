#12-TestingAssumptionsCreatingNewData.py

import numpy as np
import random
import matplotlib.pyplot as plt
from statistics import mean


def create_dataset(hm, variance, step=2, correlation=False):
    val = 1
    ys = []
    for i in range(hm):
        y = val + random.randrange(-variance, variance)
        ys.append(y)
        if correlation == "pos":
            val +=step
        elif correlation == "neg":
            val -= step

    xs = [i for i in range(hm)]
    return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)


xs, ys = create_dataset(40, 10, 2, correlation=False)


def best_fit_slope_and_intercept(xs,ys):

    m = (( mean(xs)*mean(ys)) - (mean(xs*ys))) / (((mean(xs)) ** 2) - (mean(xs**2)))
    b = ( mean(ys) ) - ( (m*mean(xs)) )
    return m, b


def squared_error(ys_orig, ys_line):
    return sum((ys_orig - ys_line)**2)


def coefficient_determination_best_fit_line(ys_orig,ys_line):
    y_mean_line = [mean(ys_orig) for _ in ys_orig]
    squared_error_y_reg = squared_error(ys_orig,ys_line)
    squared_error_y_mean = squared_error(ys_orig,y_mean_line)
    return 1 - (squared_error_y_reg/squared_error_y_mean)


m, b = best_fit_slope_and_intercept(xs,ys)



print(m,b)
# plt.plot(xs,ys)
# plt.show()
regression_line = [(m*x + b) for x in xs]
r2 = coefficient_determination_best_fit_line(ys,regression_line)
print(r2)
# equivalent
# regression_line = []
# for x in xs:
#     regression_line.append((m*x + b))
# now new data:
predict_x = 8
predict_y = m*predict_x +b


plt.scatter(xs,ys,label='data',color='#003F72')
plt.scatter(predict_x, predict_y, s=100,color = 'y')
plt.plot(xs,regression_line, label='regression line')
plt.legend(loc=4)
plt.show()
