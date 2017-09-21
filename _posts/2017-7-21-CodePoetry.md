---
layout: post
title: Making Code Write Poetry
---

Ever since my independent AI study in spring, I’ve been pretty excited about machine learning and what it can do! My AI study culminated in a recurrent neural network which writes poetry. The way it works is, you give it a word and then it generates the 32 words after. Attached are some of its musings:

> i skateboard the forest
 ravens to her i was me
 dream of the tell of forest
 from the forest of those we her steel
 i steel of nests was i was a me deny her nothing!
 yellow and and the and to the climax and that the then the instance; and and the passion-song and the owe.
 tumbling my i was the forest we a the forest
 and the yellow and the wild and the he?
>

(I have pages and pages of this, by the way. Maybe one day I’ll try submitting them to a journal :))

Making this poetry generator (my friend referred to it as the “Robot of Humanities”) was really cool, and got me seriously thinking about the implications of AI in fields like literature.

## Technology I Used to Create This

So my project was structured like a five-layer LSTM. In general, we want to use recurrent neural networks when we’re dealing with language because recurrent neural networks can remember. I used the TensorFlow machine learning library.

Here is the code snippet which reveals the architecture of my network:

> def RNN(x, weights, biases):
    x = tf.reshape(x, [-1, n_input])
    x = tf.split(x,n_input,1)
             rnn_cell = LSTMCell(n_hidden)
             rnn_cell = MultiRNNCell([rnn_cell]*2)
             outputs, states = rnn.static_rnn(rnn_cell, x, dtype=tf.float32)
             return tf.matmul(outputs[-1], weights[‘out’]) + biases[‘out’]
>
Getting this to work was a struggle! Initially, it was overfitting like crazy. Overfitting is when your ML algorithm fits too specifically to the training data. In this case, overfitting looked like nine pages of the word “and”, since that word occurred nearly 19 thousand times in the training texts, and it got lazy.

The solution is to add a dropout wrapper around the RNN Cell. Dropout is a technique to prevent overfitting. The way it works is you randomly drop some of the outputs from the neurons.

The intuition behind this is quite pretty! In overfitting, one of the hidden layer neurons is dominating, and doing all the work. This means that the output will have a much higher weight than the others. So by dropping outputs from a randomized neuron, you force all the neurons to learn the relevant characteristics, which thereby reduces overfitting.

So I added in this line,

>             rnn_cell = DropoutWrapper(rnn_cell, output_keep_prob=0.5),

right between the LSTM Cell and the two MultiRNNCells. Problem solved! 🙂

## Thought-Provoking Poetry

While a lot of what my network wrote was frivolous (it was trained on romance novels, after all), there were some lines that I found relevant to thinking about AI’s relationship to humanity. Take this line:

singing and and the warnings and the anxiety: and the fright.so and the battle—there and and the and the romance,” and the happily, and the and

Here my network is connecting actions to commonly felt feelings. Connecting “singing” to “anxiety”, for example, is really common amongst humans, and I think it’s really cool that my network was able to learn this relationship. Also, we can see it has learned the grammar of a quotation mark (while not quite doing so well with the period)! In addition, it picks up on the relationship between the word “romance” and “happily”, which is very important since we think of romances as ending happily ever after.

I think this line is beautiful. It sounds startlingly human–connecting fright and battle, romance and happily, singing and anxiety.

If I was to rearrange this into a coherent sentence, what would it be? “I get anxious from singing and warnings; and frightened of battles, romance, and happily ever afters.” Fear and insecurities are deeply human emotions. Amazing!

I’m pretty excited about the work my poetry writer has done. We can let this code have its own happily ever after.
