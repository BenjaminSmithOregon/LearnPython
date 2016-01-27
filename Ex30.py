people = 30
cars = 40
trucks = 15

# this compares cars to people, if cars are greater than people, then print the first line
if cars > people:
	print "We should take the cars."
# This compares to see if there are more people than cars, if true, then the line prints
elif cars < people:
	print "We should not take the cars."
# If cars and people are equal, then this line prints
else:
	print "We can't decide."

# Compares trucks to cars, if there are more trucks, then the first line prints out	
if trucks > cars:
	print "That's too many trucks."
# compares trucks to cars, if there are more cars, then this line prints out
elif trucks < cars:
	print "Maybe we could take the trucks."
# if cars and trucks are equal then this line prints out
else:
	print "We still can't decide."

# compares people to trucks, if people are greater, then the line below prints 	
if people > trucks:
	print "Alright, let's just take the trucks."
# if trucks and people are equal, then this line prints out.	
else:
	print "Fine, let's stay home then."