# T55, rnn_example.py
# modify the baseline code deepnet.py written in TF

import tensorflow as tf
# print(tf.__version__)
from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.contrib import rnn  # mark
import os

o = os.getcwd()
print(o)
mnist = input_data.read_data_sets('.', one_hot=True)
# print(mnist)

hm_epochs = 3
n_classes = 10
batch_size = 128
chunk_size = 28
n_chunks = 28
rnn_size = 128


# height X width
x = tf.placeholder(float, [None, n_chunks, chunk_size])
y = tf.placeholder(float)


# input * weights + bias
def recurrent_neural_network(x):
    layer = {'weights': tf.Variable(tf.random_normal([rnn_size, n_classes])),
             'biases': tf.Variable(tf.random_normal([n_classes]))}

    x = tf.transpose(x, [1, 0, 2])  # mark, check transpose-reshape-split.py
    x = tf.reshape(x, [-1, chunk_size])  # mark
    x = tf.split(x, n_chunks, 0)  # mark

    lstm_cell = rnn.BasicLSTMCell(rnn_size, state_is_tuple=True)  # mark
    outputs, states = rnn.static_rnn(lstm_cell, x, dtype=tf.float32)  # mark
    output = tf.add(tf.matmul(outputs[-1], layer['weights']), layer['biases'])  # mark

    return output


def train_nn(x):

    predictions = recurrent_neural_network(x)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=predictions, labels=y))
    optimizer = tf.train.AdamOptimizer().minimize(cost)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        # older : sess.run(tf.initialize_all_variables())
        for epoch in range(hm_epochs):
            epoch_loss = 0
            num = int(mnist.train.num_examples/batch_size)
            print(num)
            for _ in range(int(mnist.train.num_examples/batch_size)):

                x_train, y_train = mnist.train.next_batch(batch_size)
                # print(tf.shape(x_train), tf.shape(y_train))
                x_train = x_train.reshape((batch_size, n_chunks, chunk_size))  # mark
                _, c = sess.run([optimizer, cost], feed_dict={x:x_train, y: y_train})

                epoch_loss += c
            print('Epoch', epoch, 'completed out of', hm_epochs, 'loss: ', epoch_loss)

        correct = tf.equal(tf.argmax(predictions, 1), tf.argmax(y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
        print('Accuracy', accuracy.eval({x:mnist.test.images.reshape(-1, n_chunks, chunk_size), y: mnist.test.labels}))


train_nn(x)
