#
# ThinkPython Section 4.3, Exercise 1
#
# J.L.Klay
# 05-Apr-2012
#
# 1. Write a function called square that takes a parameter named t,
# which is a turtle. It should use the turtle to draw a square.
#
# Write a function call that passes bob as an argument to square, and
# then run the program again.
#

from TurtleWorld import *

# Function to take a turtle and use it to draw a square
def square(t):
    for i in range(4):
    	fd(t,100)
	lt(t)


world = TurtleWorld()
bob = Turtle()
square(bob)
