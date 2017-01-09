## What are modules?

One of the reasons that Python is powerful is that many people have written add-ons to the basic programming language that do useful things like visualization, data analysis of various sorts, work with the world wide web, manipulate images, and even control Lego robots.  This is great, because you can use all of this functionality for free.

One way to get at these tools is through using 'modules'.  A module is a way for Python to bundle together a set of several functions (i.e., mini-programs) and statements.  You can then import these modules into programs that you write and use them to do things.

A module is usually composed of a set of tools that are generally used for one type of task, such as manipulating images.  We're going to talk about two specific modules in this video: the math module and the matplotlib 'pyplot' module.

The 'math' module is exactly what it sounds like - it has all sorts of useful functions like sin(), cosine(), etc.  You access it like this:

import math

and call it like this:

math.log10(200.0)

it has constants, like pi:

math.pi

and it also has tools to do conversions, like from radians to degrees:

math.degrees(math.pi/2.0)

You can find out quite a bit about the math library by typing

help(math)

which will bring up its documentation in the Jupyter notebook.

----

Another extremely useful package is matplotlib.  Matplotlib is a python library for easily making high-quality figures of various types, including line and scatter plots, histograms, bar charts, and so on.  You can also control lots of the features of plots, like line styles, fonts, and axes.  We'll be using lots of the functionality of matplotlib during this course.

make a simple plot:

import matplotlib.pyplot as plt

(and then lots of other stuff I didn't write down here - look at video and module notebook)

----

What have we learned?

People have written all sorts of useful tools and libraries for Python

Modules are a way to access these, by typing "import modulename" or a variant of that

The math library and matplotlib.pyplot are two powerful examples of Python modules  [and we'll be using them a lot in this class]

pyplot lets us modify figures in all sorts of ways.

Useful URLs:

* [math module](https://docs.python.org/3/library/math.html)
* [matplotlib](http://matplotlib.org/)
* [matplotlib gallery](http://matplotlib.org/gallery.html)
* [pyplot tutorial](http://matplotlib.org/users/pyplot_tutorial.html)

