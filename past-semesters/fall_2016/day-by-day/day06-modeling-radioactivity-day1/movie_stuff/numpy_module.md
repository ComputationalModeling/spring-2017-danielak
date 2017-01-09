## Numpy - a very useful module

One extremely useful module is NumPy.

NumPy is the fundamental package for scientific computing in Python. It contains, among other things, a powerful N-dimensional array object, and tools for manipulating those arrays.

NumPy arrays are like the Python list data type in some way, but they are much more useful for working with data and doing modeling.  

We're talking about NumPy now because lots of tools, including matplotlib, are based on NumPy.

NumPy is very powerful; we'll start talking about it today, but will use much of the semester to learn about different things you can do with it.   

Let's go!


import numpy as np

help(np.array)

a = np.array([1,4,9,16,25,36])

and can make an array that has multiple dimensions:

amulti = np.array([[1,2,3],[4,5,6]])

amulti

can even specify the datatype:

a = np.array([1,4,9,16,25,36], dtype=float)

b = np.arange(6)

c = np.zeros(6)

mylist = [5,4,3,2,1,-1]

d = np.array([mylist])

e = np.ones_like(d)

So, why is this useful?

Can do operations on entire arrays of numbers:

a + b

a - c

d * e

a**0.5

and there are lots of built-in methods in the numpy arrays that can be very useful.  (access them in IPython by tab completion a.+tab] 

a.sum()

a.min()

a.max()

also can sort:

np.sort(d)

----

What have we learned?

* NumPy is an important package for scientific computing in Python.
* NumPy arrays are the fundamental data type [like lists in some ways, but very different in others. very powerful data type.]
* Lots of ways to create arrays  [both from a Python list and specifying ranges]
* Can do operations on entire arrays of numbers
* Lots of built-in methods to work with numpy arrays

----

## useful links

* [Numpy tutorial](http://cs231n.github.io/python-numpy-tutorial/)
* [What is NumPy?](http://docs.scipy.org/doc/numpy-1.10.1/user/whatisnumpy.html)
* [NumPy quickstart](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html)

