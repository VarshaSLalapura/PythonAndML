# 11-ProgrammingR2.py

# Q : What is R Squared / Coefficient of Determination used for?
# A : to measure how close the data fits a regression line, or how good is the best fit line w.r.to the data
# Q : What does squared error measure?
# A : Well check out the page : https://pythonprogramming.net/r-squared-coefficient-of-determination-machine-learning-
# tutorial/#!
# Q : What is the other name for co-efficient of determination
# A : squared error

import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
from matplotlib import style

# check this style
style.use('fivethirtyeight')

xs = np.array([1, 2, 3, 4, 5], dtype=np.float64)
ys = np.array([5, 4, 6, 5, 6], dtype=np.float64)

# "weird thing is without the dtype, m results in 0.5 which is 0.29999 otherwise"


def best_fit_slope_and_intercept(xs, ys):

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
print(m, b)
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


plt.scatter(xs,ys)
plt.scatter(predict_x, predict_y, color='g')
plt.plot(xs,regression_line)
plt.show()
