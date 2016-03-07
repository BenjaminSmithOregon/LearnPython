import random

from rooms import *

def battleMath(character, enemy, who):
	if who == "bad":
		a = character.armor.protection * .01
		b = 1 - a
		c = b * enemy.weapon.damage
		character.hitpoints = character.hitpoints - c

	else:
		a = enemy.armor.protection * .01
		b = 1 - a
		c = b * character.weapon.damage
		enemy.hitpoints = enemy.hitpoints - c


def hitpoints(character, enemy):

	if enemy.type == "none":
		print "\n\t\t\tThere is no enemy present in this room.  You move on to the next room."
	else:
		print """\n\t\t\tYour enemy is a(n) %s with %d hitpoints and has %s armor
		\twith %d protection and a %s for a weapon that inflicts %d damage.""" % (enemy.type, enemy.hitpoints, enemy.armor.armor, enemy.armor.protection,
		enemy.weapon.weapon, enemy.weapon.damage)
		print "\nYour current stats are:"
		print "Hitpoints: %d" % character.hitpoints
		print "Weapon: %s that inflicts %d damage" % (character.weapon.weapon, character.weapon.damage)
		print "Armor: %s that has %d protection" % (character.armor.armor, character.armor.protection)


def hitpointCheck(character, enemy, room):

	if character.hitpoints <= 0:
		print "You have taken a beating and your life is gone.  Better luck next time!"
	else:
		if enemy.hitpoints <= 0:
			print "\nYou have defeated your enemy! You scour the %s's" % enemy.type
			print "body for armor and its weapon."
			character.pickUpArmor(enemy.armor)
			character.pickUpWeapon(enemy.weapon)

			if character.hitpoints <= 15:
				character.hitpoints = character.hitpoints + 20
				print "You find a healing potion in the %s's pocket and drink it." % enemy.type
				print "Your hitpoints have increased to %d" % character.hitpoints
		else:
			decision(character, enemy, room)


def decision(character, enemy, room):
		hitpoints(character, enemy)

		if enemy.type == "none":
			pass
		else:
			loopFight = False
			while loopFight == False:
				print "\nWhat do you want to do?\n"
				print "Do you run or do you fight?\n"

				choice = raw_input("> ")

				if choice in ("fight", "Fight"):
					loopFight = True
					fight(character, enemy, room)

				elif choice in ("run", "Run"):
					loopFight = True
					roomControl(character, room, "run")
				else:
					print "Try something different.\n"


def fight(character, enemy, room):

	if character.type == "archer":
		loopMove = False
		while loopMove == False:
			print "You decide to fight, what move do you perform?\n"
			print "Do you:\n"
			print "\t1. Shoot"
			print "\t2. Trip"

			move = raw_input("> ")

			if move in ("1", "Shoot", "shoot"):
				loopMove = True
				move = Shoot(character, enemy)
				move.action()
				hitpointCheck(character, enemy, room)
			elif move in ("2", "Trip", "trip"):
				loopMove = True
				trip = Trip(character, enemy)
				trip.action()
				hitpointCheck(character, enemy, room)
			else:
				print "Try something different.\n"

	if character.type == "swordsman":
		loopMove = False
		while loopMove == False:
			print "You decide to fight, what move do you perform?\n"
			print "Do you:\n"
			print "\t1. Swing"
			print "\t2. Trip"

			move = raw_input("> ")

			if move in ("1", "Swing", "swing"):
				loopMove = True
				move = Swing(character, enemy)
				move.action()
				hitpointCheck(character, enemy, room)
			elif move in ("2", "Trip", "trip"):
				loopMove = True
				trip = Trip(character, enemy)
				trip.action()
				hitpointCheck(character, enemy, room)
			else:
				print "Try something different.\n"

	if character.type == "thief":
		loopMove = False
		while loopMove == False:
			print "You decide to fight, what move do you perform?\n"
			print "Do you:\n"
			print "\t1. Stab"
			print "\t2. Trip"

			move = raw_input("> ")

			if move in ("1", "Stab", "stab"):
				loopMove = True
				move = Stab(character, enemy)
				move.action()
				hitpointCheck(character, enemy, room)
			elif move in ("2", "Trip", "trip"):
				loopMove = True
				trip = Trip(character, enemy)
				trip.action()
				hitpointCheck(character, enemy, room)
			else:
				print "Try something different.\n"


class Swing(object):

	def __init__(self, character, enemy):
		self.character = character
		self.enemy = enemy

	def action(self):
		rand = random.randint(0, 1)

		if rand == 1:
			good = "good"
			print "You hit the %s with %s!" % (self.enemy.type, self.character.weapon.weapon)
			battleMath(self.character, self.enemy, good)
		else:
			bad = "bad"
			print "You swing your %s at the %s and you miss!" % (self.character.weapon.weapon, self.enemy.type)
			print "\nThe enemy %s makes a move at you with his %s" % (self.enemy.type, self.enemy.weapon.weapon)
			battleMath(self.character, self.enemy, bad)


class Stab(object):

	def __init__(self, character, enemy):
		self.character = character
		self.enemy = enemy

	def action(self):
		rand = random.randint(0, 1)

		if rand == 1:
			good = "good"
			print "You stab the %s with %s!" % (self.enemy.type, self.character.weapon.weapon)
			battleMath(self.character, self.enemy, good)
		else:
			bad = "bad"
			print "You stab your %s at the %s and you miss!" % (self.character.weapon.weapon, self.enemy.type)
			print "\nThe enemy %s makes a move at you with his %s" % (self.enemy.type, self.enemy.weapon.weapon)
			battleMath(self.character, self.enemy, bad)


class Shoot(object):

	def __init__(self, character, enemy):
		self.character = character
		self.enemy = enemy

	def action(self):
		rand = random.randint(0, 1)

		if rand == 1:
			good = "good"
			print "You shoot the %s with the %s!" % (self.enemy.type, self.character.weapon.weapon)
			battleMath(self.character, self.enemy, good)
		else:
			bad = "bad"
			print "You shoot your %s at the %s and you miss!" % (self.character.weapon.weapon, self.enemy.type)
			print "\nThe enemy %s makes a move at you with his %s" % (self.enemy.type, self.enemy.weapon.weapon)
			battleMath(self.character, self.enemy, bad)


class Trip(object):

	def __init__(self, character, enemy):
		self.character = character
		self.enemy = enemy

	def action(self):
		print "\nYou sweep your foot behind its leg with the utmost of"
		print "finess and put the %s on its back and continue to attack it." % self.enemy.type

		self.enemy.hitpoints = 0


# Will implement this later
# class Block(object):

	# def __init__(self, character, enemy):
		# self.character = character
		# self.enemy = enemy

	# def action(self):
		# print "Your hitpoints: %d" % self.character.hitpoints
		# print "%s hitpoints: %d" % (self.enemy.type, self.enemy.hitpoints)
		# rand = random.randint(0, 1)


# Will implement this later
# class Jump(object):

	# def __init__(self, character, enemy):
		# self.character = character
		# self.enemy = enemy


# Will implement this later
# class Duck(object):

	# def __init__(self, character, enemy):
		# self.character = character
		# self.enemy = enemy


# Implement this later
# class Skill(object):

	# def __init__(self, character, enemy):
		# self.character = character
		# self.enemy = enemy
