from unittest.mock import patch
import run_simulation


@patch("run_simulation.random.randint")
def test_dice_roll(mock_randint):
    mock_randint.return_value = 1

    inputs = ["d6", "D6", "2d3", "d3+1", "12d6+10"]

    result = []
    for input in inputs:
        result.append(run_simulation.dice_roll(input))

    assert result == [1, 1, 2, 2, 22]
