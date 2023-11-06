from unittest.mock import patch
import run_simulation
from weapon_profile import Weapon
from hit_roll_result import HitRollResult


@patch("run_simulation.random.randint")
def test_dice_roll(mock_randint):
    mock_randint.return_value = 1

    inputs = ["d6", "D6", "2d3", "d3+1", "12d6+10"]

    result = []
    for input in inputs:
        result.append(run_simulation.dice_roll(input))

    assert result == [1, 1, 2, 2, 22]


@patch("run_simulation.random.randint")
def test_attack_roll(mock_randint):
    mock_randint.return_value = 3

    # TODO: mock config.DEFENDER_UNIT_SIZE to test Blast
    inputs = [
        Weapon(
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
        Weapon(
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
    ]

    result = []
    for input in inputs:
        result.append(run_simulation.attack_roll(input))

    assert result == [20, 30]


@patch("run_simulation.random.randint")
def test_hit_roll(mock_randint):
    mock_randint.return_value = 3

    inputs = [
        {
            "weapon": Weapon(
                name="test_weapon_skill_3",
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
            "num_attacks": 20,
            "expected": [20, 0],
        },
        {
            "weapon": Weapon(
                name="test_weapon_skill_4",
                num_attacks=2,
                skill=4,
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
            "num_attacks": 20,
            "expected": [0, 0],
        },
        {
            "weapon": Weapon(
                name="test_weapon_skill_4_torrent",
                num_attacks=2,
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
            "num_attacks": 15,
            "expected": [15, 0],
        },
        {
            "weapon": Weapon(
                name="test_weapon_lethal_hits_crit_3",
                num_attacks=2,
                skill=4,
                strength=4,
                armorPen=0,
                damage=1,
                count=10,
                lethal_hits=True,
                sustained_hits=0,
                devastating_wounds=False,
                torrent=False,
                blast=False,
                twin_linked=False,
                hit_reroll_values=[],
                wound_reroll_values=[],
                damage_reroll_values=[],
                critical_hit_value=3,
                critical_wound_value=6,
            ),
            "num_attacks": 15,
            "expected": [0, 15],
        },
        {
            "weapon": Weapon(
                name="test_weapon_skill_lethal_hits_crit_with_torrent",
                num_attacks=2,
                skill=4,
                strength=4,
                armorPen=0,
                damage=1,
                count=10,
                lethal_hits=True,
                sustained_hits=0,
                devastating_wounds=False,
                torrent=True,
                blast=False,
                twin_linked=False,
                hit_reroll_values=[],
                wound_reroll_values=[],
                damage_reroll_values=[],
                critical_hit_value=3,
                critical_wound_value=6,
            ),
            "num_attacks": 12,
            "expected": [12, 0],
        },
        {
            "weapon": Weapon(
                name="test_weapon_sustained_hits_d3_crit_3",
                num_attacks=2,
                skill=3,
                strength=4,
                armorPen=0,
                damage=1,
                count=10,
                lethal_hits=False,
                sustained_hits="d3",
                devastating_wounds=False,
                torrent=False,
                blast=False,
                twin_linked=False,
                hit_reroll_values=[],
                wound_reroll_values=[],
                damage_reroll_values=[],
                critical_hit_value=3,
                critical_wound_value=6,
            ),
            "num_attacks": 2,
            "expected": [8, 0],
        },
        {
            "weapon": Weapon(
                name="test_weapon_sustained_and_lethal",
                num_attacks=2,
                skill=3,
                strength=4,
                armorPen=0,
                damage=1,
                count=10,
                lethal_hits=True,
                sustained_hits=3,
                devastating_wounds=False,
                torrent=False,
                blast=False,
                twin_linked=False,
                hit_reroll_values=[],
                wound_reroll_values=[],
                damage_reroll_values=[],
                critical_hit_value=3,
                critical_wound_value=6,
            ),
            "num_attacks": 2,
            "expected": [6, 2],
        },
    ]

    results = []
    for input in inputs:
        results.append(
            [
                run_simulation.hit_roll(input["weapon"], input["num_attacks"]),
                input["expected"],
            ]
        )

    for [result, expected] in results:
        assert [result.hits, result.lethal_hits] == expected


@patch("run_simulation.random.randint")
def test_wound_roll(mock_randint):
    mock_randint.return_value = 4

    inputs = [
        {
            "weapon": Weapon(
                name="test_weapon_4s",
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
            "hits": HitRollResult(8, 0),
            "toughness": 4,
            "expected": [8, 0],
        },
        {
            "weapon": Weapon(
                name="test_weapon_lethal_hits",
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
            "hits": HitRollResult(8, 2),
            "toughness": 5,
            "expected": [2, 0],
        },
        {
            "weapon": Weapon(
                name="test_weapon_dev_wounds_crit_4s",
                num_attacks=2,
                skill=3,
                strength=4,
                armorPen=0,
                damage=1,
                count=10,
                lethal_hits=False,
                sustained_hits=0,
                devastating_wounds=True,
                torrent=False,
                blast=False,
                twin_linked=False,
                hit_reroll_values=[],
                wound_reroll_values=[],
                damage_reroll_values=[],
                critical_hit_value=6,
                critical_wound_value=4,
            ),
            "hits": HitRollResult(8, 2),
            "toughness": 5,
            "expected": [2, 8],
        },
    ]

    results = []
    for input in inputs:
        results.append(
            [
                run_simulation.wound_roll(
                    input["weapon"], input["hits"], input["toughness"]
                ),
                input["expected"],
            ]
        )

    for [result, expected] in results:
        assert [result.wounds, result.devastating_wounds] == expected
