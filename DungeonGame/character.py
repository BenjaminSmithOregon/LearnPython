class Archer(object):
	type = "archer"
	hitpoints = 75
	armor = 0
	weapon = "nothing"
	
	def __init__(self, name):
		self.name = name
		
		
class Swordsman(object):
	type = "swordsman"
	hitpoints = 100
	armor = 0
	weapon = "nothing"
	
	def __init__(self, name):
		self.name = name

		
class Thief(object):
	type = "thief"
	hitpoints = 50
	armor = 0
	weapon = "nothing"
	
	def __init__(self, name):
		self.name = name