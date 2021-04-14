import turtle
t = turtle.Turtle()
t.shape("turtle")

ls = []
color = input("색상 #1을 입력하시오: ")
ls.append(color)
color = input("색상 #2을 입력하시오: ")
ls.append(color)
color = input("색상 #3을 입력하시오: ")
ls.append(color)

t.fillcolor(ls[0])
t.begin_fill()
t.circle(50)
t.end_fill()
t.penup()
t.goto(100,0)

t.pendown()
t.fillcolor(ls[1])
t.begin_fill()
t.circle(50)
t.end_fill()
t.penup()
t.goto(200,0)

t.pendown()
t.fillcolor(ls[2])
t.begin_fill()
t.circle(50)
t.end_fill()
