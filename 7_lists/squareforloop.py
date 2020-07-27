import turtle

t = turtle.Turtle()
t.pensize(3)

colors = ["red", "green", "blue", "magenta"]
for color in colors:
    t.pencolor(color)
    t.right(90)
    t.forward(100)

turtle.done()