# Why is my banana glowing?

## Learning goals

As stated in the students' version:  Lots of systems (physical, biological, economic, social, etc...) evolve in time, and you have to figure out how to change things at the next time based on what happened before.  Today, we're doing that using radioactivity and compare our models to some data.  This type of modeling is going to make us think about:

* How to make a system move forward in time using loops
* How to work with numpy arrays to do interesting and useful things
* How to think about a model in relation to experimental data, and to decide if your model isn't quite good enough  (ooh!  foreshadowing!)

**For the instructor:** What we really want to do in this project is get students to think about how to make simple analytic models (basically do simple integration), think about and describe some data, and think about how their very simple analytic model disagrees with the data.  **this assignment is going to require us to really pay attention and ask leading questions!**

## Implementation notes

### Group size

Pairs or groups of 3 (when there are only 3 at a table)

### Setup/Implementation

Have one of the students volunteer to be the coder for the pair, and ask the rest to just draw/make notes on the whiteboard.  The coder will email everything to their partner(s).  Also, tell the students that we're going to have a second whiteboard for sharing of code, answers, etc.

**working out on the whiteboard**

Sample of material: it's just the equation directly above.

Decays per second:  derivative of that.  Note that the solution is:

decay rate = -dN/dt = N\_0 / t\_h * 0.5^(-t/t\_h) * ln(2)

where t\_h is the half-life and N\_0 is the original amount of sample.  The ln(2) comes from taking the derivative of 2^x.

Some leading questions, since we've deliberately left a bunch of stuff vague (like half-life and amount of material):

* What quantities do you think you need? 
* Tell me about how you get a rate of something (hint: calculus!)
* Does it matter how much of it there is, or the half life?  (For the purpose of plotting)

and then a physics question:

* If you were holding this in your hand, would you want it to have a long half-life or a short half-life?  (long! less radioactive!)

**plotting measured data**

The data has noise in it.  We want them to see that the amount as a function of time falls off exponentially, and **ask them to estimate the half-life and initial amount**.  How can they do that?  (They should be able to get pretty close just by inspecting the arrays.  The half life is **1712 seconds** and the initial amount is **10^6 atoms**.

Some leading questions:

* how does this data look differently than your model?  (looking for 'noisy' or 'looks messier'
* What do you think might be going on?  (esp. w/count rates)
* Thinking about it, where might the noise be coming from?  (background from stuff around the detector - everything is radioactive!)

**modeling the data**

We want the students to use the count rates and the measured amount of stuff at t=0 to estimate how much stuff there should be as a function of time.  This will result in a value that doesn't make sense, since it goes negative really quickly, and it does not agree with the measured values at all.  What we're getting at here is that there's a background that needs to be taken into account!

**first** ask the students to work this out on the whiteboard in pseudo-code!

Leading questions:

* So, how does the count rate modify the total amount of stuff?  (every interval the total amount should go down by the number of counts)
* How would you put that into a loop?  Maybe create some arrays of times?
* Why do you think that doesn't look like the measurements?  (noise!)
* How might you modify your model to get it to look like the data?  (add some amount of noise to each count - there are more decays measured than the sample must be doing)

**Estimated times:**

* initial calculation+coding: 15 minutes
* plotting data: 15 minutes
* making model of data: 20
* Final breakdown: 10 minutes

### What students might struggle with

* Starting is probably going to be the biggest problem.  Lots of leading questions are necessary.
* It is likely that some students will be confused by the lack of information (this is related to problems with starting in a lot of ways) but remind them that the point is to think through the problem, so just make up some numbers.

### Desired student behaviors

* Discussion: are they talking about the observed data and their simple model?
* Calculation: are they creating an equation/expression and plugging things into it?
* Testing: are they discussing the accuracy of the model, and how they might modify it to get something more reasonable?


## Instructor feedback

**Leave feedback on this activity!**

* How you think it went
* What you felt went well
* What you and/or the students struggled with
* What changes you might make to future versions of this exercise

Leave your feedback at [github](https://github.com/ComputationalModeling/intro-to-computational-modeling/issues/14).
