from dice import dice_roll
import collections

print('Begin game')


goes = 0
finish = 10000 # maximum number of throws in simulation

player_position = 0 # start at Go (denoted by 0)
chance_card_positions = [7, 22, 36]
community_chest_locations = []
doubles = 0 # keeps count of the number of doubles thrown up to 3 max

position_landings = []

while goes < finish:
    print('Begin Roll')
    
    roll = dice_roll()
    if (player_position + roll[0]) == 40:
        player_position = 0
    elif (player_position + roll[0]) > 40:
         player_position = 0 + ((player_position + roll[0]) % 40)
    else:
        player_position = (player_position + roll[0])
    
    print(roll[0])
    
    print(f'Total number of goes: {goes}')
    print(player_position)
    position_landings.append(player_position)
    goes += 1
    
print(collections.Counter(position_landings))