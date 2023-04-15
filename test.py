import random

# Définition des constantes
pokemon = "P"
NUM_pokemon = 0 # nombre de pokemon à créer
CHEST = "C"
NUM_CHESTS = 0 # nombre de coffres à créer
SIZE = 80  # Taille du labyrinthe (en nombre de lignes et de colonnes)
WALL = "#"  # Caractère représentant un mur
FLOOR = "."  # Caractère représentant un sol
START = "S"  # Caractère représentant l'entrée
END = "E"  # Caractère représentant la sortie
ROOM_MIN_SIZE = 3  # Taille minimale d'une salle (en nombre de lignes et de colonnes)
ROOM_MAX_SIZE = 7  # Taille maximale d'une salle (en nombre de lignes et de colonnes)
CORRIDOR_MIN_WIDTH = 1  # Largeur minimale d'un couloir (en nombre de colonnes)
CORRIDOR_MAX_WIDTH = 3  # Largeur maximale d'un couloir (en nombre de colonnes)
num_map = 1 # numéro de la map
file_name = f"map_{num_map}.txt" # nom du fichier
# Initialisation du labyrinthe avec des murs
maze = [[WALL for _ in range(SIZE)] for _ in range(SIZE)]

def ajouter_bordures(tableau):
    # Ajouter deux lignes de '#' au début et à la fin du tableau
    tableau.insert(0, ['#'] * (len(tableau[0]) + 4))
    tableau.append(['#'] * (len(tableau[0]) + 4))
    
    # Ajouter "##" au début et à la fin de chaque ligne du tableau
    for i in range(len(tableau)):
        tableau[i] = ['##'] + tableau[i] + ['##']
    
    return tableau

# Fonction pour créer une salle dans le labyrinthe
def create_room(x, y, w, h):
    for i in range(x, x+w):
        for j in range(y, y+h):
            if i == x or i == x+w-1 or j == y or j == y+h-1:
                maze[j][i] = WALL
            else:
                maze[j][i] = FLOOR

# Fonction pour créer un couloir horizontal dans le labyrinthe
def create_horizontal_corridor(x1, x2, y):
    for i in range(min(x1, x2), max(x1, x2)+1):
        for j in range(max(0, y-CORRIDOR_MAX_WIDTH), min(SIZE, y+CORRIDOR_MAX_WIDTH+1)):
            if maze[j][i] == WALL:
                maze[j][i] = FLOOR

# Fonction pour créer un couloir vertical dans le labyrinthe
def create_vertical_corridor(y1, y2, x):
    for i in range(max(0, x-CORRIDOR_MAX_WIDTH), min(SIZE, x+CORRIDOR_MAX_WIDTH+1)):
        for j in range(min(y1, y2), max(y1, y2)+1):
            if maze[j][i] == WALL:
                maze[j][i] = FLOOR

def create_map():
    NUM_pokemon = random.randint(10, 15) # nombre de pokemon à créer
    NUM_CHESTS = random.randint(1, 5) # nombre de coffres à créer
    # Création des salles et des couloirs
    rooms = []
    for _ in range(10):  # Nombre de salles à créer
        w, h = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE), random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        x, y = random.randint(1, SIZE-w-1), random.randint(1, SIZE-h-1)
        create_room(x, y, w, h)
        rooms.append((x, y, w, h))
        
    # Création des couloirs
    for i in range(len(rooms)-1):
        x1, y1 = rooms[i][0]+rooms[i][2]//2, rooms[i][1]+rooms[i][3]//2
        x2, y2 = rooms[i+1][0]+rooms[i+1][2]//2, rooms[i+1][1]+rooms[i+1][3]//2
        if random.random() < 0.5:
            create_horizontal_corridor(x1, x2, y1)
            create_vertical_corridor(y1, y2, x2)
        else:
            create_vertical_corridor(y1, y2, x1)
            create_horizontal_corridor(x1, x2, y2)

    # Recherche de l'entrée et de la sortie
    start, end = None, None
    while start is None or end is None or start == end:
        start = (random.randint(0, SIZE-1), random.randint(0, SIZE-1))
        end = (random.randint(0, SIZE-1), random.randint(0, SIZE-1))
        if maze[start[1]][start[0]] == WALL or maze[end[1]][end[0]] == WALL:
            start, end = None, None

    # Création des coffres
    for _ in range(NUM_CHESTS):
        while True:
            x, y = random.randint(0, SIZE-1), random.randint(0, SIZE-1)
            if maze[y][x] == FLOOR:
                maze[y][x] = CHEST
                break

    # Création des pokemon
    for _ in range(NUM_pokemon):
        while True:
            x, y = random.randint(0, SIZE-1), random.randint(0, SIZE-1)
            if maze[y][x] == FLOOR:
                maze[y][x] = pokemon
                break


    # Affichage du labyrinthe
    ajouter_bordures(maze);
    for j in range(SIZE):
        for i in range(SIZE):
            if (i, j) == start:
                print(START, end="")
            elif (i, j) == end:
                print(END, end="")
            else:
                print(maze[j][i], end="")
        print()

    # Enregistrement du labyrinthe dans un fichier
    with open(file_name, "w") as f:
        f.write("\n".join(["".join(row) for row in maze]))

