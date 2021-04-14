import turtle
import random

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

for i in range(10):
    r = random.randint(1, 100)
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(r)

turtle.done()
