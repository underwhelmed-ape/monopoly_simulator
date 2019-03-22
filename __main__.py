from dice import dice_roll

print('Begin game')


goes = 0
finish = 100

while goes < finish:
    position = 0

    roll = dice_roll()

    position = 40 % (position + roll[0])

    print(position)
    print(f'Total number of goes: {goes}')
    goes += 1