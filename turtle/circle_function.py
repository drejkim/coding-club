import math
import turtle

# Create the window
wn = turtle.Screen()

# Create our turtle... his name is Alex
alex = turtle.Turtle()

# Create a function for drawing a circle
def draw_circle(x, y, color):
    alex.pencolor(color)

    # The function will always draw a circle with radius of 50
    r = 50

    # The circle's center should be (x, y)
    alex.penup()
    alex.setposition(x, y+r)

    # Use the built-in function to draw the circle
    alex.pendown()
    alex.circle(r)

# ----- Test our function here -----
draw_circle(-120, 0, 'blue')
draw_circle(0, 0, 'black')
draw_circle(120, 0, 'red')
draw_circle(-60, -50, 'yellow')
draw_circle(60, -50, 'green')

# Close window by clicking on it
wn.exitonclick()