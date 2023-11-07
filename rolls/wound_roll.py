from weapon_profile import Weapon
from rolls.hit_roll import HitRollResult
from rolls.dice_roll import dice_roll


class WoundRollResult:
    wounds = 0
    devastating_wounds = 0

    def __init__(self, wounds: int = 0, devastating_wounds: int = 0):
        self.wounds = wounds
        self.devastating_wounds = devastating_wounds

    def add_wounds(self, n: int):
        self.wounds += n

    def add_devastating_wounds(self, n: int):
        self.devastating_wounds += n


def wound_roll(weapon: Weapon, hits: HitRollResult, toughness: int) -> WoundRollResult:
    required_roll_to_wound = 4
    if weapon.strength > toughness:
        required_roll_to_wound -= 1
    if weapon.strength >= 2 * toughness:
        required_roll_to_wound -= 1
    if weapon.strength < toughness:
        required_roll_to_wound += 1
    if 2 * weapon.strength <= toughness:
        required_roll_to_wound += 1

    result = WoundRollResult(hits.lethal_hits, 0)
    for _ in range(hits.hits):
        roll = dice_roll("D6")
        if weapon.twin_linked and roll < required_roll_to_wound:
            roll = dice_roll("D6")
        elif roll in weapon.wound_reroll_values:
            roll = dice_roll("D6")
        if roll >= weapon.critical_wound_value:
            if weapon.devastating_wounds:
                result.add_devastating_wounds(1)
            else:
                result.add_wounds(1)
        elif roll >= required_roll_to_wound:
            result.add_wounds(1)

    return result
