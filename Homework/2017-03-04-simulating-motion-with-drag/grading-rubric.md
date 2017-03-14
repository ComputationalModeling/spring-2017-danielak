# Modeling Motion with Drag

## Grading Rubric

Working as a class, you desuigned this rubric together, with an emphasis on it weighing conceptual understanding much more than valuing the right answer.

### Setup (including setting initial values) - 25%

- Explanation and style (80%)
- Is it correct (20%)

### Plots (position vs. time, velocity vs. time, acceleration vs. time) - 25%

- Explanation and style (80%)
- Is it correct (20%)

### Handling data (creating columns, a dataframe, and appending to a data frame) - 25%

- Explanation and style (80%)
- Is it correct (20%)

### Updating variables by looping over time steps - 25%

- Explanation and style (80%)
- Is it correct (20%)

### How long does it take to hit the ground - 5% bonus

- is your one final number correct?

## A note about explanations 

One way to think of an explanation is like this: imagine you were talking to a high school student. This student knows the basics of python, but has never taken our modeling course or done any modeling/data science in python. How would you explain your code to that student?

Also, you can embed explanations in your code like this, using either the `#` sign or triple quotes `"""`:

```python
acceleration = acceleration + drag # drag slows the object down
"""
Drag turns out to be a function of several different quantities:

- the cross-sectional area of the object
- its drag coefficient
- the density of the fluid
- the velocity of the object
"""
```

## A note about style

In general, you'll want to do the following:

- Use descriptive variable names
- Use code comments to annotate your code
- Break long lines that scroll off the screen into several shorter lines

For reference, take a look at [Pep-8 style Python](https://www.python.org/dev/peps/pep-0008/), and in particular, [guidance on using whitespace](https://www.python.org/dev/peps/pep-0008/#whitespace-in-expressions-and-statements)
