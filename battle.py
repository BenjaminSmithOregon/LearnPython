import random

def decision(character, enemy):
	
	if character.type == "archer":
		print """\n\t\tYour enemy is a %s with %d hitpoints and has %s armor with %d protection and
		a %s for a weapon that inflicts %d damage.""" % (enemy.type, enemy.hitpoints, enemy.armor.armor, 
		enemy.armor.protection, enemy.weapon.weapon, enemy.weapon.damage) 
		print "\nYour current stats are:"
		print "Hitpoints: %d" % character.hitpoints
		print "Weapon: %s, that inflicts %d damage" % (character.weapon.weapon, character.weapon.damage)
		print "Armor: %s, that has %d protection" % (character.armor.armor, character.armor.protection)


class Swing(object):

	def __init__(self, character, enemy):
		self.character = character
		self.enemy = enemy
		
	def action(self):
		rand = random.randint(0, 1)
		
		if rand == 1:
			print "You hit the %s with %s!" % (self.enemy.type, self.character.weapon.weapon)
		else:
			print "You swing your %s at the %s and you miss!" % (self.character.weapon.weapon, self.enemy.type)
		
	
class Block(object):
	
	def __init__(self, character, enemy):
		self.character = character
		self.enemy = enemy
	
	def action(self):
		print "Your hitpoints: %d" % self.character.hitpoints
		print "%s hitpoints: %d" % (self.enemy.type, self.enemy.hitpoints)
		rand = random.randint(0, 1)
		
		
		
		
	
class Jump(object):
	
	def __init__(self, character, enemy):
		self.character = character
		self.enemy = enemy

	
class Duck(object):
	
	def __init__(self, character, enemy):
		self.character = character
		self.enemy = enemy
	
	
class Stab(object):
	
	def __init__(self, character, enemy):
		self.character = character
		self.enemy = enemy

	
class Shoot(object):
	
	def __init__(self, character, enemy):
		self.character = character
		self.enemy = enemy
	
	
class Trip(object):
	
	def __init__(self, character, enemy):
		self.character = character
		self.enemy = enemy
	
	
class Skill(object):
	
	def __init__(self, character, enemy):
		self.character = character
		self.enemy = enemy
		
		