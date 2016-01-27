i = 0
numbers = []
increment = 2

def while_loop(i, numbers, increment):
	max = 10
	# while i < max:
	for i in range (0, max):
		print "At the top i is %d" % i
		numbers.append(i)
		
		# i = i + increment
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
		
while_loop(i, numbers, increment)
		
print "The numbers: "
	
for num in numbers:
	print num