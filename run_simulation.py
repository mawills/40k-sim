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
from weapon_profile import Weapon
from charts.damage_plot import DamagePlot
from charts.damage_table import DamageTable
from rolls.dice_roll import dice_roll
from rolls.attack_roll import attack_roll
from rolls.hit_roll import hit_roll
from rolls.wound_roll import wound_roll
from rolls.saving_throw import saving_throw
from rolls.damage_roll import damage_roll


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
