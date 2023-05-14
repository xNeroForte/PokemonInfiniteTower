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


# Retrieve and parse data for each Pokemon
pokemon_data = {}
for i in range(1, 151): # 151
    #print(i, " of 150    0/4")
    pokemon_url = url + f"pokemon/{i}"
    pokemon_json = get_json_data(pokemon_url)
    if pokemon_json:
        pokemon_data[pokemon_json['id']] = {
            'nom': pokemon_json['name'],
            'type 1': pokemon_json['types'][0]['type']['name'],
            'type 2': pokemon_json['types'][1]['type']['name'] if len(pokemon_json['types']) > 1 else None,
            'capacité list': [move['move']['name'] for move in pokemon_json['moves']],
            'talent_id': pokemon_json['abilities'][0]['ability']['name']
        }
    print("\n\n Pokemon data: ")
    print(pokemon_json)    # Debug

# Write the Pokemon data to a JSON file
with open(data_Pokemon, 'w') as f:
    json.dump(pokemon_data, f)

# Retrieve and parse data for each move
capacite_data = {}
for i in range(1, 728): # 728
    #print(i, " of 727    1/4")
    move_url = url + f"move/{i}"
    move_json = get_json_data(move_url)
    if move_json:
        capacite_data[move_json['id']] = {
            'nom': move_json['name'],
            'pokemon-id': []
        }
        if 'version_group_details' in move_json:
            capacite_data[move_json['id']]['pokemon-id'] = [version['pokemon']['name'] for version in
                                                            move_json['version_group_details']]
    print("\n\n Capacite data: ")
    print(move_json)

# Write the move data to a JSON file
with open(data_Capacite, 'w') as f:
    json.dump(capacite_data, f)

# Retrieve and parse data for each ability
talent_data = {}
for i in range(1, 233): # 233
    ability_url = url + f"ability/{i}"
    ability_json = get_json_data(ability_url)
    if ability_json:
        # Initialize the description_en variable to an empty string
        description_en = ""
        # Search for the effect entry in English
        for effect_entry in ability_json['effect_entries']:
            if effect_entry['language']['name'] == 'en':
                description_en = effect_entry['effect']
                break
        talent_data[ability_json['id']] = {
            'name': ability_json['name'],
            'description': description_en
        }
print("\n\n Talent data: ")
print(talent_data) # Debug


# Write the talent data to a JSON file
with open(data_Talent, 'w') as f:
    json.dump(talent_data, f)

# Retrieve and parse data for each capacite_list
capacite_list_data = {}
for i in range(1, 728): # 728
    #print(i, " of 727   3/4")
    move_url = url + f"move/{i}"
    move_json = get_json_data(move_url)
    if move_json:
        capacite_list_data[move_json['id']] = {
            'capacite_id': move_json['id'],
            'pokemon_id': []
        }
        if 'version_group_details' in move_json:
            capacite_list_data[move_json['id']]['pokemon_id'] = [version['pokemon']['name'] for version in
                                                                 move_json['version_group_details']]
    print("\n\n Capacite_list data: ")
    print(move_json)    # Debug

# Write the capacite_list data to a JSON file
with open(data_Capacite_list, 'w') as f:
    json.dump(capacite_list_data, f)

print("4/4 Done")
