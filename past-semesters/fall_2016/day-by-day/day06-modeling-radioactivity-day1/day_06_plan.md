# Day 6 (Radioactivity - first day)

## Goals for today's class

* Write a program that includes loops and simple Boolean logic.
* Create a model that shows the evolution of a system over time, using loops.  
* Create a model that uses Boolean logic within a loop to introduce limiting behavior.


## Pre-class assignment

* V: numpy arrays
* A: work with numpy arrays and pyplot
* V: if statement and Boolean logic
* A: write a small program to make a complex decision
* V: loops
* A: write a program to work with loops
* A: What questions do you have from the videos?  Any other concerns?  How much time?  (Submit everything via notebook.)

## In-class activity overview
 
* D: Flint debrief
* D: problems with pre-class assignment? How long did it take?
* P: recap of Boolean logic and loops
* A: individually, write a simple program with loops and boolean logic
* D: How might numpy's array methods work?
* A: make a model of exponential behavior using loops
* P: end-of-class reminder: first homework due Friday!
 
## In-class activity details

**NOTE: we're going to use whiteboards for sharing of results today - try to remind students to write large and as clearly as possible**

* D: Flint water quality debrief (10-15 minutes)
  * Get students to form into their groups and discuss the last class (Flint water quality day 2).  The goals of the discussion are to have them bring up any issues that they have with Pandas after that class session
  * Following small-group discussion have a large-group discussion.  It may require some live-coding in a Jupyter notebook in class - be prepared for this!
  * Make notes of anything that comes up that isn't immediately solvable, and we can put it into a "tutorial" notebook that we share with the students.

* D: Discussion of pre-class assignment for today (5 minutes)
  * Any questions?  How long did it take?
  * Get students to discuss in group.

* P: recap of Boolean logic and control flow (10 minutes)
  * loops let us do the same thing over and over, or a bunch of things one after the other - do a quick example with range, list, numpy nditer
  * if() statements allow the code to make decisions
  * Do a quick live programming exercise: given some values of a variable, comparison using if and write out some variables - "if > blah...".  Build it up over time.

* A: individual program creation - create a *list* of random integers (randomized by hand by the students) and loop over it; for each element, if it's **even** print out "even!" and if it's **odd** print out "not even!".  Hint: tell them about the modulus operator.  Leave previous programs up on the screen.  (10 minutes)

* D: How might some of numpy's array methods work? (10 minutes)
  * Numpy has all sorts of cool tools for getting statistics out of an array - we used some of them last time.  array.sum(), array.mean(), array.max(), array.min()
  * Given what you know about loops, how do you think that one of these might work?
  * Ask students to think about it as a group and write some pseudo-code on their group's whiteboard.

* A: make a model of exponential behavior using Boolean logic (60 minutes)  
  * Look at the file radioactivity_modeling.ipynb, and radioactivity_modeling_INSTRUCTOR.md
  * Make it clear that this is a two-day assignment and we expect them to work on it next week as well.

* End-of-class announcements (2 minutes):
  * Reminder: first homework due on Friday!


## Instructor feedback

**Leave feedback on what happened in class today!**

* How you think it went
* What you felt went well
* What you and/or the students struggled with
* What changes you might make to future versions of today's activities.

Leave your feedback at [github](https://github.com/ComputationalModeling/intro-to-computational-modeling/issues/112).
