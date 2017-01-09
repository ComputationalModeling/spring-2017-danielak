# Grading rubric for Homework 5

This assignment is worth 100 points (scaled to whatever is in the grade book), divided up in the following way.

Note that we're going to give credit based on code quality, correctness, and whether or not it runs.  Here's what the students were told:

**Code quality:** make sure that you use functions whenever possible, use descriptive variable names, and use comments to explain what your code does as well as function properties (including what arguments they take, what they do, and what they return).

**Whether your code runs:** prior to submitting your homework assignment, re-run the entire notebook and test it. Go to the "kernel" menu, select "Restart", and then click "clear all outputs and restart." Then, go to the "Cell" menu and choose "Run all" to ensure that your code produces the correct results. We will take off points for code that does not work correctly.

We didn't spell out what we meant by "code correctness", but basically it means "does it produce the right answer?"  The solution does not have to be identical to what's in the solutions I've provided to you, but it *does* need to work.


## Section 1 (modified skydiver model)

**60 points total** for this section.  Point breakdown:

* 20 points: Does the code actually implement the model correctly?  (Take off points for incorrectly integrating the velocity and position, for not keeping track of positions and velocities, etc.)
* 10 points: Code quality.  Is the code logically broken up into functions? Are there enough comments, and are they usable?
  * (0 pts for no comments/functions; 3 pts for poor comments/functions; 6 pts for some, but inadequate; 10 for adequate comments/functions)
* 10 points: Does it run without crashing?  (Either it does or it doesn't, so 0 or 10 points)
* 10 points: plots.  Need plots for position (5 points) and velocity (5 points)
* 10 points: Did they answer two questions: When did the skydiver reach the ground?  (5 points).  What was their horizontal distance from where they jumped when they reached the ground? (5 points).  **Note:** Be generous when grading the questions - depending on how they did the integration, their answers could be off by a bit.

## Section 2 (modified fire spread model)

**40 points total** for this section.  Point breakdown:

* 15 points: Did they correctly modify the code from the in-class activity?
* 15 points: Did they loop over the probability of fire transmission and plot out what happens to the 'critical point' as that probability is varied from 0.1 to 1.0?  (Or do they otherwise run the simulations a bunch of times to figure it out?) 
* 10 points: Do they give a reasonable answer to the question asked about the model behavior as the probability of fire transmission is varied?  (Grade generously; they don't need to be as thorough as the solutions - they just need to get at the fact that as you drop the probability of fire transmission, the critical point moves to higher fire density.)



