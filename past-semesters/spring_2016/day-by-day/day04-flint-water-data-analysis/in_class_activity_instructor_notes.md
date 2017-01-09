### Data plotting Activity

We'll be looking at the recently released [Flint Water Quality dataset](http://flintwaterstudy.org/2015/12/complete-dataset-lead-results-in-tap-water-for-271-flint-samples/). This is a dataset of nearly 300 tests run by volunteers at Virginia Tech on water samples obtained from Flint residents. The water testing method involves collecting three different bottles worth of water at timed intervals; our analysis will focus on just the first collection at each testing site. **This work is part of the Social Responsibility strand of the course: data analysis for social impact.**

The dataset will be hard-encoded into the notebook (as a JSON string), so students won't have to do any remote fetching for it. What they will have to do is consider ans try to answer the following questions in the context of U.S. Environmental Protection Agency (EPA) guidelines about lead contaminants, which state:

> Lead and copper are regulated by a treatment technique that requires systems to control the corrosiveness of their water. **If more than 10% of tap water samples exceed the action level**, water systems must take additional steps. For copper, the action level is 1.3 mg/L, and for lead is 0.015 mg/L. 
>
> Source: (http://www.epa.gov/your-drinking-water/table-regulated-drinking-water-contaminants#seven). 

Students will have to consider the following as part of an iPython notebook:

- The sample readings are in ppb (parts per billion). But, the U.S. Environmental Protection Agency's guidelines are expressed in mg/L, or milligrams per liter. What will we need to do in order to compare the data collected to the EPA's guideline threshold?
- What's the mean of all the lead readings?
- Do you think the mean is representative of how good (or bad) the overall lead levels in Flint water? If so, why; if not, why not? **Really take some time to think this one through.** Try to justify your group's opinions by using plots, calculations, or anything else you feel appropriately supports your point.
- How does the mean for all the readings compare to the EPA's "action level"?
- Is comparing the mean to the action level enough to tell us whether Flint had a definite problem with its drinking water? If so, why? If not, why not? Take some time to think this through.

**As a class, we're going to write a letter to Governor Rick Snyder's office on behalf of the residents of Flint.** Let's show state officials our opinion on the severity of the problem. In the letter, we'll need to take a clear position on the issue: *did the water exceed the action limits? And if it did, how can we understand how badly it exceeded the limits?* We'll also  need to:

- Justify that position using whatever diagrams, plots, calculations, estimations, and/or explanations support our point
- Assume the state might be resistant. Consider how someone might argue against our point. (Could they find evidence in the data to support an opposing position to ours? How would they do it?)
- Once you've identified ways someone could try to argue against us, explain how/why their arguments are flawed. In other words, we need to think like the opposition, figure out how they would argue their case, and show why their case doesn't hold up. Again, justify our counterarguments using whatever diagrams, plots, calculations, estimations, and/or explanations support our point.

### Homework

If students don't finish the assignment in class, the remainder is going to be their homework. (That's not punishment! It's just a reflection on the fact that we don't know how far we'll get or how quickly.) In addition, if students do make rapid progress in class, then the homework will include some additional questions:

- Is the contamination better/worse in certain areas? That is, if we try to consider ZIP codes, what information (if any) do we get?
- Within a household, how variable are the bottle readings? Does that spell trouble for our position on the issue? If so, why? If not, why not?
- It seems like the sample IDs go from 1-300, but there are only about 270 rows of data. What's going on there? How can you describe/explain the numerical mismatch?

