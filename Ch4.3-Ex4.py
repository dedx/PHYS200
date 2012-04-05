#
# ThinkPython Section 4.3, Exercise 4
#
# J.L.Klay
# 05-Apr-2012
#
# 4. Write a function called circle that takes a turtle, t, and
# radius, r, as parameters and that draws an approximate circle by
# invoking polygon with an appropriate length and number of
# sides. Test your function with a range of values of r.
#
# Hint: figure out the circumference of the circle and make sure that
# length * n = circumference.
#
# Another hint: if bob is too slow for you, you can speed him up by
# changing bob.delay, which is the time between moves, in
# seconds. bob.delay = 0.01 ought to get him moving.
#

from TurtleWorld import *
import math

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

# Function to take a turtle and use it to draw a circle
def circle(t,radius):
    circumference = 2.0*math.pi*radius
    n = 50 #pick a number
    len = circumference/n;
    polygon(t,len,n)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
radius = 50.
circle(bob,radius)

radius = 10.
circle(bob,radius)

radius = 100.
circle(bob,radius)

wait_for_user()
