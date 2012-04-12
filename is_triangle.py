#
# ThinkPython Exercise 5.3.2
#
# J.L.Klay
# 12-Apr-2012
#
# Exercise 5.2 If you are given three sticks, you may or may not be
# able to arrange them in a triangle. For example, if one of the
# sticks is 12 inches long and the other two are one inch long, it is
# clear that you will not be able to get the short sticks to meet in
# the middle. For any three lengths, there is a simple test to see if
# it is possible to form a triangle:
#
# "If any of the three lengths is greater than the sum of the other
# two, then you cannot form a triangle. Otherwise, you can."
#
# 1. Write a function named is_triangle that takes three integers as
# arguments, and that prints either "Yes" or "No," depending on
# whether you can or cannot form a triangle from sticks with the given
# lengths.
#
# 2. Write a function that prompts the user to input three stick
# lengths, converts them to integers, and uses is_triangle to check
# whether sticks with the given lengths can form a triangle.
#

def is_triangle(a=1,b=2,c=3):
    """Takes three integer arguments (a,b,c) and checks whether a
    triangle can be created using these as the sides by comparing sums of two
    sides with the length of the third.
    """
    aandb=a+b
    bandc=b+c
    aandc=a+c
    if (a > bandc or b > aandc or c > aandb):
        print "No, these will not form a triangle"
    elif (a == bandc or b == aandc or c == aandb):
        print "Wow! You made a degenerate triangle!"
    else:
        print "Yes, these will form a triangle"


prompta = int(raw_input("Input three integers representing the lengths of three sticks, each one on a new line\n"))
promptb=int(raw_input())
promptc=int(raw_input())

#print prompta, " ", promptb, " ", promptc

is_triangle(prompta,promptb,promptc)
