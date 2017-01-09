## The 'List' data type

link to relevant part of https://docs.python.org/3/tutorial/

and https://docs.python.org/3/tutorial/introduction.html

In addition to numbers and strings, python has some very useful data types that are known as 'compound' data types.  These are used to group together other values.

One of the most flexible of these is a 'list', which is a listof comma-separated items in between square brackets.  Lists usually contain items of the same type, but CAN have items of different times.

mylist = [1,3,5,7,9]

python knows this is a list

type(mylist)

print mylist

and you can have lists that are combinations of the basic types:

mynewlist = [2, 4.0, 'six']

print mynewlist

type(mynewlist)

Like strings, you can use an index to get to individual items.

mynewlist[0]

and python will tell you what those individual items are:

type(mynewlist[0])

you can change the content of a list by modifying individual items:

mynewlist[1] = 'five'

print(mynewlist)

and you can use built-in methods to add things to the list.  For example, there is one called 'append', which adds to the end of the list.

mynewlist.append(8.0)	

there are several other built-in methods for lists, but we'll work with those another day.

you can find out how many things are in a list with the len() function:

len(mynewlist)

and you can even make lists of lists:

a = [2,4,6]
b = [1, 3, 5]
c = [a,b]

print(c)

and you can access them in a nested way as well:

c[0]

c[0][1]

## Summary:

1. Lists are a *compound data type* and can group together other values
2. Lists usually are of one type, but can contain multiple types
3. Can modify individual elements of a list, and can add to a list using built-in methods.