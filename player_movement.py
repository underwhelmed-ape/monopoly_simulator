from dice import dice_roll

def move_player(roll, player_position):
    if (player_position + roll[0]) == 40:
        player_position = 0
    elif (player_position + roll[0]) == 30:
        player_position = 10
    elif (player_position + roll[0]) > 40:
         player_position = 0 + ((player_position + roll[0]) % 40)
    else:
        player_position = (player_position + roll[0])
    
    return player_position

def roll_to_get_out_of_jail():
    pass