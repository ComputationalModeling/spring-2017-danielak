# Order of magnitude modeling video

In this video we're going to learn about something called an "order of magnitude model," which is useful for getting quick, approximate estimates of quantities.

This technique is often called a  "Fermi Question" or a "Fermi Problem," and is named after the physicist Enrico Fermi, because he was well-known for his ability to make good approximate questions with very little data.

These types of problems generally involve making justified guesses about quantities and their possible ranges.

They're commonly used because they give estimates that can check more complex models - if a complicated model of a similar situation produces wildly different results, it's worth looking into it a bit more!

As long as the initial assumptions in the estimate are reasonable, the result obtained will give an answer within the same scale as the correct result.  If it's not it gives you a place to start for  understanding why this is the case.

So, how does this type of model work?

The core of solving a Fermi problem is *dimensional analysis*, which is a fancy term for "unit conversion".  The basic idea is as follows:

How fast is 10 miles/hour in feet per second?

10 miles/hour * 1 hour/3600s * 5280 feet/mile = 14.67 feet/s

Many OOM questions are solvable by guessing at some starting value and then using unit conversions to get the answer you want along with reasonable guesses about values.  You may need to use a bit of geometry, etc. along the way.

So, here's the process:

1. You pose a question you want to know the answer to
2. You need to know more information to answer the question, so you start making conversions and guessing at the value of those conversions if you don't know them.
3. Guess at the range of values you might have for each part of your model.

So, let's do an example:  **How many babies are born each day?**

We need to know:

* How many people there are in the world
* What fraction of them are women
* How many babies the average woman has in their lifetime
* How long the average woman live?
* If you pick a woman at random, what's the probability she is giving birth today?

Some useful info:

* world population = 7.4 billion  (guess 5-10 billion)
* female fraction = 49.6%  (guess half)
* 1 woman has 2.33 births in 1 lifetime (let's say 2-4)
* worldwide life expectancy is 73.5 years (let's say 60-80)

(# babies born today) = (# women) * (probability of a woman having a baby today, p_baby)

p_baby = N_babies / lifetime in days

We get a number that's somewhere around 3.3e5, with a range of 1.7e5-9e5

And the UNICEF estimate, using a much more sophisticated estimate, is 353,000/day.  Not bad!

