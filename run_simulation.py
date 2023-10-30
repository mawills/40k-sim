import random
import tkinter as tk
from typing import List
from config import NUM_TRIALS, TOUGHNESS_CHARACTERISTICS, SAVE_CHARACTERISTICS
from weapon_profile import Weapon
from damage_graph import DamageGraph


def roll_d6() -> int:
    return random.randint(1, 6)


def hit_roll(weapon: Weapon) -> int:
    num_hits = 0
    total_attacks = weapon.num_attacks * weapon.count
    for _ in range(total_attacks):
        result = roll_d6()
        if result >= weapon.skill:
            num_hits += 1

    return num_hits


def wound_roll(num_hits: int, weapon: Weapon, toughness: int) -> int:
    num_wounds = 0

    required_result_to_wound = 4
    if weapon.strength > toughness:
        required_result_to_wound -= 1
    if weapon.strength >= 2 * toughness:
        required_result_to_wound -= 1
    if weapon.strength < toughness:
        required_result_to_wound += 1
    if 2 * weapon.strength <= toughness:
        required_result_to_wound += 1

    for _ in range(num_hits):
        result = roll_d6()
        if result >= required_result_to_wound:
            num_wounds += 1

    return num_wounds


def saving_throw(numWounds: int, weapon: Weapon, save: int) -> int:
    num_failed_saves = 0
    modified_save = save + weapon.armorPen

    for _ in range(numWounds):
        result = roll_d6()
        if result < modified_save:
            num_failed_saves += 1

    return num_failed_saves


def run_simulation(parent_frame: tk.Frame, weapons: List[Weapon]):
    weapon_names = [weapon.name for weapon in weapons]

    weapon_damage_results = []
    for toughness in TOUGHNESS_CHARACTERISTICS:
        for save in reversed(SAVE_CHARACTERISTICS):
            result = []
            for weapon in weapons:
                total_damage = 0
                for _ in range(NUM_TRIALS):
                    hits = hit_roll(weapon)
                    wounds = wound_roll(hits, weapon, toughness)
                    damage = saving_throw(wounds, weapon, save)
                    total_damage += damage
                result.append(round(total_damage / NUM_TRIALS, 1))
            weapon_damage_results.append(result)

    DamageGraph.render_graph(parent_frame, weapon_names, weapon_damage_results)
