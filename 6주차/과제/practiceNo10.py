import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

for _ in range(5):
    t.fd(100)
    t.right(90)
    t.fd(10)
    t.right(90)
    t.fd(100)
    t.left(90)
    t.fd(10)
    t.left(90)

turtle.done()
