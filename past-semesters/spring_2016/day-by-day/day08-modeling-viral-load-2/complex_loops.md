## complex loops

Sometimes it is useful to be able to stop a loop in the middle of iterating through a bunch of things - for example, you want to search through a list of values until you find a particular one, and then quit looking.  In this case, Python has a command called ```break```, which you can use to do this.  It works as follows:

```
my_list = ['deer','t-rex','dog','cat','fish','monkey','cow']

animals_combined = ""

for item in my_list:
    if item == 'fish':
        break
    print("this animal is a", item)
    animals_combined += item + " "

print(animals_combined)
```

Alternately, you might want to not actually break the loop, but just do nothing for one or more items.  In that case, the Python ```continue``` command will just continue on to the next iteration of the loop without doing anything else.

(show example above, but use ```continue``` if ```item``` is dog or fish.

You can also use ```else``` in a way that's different than we showed earlier: you can set it up so that a loop that goes all the way to the end (which is to say, doesn't break) will do something new.

use the code below, but switch cat in ```if item == 'cat'``` with emu and show the difference.


```
my_list = ['deer','t-rex','dog','cat','fish','monkey','cow']

animals_combined = ""

for item in my_list:
    if item == 'cat':
        break
    print("this animal is a", item)
    animals_combined += item + " "
else:
    print("what we're looking for isn't there")

print(animals_combined)
```

What have we learned?

* Sometimes we might want to have loops [for or while] behave in complex ways.
* The "break" command [immediately] stops [iterating through] a loop if some conditions are met.
* The "continue" command skips the rest of the loop and keeps iterating through it.
* The "else" command (when applied to a loop) does something if the loop doesn't break [i.e., goes all the way through and executes all elements without breaking]