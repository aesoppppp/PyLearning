import math
import turtle

t = turtle.Turtle()
t.shape("turtle")
t.pencolor("orange")

for i in range(360):
    sine = math.sin(3.14 * i / 180.0)
    t.goto(i, sine * 100)

turtle.done()
