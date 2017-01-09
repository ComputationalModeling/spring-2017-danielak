# Random numbers

There are many tasks in modeling where you may need random numbers as a part of the modeling process.  This can be used to generate statistically samples, to simulate processes that happen in a probabilistic way (i.e., the outcomes of games like poker, dice, blackjack, or radioactive decay), or to add some element of randomness to types of simulations studying how groups of things interact or otherwise behave.  Random numbers are also important in cryptography and in making video games!

In the actual physical world we generate randomness by rolling dice, flipping a coin, or shuffling a deck of cards and pulling one out.  Computers can't do that, though!

All programming languages have tools for generating random numbers, which are called "random number generators."  They are **not actually random** - they are what is known as "pseudo-random."  This means that the numbers are random in a statistical sense, but can be reproduced perfectly if you know the algorithm for doing so.  If you need truly random numbers, you generally have to use some piece of computer hardware that is built specifically for it.

Python has two tools for generating random numbers: the Python ```random``` module, and the numpy ```numpy.random``` module.  Both have a few functions that all do similar things.  I'll show the Python internal one, but the main difference is that the numpy random tools can return arrays of random numbers, whereas the python tools generally just do single random numbers at a time.  Also, numpy generates random numbers in distributions with many shapes.

seed() - this is something you can call before you start using random numbers, which will ensure you get the same set of numbers each time.  If you do not use this it's fine - the computer will use the current system time to seed the RNG!

**example** - show how to use this.

random() - this generates a random floating-point number evenly distributed between [0,1) - meaning that it can be zero, but can't be 1.  If you want a set of random numbers between (a, b), you would do a + (b-a)*random().  uniform(a,b) also does the same thing.

**example** - create a random float, keep running it over and over.  see that it's different.  But, do the seed, and show that if I run the seed every time it's the same.  But, if I do the seed once and then call the random number geneator several times, I get varying values.

randint(a,b) - returns a random integer N such that a <= N <= b.  (a, b must be integers).  uniformly sampled between a,b


gauss(mu,sigma) - returns a gaussian distribution (bell curve) with mu as the mean and sigma as the standard deviation.  This means that values are more likely to be by mu.

shuffle(list or array) - takes the list or array and shuffles it in-place.  This is often useful for doing all sorts of things.

**example** of this - create a list and shuffle it.

Emphasize that there are lots of other useful tools in the python random module and in the numpy one.  Go browse through that when you need random numbers for something - often you'll see they have exactly what you need!

## What have we learned?

* The ability to generate (pseudo)-random numbers is very useful when writing computer programs
* Python has a ```random``` module, and numpy has ```numpy.random```  [both of which have similar features, though numpy works on arrays and has more stuff]
* Both of these modules allow you to generate random floating-point numbers and integers [either uniformly distributed over an interval or in some other distribution,] and to shuffle lists and arrays

## Useful links

* [Python random module](https://docs.python.org/3/library/random.html)
* [Numpy random module](http://docs.scipy.org/doc/numpy/reference/routines.random.html)
* [Random Number Generation on Wikipedia](https://en.wikipedia.org/wiki/Random_number_generation)
* [Applications of Randomness on Wikipedia](https://en.wikipedia.org/wiki/Applications_of_randomness)
