
    """
    File: turtle.py

    Copyright (c) 2016 Lauren Graziani

    License: MIT

    Creating a program that inputs a graphic window and draws a polygon based on user inputs
    """


import turtle
bob = turtle.Pen()

n = raw_input("Enter number of sides:")
n = int(n)
side_len = raw_input("Enter length of each side:")
side_len = int(side_len)


for i in range (n):
    bob.forward(side_len)
    bob.left(360.0/n)


stopper = raw_input("Hit <enter> to quit.")
