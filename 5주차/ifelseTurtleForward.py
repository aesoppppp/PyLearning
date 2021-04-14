import turtle
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.shapesize(3, 3)

while True:
    cmd = input("명령을 입력하시오: ")
    if cmd == "l":
        t.left(90)
        t.fd(100)
    if cmd == "r":
        t.right(90)
        t.fd(100)
    if cmd == "x":
        break
