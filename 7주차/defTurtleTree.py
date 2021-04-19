import turtle
t = turtle.Turtle()
t.shape("turtle")

t.left(90)

def tree(length):
    if length > 5:
        t.fd(length)
        t.rt(20)
        tree(length-15)
        t.lt(40)
        tree(length-15)
        t.rt(20)
        t.backward(length)


t.color("green")
t.speed(0)
tree(90)

turtle.done