create_map();



"""
import random

# Définition des constantes
pokemon = "P"
NUM_pokemon = random.randint(10, 15) # nombre de pokemon à créer
CHEST = "C"
NUM_CHESTS = random.randint(1, 5) # nombre de coffres à créer
SIZE = 80  # Taille du labyrinthe (en nombre de lignes et de colonnes)
WALL = "#"  # Caractère représentant un mur
FLOOR = "."  # Caractère représentant un sol
START = "S"  # Caractère représentant l'entrée
END = "E"  # Caractère représentant la sortie
ROOM_MIN_SIZE = 3  # Taille minimale d'une salle (en nombre de lignes et de colonnes)
ROOM_MAX_SIZE = 7  # Taille maximale d'une salle (en nombre de lignes et de colonnes)
CORRIDOR_MIN_WIDTH = 1  # Largeur minimale d'un couloir (en nombre de colonnes)
CORRIDOR_MAX_WIDTH = 3  # Largeur maximale d'un couloir (en nombre de colonnes)
num_map = 1 # numéro de la map
file_name = f"map_{num_map}.txt" # nom du fichier

def ajouter_bordures(tableau):
    # Ajouter deux lignes de '#' au début et à la fin du tableau
    tableau.insert(0, ['#'] * (len(tableau[0]) + 4))
    tableau.append(['#'] * (len(tableau[0]) + 4))
    
    # Ajouter "##" au début et à la fin de chaque ligne du tableau
    for i in range(len(tableau)):
        tableau[i] = ['##'] + tableau[i] + ['##']
    
    return tableau


# Initialisation du labyrinthe avec des murs
maze = [[WALL for _ in range(SIZE)] for _ in range(SIZE)]

# Fonction pour créer une salle dans le labyrinthe
def create_room(x, y, w, h):
    for i in range(x, x+w):
        for j in range(y, y+h):
            if i == x or i == x+w-1 or j == y or j == y+h-1:
                maze[j][i] = WALL
            else:
                maze[j][i] = FLOOR

# Fonction pour créer un couloir horizontal dans le labyrinthe
def create_horizontal_corridor(x1, x2, y):
    for i in range(min(x1, x2), max(x1, x2)+1):
        for j in range(max(0, y-CORRIDOR_MAX_WIDTH), min(SIZE, y+CORRIDOR_MAX_WIDTH+1)):
            if maze[j][i] == WALL:
                maze[j][i] = FLOOR

# Fonction pour créer un couloir vertical dans le labyrinthe
def create_vertical_corridor(y1, y2, x):
    for i in range(max(0, x-CORRIDOR_MAX_WIDTH), min(SIZE, x+CORRIDOR_MAX_WIDTH+1)):
        for j in range(min(y1, y2), max(y1, y2)+1):
            if maze[j][i] == WALL:
                maze[j][i] = FLOOR


# Création des salles et des couloirs
rooms = []
for _ in range(10):  # Nombre de salles à créer
    w, h = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE), random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
    x, y = random.randint(1, SIZE-w-1), random.randint(1, SIZE-h-1)
    create_room(x, y, w, h)
    rooms.append((x, y, w, h))
    
# Création des couloirs
for i in range(len(rooms)-1):
    x1, y1 = rooms[i][0]+rooms[i][2]//2, rooms[i][1]+rooms[i][3]//2
    x2, y2 = rooms[i+1][0]+rooms[i+1][2]//2, rooms[i+1][1]+rooms[i+1][3]//2
    if random.random() < 0.5:
        create_horizontal_corridor(x1, x2, y1)
        create_vertical_corridor(y1, y2, x2)
    else:
        create_vertical_corridor(y1, y2, x1)
        create_horizontal_corridor(x1, x2, y2)

# Recherche de l'entrée et de la sortie
start, end = None, None
while start is None or end is None or start == end:
    start = (random.randint(0, SIZE-1), random.randint(0, SIZE-1))
    end = (random.randint(0, SIZE-1), random.randint(0, SIZE-1))
    if maze[start[1]][start[0]] == WALL or maze[end[1]][end[0]] == WALL:
        start, end = None, None

# Création des coffres
for _ in range(NUM_CHESTS):
    while True:
        x, y = random.randint(0, SIZE-1), random.randint(0, SIZE-1)
        if maze[y][x] == FLOOR:
            maze[y][x] = CHEST
            break

# Création des pokemon
for _ in range(NUM_pokemon):
    while True:
        x, y = random.randint(0, SIZE-1), random.randint(0, SIZE-1)
        if maze[y][x] == FLOOR:
            maze[y][x] = pokemon
            break


# Affichage du labyrinthe
ajouter_bordures(maze);
for j in range(SIZE):
    for i in range(SIZE):
        if (i, j) == start:
            print(START, end="")
        elif (i, j) == end:
            print(END, end="")
        else:
            print(maze[j][i], end="")
    print()

# Enregistrement du labyrinthe dans un fichier
with open(file_name, "w") as f:
    f.write("\n".join(["".join(row) for row in maze]))
"""