# Pandas

In this video we're going to talk about the Pandas module.

Pandas  (http://pandas.pydata.org/index.html) is an example of an extremely useful Python module, which is built on some of the general-purpose modules we're going to be using later this semester (like pyplot).

It's a good example of how general-purpose tools can be adapted for something specific.

Pandas provides tools for working with data - in particular, for doing data analysis and visualization.  We'll use it a lot this semester.

The basic Pandas data structure is a "data frame", which you can think of as being something like a spreadsheet full of data

The big difference is that we work with it using code, not mouse interactions.

* So, let's read something into a data frame
* Then let's just type the name of the data frame and see what happens.  Wow, that's a lot of data!  Note that when I use my mouse to click on the boxes with numbers in them I can't do anything - we have to use software!
* Now let's just use the `.head()` method to see the first few lines.  There's also a `.tail()` method.  
* We can get some more information about it by using `.describe()`
* We can get a single value by slicing:
```
heart_disease_data['age']
```
* Can get a histogram of that:
```
heart_disease_data['chol'].plot.hist
```
* We can plot quantities in a scatter plot:  
```
 heart_disease_data.plot.scatter(x = 'age', y = 'chol')
```



