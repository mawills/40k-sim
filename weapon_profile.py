from typing import List


class Weapon:
    def __init__(
        self,
        name: str,
        num_attacks: int | str,
        skill: int,
        strength: int,
        armorPen: int,
        damage: int | str,
        count: int,
        lethal_hits: bool,
        sustained_hits: int | str,
        devastating_wounds: bool,
        torrent: bool,
        blast: bool,
        twin_linked: bool,
        hit_reroll_values: List[int],
        wound_reroll_values: List[int],
        damage_reroll_values: List[int],
        critical_hit_value: int,
        critical_wound_value: int,
    ):
        self.name = name
        self.num_attacks = num_attacks
        self.skill = skill
        self.strength = strength
        self.armorPen = armorPen
        self.damage = damage
        self.count = count
        self.lethal_hits = lethal_hits
        self.sustained_hits = sustained_hits
        self.devastating_wounds = devastating_wounds
        self.torrent = torrent
        self.blast = blast
        self.twin_linked = twin_linked
        self.hit_reroll_values = hit_reroll_values
        self.wound_reroll_values = wound_reroll_values
        self.damage_reroll_values = damage_reroll_values
        self.critical_hit_value = critical_hit_value
        self.critical_wound_value = critical_wound_value
