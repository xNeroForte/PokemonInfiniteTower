import requests
import json

# Define the base URL for the PokeAPI
url = "https://pokeapi.co/api/v2/"

# Define the file paths
data_Pokemon = 'Pokemon.json'
data_Capacite = 'Capacite.json'
data_Talent = 'Talent.json'
data_Capacite_list = 'Capacite_list.json'

# Check if the files exist, and create them if they don't
with open(data_Pokemon, 'w') as f:
    json.dump(data_Pokemon, f, allow_nan=True)

with open(data_Capacite, 'w') as f:
    json.dump(data_Capacite, f, allow_nan=True)

with open(data_Talent, 'w') as f:
    json.dump(data_Talent, f, allow_nan=True)

with open(data_Capacite_list, 'w') as f:
    json.dump(data_Capacite_list, f, allow_nan=True)

# Define a function to retrieve and parse JSON data from a URL
def get_json_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None



# Retrieve and parse data for each move
capacite_data = {}
for i in range(1, 728):
    move_url = url + f"move/{i}"
    move_json = get_json_data(move_url)
    if move_json:
        capacite_data[move_json['id']] = {
            'nom': move_json['name'],
            'pokemon-id': []
        }
        if 'version_group_details' in move_json:
            capacite_data[move_json['id']]['pokemon-id'] = [version['pokemon']['name'] for version in move_json['version_group_details']]
    print(move_json,'\n\n')

# Write the move data to a JSON file
with open(data_Capacite, 'w') as f:
    json.dump(capacite_data, f)

# Retrieve and parse data for each talent
talent_data = {}
for i in range(1, 233):
    ability_url = url + f"ability/{i}"
    ability_json = get_json_data(ability_url)
    if ability_json:
        talent_data[ability_json['id']] = {
            'nom': ability_json['name'],
            'description': ability_json['effect_entries'][0]['effect']
        }

# Write the talent data to a JSON file
with open(data_Talent, 'w') as f:
    json.dump(talent_data, f)

# Retrieve and parse data for each capacite_list
capacite_list_data = {}
for i in range(1, 728):
    move_url = url + f"move/{i}"
    move_json = get_json_data(move_url)
    if move_json:
        capacite_list_data[move_json['id']] = {
            'capacite_id': move_json['id'],
            'pokemon_id': []
        }
        if 'version_group_details' in move_json:
            capacite_list_data[move_json['id']]['pokemon_id'] = [version['pokemon']['name'] for version in move_json['version_group_details']]
        print(move_json,'\n\n')

# Write the capacite_list data to a JSON file
with open(data_Capacite_list, 'w') as f:
    json.dump(capacite_list_data, f)