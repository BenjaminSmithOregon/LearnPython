import random

class Troll(object):
	
	def __init__(self, weapon, armor):
		self.type = "Troll"
		self.hitpoints = random.randint(20, 50)
		self.weapon = weapon
		self.armor = armor
		
class Ogre(object):
	
	def __init__(self, weapon, armor):
		self.type = "Ogre"
		self.hitpoints = random.randint(50, 70)
		self.weapon = weapon
		self.armor = armor

class Knight(object):
	
	def __init__(self, weapon, armor):
		self.type = "Knight"
		self.hitpoints = random.randint(80, 100)
		self.weapon = weapon
		self.armor = armor
		
class EnemyArcher(object):
	
	def __init__(self, weapon, armor):
		self.type = "Archer"
		self.hitpoints = random.randint(80, 100)
		self.weapon = weapon
		self.armor = armor
		
class Dwarf(object):
	
	def __init__(self, weapon, armor):
		self.type = "Dwarf"
		self.hitpoints = random.randint(80, 100)
		self.weapon = weapon
		self.armor = armor