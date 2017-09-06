---
layout: post
title: A Somewhat Artsy Introduction to ML
---
*note: in progress*

*This blog post is a transcription of the introductory talk I delivered for an AI+Art [workshop](https://aiandart.wixsite.com/creaite). As a result, it focuses on artistic applications of machine learning.*

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

