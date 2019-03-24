import collections

import pandas as pd


from dice import dice_roll
from cards import select_chance_card, select_community_chest_card

print('Begin game')


goes = 0
finish = 10000 # maximum number of throws in simulation

player_position = 0 # start at Go (denoted by 0)
chance_card_positions = [7, 22, 36]
community_chest_locations = [2, 33]
doubles = 0 # keeps count of the number of doubles thrown up to 3 max

position_landings = []

while goes < finish:
    print('Begin Roll')
    
    roll = dice_roll()
    print(roll[0])
    if (player_position + roll[0]) == 40:
        player_position = 0
    elif (player_position + roll[0]) > 40:
         player_position = 0 + ((player_position + roll[0]) % 40)
    else:
        player_position = (player_position + roll[0])
    
    if player_position in chance_card_positions:
        print(f'take chance')
        chance_card = select_chance_card()
        if isinstance(chance_card, int):
            player_position = chance_card

    elif player_position in community_chest_locations:
        print(f'take community chest')
        community_card = select_community_chest_card()
        if isinstance(community_card, int):
            player_position = community_card

    print(f'Total number of goes: {goes}')
    print(player_position)
    position_landings.append(player_position)
    goes += 1
    
print(collections.Counter(position_landings))