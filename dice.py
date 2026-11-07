import random

POSSIBLE_DICE = [4, 6, 8, 10, 12, 20, 100]

class InvalidDiceChoice(Exception):
    pass

def dice_roll (die):
    # Create a way for non-valid entries to through an error.
    if not die.isdigit():
        raise InvalidDiceChoice("That is not a valid die choice. \n")
    die = int(die)
    if die not in POSSIBLE_DICE:
        raise InvalidDiceChoice("That is not a valid die choice. \n")
    else:
        return random.randint(1, die)
