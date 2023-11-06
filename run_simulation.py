import random
import re
from typing import List
from config import (
    NUM_TRIALS,
    TOUGHNESS_CHARACTERISTICS,
    SAVE_CHARACTERISTICS,
    DEFENDER_UNIT_SIZE,
    DEFENDER_WOUND_PER_MODEL,
    SHOW_MODELS_SLAIN,
    OUTPUT_TYPE,
)
from hit_roll_result import HitRollResult
from wound_roll_result import WoundRollResult
from weapon_profile import Weapon
from damage_plot import DamagePlot
from damage_table import DamageTable


def dice_roll(dice: str) -> int:
    # small performance optimization for the most common roll
    if dice == "D6" or dice == "d6":
        return random.randint(1, 6)

    split_string = re.split("[Dd+]", dice)

    multiplier = int(split_string[0]) if split_string[0] != "" else 1
    max_roll = int(split_string[1])
    addition = 0
    if len(split_string) == 3:
        addition = int(split_string[2])

    total = 0
    for _ in range(multiplier):
        total += random.randint(1, max_roll)

    return total + addition


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


def hit_roll(weapon: Weapon, num_attacks: int) -> HitRollResult:
    if weapon.torrent:
        return HitRollResult(num_attacks)

    result = HitRollResult()
    for _ in range(num_attacks):
        roll = dice_roll("D6")
        if roll in weapon.hit_reroll_values:
            roll = dice_roll("D6")
        if roll >= weapon.critical_hit_value:
            if weapon.sustained_hits > 0:
                result.add_hits(weapon.sustained_hits)
            if weapon.lethal_hits:
                result.add_lethal_hits(1)
            else:
                result.add_hits(1)
        elif roll >= weapon.skill:
            result.add_hits(1)

    return result


def wound_roll(weapon: Weapon, hits: HitRollResult, toughness: int) -> WoundRollResult:
    required_roll_to_wound = 4
    if weapon.strength > toughness:
        required_roll_to_wound -= 1
    if weapon.strength >= 2 * toughness:
        required_roll_to_wound -= 1
    if weapon.strength < toughness:
        required_roll_to_wound += 1
    if 2 * weapon.strength <= toughness:
        required_roll_to_wound += 1

    result = WoundRollResult(hits.lethal_hits, 0)
    for _ in range(hits.hits):
        roll = dice_roll("D6")
        if weapon.twin_linked and roll < required_roll_to_wound:
            roll = dice_roll("D6")
        elif roll in weapon.wound_reroll_values:
            roll = dice_roll("D6")
        if roll >= weapon.critical_wound_value:
            if weapon.devastating_wounds:
                result.add_devastating_wounds(1)
            else:
                result.add_wounds(1)
        elif roll >= required_roll_to_wound:
            result.add_wounds(1)

    return result


def saving_throw(weapon: Weapon, wounds: WoundRollResult, save: int) -> int:
    modified_save = save + weapon.armorPen
    if modified_save > 6:
        return wounds.wounds + wounds.devastating_wounds

    num_failed_saves = wounds.devastating_wounds
    for _ in range(wounds.wounds):
        roll = dice_roll("d6")
        if roll < modified_save:
            num_failed_saves += 1

    return num_failed_saves


def damage_roll(weapon: Weapon, failed_saves: int) -> int:
    if isinstance(weapon.damage, str):
        total = 0
        for _ in range(failed_saves):
            roll = dice_roll(weapon.damage)
            if roll in weapon.damage_reroll_values:
                roll = dice_roll(weapon.damage)
            total += roll
        return total
    else:
        return weapon.damage * failed_saves


def run_simulation(weapons: List[Weapon]):
    if OUTPUT_TYPE == "plot":
        data = {}
        for weapon in weapons:
            data[weapon.name] = []
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
                    data[weapon.name].append(round(total_damage / NUM_TRIALS, 1))

        DamagePlot.render_plot(data)

    else:
        col_labels = [weapon.name for weapon in weapons]
        row_labels = []
        data = []
        for toughness in TOUGHNESS_CHARACTERISTICS:
            for save in reversed(SAVE_CHARACTERISTICS):
                row_labels.append("T%s,%s+" % (toughness, save))
                row = []
                for weapon in weapons:
                    total_damage = 0
                    for _ in range(NUM_TRIALS):
                        attacks = attack_roll(weapon)
                        hits = hit_roll(weapon, attacks)
                        wounds = wound_roll(weapon, hits, toughness)
                        failed_saves = saving_throw(weapon, wounds, save)
                        damage = damage_roll(weapon, failed_saves)
                        total_damage += damage
                    mean_damage = round(total_damage / NUM_TRIALS, 1)
                    if SHOW_MODELS_SLAIN:
                        # TODO: Not so sure this is an accurate calculation of average slain models.
                        row.append(
                            "%s (%s)"
                            % (
                                mean_damage,
                                int(
                                    min(
                                        DEFENDER_UNIT_SIZE,
                                        mean_damage // DEFENDER_WOUND_PER_MODEL,
                                    )
                                ),
                            )
                        )

                    else:
                        row.append(str(mean_damage))
                data.append(row)

        DamageTable.render_table(data, col_labels, row_labels)
