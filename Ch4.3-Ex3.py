#
# ThinkPython Section 4.3, Exercise 3
#
# J.L.Klay
# 05-Apr-2012
#
# 3. The functions lt and rt make 90-degree turns by default, but you
# can provide a second argument that specifies the number of
# degrees. For example, lt(bob, 45) turns bob 45 degrees to the left.
#
# Make a copy of square and change the name to polygon. Add another
# parameter named n and modify the body so it draws an n-sided regular
# polygon. Hint: The exterior angles of an n-sided regular polygon are
# 360.0/n degrees.
#

from TurtleWorld import *

# Function to take a turtle and use it to draw a square
def square(t,len):
    for i in range(4):
    	fd(t,len)
	lt(t)

# Function to take a turtle and use it to draw a polygon
def polygon(t,len,n):
    for i in range(n):
    	fd(t,len)
	angle = 360.0/n
	lt(t,angle)


world = TurtleWorld()
bob = Turtle()
length = 50
n = 6
polygon(bob,length,n)

wait_for_user()
