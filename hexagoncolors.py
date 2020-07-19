import turtle

t = turtle.Turtle()
t.pensize(3)

x = 0
while x < 6:
    if x % 2 == 0:
        t.pencolor("orange")
    else:
        t.pencolor("purple")

    t.right(60)
    t.forward(100)
    x = x + 1

turtle.done()