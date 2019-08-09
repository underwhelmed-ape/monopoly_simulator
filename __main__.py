import collections
import pandas as pd

from dice import dice_roll
from cards import select_chance_card, select_community_chest_card
from player_movement import move_player

games = 0 # count the number of games played
number_of_games = 500000 # number of simulated games to play

print(f'Begin {number_of_games} games')

game_results = {}

for game in range(number_of_games):

    #print(f'Game number: {game}') # start at 1

    goes = 0
    finish = 100 # maximum number of throws in game simulation

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

    player_position = 0 # start at Go (denoted by 0)

    position_landings = []

    while goes < finish:
        #print('Begin Roll')
        
        roll = dice_roll()

        if roll[1] == True:
            doubles += 1
        else:
            doubles = 0
        #print(f'Number of doubles: {doubles}')

        if doubles == 3:
            player_position == 10
            if gooj_cards > 0:
                gooj_cards -= 1
        else:
            player_position = move_player(roll, player_position)

        if player_position in chance_card_positions:
            #print('TAKE A CHANCE CARD')
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
                #print(f'Get out of jail free cards: {gooj_cards}')
            elif chance_card == 'jail':
                #print(f'Get out of jail free cards: {gooj_cards}')
                if gooj_cards == 0:
                    player_position = 10
                else:
                    gooj_cards -= 1

        elif player_position in community_chest_locations:
            #print('TAKE A COMMUNITY CHEST CARD')
            if len(community_cards) == 0:
                community_cards = [0, 19, 10, 'hospital', 'doctors', 'insurance', 'ban_error',
                                    'annuity', 'inherit', 'stock', 'interest', 
                                    'refund', 'prize', 'birthday', 'gooj', 'pay']
            community_card = select_community_chest_card(community_cards)
            if isinstance(community_card, int):
                player_position = community_card
            elif community_card == 'gooj':
                gooj_cards += 1
            

        #print(f'Total number of goes: {goes}')

        #print(player_position)
        position_landings.append(player_position)
        goes += 1
        
    res = collections.Counter(position_landings)
    #print(res)

    game_results[game] = res
results_df = pd.DataFrame()

for game_number, game_results in game_results.items():
    results_df = results_df.append(game_results, ignore_index=True)

xtab = results_df.apply(lambda r: r/r.sum()*100, axis=1)
print(xtab.mean(axis=0))



# appending dictionaries to pd.DF
# df1 = pd.DataFrame()
# d1 = {'one':1, 'two':2}
# d2 = {'one':3, 'two':4, 'three':5}
# df1 = df1.append(d1, ignore_index=True)
# df1 = df1.append(d2, ignore_index=True)
# print(df1)


# Begin 100000 games
# 0     2.982747
# 1     2.367835
# 2     2.081516
# 3     2.454893
# 4     2.602581
# 5     2.896052
# 6     2.572994
# 8     2.604271
# 9     2.575423
# 10    5.760698
# 11    2.517958
# 12    2.568942
# 13    2.987252
# 14    2.668750
# 15    2.793090
# 16    2.901533
# 17    3.024083
# 18    2.979752
# 19    3.380836
# 21    2.927911
# 22    1.913861
# 23    2.874667
# 24    3.302865
# 25    2.911423
# 26    2.900462
# 27    2.871542
# 29    2.808935
# 31    2.831517
# 32    2.766514
# 34    2.649165
# 35    2.576660
# 36    1.706357
# 37    2.393030
# 38    2.390801
# 39    2.740947
# 7     1.770901
# 20    2.958121
# 28    2.840913
# 33    2.418398
# dtype: float64