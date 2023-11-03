import json
from json_parser import JsonParser
from run_simulation import run_simulation
from run_simulation import dice_roll


# TODO:
# - validate user input
# - tests

with open("weapons.json", "r") as json_file:
    data = json.load(json_file)

parser = JsonParser()
weapons = parser.parse_input(data)
run_simulation(weapons)
