from unittest.mock import patch
import run_simulation
from weapon_profile import Weapon


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
