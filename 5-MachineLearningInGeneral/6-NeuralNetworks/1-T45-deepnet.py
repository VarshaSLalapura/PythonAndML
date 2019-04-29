import tensorflow as tf
# print(tf.__version__)
from tensorflow.examples.tutorials.mnist import input_data
import os
"""
input_data > weights > hl1  > activation fn > 
weights > hl2 > activation_fn >
weights > hl3 > activation_fn >
weights > output_layer ---- feed forwards

compare output to intended output > cost/loss fn(cross entropy)

optimize the cost fn(optimizer - Adam, SGD)

back propagation

feed_forward + back_prop = one epoch

"""
o = os.getcwd()
print(o)
mnist = input_data.read_data_sets('.', one_hot=True)
# print(mnist)
n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500
n_classes = 10
batch_size = 100

# height X width
x = tf.placeholder(float, [None, 28*28])
y = tf.placeholder(float)


# input * weights + bias
def nn_model(data):
    hl1 = {'weights': tf.Variable(tf.random_normal([28*28, n_nodes_hl1])),
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

    hm_epochs = 10
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        # older : sess.run(tf.initialize_all_variables())
        for epoch in range(hm_epochs):
            epoch_loss = 0
            num = int(mnist.train.num_examples/batch_size)
            print(num)
            for _ in range(int(mnist.train.num_examples/batch_size)):
                x_train, y_train = mnist.train.next_batch(batch_size)
                _, c = sess.run([optimizer, cost], feed_dict={x:x_train, y: y_train})

                epoch_loss += c
            print('Epoch', epoch, 'completed out of', hm_epochs, 'loss: ', epoch_loss)

        correct = tf.equal(tf.argmax(predictions, 1), tf.argmax(y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
        print('Accuracy', accuracy.eval({x:mnist.test.images, y : mnist.test.labels}))


train_nn(x)
