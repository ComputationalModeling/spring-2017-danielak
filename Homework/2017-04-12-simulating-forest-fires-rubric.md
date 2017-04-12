# Simulating Forest Fires. (No students or trees were harmed)

## What your group will turn in
A python file `.py` or Jupyter Notebook `.ipynb` that does the following:

1. **Set up** the forest (150) points) by clearly having places in your code where someone can specify:
	1. `width` and `height` for the two-dimensional forest (50 points)
	2. `density` - a number from 0 to 1 (or zero to 100) that specifies how many cells of the forest should have trees in them (50 points)
	3. A grid location (x,y or row-column coordinates) of where to start the fire.
2. **Collect data** as the simulation runs (100 points)
	1. Set up a dataframe. The dataframe should contain enough info that we can get a tree's coordinates and status (on fire? Healthy?) for every single round. (We suggest making a dataframe with at least columns for `round_number`, `tree_coordinates`, and `tree_state` 
3. **Run the simulation** (100 points)
	1. The simulation should proceed in rounds. Every round, it should spread fire to any unlit trees that are next to lit trees. 
4. **Stop the simulation** (100 points). 
	1. In your code, clearly indicate where someone could specify a number of rounds they want to simulate. 
	2. Have an option where the simulation will run as many rounds as it takes until the fire can spread no further (for example, it stops when all trees are on fire. With this option, it should also stop if there's nowhere the fire can spread (in a low-density forest, not all trees may touch each other. So, your simulation should stop when there are no healthy trees the fire can spread to.)
5. **Generate Plots** (100 points). You must generate the following plots:
	1. **After each round**
		1. A plot of the forest (with at least 3 different colors showing empty cells, healthy trees, burning trees)
	2. **After the simulation stops**
		1. A plot of round_number vs. percent_burned, just like we made on the board after our forest fire game day
6. **Reflect and explain** (500 points). In at least one paragraph **each**
	1. **Identify** and **explain** least two strengths of this kind of model for understanding fire spread. 
	2. **Identify** and **explain** at least two limitations of your model. Limitations include (but are not limited to) the simplifying assumptions your model makes  
	3. What was hard about this simulation? Why was it hard?
	4. If we were teaching this class again, do you think we should use the human-scale forest fire game we played outside? If so, why? If not, why not? If "meh" or "maybe", suggest something you think would help more and explain why you think it would help.
	5. If you had an extra week to work on this project, what changes would you make to your code?


#cmse201
