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
            "test_weapon_num_attacks_int",
            2,
            3,
            4,
            0,
            1,
            10,
            False,
            0,
            False,
            False,
            False,
            False,
            [],
            [],
            [],
            6,
            6,
        ),
        Weapon(
            "test_weapon_num_attacks_variable",
            "D6",
            4,
            4,
            0,
            1,
            10,
            False,
            0,
            False,
            True,
            False,
            False,
            [],
            [],
            [],
            6,
            6,
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
        [
            Weapon(
                "test_weapon_skill_3",
                2,
                3,
                4,
                0,
                1,
                10,
                False,
                0,
                False,
                False,
                False,
                False,
                [],
                [],
                [],
                6,
                6,
            ),
            20,
            [20, 0],
        ],
        [
            Weapon(
                "test_weapon_skill_4",
                2,
                4,
                4,
                0,
                1,
                10,
                False,
                0,
                False,
                False,
                False,
                False,
                [],
                [],
                [],
                6,
                6,
            ),
            20,
            [0, 0],
        ],
        [
            Weapon(
                "test_weapon_skill_4_torrent",
                2,
                4,
                4,
                0,
                1,
                10,
                False,
                0,
                False,
                True,
                False,
                False,
                [],
                [],
                [],
                6,
                6,
            ),
            15,
            [15, 0],
        ],
        [
            Weapon(
                "test_weapon_skill_lethal_hits_crit_3",
                2,
                4,
                4,
                0,
                1,
                10,
                True,
                0,
                False,
                False,
                False,
                False,
                [],
                [],
                [],
                3,
                6,
            ),
            15,
            [0, 15],
        ],
        [
            Weapon(
                "test_weapon_skill_lethal_hits_crit_with_torrent",
                2,
                4,
                4,
                0,
                1,
                10,
                True,
                0,
                False,
                True,
                False,
                False,
                [],
                [],
                [],
                3,
                6,
            ),
            12,
            [12, 0],
        ],
        [
            Weapon(
                "test_weapon_skill_sustained_hits_3_crit_2",
                2,
                4,
                4,
                0,
                1,
                1,
                False,
                3,
                False,
                False,
                False,
                False,
                [],
                [],
                [],
                2,
                6,
            ),
            2,
            [8, 0],
        ],
        [
            Weapon(
                "test_weapon_sustained_and_lethal",
                2,
                4,
                4,
                0,
                1,
                1,
                True,
                3,
                False,
                False,
                False,
                False,
                [],
                [],
                [],
                2,
                6,
            ),
            2,
            [6, 2],
        ],
    ]

    results = []
    for [weapon, num_attacks, expected] in inputs:
        results.append([run_simulation.hit_roll(weapon, num_attacks), expected])

    for [result, expected] in results:
        assert [result.hits, result.lethal_hits] == expected
