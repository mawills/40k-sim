from weapon_profile import Weapon
from config import DEFENDER_UNIT_SIZE
from rolls.dice_roll import dice_roll


def attack_roll(weapon: Weapon) -> int:
    blast_total = 0
    if weapon.blast:
        blast_total += DEFENDER_UNIT_SIZE // 5

    if isinstance(weapon.num_attacks, str):
        total = 0
        for _ in range(weapon.count):
            total += dice_roll(weapon.num_attacks)
        return total + blast_total
    else:
        return (weapon.num_attacks * weapon.count) + blast_total
