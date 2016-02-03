# This Python script tests all of the different definitions

# and
boolean = True and False
print boolean 
print "\n"

#as? Not sure how the "with-as" works

# assert
test = 5
assert (test == 5), "This is not correct"

print "If you are reading this then the assertion is correct."
print "\n"

# break
loop = 0
while True:
	if loop < 5:
		loop += 1
		print "loop = %d" % loop
	else:
		print "Here is the break."
		print "\n"
		break


# class
class Person(object):
	object = ' "test_variable" '
	print "Here is the person class with a passed in variable that = %s" % object
	print "\n"
	
# continue
var = 9
while var < 15:
	var += 1
	if var == 13:
		print "13 is unlucky, so we are skipping it."
		continue
	print "The current number is %d" % var
print "We are all done."
print "\n"

# definition
def my_first_definition():
	print "This is my first definition with zero passed in variables."
	print "\n"

my_first_definition()

# delete
list = [1, 2, 3, 4, 5]
print "List = %s" % list

del list[0]

print "Here is the list with the first number deleted: %s" % list
print "\n"

# elif
print "This is a test of the elif statement"
test = 2

if test == 1:
	print "Test equals 1."
elif test == 2:
	print "Test equals 2."
else:
	print "Test equals %s." % test
print "\n"

# else
print "This is a test of the else statement."
test2 = 2

if test2 != 2:
	print "test2 = %d" % test2
else:
	print "test2 = 2."
print "\n"

# except
while True:
	try:
		x = int(raw_input("Please enter a number: "))
		break
	except ValueError:
		print "That is not a valid number.  Please try again."
print "\n"

# exec
print "This is the exec definition."
exec 'print "Hello all of you who are reading this!" '
print "\n"

# finally
def divide_by_zero(x, y):
	print "This is the finally definition."
	try:
		answer = x / y
	except ZeroDivisionError:
		print "You have divided by zero."
	else:
		print "Your answer is: %d" % answer
	finally:
		print "This is the 'finally' statement executing."
	print "\n"

divide_by_zero(1, 0)

divide_by_zero(2, 1)