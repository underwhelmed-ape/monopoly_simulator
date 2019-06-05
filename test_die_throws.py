from dice import dice_roll

def test_if_dice_roll_return_integer():
    assert isinstance(dice_roll()[0], int)

