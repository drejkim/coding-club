import turtle

t = turtle.Turtle()

# Modify n to change the number of points in the star!
n = 45

# Based on n, we can automagically update the angle we need.
angle = 180 - 180 / n

for i in range(n):
    if i % 2 == 0:
        t.pencolor("magenta")
    else:
        t.pencolor("blue")

    t.forward(200)
    t.right(angle)

turtle.done()