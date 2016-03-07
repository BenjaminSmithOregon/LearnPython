class Archer(object):

	def __init__(self, name, weapon, armor, hitpoints = 75):
		self.name = name
		self.weapon = weapon
		self.armor = armor
		self.type = "archer"
		self.hitpoints = hitpoints

	def pickUpWeapon(self, weapon):
		if weapon.damage >= self.weapon.damage:
			if weapon.weapon in ("bow", "long bow", "cross bow"):
				print "You pick up the enemy's %s" % weapon.weapon
				self.weapon = weapon
			else:
				print "You can not use the %s, since you don't posses the skills to use it." % weapon.weapon
		else:
			print "You decide to leave the %s there as it is inferior to your %s" % (weapon.weapon, self.weapon.weapon)

	def pickUpArmor(self, armor):
		if self.armor <= armor.protection:
			print "You pick up the enemy's %s" % self.armor.armor
			self.armor = armor
		else:
			print "Your armor is superior to the enemy's armor, so you leave it there."

class Swordsman(object):

	def __init__(self, name, weapon, armor, hitpoints = 100):
		self.name = name
		self.weapon = weapon
		self.armor = armor
		self.type = "swordsman"
		self.hitpoints = hitpoints

	def pickUpWeapon(self, weapon):
		if weapon.damage >= self.weapon.damage:
			if weapon.weapon in ("sword", "short sword", "long sword"):
				print "You pick up the enemy's %s" % weapon.weapon
				self.weapon = weapon
			else:
				print "You can not use the %s, since you don't posses the skills to use it." % weapon.weapon
		else:
			print "You decide to leave the %s there as it is inferior to your %s" % (weapon.weapon, self.weapon.weapon)

	def pickUpArmor(self, armor):
		if self.armor <= armor.protection:
			print "You pick up the enemy's %s" % self.armor.armor
			self.armor = armor
		else:
			print "Your armor is superior to the enemy's armor, so you leave it there."

class Thief(object):

	def __init__(self, name, weapon, armor, hitpoints = 50):
		self.name = name
		self.weapon = weapon
		self.armor = armor
		self.type = "thief"
		self.hitpoints = hitpoints

	def pickUpWeapon(self, weapon):
		if weapon.damage >= self.weapon.damage:
			if weapon.weapon in ("blow gun", "dagger", "throwing knives"):
				print "You pick up the enemy's %s" % weapon.weapon
				self.weapon = weapon
			else:
				print "You can not use the %s, since you don't posses the skills to use it." % weapon.weapon
		else:
			print "You decide to leave the %s there as it is inferior to your %s" % (weapon.weapon, self.weapon.weapon)

	def pickUpArmor(self, armor):
		if self.armor <= armor.protection:
			print "You pick up the enemy's %s" % self.armor.armor
			self.armor = armor
		else:
			print "Your armor is superior to the enemy's armor, so you leave it there."
