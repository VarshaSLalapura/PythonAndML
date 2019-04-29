import tensorflow as tf
import os
from create_sentiment_featureset import create_feature_sets_and_labels
import numpy as np


path = '/home/varsha/Desktop/Datasets-Sentdex/TF'
pos_file = os.path.join(path, 'pos.txt')
neg_file = os.path.join(path, 'neg.txt')

# i wrote train_x, test_x, train_y, test_y, so badly got into the bug loop and finally compared with sentdex code
# portion by portion
# my_bug "train_x, test_x, train_y, test_y = create_feature_sets_and_labels(pos_file, neg_file)"
train_x, train_y, test_x, test_y = create_feature_sets_and_labels(pos_file, neg_file)


n_nodes_hl1 = 1500
n_nodes_hl2 = 1500
n_nodes_hl3 = 1500
n_classes = 2
batch_size = 100
hm_epochs = 10

# height X width
x = tf.placeholder('float', [None, len(train_x[0])])  # had not put float in quotes
y = tf.placeholder('float')


# input * weights + bias
def nn_model(data):
    hl1 = {'weights': tf.Variable(tf.random_normal([len(train_x[0]), n_nodes_hl1])),
           'biases': tf.Variable(tf.random_normal([n_nodes_hl1]))}
    hl2 = {'weights': tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
           'biases': tf.Variable(tf.random_normal([n_nodes_hl2]))}
    hl3 = {'weights': tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
           'biases': tf.Variable(tf.random_normal([n_nodes_hl3]))}

    ol = {'weights': tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
          'biases': tf.Variable(tf.random_normal([n_classes]))}

    l1 = tf.add(tf.matmul(data, hl1['weights']), hl1['biases'])
    l1 = tf.nn.relu(l1)

    l2 = tf.add(tf.matmul(l1, hl2['weights']), hl2['biases'])
    l2 = tf.nn.relu(l2)

    l3 = tf.add(tf.matmul(l2, hl3['weights']), hl3['biases'])
    l3 = tf.nn.relu(l3)

    output = tf.add(tf.matmul(l3, ol['weights']), ol['biases'])

    return output


def train_nn(x):

    predictions = nn_model(x)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=predictions, labels=y))
    optimizer = tf.train.AdamOptimizer().minimize(cost)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for epoch in range(hm_epochs):
            epoch_loss = 0
            i = 0
            while i < len(train_x):
                start = i
                end = i + batch_size
                batch_x = np.array(train_x[start:end])
                batch_y = np.array(train_y[start:end])
                _, c = sess.run([optimizer, cost], feed_dict={x: batch_x, y: batch_y})

                epoch_loss += c
                i += batch_size
            print('Epoch', epoch, 'completed out of', hm_epochs, 'loss: ', epoch_loss)

        correct = tf.equal(tf.argmax(predictions, 1), tf.argmax(y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
        print('Accuracy', accuracy.eval({x: test_x, y: test_y}))




train_nn(x)
