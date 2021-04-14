import turtle
t = turtle.Turtle()
t.speed(0)
t.pencolor("red")

for i in range(10):
    t.forward(-100)
    t.lt(36)
    t.forward(100)
    t.lt(36)
    t.forward(-100)
    t.lt(36)
    t.forward(100)
    t.lt(36)
    t.forward(-100)
    t.rt(134)

turtle.done()
