# Grading rubric for Homework 3

This assignment is worth 100 points (scaled to whatever is in the grade book), divided up as detailed below.

Their instructions are to implement the Schelling model *as described by Schelling and in their Jupyter notebooks*.  This means:

* You use zeros and ones (or something similar) to indicate the two types of elements.
* "Happiness" for an element is determined by the neighbors within 4 spaces being at least 50% like that element (i.e., 4 of 8, 2 of 4, etc.)
* An unhappy element moves to the *closest* neighboring space that makes it happy, to either the left or the right.

We were pretty vague in the homework assignment - I basically said "implement the 1D Schelling model" - so we need to grade fairly coarsely.  Students can't be penalized for not having the same number of elements in the list, etc.  That said, they **must** implement the actual model - it can't be circular/periodic, it can't move elements in only one direction or by a fixed amount, happiness is determined correctly, etc.

**Implementation: 90 points** 

* Does code actually execute, and produce outputs that are sensible?  (20 points)
* Is list initialized randomly?  (10 points)
  * Full points as long as it isn't hand-coded in some odd way.
* Is the "is_happy()" function correctly written?  (20 points)
  * 10 points off if happiness is not correctly calculated because of periodicity/circularity of list
  * 10 points off if happiness doesn't correctly take into account behavior at edges
  * 5 points off if happiness is incorrectly calculated because the element being considered is not correctly examined. 
* Is the function that determines where to move written correctly? (30 points) 
  * 10 points off if it only moves in one direction rather than closest point in either direction.
  * 10 points off if movement doesn't check for happiness (i.e., just moves N steps in either direction)
* Does the code implement the top-level looping in a sensible way? (10 points)
  * Schelling was vague about how to advance through the list of elements - did the students make a sensible choice for how to move through their list, or does it get stuck in an endless loop?  (Lose all points if this is done in a way that doesn't make sense to you; lose some points if the looping doesn't follow Schelling's rules in some way.)
 
**Clarity: 10 points**

This is a small part of the total points because we weren't very specific about it in the assignment.  However, if the students refuse to use functions, or if they create code that's extremely hard to follow, take either 5 or 10 points off for lack of clarity!
