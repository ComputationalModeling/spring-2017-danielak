# Grading rubric for Homework 2

This assignment is worth 100 points (scaled to whatever is in the grade book), divided up as follows:

## Section 1 (... simple model)

45 points total for this section.

**Code:**  25 points.

* 15 points: does code do the correct thing and successfully execute?
* 5 pts: does the code have the correct input assumptions? (i.e., correct values of all constants)
* 5 pts: is code relatively well organized and readable?  (If students do not use functions for the models, but instead copy and paste the loop over and over again, they DO NOT GET THESE POINTS)

**Answers to questions:**  20 points.  Note: this includes figures, answers to questions, tables, etc. (basically everything that's not code)!

* 5 points: is table of investments/inflation there and approximately correct?
* 5 points: is plot of investment returns for 6 models there and colored sensibly?
* 4 points: does table showing per-year retirement income exist?  (It's OK if it's not pretty, as long as the information is there.)
* 6 points: Are the three questions answered reasonably well?  (2 points each).

## Section 2 (... slightly more complex model)

25 points total for this section.  

**Code:**  10 points.  

* 5 points:  The primary thing we're looking for with this code is that the students have added a random element corresponding to market growth, by doing something similar to adding a call to ```random.uniform()```.  Do not penalize the students for any code oddities copied from section 1.  This is approximately a binary outcome; if they have the random element done in a sensible way, they get the points; if not, no points.
* 5 points:  This is if the students correctly implement the "two extreme scenarios" portion of the problem, by running the scenarios many times and creating a list/array that contains the final amount of money from each run.

**Answers to questions:**  15 points.   Note: this includes figures, answers to questions, tables, etc. (basically everything that's not code)

* 5 points: plot of growth of investment portfolio for each of the six scenarios.  Is it present and colored sensibly?
* 5 points: histograms for two extreme scenarios; are they there and do they display the values in a sensible way?  (Note: it doesn't matter if they don't renormalize the distribution, alter the axes, etc., just as long as the histograms show all of the data)
* 5 points: answer to "how is this different from section 1?"  The key thing we're looking for here is that is shows *variation* as well as the mean value.

## Section 3 (... an even better model)

30 points total for this section.

**Code:** 10 points.  Consult the previous section in terms of point distribution; we want to make sure that all of the randomization is taken care of correctly, and that the students generate the ensembles of outcomes correctly as well.

**Answers to questions:**  20 points.   Note: this includes figures, answers to questions, tables, etc. (basically everything that's not code)

* 5 points: plot of growth of investment portfolio for each of the six scenarios.  Is it present and colored sensibly?
* 5 points: histograms for two extreme scenarios; are they there and do they display the values in a sensible way?  (Note: it doesn't matter if they don't renormalize the distribution, alter the axes, etc., just as long as the histograms show all of the data)
* 10 points: 3 questions at the end of this section.  
  * 3 points: First question (what parts agree/disagree).  This is not particularly well-posed, since this model doesn't really look all that different from the section 2 model.  Give points if they talk about showing a range of outcomes (distribution) as opposed to just mean value.  
  * 4 points: second question (how might a portfolio behave?)  Looking for variation in investment yields over time - helps to show investors that the market has lots of randomness, and not to panic!
  * 3 points: third question (how to improve model?).  Anything reasonable gets the points.  Use your discretion.

  
