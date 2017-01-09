# Grading rubric for Homework 2

This assignment is worth 100 points (scaled to whatever is in the grade book), divided up as follows:

## Section 1 (Radioactivity wrapup)

25 points total for this section.  Point breakdown:

* 15 points for the code:
  * 5 points: does the code actually smooth over the ~2N adjacent samples (i-N to i+N), where N is a free parameter?  
  * 5 points: did they plot the noisy data with the smoothed data?
* 10 points for their answer:
  * 5 points: did they create an analytic expression using the values they determined from the smoothed data, and plot it on top of the noisy data and smoothed data?
* 10 points for their answer:
  * 6 points: did they actually give us the constants that they determined (there should be 3; 2 points/constant) in units of either counts/bin or counts/second?  (counts/second = 1/5 of counts/bin)
  * 4 points: did they state whether the values made sense, and explain why or why not?  (don't be too picky here - just looking for examples of critical thinking)

## Section 2 (Great Lakes water levels)

30 points total for this section.  Point breakdown:

* 10 points for Question 1
  * 5 points if they correctly wrote code to calculate mean values
  * 5 points if they give a correct answer, particularly explaining why Lake Ontario is much lower.  If they just state their answers without explaining Lake Ontario, only give them **2 points.**
* 10 points for Question 2
  * 5 points if they write code to make a plot showing the heights minus the historical average.  **ZERO POINTS** if they don't subtract the mean values. 
  * 5 points if they give the correct answer (similar patterns observed).  Don't penalize the students if they don't get the physical explanation (regional weather patterns) correct - just as long as they have a plausible guess.  Still give credit for a corect answer if they don't remember to subtract off the mean values in the code.
* 10 points for Question 3
  * 5 points for code - basically copy-and-paste of Question 2 but with a different x limits.  We didn't specific that they subtract off the mean values here, so don't penalize them if they don't.
  * 5 points for answer - "it has reversed itself, and it's a fluke."
 
## Section 3 (Modeling drug doses in the human body)

45 points total for this section.  Point breakdown:

* 20 points for Part 1 (aspirin):
  * 10 points for code: does it correctly solve the problem?  If there are numerical problems (concentration wrong, for example) take off 5 points and grade the answer/plot using the wrong values.
  * 5 points for plot: does it have title, x/y axis label, and appropriate x limits?  (12 hours on x-axis)
  * 5 points for answering question: be generous with numbers, accept anything in the ~1.5-2 hour range.
* 25 points for Part 2 (Dilantin):
  * 10 points for answering questions - 5 points apiece for each of the two questions asked.  Don't be too picky about the exact numbers - as long as they're reasonably close to what you find in the solutions.
  * 10 points for code: did they use some sort of Boolean logic to show the drug dosage?
  * 5 points for plot: did they have a plot, and does it have reasonable x and y limits?  We didn't specificy that they should have labels, titles, etc., so don't grade on that.

**Note:** I originally gave the students an incomplete homework - for Part 2 of Section 3 (Dilantin) I forgot to tell them that the drug is not completely absorbed into the bloodstream.  So, if they use the original (wrong) numbers, also grade it assuming that they're correct - just use the appropriate numbers in the solutions, and be relatively generous with the numbering.