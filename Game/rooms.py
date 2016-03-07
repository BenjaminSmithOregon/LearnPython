from weapons import *
from enemyRandomizer import *
from battle import *

import random


def roomControl(self, character, room, why):
	if why == "run":
		print "You decide to go back to the place that you came from.\n"
		if room.previous == "cell":
			print "You back into the cell that you came from and the %s" % enemy.type
			print "proceeds to destroy you with his superior skills and you"
			print "die. Thanks for playing and better luck next time!"
		elif room.previous == "":
			pass
	else:



class Cell(object):

	def __init__(self, player):
		self.player = player
		self.previous = "none"
		self.next = "lower room"
		self.defeated = "no"


	def play(self):

		print "\n"
		print """\t\t\tYou awaken in a dark and dirty cell in the depths of some
			 sort of dungeon.  You are not sure how you got here or how long
			 you have been here.  All you do know is that your name is %s, and
			 that you are a(n) %s by trade.  You scan the scene around you.
			 Your cell is dark and there is a guard snoozing outside of your
			 cell.\n""" % (self.player.name, self.player.type)

		if self.player.type == "swordsman":
			print """\t\t\tYou see a key ring hanging from the guards belt.  You reach
			through the bars and pull his head back against them, rendering
			him unconscious.  You then carefully take the keys off of his
			belt and unlock the door.  You then search the guard.  You find a
			short sword on him and take it into your possession."""

			#assigns damage and weapon type to picked up weapon
			damage = random.randint(7, 15)
			name = "short sword"
			weapon = GuardWeapon(damage, name)
			self.player.pickUpWeapon(weapon)

		elif self.player.type == "archer":
			print """\t\t\tYou see a key ring hanging from the guards belt.  You reach
			through the bars and pull his head back against them, rendering
			him unconscious.  You then carefully take the keys off of his
			belt and unlock the door.  You then search the guard.  You find a
			bow on him and take it into your possession."""

			#assigns damage and weapon type to picked up weapon
			damage = random.randint(7, 12)
			name = "bow"
			weapon = GuardWeapon(damage, name)
			self.player.pickUpWeapon(weapon)

		else:
			print """\t\t\tYou see a key ring hanging from the guards belt.  Your reach
			through the bars and quietly unhook the keys from his belt.  You unlock
			the door and quietly walk out.  You then search the guards belt and find
			a dagger.  You take it and put it into your belt."""

			#assigns damage and weapon type to picked up weapon
			damage = random.randint(7, 12)
			name = "dagger"
			weapon = GuardWeapon(damage, name)
			self.player.pickUpWeapon(weapon)


class LowerRoom(object):

	def __init__(self, player):
		self.player = player
		self.previous = "cell"
		self.next = "kitchen"
		self.enemy = "none"
		self.defeated = "no"


	def play(self):
		# Creates a random enemy
		enemy = RandomEnemy()
		enemy = enemy.randomize()
		self.enemy = enemy


class Kitchen(object):

	def __init__(self, player):
		self.player = player
		self.previous = "lower room"
		self.next = "mess hall"
		self.enemy = "none"
		self.defeated = "no"


	def play(self):
		# Creates a random enemy
		enemy = RandomEnemy()
		enemy = enemy.randomize()
		self.enemy = enemy


class MessHall(object):

	def __init__(self, player):
		self.player = player
		self.previous = "kitchen"
		self.next = "stairs"
		self.enemy = "none"
		self.defeated = "no"


	def play(self):
		# Creates a random enemy
		enemy = RandomEnemy()
		enemy = enemy.randomize()
		self.enemy = enemy

class Stairs(object):

	def __init__(self, player):
		self.player = player
		self.previous = "mess hall"
		self.next = "main hall"
		self.enemy = "none"
		self.defeated = "no"


	def play(self):
		# Creates a random enemy
		enemy = RandomEnemy()
		enemy = enemy.randomize()
		self.enemy = enemy


class MainHall(object):

	def __init__(self, player):
		self.player = player
		self.previous = "stairs"
		self.next = "tower"
		self.enemy = "none"
		self.defeated = "no"


	def play(self):
		# Creates a random enemy
		enemy = RandomEnemy()
		enemy = enemy.randomize()
		self.enemy = enemy


class Tower(object):

	def __init__(self, player):
		self.player = player
		self.previous = "main hall"
		self.next = "stable"
		self.enemy = "none"
		self.defeated = "no"


	def play(self):
		# Creates a random enemy
		enemy = RandomEnemy()
		enemy = enemy.randomize()
		self.enemy = enemy


class Stable(object):

	def __init__(self, player):
		self.player = player
		self.previous = "tower"
		self.next = "sunset"
		self.enemy = "none"
		self.defeated = "no"


	def play(self):
		# Creates a random enemy
		enemy = RandomEnemy()
		enemy = enemy.randomize()
		self.enemy = enemy


class Sunset(object):

	def __init__(self, player):
		self.player = player
		self.previous = "stable"
		self.next = "the end"
		self.enemy = "none"
		self.defeated = "no"


	def play(self):
