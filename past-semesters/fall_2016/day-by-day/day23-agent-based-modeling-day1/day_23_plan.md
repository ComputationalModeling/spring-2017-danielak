# Day 23

## Goals for today's class

* Observe how complex emergent phenomena result from simple rules in a model.
* Examine and quantify the concept of a "tipping point" in a model.
* Do both of these things in the context of modeling forest fires

## Pre-class assignment

* Working with 2D numpy arrays (using the 2D numpy tutorial)

## In-class activity overview

* P: Announcements
* D: Pre-class assignment
* A: Modeling forest fires, emergent phenomena, and tipping points 

## In-class activity details

* P: Announcements
  * Final slides for "tell me about a model" assignment due Friday 12/2 - powerpoint or PDF only!
  * Homework 5 assigned, due last day of class (Friday 12/9).  Remind students to get started early, since this is a big assignment.
* D: Pre-class assignment (10 minutes)
  * Have students work through their solutions in groups and ask about anything they're having trouble with.  It may be worthwhile to actually show the students some of the solutions - in particular, working on 'neighborhoods', because that's what we're going to need for the forest fire model.
* A: Modeling forest fires (rest of class; also next class)
  * Set this project up by asking students to spend five or so minutes reading the notebook.
  * Then, give a brief presentation - talk about agent-based models (ABM), complexity emerging from simple rules, and tipping points.  They've seen ABM and complexity before (Schelling, econophysics), but the tipping points are new.
  * We want students to think through all of the pieces and create pseudo-code before they do any coding.  In particular, ask them to think through (1) the 'neighborhood' calculation (which should tie back to their pre-class assignment) and (2) how to calculate the fraction of cells that are empty, on fire, full of trees, etc. (the latter can be done using some possibly useful numpy hacks - see the problem solutions).  **Make sure to have a whole-class discussion about the pseudo-code!**  During that discussion, give liberal hints about things you can do with numpy - summing up arrays, Boolean logic on arrays, etc. - that might make things easier for various pieces of the project.  You might also want to explicitly suggest that the evolution code use two arrays: the original array and the "new timestep" array.
  * The critical threshold/"tipping point" should happen at a tree covering fraction of 0.59 - basically what's going on is that there are now guaranteed to be enough trees that the fire can spread readily.  This is analogous to ideas pertaining to disease - disease runs rampant if population density is high enough (easy to infect each other if the time between infections is less than the incubation period!), and it's much harder to spread disease if most people are immune and thus can't transmit the disease (i.e., herd immunity - get your shots, people).
  * As we get to the end, make sure to have a conversation with the whole classroom about tipping points (look at the notes in the notebook itself).  Also, ask the students to talk to each other about the ways that one might make this model more realistic (terrain, weather, wind, different parts of the forest catch fire at different rates/burn for different amounts of time, roads/rivers/etc. act as firebreaks, take into account fire-fighting efforts, etc.) and make a list.
  * **Note:** This is going to lead into the final homework assignment for the class, so they need to know how to do it!
   
**If it seems that some groups are getting stuck,** it is totally reasonable to make direct suggestions about how to do things, or at least ask leading questions:

* Can you make this work with just a single array, or do you need separate "previous timestep" and "this timestep" arrays?  (The latter, unless you're really clever.)
* How do you deal with 'neighborhood' calculations near the edges of the board?  (check for values of i,j and compare it to the array's `shape[]` parameter)
* How do you make nifty animations?  (Look in the pre-class assignment, it's all worked out for you!)

**If some groups finish more rapidly than expected,** here are some questions to ask/model extensions to suggest to keep them engaged:

* Since this is a stochastic model (i.e., depends on randomization), we can see that the curve is rather jagged - particularly around the tipping point.  How might we get a better sense of both the average behavior and the variety of possible outcomes for a given value of the forest covering fraction?  (Do multiple trials per covering fraction, and keep track of the variation for each value of the covering fraction - plot both the mean and the error bars!)
* What happens if you have multiple sites of fire at the outset rather than just setting one edge of the board on fire -   how does that affect the behavior?  Is there still a tipping point, and is it at the same place?  (Ask them to plot this on the same graph as the original model.)
* What about introducing additional means of starting fire?  For example, what if there were lightning strikes?  How would you model that, and how would it affect the output?  (Each cell with trees in it would have some low probability per turn of randomly catching on fire due to "lightning").  (Ask them to plot this on the same graph as the original model.)
* How might you take into account the idea that different cells might have different types of trees (some of which are more fire resistant than others), or lots of dead underbrush that catches fire easily, etc.?  (Probably translates to some probability of a given cell catching fire - could determine this randomly.)
* What other factors might one have to take into accont to make this model more realistic?

## Instructor feedback

**Leave feedback on what happened in class today!**

* How you think it went
* What you felt went well
* What you and/or the students struggled with
* What changes you might make to future versions of today's activities.

Leave your feedback at [github](https://github.com/ComputationalModeling/intro-to-computational-modeling/issues/126).
