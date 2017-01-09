# Day 24

## Goals for today's class

* Devise an agent-based model to study the interactions of a predator species and a prey species
* Think about what you have learned since the beginning of this semester
* Think about how your understanding of models and programming has evolved over the course of the semester

## Pre-class assignment

* Download and look through the in-class notebook and Homework 7 prior to coming to class!

## In-class activity overview

* P: Announcements
* P: Presentation on agent-based modeling
* A: Implement an agent-based model of the interactions of a predator species and a prey species

## In-class activity details

* **As people come in: remind them to download the two notebooks for today's class and start looking through them - just to get people up and going!**
* P: Announcements
  * HW 7 will be the creation of an agent-based model.  It will be due on Sunday May 1st at 11:59 p.m.
  * Presentation slides (ppt or pdf) will be due this coming Sunday, April 24th at 11:59 p.m.  I emailed you instructions about your presentation.  Late submissions will not be accepted!  If you want me to look at them ahead of time, please feel free to email them.  You will be judged on both the clarity of presentation and the clarity of your slides, as well as the content!
* P: Presentation on agent-based models.  What is an agent-based model?  (Note: we've already talked about this - just revisit it.)
  * Sometimes called "cellular automata"
  * It's a model that implements a set of rules (which can be very simple or very complex) that a bunch of "agents" follow, and examines how those agents change over time.
  * It's a very useful sort of model because it's very general, and you can implement non-mathematical rules (in other words, you don't need equations, just a set of behaviors) 
  * This is used for all sorts of things - modeling disease spread, crowd behavior, traffic, animal behavior, etc.  It's used a lot in the social sciences in particular.
  * How do you create one?  Figure out the initial state, come up with a set of rules, decide on an ending condition.
  * **Demonstration: flock of birds!**  The rules for how the flock behaves are realy simple: (1) Birds want to be near other birds, and thus move toward them; (2) Birds don't want to run into other birds, so if they get too close they turn away from them; (3) birds want to go in the same direction as other birds.  **SHOW MOVIE - flock\_of\_birds.mov**
* A: Implement an agent-based model of the interaction between predators and prey
  * The in-class assignment is in Predators\_and\_prey.ipynb and the homework is in Homework\_7.ipynb - have students download both and look at both of them ahead of time!
  * The point of today is for students to think through the predator-prey model and how to implement it, to help them with their homework.  We also want them to think a bit about how their thinking about models has evolved over time.
  * We also want to get students to think about how to improve upon the model that they're being asked to implement - how can they make it more sophisticated?

## Useful links (reference)

* [Wikipedia - Agent-based modeling](https://en.wikipedia.org/wiki/Agent-based_model)
* [NetLogo](https://ccl.northwestern.edu/netlogo/) - a tool for ABM

## Instructor feedback

**Leave feedback on what happened in class today!**

* How you think it went
* What you felt went well
* What you and/or the students struggled with
* What changes you might make to future versions of today's activities.

Leave your feedback at [github](https://github.com/ComputationalModeling/intro-to-computational-modeling/issues/67).
