import os
import mysql.connector
import requests

import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="poke_db"
)

# Create a cursor object to interact with the database
pokemon_db = mydb.cursor()

# Execute a SQL query
mycursor.execute("SELECT * FROM yourtable")

# Fetch the results
results = mycursor.fetchall()

# Print the results



def get_pokemon_from_api_to_db():
    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
    if response.status_code == 200:
        data = response.json()
        pokemons = data.get('results', [])

        # Create a cursor object to execute SQL queries
        my_cursor = Pokemon_db.cursor()

        for pokemon in pokemons:
            pokemon_data = requests.get(pokemon['url']).json()

            # Extract relevant data from the API response
            pokemon_id = pokemon_data['id']
            pokemon_name = pokemon_data['name']
            pokemon_type1 = pokemon_data['types'][0]['type']['name']
            pokemon_type2 = pokemon_data['types'][1]['type']['name'] if len(pokemon_data['types']) > 1 else None
            pokemon_abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
            pokemon_ability_ids = []

            # Insert the abilities of the Pokemon into the Talent table and Capacite table
            for ability in pokemon_abilities:
                ability_query = "INSERT IGNORE INTO Talent (nom, description) VALUES (%s, %s)"
                my_cursor.execute(ability_query, (ability, "TODO: Add description"))
                Pokemon_db.commit()

                my_cursor.execute("SELECT id FROM Talent WHERE nom = %s", (ability,))
                talent_id = my_cursor.fetchone()[0]

                # Create a Capacite entry for this ability
                capacite_query = "INSERT IGNORE INTO Capacite (nom, type, status, puissance, description) VALUES (%s, %s, %s, %s, %s)"
                my_cursor.execute(capacite_query,
                                  (ability, "TODO: Add type", "TODO: Add status", "TODO: Add power",
                                   "TODO: Add description"))
                Pokemon_db.commit()

                my_cursor.execute("SELECT id FROM Capacite WHERE nom = %s", (ability,))
                capacite_id = my_cursor.fetchone()[0]

                # Add the relation between the Pokemon and the ability to the Capacite_List table
                capacite_list_query = "INSERT INTO Capacite_List (capacite_id, pokemon_id) VALUES (%s, %s)"
                my_cursor.execute(capacite_list_query, (capacite_id, pokemon_id))
                Pokemon_db.commit()

                # Add the ability ID to the list of abilities for the Pokemon
                pokemon_ability_ids.append(talent_id)

            # Insert the Pokemon into the Pokemon table
            pokemon_query = "INSERT INTO Pokemon (id, nom, type1, type2, capacite_list, talent_id) VALUES (%s, %s, %s, %s, %s, %s)"
            my_cursor.execute(pokemon_query, (
                pokemon_id, pokemon_name, pokemon_type1, pokemon_type2, str(pokemon_ability_ids),
                pokemon_ability_ids[0]))
            Pokemon_db.commit()

    else:
        print("Failed to fetch Pokemon data from the API")


def db_create():

    # Create the Pokemon table
    my_cursor.execute(
        "CREATE TABLE IF NOT EXISTS Pokemon (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), type1 VARCHAR(255), type2 VARCHAR(255), capacite_list TEXT, talent_id INT)")

    # Create the Capacite_List table
    my_cursor.execute(
        "CREATE TABLE IF NOT EXISTS Capacite_List (capacite_id INT, pokemon_id INT, FOREIGN KEY (capacite_id) REFERENCES Capacite(id), FOREIGN KEY (pokemon_id) REFERENCES Pokemon(id))")

    # Create the Capacite table
    my_cursor.execute(
        "CREATE TABLE IF NOT EXISTS Capacite (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), type VARCHAR(255), status VARCHAR(255), puissance INT, description TEXT)")

    # Create the Talent table
    my_cursor.execute(
        "CREATE TABLE IF NOT EXISTS Talent (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), description TEXT)")

    # Commit changes to the database
    Pokemon_db.commit()

    # Close the cursor and database connection
    my_cursor.close()
    get_pokemon_from_api_to_db()
    tata = pokemon_db
    Pokemon_db.close()
    return tata




db_exists = False

if __name__ == "__main__":
    arr = os.listdir('.')
    for i in arr:
        if i == 'Poke_db':
            db_exists = True
            break

    if not db_exists:
        results = db_create()
        for result in results:
            print(result)
        print('Database created successfully')
    else:
        print('Database already exists')
