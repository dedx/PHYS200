#
# ThinkPython Section 4.3, Exercise 2
#
# J.L.Klay
# 05-Apr-2012
#
# 2. Add another parameter, named length, to square. Modify the body
# so length of the sides is length, and then modify the function call
# to provide a second argument. Run the program again. Test your
# program with a range of values for length.
#

from TurtleWorld import *

# Function to take a turtle and use it to draw a square
def square(t,len):
    for i in range(4):
    	fd(t,len)
	lt(t)


world = TurtleWorld()
bob = Turtle()
length = 50
square(bob,length)
length = 100
square(bob,length)
length = 150
square(bob,length)

wait_for_user()
