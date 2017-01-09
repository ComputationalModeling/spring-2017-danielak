# Day 10

## Goals for today's class

* Finish building a predictive model for HIV viral load and programming techniques we learned previously.
* Discuss and understand the difference between a descriptive model and a predictive model

## Pre-class assignment

* None!

## In-class activity overview

* D: recap of where we were last time
* A: viral load data and model 
* D: models and data - reconciling function and form
* P: end-of-class announcements 
 
## In-class activity details

* D: recap of where we were last class
  * Make sure to have a whole-class discussion about the mathematical model we were working on in the last class, the programming of it, and how it fits together.  If necessary, have everybody in the class tell you how to actually put together the model, and then write it all down on the board (to get the various groups up to speed).

* A: Viral load modeling (from Day 8).
  * Look at the files viral\_load\_model\_STUDENT.ipynb and viral\_load\_model\_INSTRUCTOR.ipynb from the same class session - the instructor version in particular has a ton of useful information for us.
  
* D: models and data - reconciling function and form
  * Let's talk about the physical processes at work - virus reproduces in cells and is ultimately injected into the bloodstream, where more cells are infected.  drug kills viruses that are in the bloodstream (once a certain level of drug in the blood is reached) and then all that's left is viruses that emerge from the cells after incubation period.  After that, all that's left are dead viruses dead viruses.
  * Generally speaking, what would the shape of the viral load look like from this model?  (Looking for rapid growth early, then slow growth/slow decline at the medium term, then rapid decline at the late term)
  * What did the simple "exponential" and "power-law" models tell us?  (The exponential model fits pretty well, suggests some behavior.  The fit is not perfect at early or late times, suggesting there is something missing in this simple approximation.)
  * Difference between predictive vs. descriptive model!  Predictive model makes *predictions* about what's actually happening based on assumptions about the underlying processes; descriptive model (in this context) is more-or-less just telling us what the "shape" of the observations are - in other words, giving us some information about what the observations show in a quantitative way.  (Think the radioactivity model we made the other day.)  A descriptive model can be useful for trying to approximate quantities, but has limited predictive capability.

* End-of-class announcements
  * Will spend about 15 minutes discussing the data analysis project on Wednesday - bring the two datasets you're interested in + questions you're interested in asking about each dataset
  * Data analysis project - dataset due on Friday
  * Homework 2 is due Tuesday night!
  * Also there's a pre-class assignment for the next class, which is also due Tuesday night.

## Instructor feedback

**Leave feedback on what happened in class today!**

* How you think it went
* What you felt went well
* What you and/or the students struggled with
* What changes you might make to future versions of today's activities.

Leave your feedback at [github](https://github.com/ComputationalModeling/intro-to-computational-modeling/issues/114).
