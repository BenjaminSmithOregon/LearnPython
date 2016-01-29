from sys import exit

def start():
	print "You are aboard a small sailing vessel"
	print "A dark outline comes into view, and as you"
	print "get closer, you realize it is an island."
	print "You sail your vessel into the narrow channel"
	print "and you anchor your boat and swim to the shore."
	print "Upon your arrival at the base of a cliff that stretches"
	print "into the sky, you see a rope leading up the cliff face and"
	print "additionally you see a trail leading off along the face of the cliff."
	print "Do you climb the rope or walk along the narrow path."
	
	while True:
		cliffs = raw_input("> ")
		
		if cliffs in ("climb the rope", "climb rope", "the rope", "climb"):
			rope()
		elif cliffs in ("walk along the narrow path", "walk along the path", "walk the narrow path", "narrow path"):
			path()
		else:
			print "Try something else."
			

def rope():
	print "You climb the rope and get to the top of the cliffs."
	print "You look around and see a narrow path that leads into"
	print "the woods.  You decide to walk down the path.  After a"
	print "while you come across a rope bridge that spans a deep"
	print "narrow canyon with a river at the bottom.  As you look"
	print "to your left you notice a rope swing that could get you"
	print "across the canyon as well.  Do you cross the rope bridge"
	print "or pull a Tarzan and swing across the gorge?"
	
	while True:
		canyon = raw_input("> ")
			
		if canyon in ("cross the rope bridge", "cross the bridge", "the rope bridge", "the bridge", "rope bridge"):
			bridge()
		elif canyon in ("pull a Tarzan", "pull a tarzan", "swing on the rope", "the rope", "swing across the gorge", "swing", "swing across"):
			swing()
		else:
			print "Try something different."
			
	
def path():
	print "You start walking up the path and as you ascend the cliff face"
	print "the path starts to narrow.  You decide to continue on and start"
	print "shimmying along in areas.  At one point it is only narrow enough"
	print "to walk one foot in front of the other.  The loose rock breaks away"
	print "and as you fall to a bloody death you think to yourself, ""why didn't"
	print "I take the rope."
	
	death()

	

def bridge():
	print "You slowly make you way across the rickety rope bridge.  As you get to"
	print "the halfway point, the boards beneath you start to give way.  You decide"
	print "to turn around and make your way back and try the rope.  As you turn the"
	print "board beneath you cracks in half and you fall helplessly into the canyon below."
	print "Thankfully you splash into a deep part of the river and come up gasping for air."
	print "As you gain your breath, the current rushes you down stream as you bob above"
	print "and below the surface of the water you have a chance to grab onto a rock outcropping."
	print "Do you grab onto the rocks or take your chances floating downstream?"
	
	while True:
		rocks = raw_input("> ")
		
		if rocks in ("grab onto the rock outcropping", "grab onto the rocks", "grab the rocks", "grab the rock outcropping"):
			waterfall()
		elif rocks in ("take chance", "take chances", "float downstream", "take your chances floating downstream", "take a chance floating downstream"):
			death2("As you float downstream your clothes get wrapped around a submerged branch and the current sucks you under.  You slowly watch the light fade as the bubbles float over your head from the frothy current.")
		else:
			print "Try something different."
			
			
def swing():
	print "You grab the rope and take a giant running head start as you jump with the rope in your hands.  As"
	print "you float across the bottomless gaping canyon you belt out your best Tarzan roar."
	print "You overshoot your mark on the other side and catch a root with the toe on your right foot."
	print "you let go of the rope and perform what might be the greatest five time somersault"
	print "ever seen.  You exit is a little sloppy, but you manage to land on your feet....Too"
	print "bad no one was around to record that in the record books.  You find where the path"
	print "starts up again and walk for a little longer.  You come into a bright clearing in the trees."
	print "This is the meadow that you have been searching for.  There in the middle is a large stone"
	print "that holds the ancient paintings of Billy the Meek.  You take out your camera, blow off the"
	print "dust and snap your best amateur photograph that you can pull off.  You sit down, take a sip"
	print "from your canteen, and bask in the glory of your accomplishment.  Aren't you awesome?"
	
	win()

def waterfall():
	print "As you grab onto the rocks you are pulled under the water and are sucked into some sort"
	print "of underground tunnel.  You float a ways down the underground stream until you see a"
	print "light up ahead of you.  As you approach the light you start to feel a low rumble in your"
	print "chest.  When you emerge into the light of day the sound of the roar is overwhelming.  You"
	print "look up to see a magnificent waterfall.  You swim to the edge of the water and see a small"
	print "staircase off to the side of the waterfall.  The lead up behind the water.  As you look off"
	print "across the water you see a cave on the other side.  You wonder to yourself, what would be the"
	print "best choice?"
	
	while True:
		waterfall = raw_input("> ")
	
		if waterfall in ("cave", "the cave", "go in the cave", "swim to the cave", "walk in the cave"):
			print "you swim over to the cave and walk inside.  You think to yourself, 'There must be"
			print "something amazing in here.'  As you are daydreaming about the amazing things that"
			print "must be at the end of this cave, a giant spider bites your head off and your lifeless"
			print "body falls to the floor.  Good luck next time :)"
			death()	
		elif waterfall in ("take the stairs", "the stairs", "stairs", "walk up the stairs", "go up the stairs", "climb the stairs"):
			print "You walk up the stairs and behind the waterfall.  You chest is rumbling from the awesomeness"
			print "of the water pouring over the top of the rocks.  You make your way into a small cave towards"
			print "the top.  You emerge into a bright sunny opening and look upon the majestic giant rock that"
			print "house Billy the Meek's ancient paintings!  You run over and embrace the giant rock as you"
			print "have just emerged victorious from the grips of this viscous jungle.  You take out your"
			print "Lifeproof wrapped smartphone and snap your best selfie pic with the ancient paintings."
			print "You have completed what you came here to accomplish.  Well done you amazing person you!"
			win()
		else:
			print "Try something different."
	
	
def death():
	print "Game Over!"
	exit()
	
def death2(message):
	print message, "Game Over!"
	exit()

def win():
	print "You win!"
	exit()
	
start()