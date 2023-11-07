import random
import re


def dice_roll(dice: str) -> int:
    # small performance optimization for the most common roll
    if dice == "D6" or dice == "d6":
        return random.randint(1, 6)

    split_string = re.split("[Dd+]", dice)

    multiplier = int(split_string[0]) if split_string[0] != "" else 1
    max_roll = int(split_string[1])
    addition = 0
    if len(split_string) == 3:
        addition = int(split_string[2])

    total = 0
    for _ in range(multiplier):
        total += random.randint(1, max_roll)

    return total + addition
