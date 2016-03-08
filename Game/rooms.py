from weapons import *
from enemyRandomizer import *
from battle import *

import random


class RoomControl(object):

	def __init__(self, character, room, enemy):
		self.character = character
		self.room = room
		self.enemy = enemy


	def run(self, enemy):
			print "You decide to go back to the place where you came from.\n"
			if self.room.previous == "cell":
				print "You back into the cell that you came from and the %s" % self.enemy.type
				print "proceeds to destroy you with his superior skills and you"
				print "die. Thanks for playing and better luck next time!"
				exit()
			elif self.room.previous == "lower room":
				last = LowerRoom(self.character)
				last.back()
				return last
			elif self.room.previous == "kitchen":
				last = Kitchen(self.character)
				last.back()
				return last
			elif self.room.previous == "mess hall":
				last = MessHall(self.character)
				last.back()
				return last
			elif self.room.previous == "stairs":
				last =Stairs(self.character)
				last.back()
				return last
			elif self.room.previous == "main hall":
				last = MainHall(self.character)
				last.back()
				return last
			elif self.room.previous == "tower":
				print "There is no way that you can climb back up that rope"
				print "into the tower.  You are stuck!  Might as well face"
				print "the music...coward."
				return self.room


	def defeat(self):
		if self.room.next == "sunset":
			print ""
		else:
			print "\nYou forge ahead to the next room."

		if self.room.next == "lower room":
			next = LowerRoom(self.character)
			next.play()
			return next
		elif self.room.next == "kitchen":
			next = Kitchen(self.character)
			next.play()
			return next
		elif self.room.next == "mess hall":
			next = MessHall(self.character)
			next.play()
			return next
		elif self.room.next == "stairs":
			next = Stairs(self.character)
			next.play()
			return next
		elif self.room.next == "main hall":
			next = MainHall(self.character)
			next.play()
			return next
		elif self.room.next == "tower":
			next = Tower(self.character)
			next.play()
			return next
		elif self.room.next == "stable":
			next = Stable(self.character)
			next.play()
			return next
		elif self.room.next == "sunset":
			next = Sunset(self.character)
			next.play()
			return next


class Cell(object):

	def __init__(self, player):
		self.player = player
		self.previous = "none"
		self.next = "lower room"
		self.enemy = "none"
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
			belt and unlock the door.  You then search the guard."""

			#assigns damage and weapon type to picked up weapon
			damage = random.randint(7, 15)
			name = "short sword"
			weapon = GuardWeapon(damage, name)
			self.player.pickUpWeapon(weapon)

		elif self.player.type == "archer":
			print """\t\t\tYou see a key ring hanging from the guards belt.  You reach
			through the bars and pull his head back against them, rendering
			him unconscious.  You then carefully take the keys off of his
			belt and unlock the door.  You then search the guard."""

			#assigns damage and weapon type to picked up weapon
			damage = random.randint(7, 12)
			name = "bow"
			weapon = GuardWeapon(damage, name)
			self.player.pickUpWeapon(weapon)

		else:
			print """\t\t\tYou see a key ring hanging from the guards belt.  Your reach
			through the bars and quietly unhook the keys from his belt.  You unlock
			the door and quietly walk out.  You then search the guards belt and find
			a dagger."""

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

		print "\nYou enter into the lower hall from your cell."

		if self.enemy.type != "none":
			print "As you enter into the hall you see an enemy"
			print "over on the far side of the room."


	def back(self):
		# Creates a random enemy
		enemy = RandomEnemy()
		enemy = enemy.randomize()
		self.enemy = enemy

		print "\nYou enter into the lower hall from the kitchen."

		if self.enemy.type != "none":
			print "As you enter into the hall you see an enemy"
			print "over on the far side of the room."


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

		print "\nYou enter into the kitchen."

		if self.enemy.type != "none":
			print "As you enter the kitchen you see something at the end"
			print "of the counter behind the hanging pots and pans."


	def back(self):
		# Creates a random enemy
		enemy = RandomEnemy()
		enemy = enemy.randomize()
		self.enemy = enemy

		print "\nYou enter into the kitchen from the mess hall."

		if self.enemy.type != "none":
			print "As you enter the kitchen you see something at the end"
			print "of the counter behind the hanging pots and pans."


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

		print "\nYou enter into the lower hall."

		if self.enemy.type != "none":
			print "You enter the mess hall you see something move"
			print "from the top of the chandelier."


	def back(self):
		# Creates a random enemy
		enemy = RandomEnemy()
		enemy = enemy.randomize()
		self.enemy = enemy

		print "\nYou enter into the mess hall from the stairs."

		if self.enemy.type != "none":
			print "You enter the mess hall you see something move"
			print "from the top of the chandelier."


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

		print "\nYou enter into a stair case."

		if self.enemy.type != "none":
			print "As you climb the staircase something comes"
			print "charging down around the corner."


	def back(self):
		# Creates a random enemy
		enemy = RandomEnemy()
		enemy = enemy.randomize()
		self.enemy = enemy

		print "\nYou enter into the stairway from the main hall."

		if self.enemy.type != "none":
			print "As you scurry down the staircase something comes"
			print "charging up around the corner."


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

		print "\nYou step up into the main hall."

		if self.enemy.type != "none":
			print "As you enter the main hall you notice a shadow"
			print "over by the window."


	def back(self):
		# Creates a random enemy
		enemy = RandomEnemy()
		enemy = enemy.randomize()
		self.enemy = enemy

		print "\nYou enter into the main hall from the tower."

		if self.enemy.type != "none":
			print "As you enter the main hall you notice a shadow"
			print "over by the window."


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

		print "\nYou make your way across the main hall and into the tower."

		if self.enemy.type != "none":
			print "As you enter the tower, another enemy comes at you."


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

		print "\nYou climb your way to the top of the tower and find"
		print "a rope attached to the top of the window and it leads"
		print "down to a stable down below.  You decide to slide down the"
		print "rope and use it as a zipline.  You grab and rip a piece"
		print "of the curtain hanging around the window to use so that"
		print "you won't burn your hands and wrap it over the rope and"
		print "slide down!"

		if self.enemy.type != "none":
			print "As you approach the bottom of the rope you decide to"
			print "let go above a pile of hay.  You end of overshooting"
			print "it and tumbling into a big pile of metal cans, making"
			print "a loud clanging and crashing.  You get up and bruch"
			print "yourself off only to look up and see an enemy."


class Sunset(object):

	def __init__(self, player):
		self.player = player
		self.previous = "stable"
		self.next = "the end"
		self.enemy = "none"
		self.defeated = "no"


	def play(self):
		print "\nYou search the stable for a horse and find a young restless mustang"
		print "you jump into the saddle and ride off into the sunset completely"
		print "satisfied in your humble self."
		exit()
