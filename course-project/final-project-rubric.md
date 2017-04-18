# Data Analysis Final Project (Due 26 April 2017)

## What you will turn in

1. A Jupyter Notebook (`.ipynb` file) or a commented Python file (`.py`). 
2. A reference to any datasets you're using.
	1. If your pandas command looks like this `pd.read_csv("http://something.csv")`, then that means you're getting your data over the web. Just submit your Python script/notebook as normal. BUT, 
	2. If your pandas command looks like this `pd.read_csv("Some/Directory/myData.csv")`, then you're working with a downloaded copy of the data. We need you to include a copy of `myData.csv` as part of your submission. 
	
As a reminder, you can comment your Python code using triple-quotes.

```python
"""
First, we load a fake dataset that I just made up.
"""
pd.read_csv("http://clowns-in-gokarts-getting-pies.com/pie_production_data.csv")
```

## How we'll grade your submission (780 total possible points)

Pose **3** questions that you're trying to answer in your data analysis. 

### For each of your three questions (260 points )

####  1. State your question (20 points)

Say  you had data from the [Annual Nathan's Hot Dog Eating Contest](http://www.nathansfamous.com/hot-dog-eating-contest). Example questions might be:

- What's the relationship between column X and column Y? (What's the relationship between a contestant's weight and the number of hot dogs they eat? Is there one?)
- Does one country tend to produce winning eaters who weigh far less than winners from other countries? (Let's look st weight vs. hot dogs eaten, but break that down further by which country a contestant is from)
- Is there a trend or pattern in how many hot dogs it takes to win each year? (Group all the contestants by year, then figure out the winning number of hot dogs for each year. This could tell us whether there's a pattern in how many hot dogs it takes to win.)
- Can I predict future wins? Say I looked at "winning number of hot dogs eaten" vs. competition year. If I fit a mathematical model (like a simple line) to my data, can I predict how many hot dogs it might take to win ten years from now?

#### 2. Include  *at least one* plot or table that shows how you tried to answer the question. (80 points).

Be thorough. For plots, you'll have to **label your axes** and **give the plot a title**. If you're not sure how to do that, now is the time to ask us and get help.

#### 3. Reflect on your question (160 points)

In 4 or more sentences, reflect on your answer. Your reflection may include—*but isn't limited to*—the following:

- Was it what you expected? 
- Does it make sense? 
- How convincing is your evidence (plots/tables)? For example, if your data showed a fuzzy/noisy relationship between weight and hot dogs eaten, that probably means it's hard to predict hot dogs eaten from just weight alone.
- Was it tricky to write the code that answered this question?? If so, describe your obstacles and how you moved past them. 
