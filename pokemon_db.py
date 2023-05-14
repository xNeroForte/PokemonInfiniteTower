import json
import sqlite3

data_Pokemon = "Pokemon.json"
data_Capacite = "Capacite.json"
data_Talent = "Talent.json"
data_Capacite_list = "Capacite_list.json"

# creer un curseur pour executer des requêtes
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# creation des tables
cursor.execute('''CREATE TABLE IF NOT EXISTS Pokemon (
                  id INTEGER PRIMARY KEY,
                  nom TEXT,
                  type_1 TEXT,
                  type_2 TEXT,
                  capacite_list TEXT,
                  talent_id INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Capacite (
                  id INTEGER PRIMARY KEY,
                  nom TEXT,
                  type TEXT,
                  statut TEXT,
                  puissance INTEGER,
                  description TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Capacite_list (
                  capacite_id INTEGER,
                  pokemon_id INTEGER,
                  FOREIGN KEY (capacite_id) REFERENCES Capacite(id),
                  FOREIGN KEY (pokemon_id) REFERENCES Pokemon(id))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Talent (
                  talent_id INTEGER PRIMARY KEY,
                  nom TEXT,
                  description TEXT)''')


# Read the data from the JSON files
with open(data_Pokemon, 'r') as f:
    pokemon_data = json.load(f)

with open(data_Capacite, 'r') as f:
    capacite_data = json.load(f)

with open(data_Talent, 'r') as f:
    talent_data = json.load(f)

with open(data_Capacite_list, 'r') as f:
    capacite_list_data = json.load(f)

# Insert the Pokemon data into the Pokemon table
for pokemon_id, data in pokemon_data.items():
    cursor.execute("INSERT INTO Pokemon (id, nom, type_1, type_2, capacite_list, talent_id) VALUES (?, ?, ?, ?, ?, ?)",
                   (pokemon_id, data['nom'], data['type 1'], data['type 2'], json.dumps(data['capacité list']), data['talent_id']))

# Insert the move data into the Capacite table
for capacite_id, data in capacite_data.items():
    cursor.execute("INSERT INTO Capacite (id, nom, type, statut, puissance, description) VALUES (?, ?, ?, ?, ?, ?)",
                   (capacite_id, data['nom'], data.get('type'), data.get('statut'), data.get('puissance', None), data.get('description', None)))

# Insert the talent data into the Talent table
for talent_id, data in talent_data.items():
    cursor.execute("INSERT INTO Talent (talent_id, nom, description) VALUES (?, ?, ?)",
                   (talent_id, data['nom'], data['description']))

# Insert the move/pokemon mapping data into the Capacite_list table
for capacite_id, data in capacite_list_data.items():
    pokemon_names = ", ".join(data['pokemon_id'])
    cursor.execute("INSERT INTO Capacite_list (capacite_id, pokemon_id) VALUES (?, (SELECT id FROM Pokemon WHERE nom IN ({0})))".format(pokemon_names),
                   (capacite_id,))


# Commit the changes to the database
conn.commit()
