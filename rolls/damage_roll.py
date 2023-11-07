from weapon_profile import Weapon
from rolls.dice_roll import dice_roll


def damage_roll(weapon: Weapon, failed_saves: int) -> int:
    if isinstance(weapon.damage, str):
        total = 0
        for _ in range(failed_saves):
            roll = dice_roll(weapon.damage)
            if roll in weapon.damage_reroll_values:
                roll = dice_roll(weapon.damage)
            total += roll
        return total
    else:
        return weapon.damage * failed_saves
