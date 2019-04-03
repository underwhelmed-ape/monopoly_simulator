import collections
import pandas as pd

from dice import dice_roll
from cards import select_chance_card, select_community_chest_card
from player_movement import movement_pattern

print('Begin game')


goes = 0
finish = 10000 # maximum number of throws in simulation

player_position = 0 # start at Go (denoted by 0)

chance_cards = ['Drunk', 0, 39, 24, 13,
'bank_pays', 'gooj', 'back_3', 10, 'house_repairs', 
'fees', 'fine', 5, 'street_repairs', 'crossword', 'loan']
chance_card_positions = [7, 22, 36]

community_cards = [0, 19, 10, 'hospital', 'doctors', 'insurance', 'ban_error',
'annuity', 'inherit', 'stock', 'interest', 
'refund', 'prize', 'birthday', 'gooj', 'pay'] 
community_chest_locations = [2, 33]

doubles = 0 # keeps count of the number of doubles thrown up to 3 max
gooj_cards = 0

position_landings = []

while goes < finish:
    print('Begin Roll')
    
    roll = dice_roll()

    if roll[1] == True:
        doubles += 1
    else:
        doubles = 0
    print(f'Number of doubles: {doubles}')


    if doubles == 3:
        player_position == 10
        if gooj_cards > 0:
            gooj_cards -= 1
    else:
        player_position = movement_pattern(roll, player_position)

    if player_position in chance_card_positions:
        print('TAKE A CHANCE CARD')
        if len(chance_cards) == 0:
            chance_cards = ['Drunk', 0, 39, 24, 13,
                            'bank_pays', 'gooj', 'back_3', 'jail', 'house_repairs', 
                            'fees', 'fine', 5, 'street_repairs', 'crossword', 'loan']
        chance_card = select_chance_card(chance_cards)
        if isinstance(chance_card, int):
            player_position = chance_card
        elif chance_card == 'back_3':
            player_position = player_position - 3
        elif chance_card == 'gooj':
            gooj_cards += 1
            print(f'Get out of jail free cards: {gooj_cards}')
        elif chance_card == 'jail':
            print(f'Get out of jail free cards: {gooj_cards}')
            if gooj_cards == 0:
                player_position = 10
            else:
                gooj_cards -= 1

    elif player_position in community_chest_locations:
        print('TAKE A COMMUNITY CHEST CARD')
        if len(community_cards) == 0:
            community_cards = [0, 19, 10, 'hospital', 'doctors', 'insurance', 'ban_error',
                                'annuity', 'inherit', 'stock', 'interest', 
                                'refund', 'prize', 'birthday', 'gooj', 'pay']
        community_card = select_community_chest_card(community_cards)
        if isinstance(community_card, int):
            player_position = community_card
        elif community_card == 'gooj':
            gooj_cards += 1
        

    print(f'Total number of goes: {goes}')

    print(player_position)
    position_landings.append(player_position)
    goes += 1
    
res = collections.Counter(position_landings)
print(res)
