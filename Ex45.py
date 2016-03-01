import random

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

player = None


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
		
		
# Setting the first scene
print "\n"
print """ 	 You awaken in a dark and dirty cell in the depths of some
	 sort of dungeon.  You are not sure how you got here or how long
	 you have been here.  All you do know is that your name is %s, and
	 that you are a(n) %s by trade.  You scan the scene around you.
	 Your cell is dark and there is a guard snoozing outside of your
	 cell.""" % (name, player.type)

cell = Cell(player)
cell.play()


# Next Scene
enemy1 = RandomEnemy()
enemy1 = enemy1.randomize()

decision(player, enemy1, cell)


#print """\n\tYour enemy is a %s and has %s armor with %d protection and
#	a %s for a weapon that inflicts %d damage.""" % (enemy.type, enemy.armor.armor, 
#	enemy.armor.protection, enemy.weapon.weapon,enemy.weapon.damage)

print "\n", 

#battle = Swing(player, enemy)
print "\n"
