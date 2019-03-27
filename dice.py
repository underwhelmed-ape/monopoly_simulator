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
    print(roll)

    return roll