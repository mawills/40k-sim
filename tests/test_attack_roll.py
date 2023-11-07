from unittest.mock import patch
from weapon_profile import Weapon
from rolls.attack_roll import attack_roll


@patch("run_simulation.random.randint")
def test_attack_roll(mock_randint):
    # TODO: mock config.DEFENDER_UNIT_SIZE to test Blast
    inputs = [
        {
            "weapon": Weapon(
                name="test_weapon_num_attacks_int",
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
                critical_wound_value=6,
            ),
            "roll_result": 3,
            "expected": 20,
        },
        {
            "weapon": Weapon(
                name="test_weapon_num_attacks_variable",
                num_attacks="D6",
                skill=4,
                strength=4,
                armorPen=0,
                damage=1,
                count=10,
                lethal_hits=False,
                sustained_hits=0,
                devastating_wounds=False,
                torrent=True,
                blast=False,
                twin_linked=False,
                hit_reroll_values=[],
                wound_reroll_values=[],
                damage_reroll_values=[],
                critical_hit_value=6,
                critical_wound_value=6,
            ),
            "roll_result": 1,
            "expected": 10,
        },
    ]

    results = []
    for input in inputs:
        mock_randint.return_value = input["roll_result"]
        results.append([attack_roll(input["weapon"]), input["expected"]])

    for [result, expected] in results:
        assert result == expected
