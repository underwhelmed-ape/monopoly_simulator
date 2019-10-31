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
 
    return roll

# inputs roll if double and outputs 
def doubles_checker(dice_roll, doubles_tracker):
    if dice_roll[1]:
        if doubles_tracker == [False, False, False]:
            doubles_tracker[0] = True
        elif doubles_tracker == [True, False, False]:
            doubles_tracker[1] = True
        elif doubles_tracker == [True, True, False]:
            doubles_tracker[2] = True
            print('go to jail')
            doubles_tracker = [False, False, False]
    else: 
        doubles_tracker = [False, False, False]


if __name__ == "__main__":

    from random import randint    
    #import plotly.plotly as py
    #import plotly.graph_objs as go
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt

    doubles = [False, False, False]

    for i in range(1000):
        roll = dice_roll()
        if roll[1]:
            if doubles == [False, False, False]:
                doubles[0] = True
            elif doubles == [True, False, False]:
                doubles[1] = True
            elif doubles == [True, True, False]:
                doubles[2] = True
                print('go to jail')
                doubles = [False, False, False]
        else: 
            doubles = [False, False, False]
        # if find on jail square have a seperate set of rules

    # rolls = {}
    # for i in range(10000):
    #     roll = dice_roll()[0]
    #     if roll in rolls:
    #         rolls[roll] += 1
    #     else:
    #         rolls[roll] = 1
    
    # print(rolls)
    # print(rolls.items())

    # plt.bar(list(rolls.keys()), rolls.values(), color='g')
    # plt.show()
