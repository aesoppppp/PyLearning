import turtle
t = turtle.Turtle()
t.shape("turtle")

t.speed(0)
t.left(30)

for i in range(6):
    t.fd(100); t.fd(-30); t.left(60); t.fd(30); t.fd(-30);
    t.right(120); t.fd(30); t.fd(-30); t.left(60); t.fd(-70); t.left(60);

t.left(60)
turtle.done()
