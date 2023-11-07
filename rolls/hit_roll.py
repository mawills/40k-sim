from weapon_profile import Weapon
from rolls.dice_roll import dice_roll


class HitRollResult:
    hits = 0
    lethal_hits = 0

    def __init__(self, hits: int = 0, lethal_hits: int = 0):
        self.hits = hits
        self.lethal_hits = lethal_hits

    def add_hits(self, n: int):
        self.hits += n

    def add_lethal_hits(self, n: int):
        self.lethal_hits += n


def hit_roll(weapon: Weapon, num_attacks: int) -> HitRollResult:
    if weapon.torrent:
        return HitRollResult(num_attacks)

    result = HitRollResult()
    for _ in range(num_attacks):
        roll = dice_roll("D6")
        if roll in weapon.hit_reroll_values:
            roll = dice_roll("D6")
        if roll >= weapon.critical_hit_value:
            if isinstance(weapon.sustained_hits, str):
                result.add_hits(dice_roll(weapon.sustained_hits))
            elif weapon.sustained_hits > 0:
                result.add_hits(weapon.sustained_hits)
            if weapon.lethal_hits:
                result.add_lethal_hits(1)
            else:
                result.add_hits(1)
        elif roll >= weapon.skill:
            result.add_hits(1)

    return result
