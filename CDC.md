Genre : Rogue-like solo
Style : RPG
Plate-forme : PC windows (+Linux ?) 
Moteur : Godot Engine
Nombre de Joueurs: 1

Character : dresseur et son équipe de pokemon, tour par tour, choix parmis 4 attaques
Caméra : 2.5D vue de 3/4 avec changement de caméra quand en combat
Control : Clavier

**PITCH**

**Principe de jeu:**
Préparation:
- Le joueur choisit l'intensité du jeu (Facile, Moyen, Difficile)
- Le joueur choisit un starter parmis des pokémons une séléction (en plus des pokémons accumulés lors des parties précédentes)
Inspi: Pokemon, Hadès

**Grand axe technique :**
Génération procédurale des niveaux
	- dresseurs dans les salles
	- Dispositions des salles
	- Récompense des salles

**Action:**
- Le monde est généré aléatoirement, divisé en 4 zones (2 mini-boss par zone, 4 boss de zone, 1 boss final)
- Tous les 10 niveaux, un PNJ soigne complètement l'équipe


**Fonctionnalités:**
Une BDD contenant tous les Pokémons (.json)

Table Pokemon :
id - nom - type 1 - type 2 - capacité list - talent_id

Table capacité-list :
capacité id - pokemon-id

Table Capacité :
nom - type - status - puissance - description

Table talent
talent_id - nom - description
