---
layout: post
title: Odd Behaviors
---

So you know how most high schools have homecoming week, a week where people twin during the days, wear pom-poms, attend pep rallies, and generally cheer their heads off while dancing around wildly?

Well, my school has Math Burst week! Math Burst is a week devoted to researching open math problems and presenting them at a symposium.
Although cheering is involved, a lot of Math Burst feels like this: ![Thomas Edison Quote](/res/te-quote.png)

Math Burst is a choose-your-own adventure type of deal. Last year, me and my friend investigated playing a bread-passing game in 3D; this year, I’m part of the group which (apparently) figures out the best way to hit a pedestrian with a car. (Our math teachers have very dry senses of humor.)

Yet math research can be frustrating. Last year, a half of my group didn’t get anywhere with their subproblem. A lot of the times, you don’t know what to do, or you have a result but you don’t know where to go from there. Other times, you end up finding counterexamples to what you are trying to prove!

Last year, I was part of the combinatorial games group. We investigated a game called the bread-passing game, although it goes by other names, like a Galton board.

## How the Bread Game Works

Consider a circle of n people. One person begins with a piece of bread. Let’s call him Greenie.

![Demo #1](\res\demogame-1)

(The line wraps around.)

Now Bluey and Purplie don’t appreciate how greedy Greenie is being, so they force him to break his bread and give half to both of them.

![Demo #2](\res\demogame-2)

The people are still unhappy with this arrangement, so then Bluey and Purplie break their bread in half and pass it to both of their neighbors on either side.

![Demo #3](\res\demogame-3)

## Patterns

Now let’s play with n, the number of people in this game. I encourage you to mess around with the numbers! (Fractions…fun!)

After a while, we notice a pattern.

If n is even, then at any point in time after a few rounds have passed, exactly n/2 people will be holding a piece of bread. The other n/2 people will have no bread in their hands.

If n is odd, then after an arbitrary amount of time t, n people will be holding a piece of bread.

We can visualize this with connectivity graphs. In this case, a node is a person, and the vertices are connections between neighbors.

Here is a graph of the game with four people: ![Fourppl](\res\fourppl.png)

This is a graph with three people: ![Threeppl](\res\threeppl.png)

We will arrive at the explanation for this later. For now, let’s push this whole party game thing a bit further, and ask ourselves: what happens if we play the game in 3D?

## A Whole New World (or Dimension)

It was at this point that me and my friend branched off from the rest of our group. The other members were committed to finding a formula that would solve the Galton board–i.e. give you the optional strategy for retaining the bread. Sadly, they did not find a formula.

My friend had a crazy idea: why don’t we try playing this game in three dimensions? I, being equally as crazy, latched onto the idea with enthusiasm.

So we put our players onto the vertices of a tetrahedron, cube, and a dodecahedron and ran the numbers.

Here’s what we got:
![Tetrahedron](\res\tetrahedron.png)
![Cube](\res\cube.png)
![Dodecahedron](\res\dodecahedron.png)

Well, well, well! What do we have here?

Our earlier hypothesis, that the behavior of a game depends on the number of players, doesn’t work here! A tetrahedron, cube, and dodecahedron all have an even number of vertices. So what is going on here?

Let’s take a look at the connectivity graph of a tetrahedron, which exhibits “odd” behavior (lol), and the connectivity graph of a cube, which exhibits “even” behavior. As you can see, I’ve colored the vertices red and blue, and colored certain edges green.
