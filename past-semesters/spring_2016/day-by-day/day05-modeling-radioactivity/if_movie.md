# "If" statements and Boolean logic

Computer programs need to have a way of making decisions.  One of the most common ways to do this is using Boolean logic and the "if" statement.

"Boolean logic" is named after the 19th century mathematician George Boole, and is a type of logic where every value is reduced to being either "True" or "False".  This works well with computers and for decision making.

You can use Boolean logic to compare things in Python, to find out if it's True or False.  There are several ways to do comparison of two variables 'a' and 'b', each of which returns true or false:

a == b   -- note that it's two equal signs.  Is 'a' equal to 'b'?

a != b   is 'a' NOT equal to 'b'?

a > b    is a greater than b?

a < b    is a less than b?

a >= b   is a greater than or equal to b?

a <= b   is a less than or equal to b?

can use this for numbers, and also for strings (though really it mostly makes sense for equals)

You can do this very easily in python!  It will return 'True' or 'False'

(live demo)

Now, on to 'if' statements.  This is a way to use Boolean logic to tell a computer to do something.

the syntax in python is:

if variable1 (comparison) variable2:
    do something!

Note the indentation.  The body of the if statement is indented: indentation is Python’s way of grouping statements into blocks (and each line within the block should be indented by the same amount). When you put in the colon after the if statement, Jupyter should automatically do this when you hit enter.  Go back to the original level of indentation to get out of the loop.

Can nest levels of indentation and have multiple if statements!

Coding example:

a = 17
b = 23
c = 3

if a > b:
    print(a)
    
This shouldn't do anything!

We can also chain together these statements with the 'and' and 'or' evaluators and parentheses.

## What have we learned?

* Boolean logic tells us if expressions are true or false [can evaluate with equals, not equals, greater than, less than, etc.]
* We use the 'if' statement in python to evaluate expressions
* We can combine multiple expressions together to make very complex comparisons and decisions.


## Potentially useful links

* [python tutorial - control flow](https://docs.python.org/3/tutorial/controlflow.html)
* [WikiBooks Python Programming - conditional statements]()
* [Learn Python the Hard Way - Boolean Logic](http://learnpythonthehardway.org/book/ex28.html)
* [How To Think Like a Computer Scientist: Conditionals](http://openbookproject.net/thinkcs/python/english3e/conditionals.html)
* [Python basic operators](http://www.tutorialspoint.com/python/python_basic_operators.htm)
* [Python logical operators](http://www.tutorialspoint.com/python/logical_operators_example.htm)
* [Python comparison operators](http://www.tutorialspoint.com/python/comparison_operators_example.htm)
