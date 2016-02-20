class Scene(object):

	def enter(self):
		pass
		
	
class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
		pass
		
	def play(self):
		print "You start in the %s of the ship." % a_map.start_scene
		print "A Gothon stands in front of you, and you can defeat"
		print "him by telling him a joke. \n"
		
		joke = raw_input("> ")
		
		if len(joke) >= 4:
			print "That was a great joke!  You have killed the Gothon."
			print "You step over his dead body and make your way"
			print "to the next room."
			print "\n"
			hall = CentralCorridor()
			hall.enter()
			
		else:
			print "That was a terrible joke!  The Gothon approaches you rapidly..."
			death = Death()
			death.enter()
		
		
class Death(Scene):

	def enter(self):
		print "The Gordon swallows you whole and spits you back out."
		print "Apparently, you taste horrible.  It stares at you intensely"
		print "then proceeds to turn you into dust with its laser vision."
		print "Better luck next time, dust bunny."
		
	def explode(self):
		print "The cabinet self destructs leaving your torso now separated"
		print "from your cerebral cortex."
		print "Next time put your head to better use."
		
	def hammer(self):
		print "You have chosen poorly.  He proceeds to knock on your skull"
		print "with his 10 pound hammer and performs a lobotomy."
		print "Next time try knocking on the door labelled \"your mom.\""
		print "\n"
		
		
class CentralCorridor(Scene):

	def enter(self):
		print "You walk down the corridor and take your first left."
		print "You come into the armory."  
		armory = LaserWeaponArmory()
		armory.enter()

class LaserWeaponArmory(Scene):

	def enter(self):
		print "There is a cabinet across"
		print "the room that contains bombs in it.  You walk over to"
		print "to the cabinet and find a coded lock.  There are"
		print "numbers 1 through 9 on the key pad.  The lock only"
		print "requires one number to be input in order to unlock it"
		print "....but if you enter the wrong number the cabinet self"
		print "destructs. \n"
		
		code = 3
		print "Enter the code: "
		entered = int(raw_input("> "))
		print entered
		print code
		print code == entered
		
		if entered == code:
			print "You have chosen wisely.  The lock on the cabinet opens."
			print "You take one of the bombs and tuck it under your arm."
			print "Now to plant the bomb and escape to the planet below."
			print "You head for the door and... \n"
			bridge = TheBridge()
			bridge.enter()

		else:
			print "You press %s on the lock and a little red LED starts to" % input
			print "blink. Then it starts making an audible beeping sound"
			print "that gets faster and faster.  You turn and run as you"
			print "realize it is about to self destruct.... \n"
			death = Death()
			death.explode()
		
class TheBridge(Scene):

	def enter(self):
		print "You enter the bridge and come face to face with another Gothon."
		print "You have to pull another joke out of your memory to defeat this one."
		print "He looks like he might be a little hard to defeat...better"
		print "come up with a good one. \n"
		print "Do you go with the knock knock joke or the one about his mom? \n"
		
		loop = False
		
		while loop == False:
			input = raw_input("> ")
		
			if input in ("knock knock", "knock knock joke", "the knock knock joke", "the knock knock"):
				loop = True
				death = Death()
				death.hammer()
				
			elif input in ("the one about his mom", "his mom", "about his mom", "mom", "your mom"):
				loop = True
				print "You chose well.  He laughs so hard he explodes."
				print "You step over his blasted remains and place the bomb"
				print "right on top of the control console.  You set the bomb's"
				print "timer for 5 minutes. \n"
				escape = EscapePod()
				escape.enter()
				
			else:
				print "Try a different joke."
		
class EscapePod(Scene):

	def enter(self):
		print "You run from the bridge and take the lift down to the escape pod room."
		print "You open the hatch door and proceed to power the unit on."
		print "You put on your suit for the surface and sit down and buckle yourself in."
		print "You seal up the hatch as another Gothon enters the escape pod room."
		print "You pull the lever to jetison the pod and the vacuum sucks the Gothon out"
		print "with you.  You blast towards the surface a you watch the Gothon gasping"
		print "for air and drifting out to space.  As your ship slowly fades away it"
		print "blasts into a thousand little fragments.  You wonder to yourself what the"
		print "surface holds for you."
		
		
class Map(object):

	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		self.scene_name = scene_name
		
		if scene_name == Death:
			Death()
		pass
		
	def opening_scene(self):
		print "Your ship is under attack by the dreaded Gothons."
		print "You need to make your way to the escape pod, but"
		print "you need to plant a bomb to destroy the ship first."
		print "\n"
		
		
a_map = Map('central corridor')
a_map.opening_scene()
a_game = Engine(a_map)
a_game.play()