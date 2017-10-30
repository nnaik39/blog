---
layout: post
title: Making Code Write Poetry
---

For a long time, I’ve nurtured two interests: coding and creative writing. Competitive coding is like solving a puzzle. You’re given a problem, now find an algorithm to solve it. Ready, set, go!
Creative writing is more like the process of designing a puzzle. You use language to evoke an emotion, then dive behind the scenes and craft your characters to convey that feeling. This was a part of my life which I honestly never believed could mesh with coding. How could it? How can computers express emotion?
At SAILORS, I learned about natural language processing. We listened to lectures about computational linguistics. Also, my small group focused on NLP, classifying tweets for disaster relief.
When summer ended, I kept what I had learned at SAILORS in the back of my mind. Sure, computers can understand words. But can they put words together in an expressive way? This question sparked my interest in generative natural language processing.
During my sophomore year, I built a recurrent neural network which writes poetry. It is trained on a poem I wrote and some English romance novels. Here are some of its lines:
*i skateboard the forest ravens to her i was me dream of the tell of forest from the forest of those we her steel i steel of nests was i was a me deny her nothing! tumbling my i was the forest we a the forest and the yellow and the wild and the he?*

Making this poetry generator got me thinking about meshing coding and literature. I had found a place where I belonged.

**Technical Details**

To summarize the technical details, my project was structured as a five-layer LSTM. In SAILORS, we learned about scikit-learn, the machine learning library. I used a similar library called TensorFlow.
Here is a code snippet which reveals the architecture of my network:

> def RNN(x, weights, biases):
             rnn_cell = LSTMCell(n_hidden)
             rnn_cell = MultiRNNCell([rnn_cell]*2)
             outputs, states = rnn.static_rnn(rnn_cell, x, dtype=tf.float32)
             return tf.matmul(outputs[-1], weights[‘out’]) + biases[‘out’]
>

Getting this to work was a struggle! Initially, it was overfitting like crazy. Overfitting is when your ML algorithm fits too specifically to the training data. In this case, overfitting looked like nine pages of the word “and”, since that word occurred nearly 19 thousand times in the training texts, and it got lazy.

The solution is to add a dropout wrapper around the RNN Cell. Dropout is a technique to prevent overfitting. The way it works is you randomly drop some of the outputs from the neurons.

The intuition behind this is quite pretty! In overfitting, one of the hidden layer neurons is dominating, and doing all the work. This means that the output will have a much higher weight than the others. So by dropping outputs from a randomized neuron, you force all the neurons to learn the relevant characteristics, which thereby reduces overfitting.

So I added in this line,

>         rnn_cell = DropoutWrapper(rnn_cell, output_keep_prob=0.5), 

right between the LSTM Cell and the two MultiRNNCells. Problem solved!

** Connections to Humanity **

While a lot of what my network wrote was frivolous, there were some lines that I found relevant to thinking about AI’s relationship to humanity. Take this line:
*singing and and the warnings and the anxiety: and the fright.so and the battle—there and and the and the romance,” and the happily, and the and*
Here my network is connecting actions to commonly felt feelings. Connecting “singing” to “anxiety”, for example, is really common amongst humans, and I think it’s cool that my network was able to learn this relationship. Also, we can see it has learned the grammar of a quotation mark (while not doing so well with periods)! In addition, it picks up on the relationship between the word “romance” and “happily”, which is very important since we think of romances as ending happily ever after.
I think this line has insight. It sounds startlingly human–connecting fear and a battle, romance and happiness, singing and anxiety. Fear and insecurities are deeply human emotions, and I’m proud that my network is learning to capture these in language.
Going forward, I want to keep learning about the intersection of coding and literature. SAILORS showed me what natural language processing could do. Seeing a computer put words together and create emotional depth was inspiring. Now, I feel that I know where I want to be.
