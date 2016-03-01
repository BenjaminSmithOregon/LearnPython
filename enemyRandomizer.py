import random
from armor import *
from weapons import *
from enemies import *

class RandomEnemy(object):
	
	def __init__(self):
		self.enemyAssign = "none"
		
	def randomize(self):
		self.enemyList = ["troll", "ogre", "knight", "archer", "dwarf", "none"]
		index = random.randint(0,5)
		self.enemyAssign = self.enemyList[index]
		
		if self.enemyAssign == "troll":
			weapon = TrollWeapon()
			weapon2 = weapon.assign()
			armor = Armor()
			armor2 = armor.assign()
			troll = Troll(weapon, armor)
			return troll
		elif self.enemyAssign == "ogre":
			weapon = OgreWeapon()
			weapon2 = weapon.assign()
			armor = Armor()
			armor2 = armor.assign()
			ogre = Ogre(weapon, armor)
			return ogre
		elif self.enemyAssign == "knight":
			weapon = KnightWeapon()
			weapon2 = weapon.assign()
			armor = Armor()
			armor2 = armor.assign()
			knight = Knight(weapon, armor)
			return knight
		elif self.enemyAssign == "archer":
			weapon = ArcheryWeapon()
			weapon2 = weapon.assign()
			armor = Armor()
			armor2 = armor.assign()
			archer = EnemyArcher(weapon, armor)
			return archer
		elif self.enemyAssign == "dwarf":
			weapon = DwarfWeapon()
			weapon2 = weapon.assign()
			armor = Armor()
			armor2 = armor.assign()
			dwarf = Dwarf(weapon, armor)
			return dwarf
		else:
			weapon = NoWeapon()
			armor = Armor()
			noEnemy = NoEnemy(weapon, armor)
			return noEnemy