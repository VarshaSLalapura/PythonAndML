import csv
import numpy as np
import os
import matplotlib.pyplot as plt

# this is to load the data called "example.txt"
# as cvs file or read it using numpy

path = "/home/varshalalapura/Desktop/Inspiration"
file_name = "example.txt"

# 1:

with open(os.path.join(path,file_name)) as csvfile:
     my_file = csv.reader(csvfile,delimiter = ',')
     x = []
     y = []
     for row in my_file:
         x.append(row[0])
         y.append(row[1])

plt.scatter(x,y,label='Loaded from file!')
plt.show()
plt.plot(x,y,label='Loaded from txt file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('InterestingPlot\nOpenedNow')
plt.show()

# 2: Using numpy

x, y = np.loadtxt((os.path.join(path, file_name)), delimiter = ',', unpack=True)
plt.plot(x,y)
plt.show()
