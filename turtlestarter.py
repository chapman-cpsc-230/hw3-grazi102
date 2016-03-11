import turtle

def draw_reg_polygon(t,num_sides, side_len) :
        for i in range (num_sides):
            t.forward(side_len)
            t.left(360.0/num_sides)

# Ask user for input here.

# Now create a graphics window.
bob = turtle.Pen()

#side = 10
bob.left(30)
for j in range (3): #number of sides
    draw_reg_polygon(bob,6,10)
    bob.left (120)
    #side += 5

# Put the rest of your code can go here

# Prevent the graphics window from diappearing too
# quickly to see it.
stopper = raw_input("Hit <enter> to quit.")

# Now remove the graphics window before exiting.
turtle.bye()
"""
#drawing star
for i in range (3):
    t.forward (side_len/3.0)
    t.left (-60)
    t.forward(-60)
    t.left (120.0)
    t.forward(120)
    t.left (-60)
    t.forward(-60)


    t.left(360.0/3)
