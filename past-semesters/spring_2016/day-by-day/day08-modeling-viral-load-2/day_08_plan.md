# Day 8

## Goals for today's class

* Complete HIV activity from day 7
* Discuss and understand the difference between a descriptive model and a predictive model
* Build a predictive model for HIV viral load and programming techniques we learned previously.

## Pre-class assignment

* V: complex if statements
* A: write a loop that uses complex if/elif/else statements
* V: complex loops (break/continue/else)
* V: write small programs to use break/continue/else features with loops.

## In-class activity overview

* D: getting started - recap of what we did last time!
* A: wrap up HIV activity
* D: models and data - reconciling function and form
* A: making a model to understand the HIV viral load from first principles
* P: end-of-class announcements 
 
## In-class activity details

* D: getting started
  * Get students to discuss as a group how far they got on the HIV modeling project last time.  What do they feel confident about, and what questions do they have?
  * Any questions to discuss with the room?

* A: Wrap up HIV activity
  * What values for A, B, alpha, beta did people use?  Positive only, or positive and negative?
  * Suggest that they try various values for A, B, alpha, beta -- maybe loop over a bunch of stuff to see what the various possible solutions are, and to use both positive and negative values for A, B, alpha and beta!

* D: models and data - reconciling function and form
  * Let's talk about the physical processes at work - virus reproduces in cells and is ultimately injected into the bloodstream, where more cells are infected.  drug kills viruses that are in the bloodstream (once a certain level of drug in the blood is reached) and then all that's left is viruses that emerge from the cells after incubation period.  After that, all that's left are dead viruses dead viruses.
  * Generally speaking, what would the shape of the viral load look like from this model?  (Looking for rapid growth early, then slow growth/slow decline at the medium term, then rapid decline at the late term)
  * While maybe we can get the double-exponential model to generally describe the shape of the curve made by the data points, does it really predict the growth and decay of our model?*
  * Difference between predictive vs. descriptive model!  Predictive model makes *predictions* about what's actually happening based on assumptions about the underlying processes; descriptive model (in this context) is more-or-less just telling us what the "shape" of the observations are - in other words, giving us some information about what the observations show in a quantitative way.  (Think the radioactivity model we made the other day.)

* A: make model of viral load behavior from first principles (using what we learned from pre-class stuff).
  * see the file viral\_load\_model.md for instructor information, the file viral\_load\_model\_STUDENT.ipynb for what the students see, and viral\_load\_model\_INSTRUCTOR.ipynb for a solution and some notes.

* End-of-class announcements
  * Homework assignment this week: we're going to be doing some financial modeling - particularly, how different investment strategies and choices affect how much money people have available for retirement. 

## Instructor feedback

**Leave feedback on what happened in class today!**

* How you think it went
* What you felt went well
* What you and/or the students struggled with
* What changes you might make to future versions of today's activities.

Leave your feedback at [github](https://github.com/ComputationalModeling/intro-to-computational-modeling/issues/23).
