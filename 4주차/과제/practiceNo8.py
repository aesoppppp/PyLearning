import turtle
t = turtle.Turtle()
t.shape("turtle")

ls = []
ls.append(int(input("x1: ")))
ls.append(int(input("y1: ")))
ls.append(int(input("x2: ")))
ls.append(int(input("y2: ")))
ls.append(int(input("x3: ")))
ls.append(int(input("y3: ")))

t.goto(ls[0], ls[1])
t.goto(ls[2], ls[3])
t.goto(ls[4], ls[5])
