import turtle

# Create the window
wn = turtle.Screen()

# Create our turtle... his name is Alex
alex = turtle.Turtle()

# ----- Draw a star -----
sides = 5
side_length = 100
angle = 144

n = 0
while n < sides:
    alex.forward(side_length)
    alex.right(angle)
    n += 1

# Close window by clicking on it
wn.exitonclick()