import numpy as np
chunk_size = 1
n_chunks = 2

# quick example

x = np.ones((1,
             2,
             3))
print(x)
print()
print(np.shape(x))
x = np.transpose(x, (1, 0, 2))
print(x)
print(np.shape(x))
# x = np.reshape(x, (-1, chunk_size))
# print(x)
# x = np.split(x, n_chunks, 0)
# print(x)


# y = np.ones((1, 2, 2))
# print(y)
# print()
# z = np.ones((2, 2, 2))
# print(z)