---
layout: post
title: Solving the Knapsack Problem with a Genetic Algorithm
---

The knapsack problem is in optimization: given a set of N items, each with a weight and a value, what is the optimal subset of them which keeps the total weight under a fixed number and maximizes the total value? The name refers to a common problem in packing luggage, and this problem appears in a lot of different fields like cryptography and investments and portfolios.

There are three types of the knapsack problem. The most common is the 0-1, where only one of each item in the set is provided. In this, the total number of subsets would be 2^n, and you must choose the optimal subset whose weight is under a value and whose total value is maximal.

Another is the bounded knapsack problem, where the quantities of each item can be more than 1, but are restricted to a given value c. There is also an unbounded knapsack problem, where there is no upper limit on how much of an item can be in the knapsack. Both these problems have the same objective: maximize value, keep weight under a fixed value.

There is a particularly interesting solution to the 0-1 problem called the genetic algorithm. This optimization algorithm is inspired by evolution. Basically, the "population" is a random initialization of problem solutions. A fitness function evaluates the quality of the individuals, and then a parent selection takes place. Then the offspring is "mutated".

How can this solve the 0-1 knapsack problem? We can represent every possible solution with a binary string. Then we pick two at random out of the population, and choose the better one. This one will generate offspring, and a random calculation will determine whether the offspring is mutated. Then survivors are selected. This algorithm terminates if there was no improvement over the last 25 generations.
