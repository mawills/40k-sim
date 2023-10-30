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
    ):
        self.name = name
        self.num_attacks = num_attacks
        self.skill = skill
        self.strength = strength
        self.armorPen = armorPen
        self.damage = damage
        self.count = count
