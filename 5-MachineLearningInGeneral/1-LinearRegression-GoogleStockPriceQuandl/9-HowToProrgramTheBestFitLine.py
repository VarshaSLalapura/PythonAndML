# 9-HowToProgramTheBestFilLine.py

import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
from matplotlib import style

# check this style
style.use('fivethirtyeight')

xs = np.array([1, 2, 3, 4, 5], dtype=np.float64)
ys = np.array([5, 4, 6, 5, 6], dtype=np.float64)

# "weird thing is without the dtype, m results in 0.5 which is 0.29999 otherwise"


def best_fit_slope_and_intercept(xs,ys):

    m = (( mean(xs)*mean(ys)) - (mean(xs*ys))) / (((mean(xs)) ** 2) - (mean(xs**2)))
    b = ( mean(ys) ) - ( (m*mean(xs)) )
    return m, b


m, b = best_fit_slope_and_intercept(xs,ys)
print(m,b)
# plt.plot(xs,ys)
# plt.show()
regression_line = [(m*x + b) for x in xs]


# equivalent
# regression_line = []
# for x in xs:
#     regression_line.append((m*x + b))
# now new data:
predict_x = 8
predict_y = m*predict_x +b


plt.scatter(xs, ys)
plt.scatter(predict_x, predict_y, color='g')
plt.plot(xs, regression_line)
plt.show()
