import turtle

# Create the window
wn = turtle.Screen()

# Create our turtle... his name is Alex
alex = turtle.Turtle()

# Create a function for drawing a line
def draw_line(x1, y1, x2, y2):
    alex.penup()
    alex.setposition(x1, y1)
    alex.pendown()
    alex.setposition(x2, y2)

# ----- Test our function here -----
draw_line(-50, 0, 0, 100)
draw_line(0, 0, 25, -50)

# Close window by clicking on it
wn.exitonclick()