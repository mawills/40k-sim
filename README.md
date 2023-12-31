# Warhammer 40k 10th Edition Damage Simulator

A damage simulator for the Warhammer 40k tabletop miniatures game, which simulates the dice rolls during an attack sequence to compare, at a glance, different weapon options and how they perform against an array of defensive profiles.

To run, create copies of `example.config.py` and `example.weapons.json` and rename them to `config.py` and `weapons.json`. Then, navigate to the root directory and run `python main.py`. This will run the simulation using the weapons found in `weapons.json` and the config options found in `config.py`.

To run tests, run `pytest` in the root directory.

![Example Graph](https://drive.google.com/uc?id=1BQGkIKfHA0gwiwLpOpr7ghRAE3ZNujKd)

## Weapon Properties

_\* required fields._

### (str) `name`\*:

A name for the weapon. It will appear on the legend of the generated chart.

### (int | str) `num_attacks`\*:

The attacks (A) characteristic of the weapon i.e. the number of attack rolls it will make. Accepts integer values, or a dice string e.g. `"2D6"` or `"12d6+5"`

### (int) `skill`\*:

The Ballistic Skill (BS) or Weapon Skill (WS) characteristic of the weapon. A hit roll of this value or higher is required for a successful hit.

### (int) `strength`\*:

The Strength (S) characteristic of the weapon. It will be compared against the Toughness (T) characteristic of the defender to determine the wound roll value required for a successful wound.

### (int) `armorPen`:

**Default: 0**. The Armor Penetration (AP) characteristic of the weapon, represented as a positive integer. Each point of armor penetration will worsen the saving throw of the defender by 1.

### (int | str) `damage`\*:

The damage (D) characteristic of the weapon. This is how much damage the weapon will inflict when the defender fails a saving throw. Accepts integer values, or a dice string e.g. `"2D6"` or `"12d6+5"`

### (int) `count`\*:

The number of copies of this weapon equipped by the attacking unit.

### (int) `critical_hit_value`:

**Default: 6**. An unmodified hit roll of 6 or higher, by default. A critical hit always counts as a successful hit.

### (int) `critical_wound_value`:

**Default: 6**. An unmodified wound roll of 6 or higher, by default. A critical wound always counts as a successful wound.

### (bool) `lethal_hits`:

**Default: False**. When a weapon with Lethal Hits scores a critical hit, that attack automatically wounds. Do not make a wound roll.

### (int) `sustained_hits`:

**Default: 0**. A weapon with Sustained Hits N scores N additional hits on a critical hit.

### (bool) `devastating_wounds`:

**Default: False**. When a weapon with Devastating Wounds scores a critical wound, no saving throw can be made against that attack.

### (bool) `torrent`:

**Default: False**. A weapon with torrent cannot miss. It skips making a hit roll and goes straight to making a wound roll.

### (bool) `blast`:

**Default: False**. A weapon with Blast adds 1 to its number of attacks for every 5 models in the defending unit.

### (bool) `twin_linked`:

**Default: False**. A weapon that is Twin-Linked will re-roll any failed wound rolls.

### (int[]) `hit_reroll_values`:

**Default: []**. Any hit rolls of a value found in this array will be re-rolled e.g. to re-roll any result less than a 6, use `[1, 2, 3, 4, 5]`.

### (int[]) `wound_reroll_values`:

**Default: []**. Any wound rolls of a value found in this array will be re-rolled e.g. to re-roll any result less than a 6, use `[1, 2, 3, 4, 5]`.

### (int[]) `damage_reroll_values`:

**Default: []**. Any damage rolls of a value found in this array will be re-rolled e.g. to re-roll any result less than a 4, use `[1, 2, 3]`.

## Config

### (int) `NUM_TRIALS`:

**Example: 1000**. The number of times the attack sequence will be performed against each defender profile.

### (int[]) `TOUGHNESS_CHARACTERISTICS`:

**Example: [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]**. The attack sequence will be performed and plotted against each combination of toughness and save values.

### (int[]) `SAVE_CHARACTERISTICS`:

**Example: [2, 3, 4, 5, 6]**. The attack sequence will be performed and plotted against each combination of toughness and save values.

### (str) `OUTPUT_TYPE`:

**Default: "table"**. Determines how the data will be visually represented. Options are "table" or "plot".

### (int) `DEFENDER_UNIT_SIZE`:

**Example: 10**. The number of models in the defending unit. This is relevant for certain weapons, like those with Blast, which gain additional attacks against units with a large number of models.

### (int) `DEFENDER_WOUND_PER_MODEL`:

**Example: 2**. The number of wounds on each unit in the defending model. When combined with the `SHOW_MODELS_SLAIN` config option, it's possible to calculate the average number of slain models as well as the average damage.

### (str[]) `BENCHMARKS`:

**Example: ["T4,3+", "T5,2+", "T6,3+", "T10,2+"]**. This is useful for highlighting common or important defensive profiles to make them easier to see. If `OUTPUT_TYPE` is `"plot"`, any x-axis labels included in this array will be plotted with a vertical line to make them stand out. If `OUTPUT_TYPE` is `"table"`, this will highlight any rows with a label in this array.

### (bool) `SHOW_SLAIN_MODELS`:

**Example: "True"**. If the `OUTPUT_TYPE` is `"table"`, this option will display the average number of slain models in the defending unit in parenthesis next to the average damage. Requires that the `DEFENDER_WOUND_PER_MODEL` config option be set.

### (int) `WINDOW_HEIGHT_IN`:

**Example: 11**. The default height of the window generated by Matplotlib. The library accepts a number in inches.

### (int) `WINDOW_WIDTH_IN`:

**Example: 8**. The default width of the window generated by Matplotlib. The library accepts a number in inches.
