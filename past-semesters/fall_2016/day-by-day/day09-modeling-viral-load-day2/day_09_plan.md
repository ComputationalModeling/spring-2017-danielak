# Day 9

## Goals for today's class

* Continue experimenting with more complex analytical models
* Think about fitting these models to datasets 
* Build a predictive model for HIV viral load and programming techniques we learned previously.
* Discuss and understand the difference between a descriptive model and a predictive model

## Pre-class assignment

* None!

## In-class activity overview

* D: recap of where we were last week
* A: viral load data and model 
* D: models and data - reconciling function and form
* P: end-of-class announcements 
 
## In-class activity details

* D: recap of where we were last class
  * Make sure to have a whole-class discussion about the mathematical model we were working on in the last class, and how it fits together.  If necessary, have everybody in the class tell you how to actually put together the model, and then write it all down on the board (to get the various groups up to speed).

* A: Viral load modeling (from last class).
  * Look at the files viral\_load\_model\_STUDENT.ipynb and viral\_load\_model\_INSTRUCTOR.ipynb from the previous class session - the instructor version in particular has a ton of useful information for us.
  
* D: models and data - reconciling function and form
  * Let's talk about the physical processes at work - virus reproduces in cells and is ultimately injected into the bloodstream, where more cells are infected.  drug kills viruses that are in the bloodstream (once a certain level of drug in the blood is reached) and then all that's left is viruses that emerge from the cells after incubation period.  After that, all that's left are dead viruses dead viruses.
  * Generally speaking, what would the shape of the viral load look like from this model?  (Looking for rapid growth early, then slow growth/slow decline at the medium term, then rapid decline at the late term)
  * What did the simple "exponential" and "power-law" models tell us?  (The exponential model fits pretty well, suggests some behavior)
  * Difference between predictive vs. descriptive model!  Predictive model makes *predictions* about what's actually happening based on assumptions about the underlying processes; descriptive model (in this context) is more-or-less just telling us what the "shape" of the observations are - in other words, giving us some information about what the observations show in a quantitative way.  (Think the radioactivity model we made the other day.)

* End-of-class announcements
  * Homework assignment handed out soon - details forthcoming.
  * Will also talk about a data analysis project that's forthcoming.

## Instructor feedback

**Leave feedback on what happened in class today!**

* How you think it went
* What you felt went well
* What you and/or the students struggled with
* What changes you might make to future versions of today's activities.

Leave your feedback at [github](https://github.com/ComputationalModeling/intro-to-computational-modeling/issues/114).
