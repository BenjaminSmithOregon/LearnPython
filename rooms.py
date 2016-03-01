import random
from armor import *
from weapons import *
from enemies import *
from EnemyRandomizer import *
from battle import *

def roomControl(self, character, room):
	if room.run == "no"


class Cell(object):
	
	def __init__(self, player):
		self.player = player
		self.previous = "none"
		self.next = "lower room"
		self.run = "no"
		
	def play(self):
	
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
	
	def __init__(self, character):
		self.character = character
		self.previous = "cell"
		self.next = "kitchen"
		
	def play(self):
		enemy = RandomEnemy()
		enemy.randomize()