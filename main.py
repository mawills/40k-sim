import json
from typing import List
from run_simulation import run_simulation
from weapon_profile import Weapon

with open("weapons.json", "r") as json_file:
    data = json.load(json_file)

# TODO:
# - validate user input
# - pull data from user input instead of hardcoded weapons
# - add weapon abilities (lethal hits, sustained hits, etc.)


def parse(data) -> List[Weapon]:
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


weapons = parse(data)
run_simulation(weapons)
