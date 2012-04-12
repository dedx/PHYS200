#
# ThinkPython Section 4.3, Exercise 5
#
# J.L.Klay
# 05-Apr-2012
#
# 5. Make a more general version of circle called arc that takes an
# additional parameter angle, which determines what fraction of a
# circle to draw. angle is in units of degrees, so when angle=360, 
# arc should draw a complete circle.
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

# Function to take a turtle and use it to draw an arc
def arc(t,radius,angle):
    circumference = 2.0*math.pi*radius
    frac = angle/360.0
    arclength = circumference*frac
    n = 50 # pick a number
    len = arclength/n;
    turnang = angle/n
    for i in range(n):
        fd(t,len)
	lt(t,turnang)
	
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
ray = Turtle()

radius = 100.
angle = 60.
arc(bob,radius,angle)

length = 100.
square(ray,length)

# Note: reason it doesn't draw over itself exactly is because of the
# extra left turn at the end of the loop *I think*

wait_for_user()
