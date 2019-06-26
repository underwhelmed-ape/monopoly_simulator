#%% Import packages

from random import randint    
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from dice import dice_roll



#%% Dice roll statistics


rolls = {}
for i in range(10000):
    roll = dice_roll()[0]
    if roll in rolls:
        rolls[roll] += 1
    else:
        rolls[roll] = 1

print(rolls)
print(rolls.items())

plt.bar(list(rolls.keys()), rolls.values(), color='g')
