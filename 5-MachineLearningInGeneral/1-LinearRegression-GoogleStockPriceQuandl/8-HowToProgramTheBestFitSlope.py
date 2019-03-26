import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

xs = np.array([1,2,3,4,5], dtype = np.float64)
ys = np.array([5,4,6,5,6], dtype = np.float64)

# "weird thing is without the dtype, m results in 0.5 which is 0.29999 otherwise"

def best_fit_slope(xs,ys):

    m = (( mean(xs)*mean(ys)) - (mean(xs*ys))) / (((mean(xs)) ** 2) - (mean(xs**2)))
    # m = (((mean(xs) * mean(ys)) - mean(xs * ys)) /
    #     ((mean(xs) ** 2) - mean(xs ** 2)))
    return m

m = best_fit_slope(xs,ys)
print(m)
# plt.plot(xs,ys)
# plt.show()