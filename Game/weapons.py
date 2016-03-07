import random

class NoWeapon(object):
	damage = 0
	weapon = "None"


class GuardWeapon(object):
	damage = 0
	weapon = "None"

	def __init__(self, damage, weapon):
		self.damage = damage
		self.weapon = weapon


class ArcheryWeapon(object):

	def __init__(self):
		self.damage = 0
		self.weapon = "none"

	def assign(self):
		archerWeapons = ["bow", "long bow", "cross bow"]
		self.weapon = archerWeapons[random.randint(0,2)]

		if self.weapon == "bow":
			self.damage = random.randint(10,20)
		elif self.weapon == "long bow":
			self.damage = random.randint(20, 30)
		else:
			self.damage = random.randint(20, 35)


class SwordWeapon(object):

	def __init__(self):
		self.damage = 0
		self.weapon = "none"

	def assign(self):
		swordsmanWeapons = ["sword", "short sword", "long sword"]
		self.weapon = swordsmanWeapons[random.randint(0,2)]

		if self.weapon == "sword":
			self.damage = random.randint(30, 40)
		elif self.weapon == "short sword":
			self.damage = random.randint(20, 30)
		else:
			self.damage = random.randint(30, 40)


class ThiefWeapon(object):

	def __init__(self):
		self.damage = 0
		self.weapon = "none"

	def assign(self):
		thiefWeapons = ["blow gun", "dagger", "throwing knives"]
		self.weapon = thiefWeapons[random.randint(0,2)]

		if self.weapon == "blow gun":
			self.damage = random.randint(10, 20)
		elif self.weapon == "dagger":
			self.damage = random.randint(20, 30)
		else:
			self.damage = random.randint(30, 40)


class TrollWeapon(object):

	def __init__(self):
		self.damage = 0
		self.weapon = "none"

	def assign(self):
		trollWeapons = ["short sword", "dagger", "cross bow"]
		self.weapon = trollWeapons[random.randint(0,2)]

		if self.weapon == "short sword":
			self.damage = random.randint(10, 20)
		elif self.weapon == "dagger":
			self.damage = random.randint(10, 20)
		else:
			self.damage = random.randint(10, 20)


class OgreWeapon(object):

	def __init__(self):
		self.damage = 0
		self.weapon = "none"

	def assign(self):
		ogreWeapons = ["short sword", "hammer", "cross bow"]
		self.weapon = ogreWeapons[random.randint(0,2)]

		if self.weapon == "short sword":
			self.damage = random.randint(15, 25)
		elif self.weapon == "hammer":
			self.damage = random.randint(15, 25)
		else:
			self.damage = random.randint(15, 25)


class KnightWeapon(object):

	def __init__(self):
		self.damage = 0
		self.weapon = "none"

	def assign(self):
		knightWeapons = ["long sword", "mace", "cross bow"]
		self.weapon = knightWeapons[random.randint(0,2)]

		if self.weapon == "long sword":
			self.damage = random.randint(25, 35)
		elif self.weapon == "mace":
			self.damage = random.randint(30, 40)
		else:
			self.damage = random.randint(15, 25)


class DwarfWeapon(object):

	def __init__(self):
		self.damage = 0
		self.weapon = "none"

	def assign(self):
		knightWeapons = ["hammer", "short sword", "cross bow"]
		self.weapon = knightWeapons[random.randint(0,2)]

		if self.weapon == "hammer":
			self.damage = random.randint(25, 35)
		elif self.weapon == "short sword":
			self.damage = random.randint(30, 40)
		else:
			self.damage = random.randint(15, 25)
			
