    ```
    """
    File: turtlestar.py

    Copyright (c) 2016 Lauren Graziani

    License: MIT

    <Creating a program that inputs a graphic window and draws a star based on user inputs>
    """
    ```

import turtle
t = turtle.Pen()

n = raw_input ("Enter number of sides:")
n = int(n)
side_len = raw_input ("Enter length of each side:")
side_len = int(side_len)



for j in range(1):
    for i in range (n):
        t.forward(side_len)
        t.left(163.5)
stopper = raw_input ("Hit enter to quit")
turtle.bye()
