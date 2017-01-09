# Grading rubric for Homework 4

This assignment is worth 100 points (scaled to whatever is in the grade book), divided up in the following way.

Note that we're going to give credit based on code quality, correctness, and whether or not it runs.  Here's what the students were told:

**Code quality:** make sure that you use functions whenever possible, use descriptive variable names, and use comments to explain what your code does as well as function properties (including what arguments they take, what they do, and what they return).

**Whether your code runs:** prior to submitting your homework assignment, re-run the entire notebook and test it. Go to the "kernel" menu, select "Restart", and then click "clear all outputs and restart." Then, go to the "Cell" menu and choose "Run all" to ensure that your code produces the correct results. We will take off points for code that does not work correctly.

We didn't spell out what we meant by "code correctness", but basically it means "does it produce the right answer?"  The solution does not have to be identical to what's in the solutions I've provided to you, but it *does* need to work.


## Section 1 (1D Schelling model)

**40 points total** for this section.  Point breakdown:

* 20: Does the code actually implement the Schelling model and the directions given?  (Using 0s and 1s, goes 2x through list of values, addresses neighborhoods that are 4 neighbors on either side, printing out the list at each time to see how it goes)
  * Take off 5 points if it doesn't loop through twice (and instead does something else)
  * Take off 10 points if it doesn't treat neighborhoods correctly (esp. at the edges)
  * Take off 5 points if it doesn't print out at each timestep
* 10 points: Code quality.  Is the code logically broken up into functions? Are there enough comments, and are they usable?
  * (0 pts for no comments/functions; 3 pts for poor comments/functions; 6 pts for some, but inadequate; 10 for adequate comments/functions)
* 10 points: Does it run without crashing?  (Either it does or it doesn't, so 0 or 10 points)

## Section 2 (Twitter analysis)

**60 points total** for this section.  Point breakdown:

### Data cleaning

10 points for this part, broken down as follows:

* 5 points: does their code actually remove hash tags?  (The whole word, not just the #)
* 5 points: Does it remove empty strings when the big string is split into words?

Basically, if the test string doesn't come back as **only** lower-case, punctuationless words with the hash tags removed, they lose points.

### "A more comprehensive examination of the candidates' twitter styles"

20 points for this part, broken down as follow:

* 8 points for summary: do they adequately summarize both of the questions asked?  Grade generously, but take off 4 points if they only answer one question, and give no points if they don't summarize at all.

* 12 points for code:  Does the code support their summary, with figures and printed-out numbers?
  * 4 points for code quality (0 for no comments/functions; 1 for poor comments/functions; 2 for some; 4 for adequate comments/functions)
  * 4 points for whether it runs (0 or 4; does or doesn't run)
  * 4 points for correctness (use your judgement here)

### "How do the candidates talk about each other?"

20 points for this part, broken down as follow:

* 8 points for summary: do they adequately summarize both of the questions asked?  Grade generously, but take off 4 points if they only answer one question, and give no points if they don't summarize at all.

* 12 points for code:  Does the code support their summary, with figures and printed-out numbers?
  * 4 points for code quality (0 for no comments/functions; 1 for poor comments/functions; 2 for some; 4 for adequate comments/functions)
  * 4 points for whether it runs (0 or 4; does or doesn't run)
  * 4 points for correctness (use your judgement here)


### "A different way of visualizing data"

10 points for this part.  They are supposed to generate four word clouds (2 for each candidate, positive and negative words), using text that has been provided for them.  I don't care about comments or anything here, since we gave them the code.  Give them:

* 10 points if they have all 4 word clouds
* 5 points if they have 2-3 word clouds
* 3 points if they only have 1 word cloud
* 0 points if they have zero word clouds