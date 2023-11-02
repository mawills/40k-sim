from typing import List
from weapon_profile import Weapon


class JsonParser:
    def parse_input(self, data) -> List[Weapon]:
        weapons = []
        for weapon in data:
            name = weapon
            weapon = data[weapon]
            weapons.append(
                Weapon(
                    name,
                    weapon["num_attacks"],
                    weapon["skill"],
                    weapon["strength"],
                    weapon["armor_pen"],
                    weapon["damage"],
                    weapon["count"],
                    weapon.get("lethal_hits", False),
                    weapon.get("sustained_hits", 0),
                    weapon.get("devastating_wounds", False),
                    weapon.get("critical_hit_value", 6),
                    weapon.get("critical_wound_value", 6),
                )
            )
        return weapons
