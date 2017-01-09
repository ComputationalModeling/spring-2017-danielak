## complex if statements

We've already had some experience with if() statements and Boolean logic, and even if() statements that have fairly complex logic.  But what if you need to do make even more complex statements?

Python if statements have the ability to use "else" and "else if" to make things more complicated.

Example:  loop over some range.  if the number is < 0, print "negative!" otherwise print "not negative!"


Example:  loop over a list of animals.  if one is a cat, print "meow!"  If one is a dog, print "woof!".  If it's anything else, print "you probably shouldn't be in my house!"
_
```
animals = ['dog','cat','monkey','velociraptor',
           'goldfish','wolverine','snake']

for this_animal in animals:
    if this_animal == "dog":
        print(this_animal,"woof!")
    elif this_animal == "cat":
        print(this_animal,"meow!")
    else:
        print(this_animal,"probably isn't a pet")
```
    

we can add and/or statements (more complex boolean logic):

```
animals = ['dog','cat','monkey','Cat','rabbit',
           'goldfish','wolverine','Dog','snake']

for this_animal in animals:
    if this_animal == "dog" or this_animal == "Dog":
        print(this_animal,"woof!")
    elif this_animal == "cat" or this_animal == "Cat":
        print(this_animal,"meow!")
    elif this_animal == "goldfish":
        print(this_animal,"glub!")
    else:
        print(this_animal,"probably isn't a pet")
```  

What have we learned?

* sometimes we can't use just a simple if() statement to make decisions
* can use "if" and "else" to decide between two sets of choices (w/Boolean logic)
* can use "if", "elif" (more than one)! and "else" to decide between more choices
* We can use these building blocks to write programs that make very complex decisions!


## references

[Python tutorial on control flow](https://docs.python.org/3/tutorial/controlflow.html)