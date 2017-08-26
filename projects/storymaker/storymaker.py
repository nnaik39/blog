from __future__ import print_function

import numpy as np
import tensorflow as tf
from tensorflow.contrib import rnn
import random
import collections
import time
#%matplotlib inline
from tensorflow.contrib.rnn import LSTMCell, DropoutWrapper, MultiRNNCell
import matplotlib.pyplot as plt
#from tensorflow.models.rnn.ptb import reader

logs_path = '/tmp/tensorflow/rnn_words'
writer = tf.summary.FileWriter(logs_path)

#uncomment the below line to train the model on king_midas.txt
#training_file = 'short_star_of_india.txt'
training_file = 'star_of_india.txt'
#make sure all text is lowercase
def read_data(fname):
    with open(fname,encoding='utf-8') as f:
        content = f.readlines()
    
    if (len(content) != 0):
        content = [x.strip() for x in content]
        content = [content[i].split() for i in range(len(content))]
        content = np.array(content)
        content = np.reshape(content, [-1, ])
        return content

training_data = read_data(training_file)
print("Loaded story...")

def build_dataset(words):
    count = collections.Counter(words).most_common()
    dictionary = dict()
    for word, _ in count:
        dictionary[word] = len(dictionary)
    reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
    return dictionary, reverse_dictionary

dictionary, reverse_dictionary = build_dataset(training_data)
vocab_size = len(dictionary)

learning_rate = 0.001
#training_iters = 5000
#tonight, change training_iters = 1000000
training_iters = 10000
n_input = 3

n_hidden = 512

x = tf.placeholder("float", [None, n_input, 1])
y = tf.placeholder("float", [None, vocab_size])

weights = {
    'out': tf.Variable(tf.random_normal([n_hidden, vocab_size]))
}
biases = {
    'out': tf.Variable(tf.random_normal([vocab_size]))
}

def RNN(x, weights, biases):
    x = tf.reshape(x, [-1, n_input])
    x = tf.split(x,n_input,1)
    rnn_cell = LSTMCell(n_hidden)
    rnn_cell = DropoutWrapper(rnn_cell, output_keep_prob=0.5)

    stacked_rnn = []
    for iiLyr in range(3):
        stacked_rnn.append(tf.nn.rnn_cell.LSTMCell(num_units=n_hidden))
    rnn_cell = tf.nn.rnn_cell.MultiRNNCell(cells=stacked_rnn)
#    rnn_cell = MultiRNNCell([rnn_cell]*2)
    outputs, states = rnn.static_rnn(rnn_cell, x, dtype=tf.float32)
    return tf.matmul(outputs[-1], weights['out']) + biases['out']

pred = RNN(x, weights, biases)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
#print("cost " + str(cost))
optimizer = tf.train.RMSPropOptimizer(learning_rate=learning_rate).minimize(cost)
correct_pred = tf.equal(tf.argmax(pred,1), tf.argmax(y,1))
#print("correct pred " + str(correct_pred))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
init = tf.global_variables_initializer()

with tf.Session() as session:
    session.run(init)
    step = 0
    offset = random.randint(0,n_input+1)
    end_offset = n_input + 1
    acc_total = 0
    loss_total = 0

    writer.add_graph(session.graph)

    while step < training_iters:
        if offset > (len(training_data)-end_offset):
            offset = random.randint(0, n_input+1)

        symbols_in_keys = [ [dictionary[ str(training_data[i])]] for i in range(offset, offset+n_input) ]
        symbols_in_keys = np.reshape(np.array(symbols_in_keys), [-1, n_input, 1])
        symbols_out_onehot = np.zeros([vocab_size], dtype=float)
        symbols_out_onehot[dictionary[str(training_data[offset+n_input])]] = 1.0
        symbols_out_onehot = np.reshape(symbols_out_onehot,[1,-1])
        _, acc, loss, onehot_pred = session.run([optimizer, accuracy, cost, pred], \
                                                feed_dict={x: symbols_in_keys, y: symbols_out_onehot})
        loss_total += loss
        acc_total += acc
        if (step+1) % 1000 == 0:
            print("Time = " + str(step+1))
            print("Error = " + "{:.6f}".format(loss_total/1000))
            print("Accuracy = " + "{:.2f}%".format(100*acc_total/1000))
            print("-----------------------------")
            acc_total = 0
            loss_total = 0
            symbols_in = [training_data[i] for i in range(offset, offset + n_input)]
            symbols_out = training_data[offset + n_input]
            symbols_out_pred = reverse_dictionary[int(tf.argmax(onehot_pred, 1).eval())]
        step += 1
        offset += (n_input+1)
       # offset += random.randint(0, n_input+1)

    print("Optimization Finished!")
    while True:
        prompt = "%s word: " % n_input
        sentence = input(prompt)
        sentence = sentence.strip()
        words = sentence.split(' ')
        if len(words) != n_input:
            print("Please run the program again and enter 1 word.")
            continue
        try:
            symbols_in_keys = [dictionary[str(words[i])] for i in range(len(words))]
            for i in range(32):
                keys = np.reshape(np.array(symbols_in_keys), [-1, n_input, 1])
                onehot_pred = session.run(pred, feed_dict={x: keys})
                onehot_pred_index = int(tf.argmax(onehot_pred, 1).eval())
                sentence = "%s %s" % (sentence,reverse_dictionary[onehot_pred_index])
                symbols_in_keys = symbols_in_keys[1:]
                symbols_in_keys.append(onehot_pred_index)
            print(sentence)
        except:
            print("Sorry! I'm too dumb for that word. Pick a word from the training text. :D")
