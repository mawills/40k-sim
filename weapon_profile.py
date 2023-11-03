class Weapon:
    def __init__(
        self,
        name: str,
        num_attacks: int | str,
        skill: int,
        strength: int,
        armorPen: int,
        damage: int,
        count: int,
        lethal_hits: bool,
        sustained_hits: int,
        devastating_wounds: bool,
        torrent: bool,
        blast: bool,
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
        self.critical_hit_value = critical_hit_value
        self.critical_wound_value = critical_wound_value
