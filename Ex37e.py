# +
addition = 3 + 5
print "This is addition: 3 + 5 =", addition
print "\n"

# -
subtraction = 8 - 5
print "This is subtraction: 8 - 5 =", subtraction
print "\n"

# *
multiplication = 2 * 5
print "This is multiplication: 2 * 5 =", multiplication
print "\n"

# /
division = 10 / 5.0
print "This is division: 10 / 5.0 =", division
print "\n"

# **
power = 2 ** 2
print "This is a power function: 2 ** 2 =", power
print "\n"

# //
floor_division = 2 // 4.0
print "This is floor division: 2 // 4.0 =", floor_division
print "\n"

# %
modulus = 10 % 3
print "This is the modulus: 10 % 3 =", modulus
print "\n"

# <
less = 3 < 10
print "This is the less than: 3 < 10 =", less
print "\n"

# >
more = 3 > 10
print "This is the more than: 3 > 10", more
print "\n"

# <=
less_equal = 3 <= 10
print "This is the less than or equal to: 3 <= 10 =", less_equal
print "\n"

# >=
more_equal = 3 >= 10
print "This is the more than or equal to: 3 >= 10 =", more_equal
print "\n"

# ==
equal = 10 == 10
print "This is the equal to: 10 == 10 =", equal
print "\n"

# !=
not_equal = 10 != 10
print "This is the not equal: 10 != 10 = ", not_equal
print "\n"

# <>
not_equal2 = 10 <> 10
print "This is also the equal: 10 <> 10 =", not_equal2
print "\n"

# ()
paren = len('Hello')
print "This is the length of 'hello': ", paren
print "\n"

# []
brackets = [1, 2 ,3]
print "These are brackets: [1, 2, 3] = ", brackets
print "\n"

# {}
braces = {'a':2, 'b':3}
print "These are braces: ", braces
print "\n"

# @ 
# I'm not sure how the decorator works
# @decorator
# def test():
	# return "This is the inside of the test function...aka '@decorator'"
# print "This is a decorator: ", decorator()
# print "\n"

# ,
comma = (0, 1, 2)
print "This shows the use of the comma: ", comma
print "\n"

# .
class Test(object):
	def __init__(self, word='hi', letter='ben'):
		self.letter = letter
	def a(self):
		print self.letter
	def b(self):
		print "b"
	def c(self):
		print "c"

dot = Test(letter='jason')
		
print "This is the dot notation: " 
dot.a()
print "\n"

# =
x = '='
print "This is the equal sign:", x
print "\n"

# ;
print "This is the semicolon: "; print ";"
print "\n"

# +=
x = 1
x += 2
print "This is the add and assign: += =>"; print "x = 1 =>", "x += 2 =>", "x = %d" % x
print "\n"

# -=
y = 1
y -= 2
print "This is the subtract and assign: -= =>"; print "x = 1 =>", "x -= 2 =>", "x = %d" % y
print "\n"

# *=
z = 1
z *= 2
print "This is the multiply and assign: *= =>"; print "x = 1 =>", "x *= 2 =>", "x = %d" % z
print "\n"

# /=
a = 1.0
a /= 2.0
print "This is the divide and assign: /= =>"; print "a = 1 =>", "a /= 2 =>", "a = %d" % a
print "\n"

# //=
b = 1
b //= 2
print "This is the floor divide and assign: //= =>"; print "b = 1 =>", "b //= 2 =>", "b = %d" % b
print "\n"

# %=
c = 1
c %= 2
print "This is the modulus and assign: %= =>"; print "c = 1 =>", "c %= 2 =>", "c = %d" % c
print "\n"

# **=
d = 1
d **= 2
print "This is the power and assign: **= =>"; print "d = 1 =>", "d **= 2 =>", "d = %d" % d
print "\n"