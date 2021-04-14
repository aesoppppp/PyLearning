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

for i in range(3):
    t.fillcolor(ls[i])
    t.pendown()
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.penup()
    if(i<2):
        t.goto(100*(i+1),0)
    else:
        break
turtle.done()