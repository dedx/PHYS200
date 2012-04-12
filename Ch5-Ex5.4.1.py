#
# ThinkPython Exercise 5.4.1
#
# J.L.Klay
# 12-Apr-2012
#
# Exercise 5.4 To draw a Koch curve with length x, all you have to do
# is
# 1. Draw a Koch curve with length x/3. 
# 2. Turn left 60 degrees.
# 3. Draw a Koch curve with length x/3. 
# 4. Turn right 120 degrees.
# 5. Draw a Koch curve with length x/3. 
# 6. Turn left 60 degrees.
# 7. Draw a Koch curve with length x/3.
#
# The only exception is if x is less than 3. In that case, you can just
# draw a straight line with length x.
#
# 1. Write a function called koch that takes a turtle and a length as
# parameters, and that uses the turtle to draw a Koch curve with the
# given length.
#

from TurtleWorld import *

def koch(t, length): 
    """takes a turtle and a length as parameters, and uses 
    the turtle to draw a Koch curve with the given length.
    """
    angle = 60
    if (length < 3):
       fd(t,length)
    else:
       koch(t,length/3)
       lt(t,angle)
       koch(t,length/3)
       rt(t,2*angle)
       koch(t,length/3)
       lt(t,angle)
       koch(t,length/3)

#call the koch function to create a pretty fractal:
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.001
length = 300
pu(bob)
bk(bob,150) #start at the left of canvas
pd(bob)
koch(bob,length)
pu(bob)
fd(bob,50) #get bob out of the way
pd(bob)

wait_for_user()
