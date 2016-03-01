This is the readMe file for the Dungeon game:

There are the following files:

Ex45.py
battle.py
rooms.py
character.py
enemies.py
armor.py
weapons.py
enemyRandomizer.py

Ex45.py is the "main" for the game.  It imports all other files and then
	calls the character and rooms files.
	
battle.py is the file that takes in the character and enemy files and creates
	different objects based on what type of move that the character makes and
	calculates hitpoints based on what the damage of a weapon is and what the
	protection of the armor is.

rooms.py is the file that holds all of the classes for all of the different
	rooms.  It takes in the character and enemy objects and then passes them to
	the battle object.

character.py takes in the players name and then initially creates a character
	with no armor and no weapon.  Then the character's armor and weapon attributes
	change as they defeat enemies and pick up their foe's armor and weapon.

enemies.py takes in an armor and a weapon and then assigns both of them to the enemy

armor.py takes no parameters and randomly assigns a protection value based on the
	random number that it generates.
	
weapons.py takes in no parameters and creates a damage number based on the random
	number that is generated.
	
enemyRandomizer.py randomly creates an enemy.  It first calls an armor class and
	creates an armor object based on the enemy that it has randomly created and
	then assigns that armor to it.  Then it calls a weapon class and creates a
	weapon object based on the same randomly selected enemy and assigns the weapon
	to the enemy as well.  Then it passes the enemy to the room object that the 
	character has just walked into.
	
The essential flow at the present time is:

1. Player enters name
2. Player enters type of character they want to play
3. Player escapes from prison cell
4. Player walks into the next room
5. Random enemy is generated and its stats are presented
6. Based on the stats presented, the player can either fight or run
7. If the player runs, they run back to cell and die
8. If the player fights, the fight is done one move at a time
9. The player and the enemy take turns with each move, and the 
	player has the option to run or keep fighting after every move
10.....More to come later