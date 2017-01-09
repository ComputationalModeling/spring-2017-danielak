# Exploring Social Demographic Changes Through Simulation

Today we're going to use a game-based simulation to try to see how small-scale individual preferences can have larger effects on society.

We want you to:

- play the simulation, to
- build an intuition about how this works
- See how it plays out at larger scales
- actually build your own version

We'll alternate between playing/within-group discussion and whole-class discussion. Ask that if students are already familiar with this model, they try to refrain from just jumping in. Students who are trying to make sense of this for themselves should have that chance.

## Demo the game on-screen for the whole class (5 min)

Show them quickly how moving shapes makes them happier (by dragging and dropping the unhappy polygons just once).

## Whole-class discussion questions (5-10 min)

- The game describes polygons being happy or unhappy. What kind of measure is "happiness?" (point to the unhappy/happy/meh explanation on the page)
- Before playing the game, what do you predict an overall solution would look like if it tried to maximize the total happiness of the society of shapes (that is, if it tried to make sure that however we're measuring society-wide happiness, we try to optimize for it)?

## Play the first round of the game in your groups. (10-15 min, or until you feel satisfied everyone has played a bit)

Think about what we discussed as a class as you work. 

## Whole class discussion (10-15 min)

- What were people's reactions?
- Did anyone pay attention to how many moves it took?
- What would happen if we tried to maximize happiness with the minimum number of moves?
- How/when did you decide to stop playing a given board/reset to a new board? What might that mean for coded models that try to "play" the same game?

segue into...

## Run the simulation (15-20 min)

Questions groups can think about:

- How is segregation being measured?
- How is the game actually operating each time you run it?
- Does "segregation" ever stabilize? 
	- If the game stops, why do you think it stops?

## Whole-class discussion (15-20 min)

- How do you think segregation gets computed? 
	- What do you think it means?
	- Does the segregation graph look noisy?
	- If so, why?
- What happens if you try different kinds of initial board setups?
	- Can you start with different kinds of neighborhoods?
	- How do they change?
- The simulation seems to show segregation, but not happiness. What do you think it would look like if you tried to also have a plot of happiness over time that ran during the simulation. How would you decide to compute the metric as a function of each individual shape?
- If we think of the game as taking "turns" as it simulates, *how* is it taking a turn? 
	- How would you write instructions that tell the game how to take a turn?
- What's the smallest "turn" that you think happens in the game?
	- Should you compute the happiness as a function of time at the resolution of per-turn? Why or why not?
	- If you tried to compute happiness, how would you write instructions to compute the happiness value each turn?
	- 


