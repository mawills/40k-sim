class Weapon:
    def __init__(
        self,
        name: str,
        num_attacks: int,
        skill: int,
        strength: int,
        armorPen: int,
        damage: int,
        count: int,
        lethal_hits: bool = False,
        sustained_hits: int = False,
        devastating_wounds: bool = False,
        critical_hit_value: int = 6,
        critical_wound_value: int = 6,
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
        self.critical_hit_value = critical_hit_value
        self.critical_wound_value = critical_wound_value
