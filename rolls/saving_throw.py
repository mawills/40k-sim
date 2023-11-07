from weapon_profile import Weapon
from wound_roll_result import WoundRollResult
from rolls.dice_roll import dice_roll


def saving_throw(weapon: Weapon, wounds: WoundRollResult, save: int) -> int:
    modified_save = save + weapon.armorPen
    if modified_save > 6:
        return wounds.wounds + wounds.devastating_wounds

    num_failed_saves = wounds.devastating_wounds
    for _ in range(wounds.wounds):
        roll = dice_roll("d6")
        if roll < modified_save:
            num_failed_saves += 1

    return num_failed_saves
