# These are all of the string formats

# %d
print "This is for integers: %d." % 15
print "\n"

# %i
print "This is also for integers: %i." % 10
print "\n"

# %o 
print "This is for octal numbers: %o." % 100
print "\n"

# %u
print "This is for unsigned numbers: %u." % -100
print "\n"

# %x
print "This is for hexadecimal lower case: %x" % 1001
print "\n"

# %X
print "This is for upper case hexadecimal numbers: %X" % 1001
print "\n"

# %e
print "This is for lower case exponential notation: %e." % 1001
print "\n"

# %E
print "This is for upper case exponential notation: %E." % 1001
print "\n"

# %f OR %F
print "These are both for floating point real numbers: %f and %F." % (10.34, 10.34)
print "\n"

# %g or %G
print """These both do what %e or %f do,""" 
print "but one is upper case and one is lower case: %g and %G." % (10.34, 10.34)
print "\n"

# %c
print "This is a character format: %c." % 100
print "\n"

# %r
print "This is debugging format: %r." % int
print "\n"

# %s
print "This is the string format: %s." % 'hello'
print "\n"

# %%
print "This is a percent sign: %f%%." % 10
print "\n"