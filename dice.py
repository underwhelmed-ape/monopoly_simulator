from random import randint

# rolls two dice and returns the sum and boolean of double throw

def dice_roll():
    roll = []
    die_1 = randint(1, 6)
    die_2 = randint(1, 6)
    roll.append((die_1 + die_2))
    if die_1 == die_2:
        roll.append(True)
    else: 
        roll.append(False)
    #print(roll) 

    return roll

if __name__ == "__main__":

    from random import randint    
    #import plotly.plotly as py
    #import plotly.graph_objs as go
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt

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
    plt.show()
