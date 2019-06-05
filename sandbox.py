from dice import dice_roll

doubles = 0

def doubles_counter(roll):
    doubles = 0
    if roll[1] == True:
        doubles += 1
    else:
        doubles = 0
    print(f'Number of doubles: {doubles}')

    

for i in range(150):
    roll = dice_roll()

    if roll[1] == True:
        doubles += 1
    else:
        doubles = 0
    print(f'Number of doubles: {doubles}')

    if doubles == 3:
        doubles = 0
        print(f'go to jail. Number of doubles is now {doubles}')
        
