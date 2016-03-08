import random
import pdb

from character import *
from battle import *
from rooms import *
from enemies import *
from weapons import *
from armor import *
from enemyRandomizer import *

# Asks for player's name
print "\nWhat is your name?"

name = raw_input("> ")

print "\nExcellent %s, thanks for playing! \n" % name

# initiates player and room to None
player = None
room = None


# Asks player to choose character type
while player is None:

	print "Now choose what type of character that you would like to play: \n"
	print "1. Archer \n"
	print "2. Swordsman \n"
	print "3. Thief \n"
	player = raw_input("> ")

	if player in ("1", "Archer", "archer"):
		player = Archer(name, NoWeapon(), Armor())
	elif player in ("2", "Swordsman", "swordsman"):
		player = Swordsman(name, NoWeapon(), Armor())
	elif player in ("3", "Thief", "thief"):
		player = Thief(name, NoWeapon(), Armor())
	else:
		print "\nTry something different \n"
		player = "None"


# Initiates game play and starts player in the "cell" room
room = Cell(player)
room.play()

control = RoomControl(character = player, room = room, enemy = room.enemy)

room = control.defeat()

decision(room.player, room.enemy, room)
