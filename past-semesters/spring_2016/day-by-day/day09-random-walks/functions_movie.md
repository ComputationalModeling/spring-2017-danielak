# Functions

So far we've mainly been working with small pieces of code.  However, as your programs grow it's often useful to think about a way to break a big program up into smaller pieces to make it easier to write, to read, and to debug.  Also, there are some pieces of code (like a tool to make a plot, or calculate the cosine of an angle) that are useful for lots of different purposes, not just whatever it is that you're doing right now.  

These pieces of code are referred to as "functions", and are a self-contained piece of code that accomplishes a specific task.  

Python has lots of these functions - you've already been using them!  range() is a function, as is print(), and so is the matplotlib plot() command.

Functions are very handy for two reasons:

1.  Reusability.  Once you define a function, you can use it over and over again, either within the same program or in different programs.  For example, you can use the plot() function wherever you want and you don't have to worry about rewriting it each time!  And, in this class you can go back and find things that you wrote in the past, or that others have written, and use them to do something without having to reinvent the wheel.

2.  Abstraction.  To use a function, you have to know:
  * the name of the function
  * what it does
  * the arguments that you give the function
  * what kind of result(s) the function returns

And that's it.  You don't have to worry about how it works internally, or what other functions it calls, or anything like that.  The only time you need to worry about how it works is when you create one yourself, or need to figure out how to modify something somebody else did.

Together, these two reasons make functions absolutely essential for programming - they allow us to divide programs into abstract, reusable sub-pieces and write large programs that actually work!

How do python functions work in practice?

* There's a function definition that has a line of code that's referred to as "the function call."
* The program enters the function and starts at the first line of the function
* It follows whatever instructions are in the function in order, and proceeds to the first 'return' statement that it executes (which can be at the end, but doesn't have to be)
* The program leaves the function and **goes back to where it started from**

Note: anything you pass into a function can be modified by the function, and when it's modified it will still be modified after the function has run.

What do they look like in Python?

```
def double_it(a):  # def = says this is a function. a is an argument.
    b = 2*a  # do stuff
    return b   # return says to return a variable that was created here
```

so we call this with:

```
mynum = 4
newnum = double_it(mynum)
print(newnum)
```

and ```newnum``` should be 8.

We can do all sorts of interesting things:

multiple function arguments and returns (they must always go in and out in the same order!):


set default values for arguments:


## What have we learned?

1.  Functions provide a way to break a program up into smaller chunks
2.  The two main reasons functions are useful is because of reusability and abstraction
3. Python functions have several interesting features, including:
  * taking multiple function arguments and returns
  * setting default values for arguments [some or all!]
  * out-of-order arguments that have defauls


## Useful links

* [Dive Into Python - section on functions](http://www.diveintopython3.net/your-first-python-program.html#declaringfunctions)
* [Defining functions in python](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
* [Why use functions?](https://www.cs.utah.edu/~zachary/computing/lessons/uces-10/uces-10/node11.html)
* [Functions](http://www.cs.utah.edu/~germain/PPS/Topics/functions.html)
* [Functions as used in programming languages](http://www.mathopenref.com/functionsprog.html)
* [Tutorial on functions](http://www.tutorialspoint.com/python/python_functions.htm)
