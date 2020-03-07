import collections
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from dice import dice_roll
from cards import select_chance_card, select_community_chest_card
from player_movement import move_player

def run_games(number_of_throws=100, games=10000):

    number_of_games = games # number of simulated games to play
    game_results = {}

    print(f'Begin {number_of_games} games')

    for game in range(number_of_games):

        throws_counter = 0
        number_of_throws = number_of_throws # maximum number of throws in game simulation

        # list of chance cards and actions
        chance_cards = ['Drunk', 0, 39, 24, 13,
                        'bank_pays', 'gooj', 'back_3', 10, 'house_repairs', 
                        'fees', 'fine', 5, 'street_repairs', 'crossword', 'loan']

        chance_card_positions = [7, 22, 36]

        # list of community chest cards and actions
        community_cards = [0, 19, 10, 'hospital', 'doctors', 'insurance', 'ban_error',
                        'annuity', 'inherit', 'stock', 'interest', 
                        'refund', 'prize', 'birthday', 'gooj', 'pay'] 

        community_chest_locations = [2, 33]

        # track number of consecutive doubles thrown and 'get out of jail free' cards acquired
        doubles = [False, False, False]
        non_doubles_in_jail = 0 
        gooj_cards = 0

        player_position = 0 # start at Go (denoted by 0)
        in_jail = False # tracks if player is in jail or visiting jail, defaults visiting

        # track every space landed on during a game
        position_landings = []

        while throws_counter <= number_of_throws:
        
            roll = dice_roll()

            # if roll is a third consecutive double, move to jail
            if roll[1]:
                if doubles == [False, False, False]:
                    doubles[0] = True
                elif doubles == [True, False, False]:
                    doubles[1] = True
                elif doubles == [True, True, False]:
                    doubles[2] = True
                    player_position = 10
                    in_jail = True
                    doubles = [False, False, False]
                    position_landings.append(player_position)
                    throws_counter += 1
                    continue
            else: 
                doubles = [False, False, False]
            
            # if find on jail square have a seperate set of rules
            if in_jail:
                if gooj_cards > 0:
                    gooj_cards -= 1
                    in_jail = False
                    throws_counter += 1
                    continue
                
                if roll[1]:
                    #player_position = move_player(roll, player_position)
                    non_doubles_in_jail = 0
                    in_jail = False
                    throws_counter += 1
                    continue
                else:
                    non_doubles_in_jail += 1
                    throws_counter += 1
                    if non_doubles_in_jail >= 3:
                        in_jail = False
                        continue
                    else:
                        continue
                # currently if roll double and get out of jail, the counter still removes a card
                # also only want to roll three times before getting out of jail automatically


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
                elif chance_card == 'jail':
                    player_position = 10
                    in_jail = True


            elif player_position in community_chest_locations:
                #print('TAKE A COMMUNITY CHEST CARD')
                if len(community_cards) == 0:
                    community_cards = [0, 1, 'jail', 'hospital', 'doctors', 'insurance', 'ban_error',
                                        'annuity', 'inherit', 'stock', 'interest', 
                                        'refund', 'prize', 'birthday', 'gooj', 'pay']
                community_card = select_community_chest_card(community_cards)
                if isinstance(community_card, int):
                    player_position = community_card
                elif community_card == 'gooj':
                    gooj_cards += 1
                elif community_card == 'jail':
                    player_position = 10
                    in_jail = True

            #print(f'Total number of goes: {throws_counter}')

            #print(player_position)
            position_landings.append(player_position)
            throws_counter += 1
            
        res = collections.Counter(position_landings)
        #print(res)

        game_results[game] = res
    results_df = pd.DataFrame()

    for game_number, game_results in game_results.items():
        results_df = results_df.append(game_results, ignore_index=True)
    return results_df
    
