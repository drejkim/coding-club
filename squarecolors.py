import turtle

t = turtle.Turtle()

x = 0
while x < 4:
    if x == 1:
        t.pencolor("red")
    # else:
    #     t.pencolor("black")

    t.right(90)
    t.forward(100)
    x = x + 1

turtle.done()