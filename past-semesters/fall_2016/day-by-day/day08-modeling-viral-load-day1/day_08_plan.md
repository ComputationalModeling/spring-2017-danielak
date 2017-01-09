# Day 8

## Goals for today's class

* Experiment with more complex analytical models 
* Think about fitting these models to datasets 
* Build a predictive model for HIV viral load and programming techniques we learned previously.
* Discuss and understand the difference between a descriptive model and a predictive model

## Pre-class assignment

* V: complex if statements
* A: write a loop that uses complex if/elif/else statements
* V: complex loops (break/continue/else)
* A: write small programs to use break/continue/else features with loops.

## In-class activity overview

* D: recap of the radioactivity model!
* D: pre-class activity review
* A: viral load data and model 
* P: end-of-class announcements 
 
## In-class activity details

* D: recap of the radioactivity model!  (10-15 minutes)
  * Lingering questions?  (get students to discuss as groups)
  * Leading questions for the students:  (second discussion)
    * How might we make a model for the count rate data?  (i.e., how do we account for the noise in the experimental count rate data?)
    * If we only had the count rate data, and not the total amount data, how could we get rid of the noise and figure out the count rate?
  * Talk about this - want to get the students to the idea that there's data with a half-life that we can see, plus a background.  If we wanted to calculate the half-life from the count rates we have to subtract off the background.  We can do that by fitting a mean value at late times!  (**Note:** This assumes that students didn't actually do the fitting in the last class!)

* D: Discussion of pre-class assignment  (5 minutes)
  * Any problems?
  * How long did it take?  (Approximately)

* P: recap of complex Boolean logic and control flow (10 minutes)
  * Do some live-coding here!

* A: Examine experimental data on viral load when a drug is administered, and then make a model of viral load behavior using both simple models and a more sophisticated mathematical model.
  * Look at the files viral\_load\_model\_STUDENT.ipynb and viral\_load\_model\_INSTRUCTOR.ipynb - the instructor version in particular has a ton of useful information for us.
  * Note: this will probably take most of both days of class.

* End-of-class announcements
  * Homework assignment handed out soon - details forthcoming.
  * Will also talk about a data analysis project that's forthcoming.
  * Class cancelled on Oct. 3/4 due to CMSE Frontiers in Computational and Data Science workshop 

## Instructor feedback

**Leave feedback on what happened in class today!**

* How you think it went
* What you felt went well
* What you and/or the students struggled with
* What changes you might make to future versions of today's activities.

Leave your feedback at [github](https://github.com/ComputationalModeling/intro-to-computational-modeling/issues/114).
