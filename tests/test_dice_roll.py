from unittest.mock import patch
from rolls.dice_roll import dice_roll


@patch("rolls.dice_roll.random.randint")
def test_dice_roll(mock_randint):
    mock_randint.return_value = 1

    inputs = ["d6", "D6", "2d3", "d3+1", "12d6+10"]

    result = []
    for input in inputs:
        result.append(dice_roll(input))

    assert result == [1, 1, 2, 2, 22]
