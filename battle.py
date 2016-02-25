import random

class Swing(object):

	def __init__(self, character, hitpoints, armor, weapon):
		self.character = character
		self.hitpoints = hitpoints
		self.armor = armor
		self.weapon = weapon
		
	def action(self):
		rand = random.randint(0, 1)
		
		if rand == 1:
			print "You hit your enemy with %s!" % self.weapon
			return True
		else:
			print "You swing your %s at your enemy and you miss!" % self.weapon
			return False
		
	
class Block(object):
	
	def __init__(self, character, hitpoints, armor, weapon):
		self.character = character
		self.hitpoints = hitpoints
		self.armor = armor
		self.weapon = weaponn
	
	
class Jump(object):
	
	def __init__(self, character, hitpoints, armor, weapon):
		self.character = character
		print character
		self.hitpoints = hitpoints
		print hitpoints
		self.armor = armor
		print armor
		self.weapon = weapon
		print weapon

	
class Duck(object):
	
	def __init__(self, character, hitpoints, armor, weapon):
		self.character = character
		print character
		self.hitpoints = hitpoints
		print hitpoints
		self.armor = armor
		print armor
		self.weapon = weapon
		print weapon
	
	
class Stab(object):
	
	def __init__(self, character, hitpoints, armor, weapon):
		self.character = character
		print character
		self.hitpoints = hitpoints
		print hitpoints
		self.armor = armor
		print armor
		self.weapon = weapon
		print weapon

	
class Shoot(object):
	
	def __init__(self, character, hitpoints, armor, weapon):
		self.character = character
		print character
		self.hitpoints = hitpoints
		print hitpoints
		self.armor = armor
		print armor
		self.weapon = weapon
		print weapon
	
	
class Trip(object):
	
	def __init__(self, character, hitpoints, armor, weapon):
		self.character = character
		print character
		self.hitpoints = hitpoints
		print hitpoints
		self.armor = armor
		print armor
		self.weapon = weapon
		print weapon
	
	
class Skill(object):
	
	def __init__(self, character, hitpoints, armor, weapon):
		self.character = character
		print character
		self.hitpoints = hitpoints
		print hitpoints
		self.armor = armor
		print armor
		self.weapon = weapon
		print weapon
		
		