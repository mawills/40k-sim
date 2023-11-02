import random
import re
from typing import List
from config import NUM_TRIALS, TOUGHNESS_CHARACTERISTICS, SAVE_CHARACTERISTICS
from hit_roll_result import HitRollResult
from wound_roll_result import WoundRollResult
from weapon_profile import Weapon
from damage_graph import DamageGraph


def dice_roll(dice: str) -> int:
    split_string = re.split("[Dd+]", dice)

    multiplier = int(split_string[0]) if len(split_string[0]) > 1 else 1
    max_roll = int(split_string[1]) or 1
    addition = 0
    if len(split_string) > 2:
        addition = int(split_string[2]) if len(split_string[2]) > 1 else 0

    return multiplier * random.randint(1, max_roll) + addition


def attack_roll(weapon: Weapon) -> int:
    if isinstance(weapon.num_attacks, str):
        total = 0
        for _ in range(weapon.count):
            total += dice_roll(weapon.num_attacks)
        return total
    else:
        return weapon.num_attacks * weapon.count


def hit_roll(weapon: Weapon, num_attacks: int) -> HitRollResult:
    result = HitRollResult()
    for _ in range(num_attacks):
        roll = dice_roll("D6")
        if weapon.lethal_hits and roll >= weapon.critical_hit_value:
            result.add_lethal_hits(1)
        elif roll >= weapon.skill:
            result.add_hits(1)

    return result


def wound_roll(weapon: Weapon, hits: HitRollResult, toughness: int) -> WoundRollResult:
    result = WoundRollResult(hits.lethal_hits, 0)

    required_roll_to_wound = 4
    if weapon.strength > toughness:
        required_roll_to_wound -= 1
    if weapon.strength >= 2 * toughness:
        required_roll_to_wound -= 1
    if weapon.strength < toughness:
        required_roll_to_wound += 1
    if 2 * weapon.strength <= toughness:
        required_roll_to_wound += 1

    for _ in range(hits.hits):
        roll = dice_roll("D6")
        if weapon.devastating_wounds and roll >= weapon.critical_wound_value:
            result.add_devastating_wounds(1)
        elif roll >= required_roll_to_wound:
            result.add_wounds(1)

    return result


def saving_throw(weapon: Weapon, wounds: WoundRollResult, save: int) -> int:
    num_failed_saves = wounds.devastating_wounds
    modified_save = save + weapon.armorPen

    for _ in range(wounds.wounds):
        roll = dice_roll("d6")
        if roll < modified_save:
            num_failed_saves += 1

    return num_failed_saves


def damage_roll(weapon: Weapon, failed_saves: int) -> int:
    if isinstance(weapon.damage, str):
        total = 0
        for _ in range(failed_saves):
            total += dice_roll(weapon.damage)
        return total
    else:
        return weapon.damage * failed_saves


def run_simulation(weapons: List[Weapon]):
    result = {}

    for weapon in weapons:
        result[weapon.name] = []
        for toughness in TOUGHNESS_CHARACTERISTICS:
            for save in reversed(SAVE_CHARACTERISTICS):
                total_damage = 0
                for _ in range(NUM_TRIALS):
                    attacks = attack_roll(weapon)
                    hits = hit_roll(weapon, attacks)
                    wounds = wound_roll(weapon, hits, toughness)
                    failed_saves = saving_throw(weapon, wounds, save)
                    damage = damage_roll(weapon, failed_saves)
                    total_damage += damage
                result[weapon.name].append(round(total_damage / NUM_TRIALS, 1))

    DamageGraph.render_graph(result)
