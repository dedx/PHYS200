#
# ThinkPython Exercise 5.3
#
# J.L.Klay
# 12-Apr-2012
#
# Exercise 5.3 Read the following function and see if you can figure
# out what it does. Then run it (see the examples in Chapter 4).
#

from TurtleWorld import *

def draw(t, length, n): 
    if n==0:
       return 
    angle = 50
    fd(t, length*n) 
    lt(t, angle) 
    draw(t, length, n-1) 
    rt(t, 2*angle)
    draw(t, length, n-1) 
    lt(t, angle)
    bk(t, length*n)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
length = 6
n = 6
draw(bob,length,n)

wait_for_user()
