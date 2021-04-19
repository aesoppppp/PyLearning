import turtle
t = turtle.Turtle()


def n_polygon(n, length):
    for i in range(n):
        t.fd(length)
        t.lt(360//n)


for i in range(10):
    t.lt(20)
    n_polygon(6, 100)

turtle.done()
