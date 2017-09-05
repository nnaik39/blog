---
layout: post
title: A Somewhat Artsy Introduction to ML
---
*note: in progress*

*This blog post is a transcription of the introductory talk I delivered for an AI+Art [workshop](https://aiandart.wixsite.com/creaite). As a result, it focuses on artistic applications of machine learning.*

## What happens when art interacts with technology?

[![First Photograph](https://upload.wikimedia.org/wikipedia/commons/5/5c/View_from_the_Window_at_Le_Gras%2C_Joseph_Nic%C3%A9phore_Ni%C3%A9pce.jpg)](https://upload.wikimedia.org/wikipedia/commons/5/5c/View_from_the_Window_at_Le_Gras%2C_Joseph_Nic%C3%A9phore_Ni%C3%A9pce.jpg)

This is the first photograph that was ever taken. It was taken by Joseph Niepce around 1826. This is the view from an upstairs window at his estate. Nowadays, photographs look more realistic and colorful and vibrant, like the ones in National Geographic. I imagine that when Joseph Niepce took this photograph, he could have never foreseen the many directions photography has taken art over the years. 

Then we get to digital art, which is a huge field today. Below we can see an example of photoshop, as this image has definitely been photoshopped like crazy!

[![Funny Photoshop](
https://s-media-cache-ak0.pinimg.com/originals/c9/b8/c4/c9b8c4461b9b1c1dc2b8beb6cb9519c2.jpg)](
https://s-media-cache-ak0.pinimg.com/originals/c9/b8/c4/c9b8c4461b9b1c1dc2b8beb6cb9519c2.jpg)

We see PhotoShopped images in our daily lives all the time, from magazine covers to advertisements to Instagram pictures. Indeed, the ability to digitally edit images has fundamentally altered the art of photography. Crucially, this isn't machine intelligence. Why not?

** Answer: none of these are machine intelligence, because a human is doing the thinking. **

This post is concerned with what happens when the machine is more than a tool, when it can make intelligent decisions.

## So what does machine-generated art look like?

[insert example]

To get a closer look at machine learning, let’s investigate Snapchat.
People my age use newfangled filters, like the puppy-dog face filter, where they can superimpose a puppy’s nose over their own and give themselves puppy ears.
[insert example below]

## What’s going on here?

(Note: Snapchat’s algorithm isn’t available to the general public, but several journalists have published articles on the high-level version.)

In order to give you puppy ears, Snapchat first has to identify the different parts of your face. To do this, it constructs a
facial mesh or "point mask".

[insert image below]

The mesh uses **computer vision**, which involves understanding images. 

Snapchat’s algorithm **learns** from thousands of face pictures manually tagged with these dots,
Then it **predicts** where the nose is in every new face that uses the puppy filter!

(Learning & prediction are two key concepts in machine learning!)

# What is machine learning?

All this Snapchat talk leads us to a definition: broadly speaking, machine learning is learning from data. We just saw an example of that!

It works similar to our brain. Just like us, it learns from observing, predicting, and self-correcting. To see how it works, let’s take an example.

(This example was adapted from Michael Nielsen’s wonderful [book] (http://neuralnetworksanddeeplearning.com/)

Suppose the weekend’s coming up, and you heard of a concert. You have to make a decision: do you go to the concert? Or stay home?

[insert image]

Well, this isn’t enough information for you to make a decision yet! There are several factors that might affect your decision:
1. Do I have a test coming up? If so, which class is it in?
3. What’s the weather going to be like?
4. Do I have a friend who wants to come? Who?
5. How much do I really like the band?

But these factors aren’t all equal! For example, I really like Fall Out Boy, and will go to a concert even in the pouring rain. Some may be more important, or have a higher **weight**. (Weights are also a key concept in machine learning.)

[insert diagram]

## Problem

Suppose we want a computer to solve this problem. Computers don’t know how important these factors are! (or, in other words, what weights to give them).

At least, not right away.

## Solution

They **learn** the weights by studying lots and lots of examples. This comes back to our definition: machine learning is learning from data.

To understand how a machine learns from data, let’s take a simple example: linear regression.

Suppose I go around my school and ask nine kids: what’s your current grade? How many hours of homework do you have each night?
Then I plot the answers on this graph.

[insert graph]

A new person enrolls at my school, and I know their current grade. I want to predict: how many hours of homework would they have? Graphically, it would look like this:

[insert graph]

What's the best way for me to predict the y-value for the purple dot?

(Take a moment or two to think about this)

Answer: Fit a line to the data!

[insert graph]

Then we can nicely predict where the purple dot is going to fall.

[insert graph]

What if we want a computer to learn this function?

## Goal: Guess f(x)!

Let's assume f(x) is linear, so we can write y = wx + b. We don't know what *w* and *b* are. Let's guess.

Guess #1:

[insert graph]

Guess #2:

[insert graph]

Guess #3:

[insert graph]

