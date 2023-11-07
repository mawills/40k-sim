from unittest.mock import patch
from weapon_profile import Weapon
from rolls.wound_roll import WoundRollResult
from rolls.saving_throw import saving_throw


@patch("rolls.dice_roll.random.randint")
def test_saving_throw(mock_randint):
    inputs = [
        {
            "weapon": Weapon(
                name="test_failed_saves",
                num_attacks=2,
                skill=3,
                strength=4,
                armorPen=0,
                damage=1,
                count=10,
                lethal_hits=False,
                sustained_hits=0,
                devastating_wounds=False,
                torrent=False,
                blast=False,
                twin_linked=False,
                hit_reroll_values=[],
                wound_reroll_values=[],
                damage_reroll_values=[],
                critical_hit_value=6,
                critical_wound_value=4,
            ),
            "wounds": WoundRollResult(8, 0),
            "save": 5,
            "roll_value": 4,
            "expected": 8,
        },
        {
            "weapon": Weapon(
                name="test_failed_saves_dev_wounds",
                num_attacks=2,
                skill=3,
                strength=4,
                armorPen=0,
                damage=1,
                count=10,
                lethal_hits=False,
                sustained_hits=0,
                devastating_wounds=False,
                torrent=False,
                blast=False,
                twin_linked=False,
                hit_reroll_values=[],
                wound_reroll_values=[],
                damage_reroll_values=[],
                critical_hit_value=6,
                critical_wound_value=4,
            ),
            "wounds": WoundRollResult(8, 4),
            "save": 5,
            "roll_value": 4,
            "expected": 12,
        },
        {
            "weapon": Weapon(
                name="test_failed_saves_armor_pen",
                num_attacks=2,
                skill=3,
                strength=4,
                armorPen=1,
                damage=1,
                count=10,
                lethal_hits=False,
                sustained_hits=0,
                devastating_wounds=False,
                torrent=False,
                blast=False,
                twin_linked=False,
                hit_reroll_values=[],
                wound_reroll_values=[],
                damage_reroll_values=[],
                critical_hit_value=6,
                critical_wound_value=4,
            ),
            "wounds": WoundRollResult(3, 0),
            "save": 3,
            "roll_value": 3,
            "expected": 3,
        },
        {
            "weapon": Weapon(
                name="test_successful_saves",
                num_attacks=2,
                skill=3,
                strength=4,
                armorPen=1,
                damage=1,
                count=10,
                lethal_hits=False,
                sustained_hits=0,
                devastating_wounds=False,
                torrent=False,
                blast=False,
                twin_linked=False,
                hit_reroll_values=[],
                wound_reroll_values=[],
                damage_reroll_values=[],
                critical_hit_value=6,
                critical_wound_value=4,
            ),
            "wounds": WoundRollResult(2, 0),
            "save": 2,
            "roll_value": 3,
            "expected": 0,
        },
        {
            "weapon": Weapon(
                name="test_successful_saves_dev_wounds",
                num_attacks=2,
                skill=3,
                strength=4,
                armorPen=1,
                damage=1,
                count=10,
                lethal_hits=False,
                sustained_hits=0,
                devastating_wounds=False,
                torrent=False,
                blast=False,
                twin_linked=False,
                hit_reroll_values=[],
                wound_reroll_values=[],
                damage_reroll_values=[],
                critical_hit_value=6,
                critical_wound_value=4,
            ),
            "wounds": WoundRollResult(3, 5),
            "save": 2,
            "roll_value": 3,
            "expected": 5,
        },
    ]

    results = []
    for input in inputs:
        mock_randint.return_value = input["roll_value"]
        results.append(
            [
                saving_throw(input["weapon"], input["wounds"], input["save"]),
                input["expected"],
            ]
        )

    for [result, expected] in results:
        assert result == expected
