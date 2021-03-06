---
layout: post
title: A Somewhat Artsy Introduction to ML
---

*This blog post is a transcription of the introductory talk I delivered for an AI+Art [workshop](https://aiandart.wixsite.com/creaite). As a result, it begins with artistic applications of machine learning.*

## What happens when art interacts with technology?

[![First Photograph](https://i0.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-05-at-7-36-07-pm.png?ssl=1&w=450)](https://upload.wikimedia.org/wikipedia/commons/5/5c/View_from_the_Window_at_Le_Gras%2C_Joseph_Nic%C3%A9phore_Ni%C3%A9pce.jpg)

This is the first photograph that was ever taken. It was taken by Joseph Niepce around 1826. This is the view from an upstairs window at his estate. Nowadays, photographs look more realistic and colorful and vibrant, like the ones in National Geographic. I imagine that when Joseph Niepce took this photograph, he could have never foreseen the many directions photography has taken art over the years. 

Then we get to digital art, which is a huge field today. Below we can see an example of photoshop, as this image has definitely been photoshopped like crazy!

[![Funny Photoshop](
https://i1.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-05-at-7-36-16-pm.png?ssl=1&w=450)](
https://s-media-cache-ak0.pinimg.com/originals/c9/b8/c4/c9b8c4461b9b1c1dc2b8beb6cb9519c2.jpg)

We see PhotoShopped images in our daily lives all the time, from magazine covers to advertisements to Instagram pictures. Indeed, the ability to digitally edit images has fundamentally altered the art of photography. Crucially, this isn't machine intelligence. Why not?

**Answer: none of these are machine intelligence, because a human is doing the thinking.**

This post is concerned with what happens when the machine is more than a tool, when it can make intelligent decisions.

## So what does machine-generated art look like?

![ml art](https://i1.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-05-at-7-18-51-pm.png?ssl=1&w=450)

[![ml art](
https://i1.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-05-at-7-18-51-pm.png?ssl=1&w=450)](
https://theredlist.com/media/database/fine_arts/arthistory/painting/realism_figurative_painting/georgia-o-keefe/015-georgia-o-keefe-theredlist.jpg)

This is an example of style transfer! We'll go more into this concept in a later post. When my face is merged with a flower painting, it takes on some...interesting qualities. Note that this *is* machine intelligence, because the computer is making all the image-altering decisions.

Let's look at another transformation.

**Before:**

[![ml art](https://i1.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-05-at-7-38-26-pm.png?ssl=1&w=450
)](
https://farm8.staticflickr.com/7294/8732030861_1a72dec272_b.jpg)

**After:**

[![ml art](https://i2.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-05-at-7-38-33-pm.png?ssl=1&w=450
)](
https://farm8.staticflickr.com/7294/8732030861_1a72dec272_b.jpg)


Interestingly, the machine found a pattern of a bird inside these abstract swirls! This was made with Google's DeepDream. Imagine how hard it would be to PhotoShop this.

## To get a closer look at machine learning, let’s investigate Snapchat filters.

People my age use something called the puppy-dog face filter, where the camera superimposes a puppy’s nose over their own and give themselves puppy ears.
Here's an example of Ariana Grande with the puppy face filter.

[![puppy filter](https://i0.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-05-at-7-34-41-pm.png?ssl=1&w=450
)](http://assets.teenvogue.com/photos/579918989e016460296a15a2/master/pass/2%20-%20Ariana%20Grande.jpg)


## What’s going on here?

(Note: Snapchat’s algorithm isn’t available to the general public, but several journalists have published articles on the high-level version.)

In order to give you puppy ears, Snapchat first has to identify the different parts of your face. To do this, it constructs a
facial mesh or "point mask".

[![mesh ex.](https://i1.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-05-at-7-39-32-pm.png?ssl=1&w=450)](
https://petapixel.com/2016/06/30/snapchats-powerful-facial-recognition-technology-works/)

The mesh uses **computer vision**, which involves understanding images. 

Snapchat’s algorithm **learns** from thousands of face pictures manually tagged with these dots,
Then it **predicts** where the nose is in every new face that uses the puppy filter!

(Learning & prediction are two key concepts in machine learning!)

# What is machine learning?

All this Snapchat talk leads us to a definition: broadly speaking, machine learning is learning from data. We just saw an example of that!

It works similar to our brain. Just like us, it learns from observing, predicting, and self-correcting. To see how it works, let’s take an example.

(This example was adapted from Michael Nielsen’s wonderful [book] (http://neuralnetworksanddeeplearning.com/)

Suppose the weekend’s coming up, and you heard of a concert. You have to make a decision: do you go to the concert? Or stay home?

[![simple brain diagram](https://i1.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-05-at-7-45-51-pm.png?ssl=1&w=450)](
https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=0ahUKEwjf8cXzwpHVAhUC-GMKHZnLBUAQjBwIBA&url=http%3A%2F%2Fclipartsign.com%2Fdl.php%3Fd%3D1842&psig=AFQjCNFX3ELQAeMYAThepSCDNdqaoqCOcg&ust=1500422330517855)

Well, this isn’t enough information for you to make a decision yet! There are several factors that might affect your decision:
1. Do I have a test coming up? If so, which class is it in?
3. What’s the weather going to be like?
4. Do I have a friend who wants to come? Who?
5. How much do I really like the band?

But these factors aren’t all equal! For example, I really like Fall Out Boy, and will go to a concert even in the pouring rain. Some may be more important, or have a higher **weight**. (Weights are also a key concept in machine learning.)

[![brain diagram](
https://i2.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-05-at-7-46-59-pm.png?ssl=1&w=450)](
https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=0ahUKEwjf8cXzwpHVAhUC-GMKHZnLBUAQjBwIBA&url=http%3A%2F%2Fclipartsign.com%2Fdl.php%3Fd%3D1842&psig=AFQjCNFX3ELQAeMYAThepSCDNdqaoqCOcg&ust=1500422330517855)

## Problem

Suppose we want a computer to solve this problem. Computers don’t know how important these factors are! (or, in other words, what weights to give them).

At least, not right away.

## Solution

They **learn** the weights by studying lots and lots of examples. This comes back to our definition: machine learning is learning from data.

To understand how a machine learns from data, let’s take a simple example: linear regression.

Suppose I go around my school and ask nine kids: what’s your current grade? How many hours of homework do you have each night?
Then I plot the answers on this graph.

![graph #1](https://i0.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-05-at-7-48-39-pm.png?ssl=1&w=450)

A new person enrolls at my school, and I know their current grade. I want to predict: how many hours of homework would they have? Graphically, it would look like this:

![graph #2](https://i2.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-05-at-7-48-46-pm.png?ssl=1&w=450)

What's the best way for me to predict the y-value for the purple dot?

(Take a moment or two to think about this)

Answer: Fit a line to the data!

![graph #3](https://i2.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-05-at-7-48-50-pm.png?ssl=1&w=450)

Then we can nicely predict where the purple dot is going to fall.

![graph #4](https://i1.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-05-at-7-48-56-pm.png?ssl=1&w=450)

What if we want a computer to learn this function?

## Goal: Guess f(x)!

Let's assume f(x) is linear, so we can write y = wx + b. We don't know what *w* and *b* are. Let's guess.

Guess #1:

![guess graph 1](https://i2.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-05-at-7-53-00-pm.png?ssl=1&w=450)

Guess #2:

![guess graph 2](https://i0.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-05-at-7-53-06-pm.png?ssl=1&w=450)

Guess #3:

![guess graph 3](https://i1.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-05-at-7-53-12-pm.png?ssl=1&w=450)

## Measuring Loss

At this point, we have many guesses, but no way of comparing them to each other. How do we know how good our guess is?

Let's measure **loss**. Loss is defined as the penalty for a wrong prediction. There are many different ways researchers use to compute this, such as the root mean squared error (RMS), and many others, but they're not very important. The most important idea regarding loss is that: less loss is better than more loss.

The two graphs below demonstrate measuring loss for different functions.
Question: Which function has the *most* loss? Which one is better?

![loss graph 1](https://i0.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-05-at-8-04-56-pm.png?ssl=1&w=450)

![loss graph 2](https://i2.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-05-at-8-05-10-pm.png?ssl=1&w=450)

(Answer: The first one.)

Cool! So we can guess functions, and evaluate how good or bad they are. Our goal now is to minimize the loss. We can do this using an optimization algorithm called gradient descent. Gradient descent is beyond the scope of this post--you can explore it further in this wonderful [explanation](http://ucanalytics.com/blogs/intuitive-machine-learning-gradient-descent-simplified/).
The main idea is that we adjust our weights to arrive at the minimum loss.

## Recap

- **linear regression** is fitting a line to data
- Steps:
  1. Randomly choose *w* and *b* (in y = wx + b)
  2. Calculate our loss ("less loss" means we are closer to the optimal function)
  3. Adjust our weights until we arrive at the smallest loss

Suppose this is the line we finally arrive at.

![final line](https://i1.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-06-at-7-28-23-pm.png?ssl=1&w=450)

## Why do we even care?

The line we came up with doesn't get every data point exactly right. Why should we even try?

See, the value of machine learning is not just telling us what we already know. The real value is in using machines to predict data we have never seen before. Fitting a line allows us to create a *generalized* function so that we can predict values for new data.

So now we know how to fit a line to our homework hours vs. grades data. What if we want to fit a nonlinear function? Not everything in life can be explained linearly! How can we improve?

Let's think carefully about what kind of nonlinear function we want.

Does this look like a nice function?

![overfitting graph](https://i2.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-06-at-7-31-44-pm.png?ssl=1&w=450)

If your answer is NO, please skip the section below. Else follow along.

## Overfitting

Suppose we do use the function above, and a new person walks in the room.

![overfit graph](https://i0.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-06-at-7-34-03-pm.png?ssl=1&w=450)

Let's use f(x) to predict how many homework hours they have!

![graph](https://i1.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-06-at-7-34-09-pm.png?ssl=1&w=450)

Wait...is this the best prediction?

There's a theorem called Occam's Razor, which holds that the simplest explanation is most often the correct one. Occam's Razor would apply here. We're overcomplicating this function.

This is a problem where the function we have is *too specific* to our training data. There's a term for this--**overfitting**, which happens when our function doesn't generalize to unfamiliar data. And if it can't do that, what's the point of applying fancy algorithms?

For some real-world overfitting examples, check out [this](https://stats.stackexchange.com/questions/128616/whats-a-real-world-example-of-overfitting) StackOverflow thread.

---

So we don't want a nonlinear function which overfits. What about a function like the one below?

![nonlinear graph](https://i2.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-06-at-7-43-56-pm.png?ssl=1&w=450)

It seems to fit the data reasonably, and isn't ridiculously specific to the data we already know. How could we model a function like this?

**In general, for learning nonlinear functions, we want to use activation functions & neural networks.**

---

The inventor of the first neurocomputer defines a neural network as:

'''
"...a computing system made up of a number of simple, highly interconnected processing elements, which process information by their dynamic state response to external inputs.
In "Neural Network Primer: Part I" by Maureen Caudill, AI Expert, Feb. 1989
'''

A neural network takes in the weights and input data, and outputs a function. Below is a model where the green dot represents a general neural network.

![nn](https://i2.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-06-at-7-46-04-pm.png?ssl=1&w=450)

If we dive into this green dot, we'll find many other circles (which I'll call neurons), all of which are connected to each other. Neurons are organized into layers, such that the output of a neuron in layer X is the input of a neuron in layer X+1.

![full nn](https://i1.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-20-at-8-27-36-pm.png?ssl=1&w=450)

Most often, there are other layers in between the input and output layer. Their job is to transform the input into something the output can use.

![hidden layers](https://i0.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-20-at-8-32-49-pm.png?ssl=1&w=450)

To model nonlinearity, the network puts the outputs of individual neurons through a function such as a rectified linear unit, aka a ReLU.

![relu](https://i1.wp.com/nanditanaik.files.wordpress.com/2017/09/screen-shot-2017-09-06-at-7-51-55-pm.png?ssl=1&w=450)

A ReLU is defined as f(x) = max(0,x). There are many other kinds of nonlinear functions, but a ReLU is one of the simplest.

## How does an activation function work?

On a mathematical level, when we pass a value from one neuron to the other, we're composing the functions of those various neurons. (By function composition, I mean

Therefore if f~1, f~2, ..., f~n are the various functions of neurons, our output layer is going to be f~n(f~(n-1)...f~1).

If all those functions are linear, the composition of linear functions is also a linear function. Our output is also going to be linear! Oh no! That means there's no difference between our network and linear regression!

That's why we need an activation function, so that we're actually composing non-linear functions. This means we can model any function, no matter whether it is linear or not.

# Zooming out...

A powerful neural network can, with these somewhat-simple tools, can process millions of any kind of data, learn the properties of that data, and generalize those properties to data it’s never seen before. For more learning resources, check out my other [post](https://nnaik39.github.io/Resources/).
