

def movement_pattern():
    if (player_position + roll[0]) == 40:
        player_position = 0
    elif (player_position + roll[0]) > 40:
         player_position = 0 + ((player_position + roll[0]) % 40)
    else:
        player_position = (player_position + roll[0])