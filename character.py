class Archer(object):
	
	def __init__(self, name, weapon, armor, hitpoints = 75):
		self.name = name
		self.weapon = weapon
		self.armor = armor
		self.type = "archer"
		self.hitpoints = hitpoints
	
	def pickUpWeapon(self, weapon):
		self.weapon = weapon
		
class Swordsman(object):
	type = "swordsman"
	hitpoints = 100
	
	def __init__(self, name, weapon, armor):
		self.name = name
		self.weapon = weapon
		self.armor = armor
		
	def pickUpWeapon(self, weapon):
		self.weapon = weapon
		
class Thief(object):
	type = "thief"
	hitpoints = 50
	
	def __init__(self, name, weapon, armor):
		self.name = name
		self.weapon = weapon
		self.armor = armor
		
	def pickUpWeapon(self, weapon):
		self.weapon = weapon