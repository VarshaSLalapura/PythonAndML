# cnn_step_by_step from coursera

import numpy as np
import h5py
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

np.random.seed(1)


def zero_pad(x, pad):

    """

    :param x: numpy array of shape (m, n_H, n_W, n_C)
    :param pad: integer , amount of padding each image on vertical and horizontal dimensions
    :return: x_pad: padded image of shape (m, n_H + 2*pad, n_W + 2*pad, n_C)
    """

    x_pad = np.pad(x, ((0, 0), (pad, pad), (pad, pad), (0, 0)), 'constant')
    # caveat the inner parenthesis for np.pad
    return x_pad


# test for padding

# sample = np.random.randn(4, 3, 3, 2)
# # print(x)
# print(np.shape(sample))
# x_pad = zero_pad(x=sample, pad=2)
# print(np.shape(x_pad))
# # print(x[0, 0])
# # print(x_pad[0, 0])
# # print(x_pad)
#
# fig, ax = plt.subplots(1, 2)
# ax[0].set_title('x')
# ax[0].imshow(sample[0, :, :, 0])
# ax[1].set_title('x_pad')
# ax[1].imshow(x_pad[0, :, :, 0])
# plt.show()


# single step of convolution

def conv_single_step(a_slice_prev, W, b):

    """
    :param a_slice_prev: slice of input data of shape (f, f, n_C_prev)
    :param W: Weight parameters contained in a window - matrix of shape (f, f, n_C_prev)
    :param b: Bias parameters contained in a window -matrix of shape (1, 1, 1)

    :return: Z: a scalar value, result of convolving sliding window (W, b) on slice of input data
    """

    s = np.multiply(a_slice_prev, W)
    Z = np.sum(s)
    Z = np.add(Z, np.float(b))

    return Z


# test conv_single_step
# np.random.seed(1)
# a_slice_prev = np.random.randn(4, 4, 3)
# W = np.random.randn(4, 4, 3)
# b = np.random.randn(1, 1, 1)
#
# Z = conv_single_step(a_slice_prev, W, b)
# print(Z)  # expected answer = -6.999089


# conv_forward
def conv_forward(A_prev, W, b, hparameters):

    """

    :param A_prev: output of prev activation with shape (m, n_H_prev, n_W_prev, n_C_prev)
    :param W: shape (f, f, n_C_prev, n_C)
    :param b: shape (1, 1, 1, n_C)
    :param hparameters: dict of hyperparameters contrining stride and padding value
    :return: Z : convolution output of shape (m, n_H, n_W, n_C)

    """
    m, n_H_prev, n_W_prev, n_C_prev = np.shape(A_prev)
    f, f, n_C_prev, n_C = np.shape(W)
    stride = hparameters["stride"]
    pad = hparameters["pad"]

    n_H = int(((n_H_prev-f+2*pad)/stride +1))
    print(n_H)
    n_W = int(((n_W_prev-f+2*pad)/stride +1))
    print(n_W)
    Z = np.zeros((m, n_H, n_W, n_C))

    a_prev_pad = zero_pad(A_prev, pad)
    print(np.shape(a_prev_pad))

    for i in range(m):
        a_prev = a_prev_pad[i]
        print(np.shape(a_prev))
        for h in range(n_H):  # 1/ n_H for test
            for w in range(n_W):  # 1/ n_W
                for c in range(n_C):  # 1/ n_C
                    vert_start = h*stride
                    vert_end = (h*stride) + f
                    horiz_start = w*stride
                    horiz_end = (w*stride) + f
                    a_slice_prev = a_prev[vert_start:vert_end, horiz_start:horiz_end, :]
                    # print(np.shape(a_slice_prev))
                    # print()
                    Z[i, h, w, c] = conv_single_step(a_slice_prev, W[:, :, :, c], b[:, :, :, c])
                    # print(np.shape(Z))

    assert(Z.shape == (m, n_H, n_W, n_C))

    cache = (A_prev, W, b, hparameters)
    # print(cache)
    return Z, cache


# test conv_forward
# np.random.seed(1)
# A_prev = np.random.randn(4, 5, 5, 3)
# A_prev = np.random.randn(10, 4, 4, 3)
# # 3 x 3 kernel on a 5 x 5 image,
# # input volume = 3 = n_C_prev
# # output_volume = 9 = n_C
# W = np.random.randn(2, 2, 3, 8)
# b = np.random.randn(1, 1, 1, 8)
#
# hparameters = {"stride": 2, "pad": 2}
# Z, cache_conv = conv_forward(A_prev, W, b, hparameters)
#
# print("Z's mean: ", np.mean(Z))
# print("Z[3,2,1] =", Z[3, 2, 1])
# print("cache_conv[0][1][2][3] =", cache_conv[0][1][2][3])


def pool_forward(A_prev, hparameters, mode="max"):

    """
    # no padding in pooling
    :param A_prev: A_prev: output of prev activation with shape (m, n_H_prev, n_W__prev, n_C_prev)
    :param hparameters: dict of hyperparameters contrining stride and padding value
    :param mode: pooling mode you would liek to use: "max" or "average"
    :return: A -- output of the pool layer, a numpy array of shape (m, n_H, n_W, n_C)
    cache -- cache used in the backward pass of the pooling layer, contains the input and hparameters
    """

    (m, n_H_prev, n_W_prev, n_C_prev) = np.shape(A_prev)
    stride = hparameters["stride"]
    f = hparameters["f"]

    n_H = int(1 + (n_H_prev-f)/stride )
    print(n_H)
    n_W = int(1 + (n_W_prev-f)/stride)
    print(n_W)
    n_C = n_C_prev
    A = np.zeros((m, n_H, n_W, n_C))

    for i in range(m):
        for h in range(n_H):  # 1/ n_H for test
            for w in range(n_W):  # 1/ n_W
                for c in range(n_C):  # 1/ n_C
                    vert_start = h*stride
                    vert_end = (h*stride) + f
                    horiz_start = w*stride
                    horiz_end = (w*stride) + f
                    a_slice_prev = A_prev[i, vert_start:vert_end, horiz_start:horiz_end, c]
                    # print(np.shape(a_slice_prev))
                    # print()
                    if mode == "max":
                        A[i, h, w, c] = np.max(a_slice_prev)
                    elif mode == "average":
                        A[i, h, w, c] = np.max(a_slice_prev) / np.mean(a_slice_prev)

                    # print(np.shape(Z))

    cache = (A_prev, hparameters)
    # print(cache)
    assert(A.shape == (m, n_H, n_W, n_C))

    return A, cache


# test pool_forward
np.random.seed(1)
A_prev = np.random.randn(2, 4, 4, 3)
hparameters = {"stride": 2, "f": 3}

A, cache = pool_forward(A_prev, hparameters)
print("mode = max")
print("A =", A)
print()
A, cache = pool_forward(A_prev, hparameters, mode="average")
print("mode = average")
print("A =", A)