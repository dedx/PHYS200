#
# ThinkPython Chapter 4
#
# J.L.Klay
# 03-Apr-2012
#

for i in range(4):
    print 'Hello!'

from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob

for i in range(4):
    fd(bob, 100)
    lt(bob)

wait_for_user()
