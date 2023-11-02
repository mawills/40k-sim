import json
from json_parser import JsonParser
from run_simulation import run_simulation


# TODO:
# - validate user input
# - add weapon abilities:
#   - sustained hits
#   - blast
#   - improve critical hit
#   - improve critical wound
#   - torrent

with open("weapons.json", "r") as json_file:
    data = json.load(json_file)

parser = JsonParser()
weapons = parser.parse_input(data)
run_simulation(weapons)
