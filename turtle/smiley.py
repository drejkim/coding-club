import turtle

# Create the window
wn = turtle.Screen()

# Speed up the drawing...
wn.tracer(10, 0)

# Create our turtle... his name is Alex
alex = turtle.Turtle()

# ----- Draw the face -----
alex.penup()
alex.setposition(0, 200)
alex.pendown()

sides = 1440
side_length = 1
angle = 0.25

n = 0
while n < sides:
    alex.forward(side_length)
    alex.right(angle)
    n += 1

# ----- Draw the left eye -----
alex.penup()
alex.setposition(-100, 100)
alex.pendown()

sides = 180
side_length = 1
angle = 2

n = 0
while n < sides:
    alex.forward(side_length)
    alex.right(angle)
    n += 1

# ----- Draw the right eye -----
alex.penup()
alex.setposition(100, 100)
alex.pendown()

sides = 180
side_length = 1
angle = 2

n = 0
while n < sides:
    alex.forward(side_length)
    alex.right(angle)
    n += 1

# ----- Draw the mouth -----
alex.penup()
alex.setposition(115, -50)
alex.pendown()

# Change the turtle's orientation... why?
alex.setheading(270)

sides = 360
side_length = 1
angle = 0.5

n = 0
while n < sides:
    alex.forward(side_length)
    alex.right(angle)
    n += 1

# Close window by clicking on it
wn.exitonclick()