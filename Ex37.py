# This Python script tests all of the different functions/definitions

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
	print "Here is the Person class with a passed in variable that = {}".format(object)
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

# function
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
	except ValueError as ex:
		message = ex.message
		print "That is not a valid number.  Your error is: %s.  Please try again." % message
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

# for
print "This is the for loop."
for number in [1, 2, 3, 4 ,5]:
	print "The current number is: ", number	
print "\n"

# from
# Not really sure how to implement this

# global
def global_func():
	global var
	print var
	var = "This is the new GLOBAL var."
	print var

var = "This is the INITIAL var."	
global_func()
print var
print "\n"

# if
x = 7
y = 6
print "X is %d, Y is %d." % (x, y)

if x > y:
	print "X IS greater than Y"
else:
	print "X is NOT greater than Y."
print "\n"	
	
# import
import os

print "This is showing that I have imported the 'os' module"
print "\n"

# in
print "This is the in definition"
for test in 'test':
	print "This is the letter %s that I have pulled from test." % test
print "\n"

# is
print "This is the 'is' definition."
print "100 is 100", 100 is 100 
print "100 is 101", 100 is 101
print "\n"

# lambda
print "This is the lambda function."
print "passing in 2 to the lambda and squaring it to get..."
squared = lambda x: x ** x
print squared(2)
print "\n"

# not
print "This is the NOT function."
print "not True = ", not True
print "\n"

# or
print "This is the OR function."
print "True or False = ", True or False
print "\n"

# pass
print "This is the pass function."
for letter in 'pass':
	if letter == 'a':
		pass
		print "This is the pass line."
	print "The current letter is %s." % letter
print "\n"

# print
print "This is the print function."
print "You are now seeing what I am telling to print."
print "\n"

# raise
# Not really sure how to use the raise statement

# return
print "This is the return statement."

def return_func(a, b):
	test = a + b
	return test

print return_func(5, 5)
print "\n"

# try
print "This is the try function."
try:
	print 5 > t
except:
	print "That is not correct."
print "\n"

# while
print "This is the while loop."
number = 0
while number < 5:
	print number
	if number < 5:
		number += 1
print "This is the end of the loop."
print "\n"

#with
print "This is the with statement."
print "opening file..."
with open('Ex37.txt') as x:
	output = x.read()
	print output
print "Closing file..."
print "\n"

#yield
#I am not quite sure how this is working, but I understand somewhat what it is doing.
print "This is the yield function."
def is_prime(number):
	if number > 1:
		if number == 2:
			return True
		if number % 2:
			return False
		for current in range(3, int(math.sqrt(number) + 1), 2):
			if number % current == 0:
				return False
		return True
	return False
			
def get_primes(number):
	while True:
		if is_prime(number):
			number = yield number
		number += 1
		
print get_primes(11)
