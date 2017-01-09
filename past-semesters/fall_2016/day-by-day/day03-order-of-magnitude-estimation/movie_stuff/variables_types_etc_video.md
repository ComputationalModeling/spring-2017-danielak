## Variables, types, etc.

link to relevant part of https://docs.python.org/3/tutorial/

and https://docs.python.org/3/tutorial/introduction.html

* what's a variable?  what does it do?
* types of variables: integers, floats, strings, etc.
* order of mathematical operations

--

This video: learn about types of variables, and also use Python as a calculator.

variables = memory locations that store values.  But, those values can be different types of things.

Python has a lot of different data types.  The two we're going to talk about in this video are numbers and strings.

Numbers can either be integers or real numbers (what we call 'floating point' numbers)

Integers are numbers without fractional parts, and real numbers have a fractional part (i.e., with a decimal point and a non-zero number after it).

Python figures out from context what type of variable you're using.

assign variable x the integer 2:

x = 2  #  integer

type(x)

y = 2.0  # floating point

type (y)

x + y  is what?

operators with mixed type operands convert to floating point.

2 * 2.5

10.0 / 2

string = big list of characters.

Python can do clever things with strings.

d = "monkey"

e = 'rhinoceros'

Can concatenate strings together (i.e., put them together) with the 'x' sign and repeat them with the * sign.

can I mix numbers and strings?  NO!

can I convert numbers TO strings?  YES!

can I convert strings to numbers?  SOMETIMES!

Summary:

* Python = many data types.  Two types are numbers and strings.
* Numbers can be either integers or floating point numbers, and you can do arithmetic with both types together.  Python figures out from context what 
* Strings are lists of characters, and you can do things like concatenate (add) strings, repeate them, and access individual characters in the string.
* Python will let you change variables from one type to another, as long as it can be done sensibly.   [i.e., string 8 to number 8, but can't convert string 'monkey' to a number]

