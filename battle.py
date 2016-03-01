import random

def hitpoints(character, enemy, room):
	
	if character.hitpoints <= 0
		print "You have taken a beating and your life is gone.  Better luck next time!"
	else:
		decision(character, enemy, room)
		

def decision(character, enemy, room):
	
	if character.type == "archer":
		print """\n\t\tYour enemy is a %s with %d hitpoints and has %s armor 
		with %d protection and a %s for a weapon that inflicts %d damage.""" % (enemy.type, enemy.hitpoints, enemy.armor.armor, enemy.armor.protection,
		enemy.weapon.weapon, enemy.weapon.damage) 
		print "\nYour current stats are:"
		print "Hitpoints: %d" % character.hitpoints
		print "Weapon: %s that inflicts %d damage" % (character.weapon.weapon, character.weapon.damage)
		print "Armor: %s that has %d protection" % (character.armor.armor, character.armor.protection)
		
		loopFight = False
		
		while loopFight == False:
			print "What do you want to do?\n"
			print "Do you run or do you fight?\n"
			
			fight = raw_input("> ")
			
			if fight in ("fight", "Fight"):
				loopFight = True
				
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
					elif move in ("2", "Trip", "trip"):
						loopMove = True
						move = Trip(character, enemy)
						move.action()
					else:
						print "Try something different.\n"
			elif fight in ("run", "Run"):
				loopFight = True
				print "You decide to go back to the place that you came from.\n"
				if room.previous == "none":
					print "You back into the cell that you came from and the %s" % enemy.type
					print "proceeds to destroy you with his superior skills and you"
					print "die. Thanks for playing and better luck next time!"
				else: 
					roomControl(character, room)
			else:
				print "Try something different.\n"

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
	
	
class Stab(object):
	
	def __init__(self, character, enemy):
		self.character = character
		self.enemy = enemy
		
	def action(self):
		rand = random.randint(0, 1)
		
		if rand == 1:
			print "You stab the %s with %s!" % (self.enemy.type, self.character.weapon.weapon)
		else:
			print "You stab your %s at the %s and you miss!" % (self.character.weapon.weapon, self.enemy.type)

		
	
class Shoot(object):
	
	def __init__(self, character, enemy):
		self.character = character
		self.enemy = enemy
	
	def action(self):		
		rand = random.randint(0, 1)
		
		if rand == 1:
			print "You shoot the %s with the %s!" % (self.enemy.type, self.character.weapon.weapon)
		else:
			print "You shoot your %s at the %s and you miss!" % (self.character.weapon.weapon, self.enemy.type)
	
class Trip(object):
	
	def __init__(self, character, enemy):
		self.character = character
		self.enemy = enemy
	
	
# Implement this later
# class Skill(object):
	
	# def __init__(self, character, enemy):
		# self.character = character
		# self.enemy = enemy
		
		