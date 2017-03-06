### Import our stuff
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

### Set up initial values
position = 555 # feet
velocity = 0 # feet/second
acceleration = -32.17 # feet / second^2
time_steps = np.linspace(0, 5, 501) # creates two entries at time zero
time_step_size = time_steps[1] - time_steps[0]

### Create a way to collect/record data
initial_data = {
    'position': [position],
    'velocity': [velocity],
    'acceleration': [acceleration],
    'time': [0]
}

motion_data = pd.DataFrame(initial_data)

### Evolve the simulation forward using our update rules

for time_step in time_steps:
    velocity = velocity + (acceleration * time_step_size)
    position = position + (velocity * time_step_size)
    
    updated_data = pd.DataFrame({
        'position': [position],
        'velocity': [velocity],
        'acceleration': [acceleration],
        'time': [time_step]
    })
    motion_data = motion_data.append(updated_data)

motion_data.plot.line(
    x = 'time',
    y = 'position'
)

motion_data
    



