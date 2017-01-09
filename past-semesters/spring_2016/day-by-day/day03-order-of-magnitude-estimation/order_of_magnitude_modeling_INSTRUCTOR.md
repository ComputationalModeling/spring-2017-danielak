# How many mice would it take to fill up this classroom?

## Learning goals

As stated in the students' version:  One type of modeling is called "order-of-magnitude estimation" or "order-of-magnitude modeling."  A physicist would call this a "Fermi Problem" after Enrico Fermi, a physicist who participated in the Manhattan Project and who was famously good at making estimates of this sort.  More specifically, this sort of modeling makes us think about:

* The quantities that should go into our models, and the reasonable values of those quantities.
* How the different parts of our model might interact with one another.
* What a "good enough" answer would be to a particular problem

**For the instructor:** What we really want to do in this project is give students a bit of experience with order-of-magnitude estimation (i.e., Fermi problems), which we will build on throughout this semester.  This is probably going to take some work on the instructor's part to get the students primed.

## Implementation notes

### Group size

Full table (~4 students)

### Setup/Implementation

Have one of the students volunteer to be the record-keeper for the group, and ask the rest to just draw/make notes on the whiteboard. 

Before students get going on their own projects, we need to prime this by doing an example for them.  Let's start with the title of the exercise - "how many mice would it take to fill this classroom?"  We want to get an order-of-magnitude estimate (i.e., correct to within a power of 10) by making reasonable assumptions about the situation.  It's not critical to have definite knowledge.  It's useful to ask questions to get started:

* Generally, how might I estimate this?  (Go to a more obvious thing - number of blocks in a box, etc... want to get them to N_mice = volume of room / volume of a mouse.
* How big is this classroom?  (Volume!  Get estimates.)
* How big is a mouse?  (Volume!  Get estimates, maybe by having somebody google the mass of a mouse and assuming its density is about that of water.)
* How much of the classroom is taken up by stuff already?  (Estimates.)
* OK, now let's divide through:  N_mice = (V\_room - V\_stuff)/V\_mouse.
* What's the range of estimates we might expect?  (Show how to vary numerator and denominator to get range.)

After we discuss this a bit, now it's time for the students to do it themselves.  Remind the students that it's OK to not have enough information, and that a large part of the goal is to figure out what is actually important in such an estimate.  So, they should think about it and come up with ranges that seem reasonable, and Google numbers that they don't know!

The instructors should be wandering around listening and asking questions.  Some leading questions are:

* Tell me about your thought process so far.  
* What are the questions you need to answer in order to figure out this problem?
* What quantities do you think you need?
* How do they relate to each other?  What has to be multiplied, divided, etc.?
* Also more specific questions about their individual models - "How many airline flights do you think there are in a given day?  What's the average duration of one of those?"

The students should come up with their OOM models and write a simple computer program to implement it, and then put in some values and get a range of estimates.

After the students spend ~30 minutes creating models as a table, tell them that you're going to **ask some of the groups** to explain their model and answers, and encourage people from other groups to ask questions.  Instructors can ask questions like:

* How did you arrive at the things that you need for this model?
* what additional parameters might be included?  How is that important?

After the students all figure this out, maybe do one of the remaining problems as a group, just to solidify things.  It's also valuable to do a wrapup to get students to think about why this might be a helpful thing to do!

**Estimated times:**

* Whole-class example at the beginning: 10 minutes
* Individual group work: 30 minutes
* 2-3 groups explaining their models: 5 minutes per group
* Final breakdown: 5 minutes

**Useful references**

These problems came from the book __Guesstimation: Solving the world's problems on the back of a cocktail napkin__, by Weinstein and Adam.  

Also, the [Wikipedia article on Fermi Problems](https://en.wikipedia.org/wiki/Fermi_problem) is handy, as is this [collection of links relating to Fermi Problems](http://www.vendian.org/envelope/dir0/fermi_questions.html) and a [Library of Fermi Problems](http://mathforum.org/workshops/sum96/interdisc/sheila3.html).

### What students might struggle with

* Starting is probably going to be the biggest problem.  Asking questions like "What questions do you need to answer in order to figure out this problem?" or "What measurements might you need to take?"
* It is likely that some students will be confused by the lack of information (this is related to problems with starting in a lot of ways) but remind them that the point is to think through the problem, not get a really precise answer.  (i.e., the thought process is useful)


### Desired student behaviors

* Discussion: are they talking about the possible parameters in their model?
* Calculation: are they creating an equation/expression and plugging things into it?
* Testing: are they discussing the accuracy of this model, or what a desired range of model parameters might be?

## Instructor feedback

**Leave feedback on this activity!**

* How you think it went
* What you felt went well
* What you and/or the students struggled with
* What changes you might make to future versions of this exercise

Leave your feedback at [github](https://github.com/ComputationalModeling/intro-to-computational-modeling/issues/9).
