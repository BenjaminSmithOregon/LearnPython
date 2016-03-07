import random

class NoEnemy(object):

	def __init__(self, weapon, armor):
		self.type = "none"
		self.hitpoints = random.randint(0, 0)
		self.weapon = weapon
		self.armor = armor

class Guard(object):

	def __init__(self, weapon, armor):
		self.type = "Guard"
		self.hitpoints = random.randint(0, 0)
		self.weapon = weapon
		self.armor = armor

class Troll(object):

	def __init__(self, weapon, armor):
		self.type = "Troll"
		self.hitpoints = random.randint(5, 10)
		self.weapon = weapon
		self.armor = armor

class Ogre(object):

	def __init__(self, weapon, armor):
		self.type = "Ogre"
		self.hitpoints = random.randint(15, 20)
		self.weapon = weapon
		self.armor = armor

class Knight(object):

	def __init__(self, weapon, armor):
		self.type = "Knight"
		self.hitpoints = random.randint(20, 25)
		self.weapon = weapon
		self.armor = armor

class EnemyArcher(object):

	def __init__(self, weapon, armor):
		self.type = "Archer"
		self.hitpoints = random.randint(15, 20)
		self.weapon = weapon
		self.armor = armor

class Dwarf(object):

	def __init__(self, weapon, armor):
		self.type = "Dwarf"
		self.hitpoints = random.randint(5, 15)
		self.weapon = weapon
		self.armor = armor
