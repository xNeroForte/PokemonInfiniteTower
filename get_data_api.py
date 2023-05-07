import sqlite3
import requests

# establish connection to the database
conn = sqlite3.connect('pokemon.db')
cursor = conn.cursor()

# create the Pokemon table
cursor.execute('''CREATE TABLE IF NOT EXISTS Pokemon
                (id INTEGER PRIMARY KEY UNIQUE,
                 nom TEXT,
                 type1 TEXT,
                 type2 TEXT,
                 talent_id INTEGER,
                 FOREIGN KEY(talent_id) REFERENCES Talent(id))''')

# create the Capacité table
cursor.execute('''CREATE TABLE IF NOT EXISTS Capacité
                (id INTEGER PRIMARY KEY,
                 nom TEXT,
                 type TEXT,
                 status TEXT,
                 puissance INTEGER,
                 description TEXT)''')

# create the Capacité-list table
cursor.execute('''CREATE TABLE IF NOT EXISTS Capacité_list
                (pokemon_id INTEGER,
                 capacité_id INTEGER,
                 FOREIGN KEY(pokemon_id) REFERENCES Pokemon(id),
                 FOREIGN KEY(capacité_id) REFERENCES Capacité(id),
                 PRIMARY KEY(pokemon_id, capacité_id))''')

# create the Talent table
cursor.execute('''CREATE TABLE IF NOT EXISTS Talent
                (id INTEGER PRIMARY KEY,
                 nom TEXT,
                 description TEXT)''')

# fetch the data from the API
url = "https://pokeapi.co/api/v2/pokemon?limit=151"
response = requests.get(url)

if response.ok:
    pokemon_data = response.json()['results']

    # loop through the pokemon_data and insert into the Pokemon table
    for i, pokemon in enumerate(pokemon_data):
        url = pokemon['url']
        response = requests.get(url)
        if response.ok:
            pokemon_details = response.json()
            name = pokemon_details['name'].capitalize()
            type1 = pokemon_details['types'][0]['type']['name'].capitalize()
            try:
                type2 = pokemon_details['types'][1]['type']['name'].capitalize()
            except IndexError:
                type2 = None
            talent1_url = pokemon_details['abilities'][0]['ability']['url']
            talent1_id = int(talent1_url.split('/')[-2])
            talent1_name = requests.get(talent1_url).json()['name'].capitalize()
            talent1_effect = requests.get(talent1_url).json()['effect_entries'][0]['effect']
            talent2_name = None
            talent2_effect = None
            if len(pokemon_details['abilities']) > 1:
                talent2_url = pokemon_details['abilities'][1]['ability']['url']
                talent2_id = int(talent2_url.split('/')[-2])
                talent2_name = requests.get(talent2_url).json()['name'].capitalize()
                talent2_effect = requests.get(talent2_url).json()['effect_entries'][0]['effect']

            # insert into the Pokemon table
            cursor.execute("INSERT OR IGNORE INTO Pokemon (id, nom, type1, type2, talent_id) VALUES (?, ?, ?, ?, ?)",
                           (i + 1, name, type1, type2, talent1_id))

            # insert into the Talent table
            cursor.execute("INSERT OR IGNORE INTO Talent (id, nom, description) VALUES (?, ?, ?)",
                           (talent1_id, talent1_name, talent1_effect))
            if talent2_name is not None:
                cursor.execute("INSERT OR IGNORE INTO Talent (id, nom, description) VALUES (?, ?, ?)",
                               (talent2_id, talent2_name, talent2_effect))

            ## loop through the pokemon's moves and insert into the Capacité and Capacité_list tables
            for move in pokemon_details['moves']:
                url = move['move']['url']
                response = requests.get(url)
                if response.ok:
                    move_details = response.json()
                    name = move_details['name'].capitalize()
                    type = move_details['type']['name'].capitalize()
                    status = move_details['damage_class']['name'].capitalize()
                    power = move_details['power']
                    description = move_details['effect_entries'][0]['short_effect']

                    # insert into the Capacité table
                    cursor.execute(
                        "INSERT OR IGNORE INTO Capacité (id, nom, type, status, puissance, description) VALUES (?, ?, ?, ?, ?, ?)",
                        (move_details['id'], name, type, status, power, description))

                    # fetch the capacité id and insert into the Capacité_list table
                    capacite_id = move_details['id']
                    cursor.execute("INSERT INTO Capacité_list (pokemon_id, capacité_id) VALUES (?, ?)",
                                   (i + 1, capacite_id))

                    print(
                        f"Inserted move '{name}' for pokemon '{pokemon['name']}' into Capacité and Capacité_list tables")

            conn.commit()
