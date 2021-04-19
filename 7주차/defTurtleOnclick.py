import turtle


t = turtle.Turtle()
t.shape("turtle")
t.pensize(10)

def draw(x, y):
    t.goto(x, y)


s = turtle.Screen()
s.onscreenclick(draw)
