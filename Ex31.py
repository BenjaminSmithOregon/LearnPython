print  " You enter a dark room with two doors marked with a 1 and a 2....then you turn around and see there is another door behind you marked with a 666 and there is a rope swinging from above....wait there is something on the floor.  You examine it closer and realize that there is a line on the floor and as you follow it, you realize it makes the shape of a square.  Then you see a handle.  It is a trapdoor.  Do you open door 1, 2, 666, the trapdoor, or do you climb the rope?"

# Change here

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheesecake.  What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	print "3. Shoot the bear."
	print "4. Talk to the bear calmly."
	print "5. Ride around on its cub's back while shining the bear on"
	
	bear = raw_input("> ")
	
	if bear =="1":
		print "The bear eats your face off.  God job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	elif bear == "3":
		print "The bear falls dead on the floor.  I hope you are happy, animal hater!"
	elif bear == "4":
		print "The bear looks at you, then looks at the cheesecake, then back at you and decides you look more delicious than the cake and eats you.  Good job, some bear whisperer you are!"
	elif bear == "5":
		print "The bear starts charging and you pull out your revolver and shoot it between the eyes.  You then decide to skin it on the spot and dance around with it's freshly peeled flesh wrapped around you and yell into the sky, 'I have won!'  You really are one sick individual...but one alive sick individual :)"
	else:
		print "Well, %sing is probably better.  The bear runs away, and you are left alone." % bear
		
elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothes pins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello.  Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck.  Good job!"
	
elif door == "666":
	print "You open the door and your are engulfed in a giant fireball as you descend into the fiery abyss that is hell and realize that you are damned to a life of eternity in the lake of fire and brimstone and to live in constant pain, agony, and suffering.  Bet you were wishing you would have tried the rope instead, huh?"
	
elif door == "the trapdoor" or door == "trapdoor":
	print "As you open the trapdoor, you see that there is a slide that curves out of your sight and there seems to be a light emitting from around the corner.  What do you do?"
	print "1. Close the trapdoor and try another option?"
	print "2. Slide down the slide."
	
	trapdoor = raw_input("> ")
	
	if trapdoor == "1":
		print "There are no other options.  Good try though....bye bye."
	else:
		print "You descend down the tube curving right and then to the left and then you slide into a giant pool of balls.  The bright light in the room begins to dim slowly, and you are greeted by the ghost of Christmas present.  You are toured around your present life in order to reflect on how you are living.  You come back to reality and decide to change your life.  Congratulations!"
	
elif door == "the rope" or "climb the rope" or "rope":
	print "You climb the rope higher and higher and higher.  You finally ascend above into the outside.  You have escaped the dark labyrinth of rooms and doors that you have been trying to escape for the past decade.  Your misery is over and now it is time to pick life back up where you left off and write a book about your experience and....wait, how did you get here anyway..."
else:
	print "That is not an option.  You stumble around and fall on a knife and die.  Good job!"
	