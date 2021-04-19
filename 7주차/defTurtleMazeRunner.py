import random
import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

def draw_maze(x, y):
    for i in range(2):
        t.penup()
        if i == 1:
            t.goto(x+100, y+100)
        else:
            t.goto(x, y)
        t.pendown()
        t.fd(300)
        t.rt(90)
        t.fd(300)
        t.lt(90)
        t.fd(300)


def turn_left():
    t.lt(10)
    t.fd(10)


def turn_right():
    t.rt(10)
    t.fd(10)


screen = turtle.Screen()
draw_maze(-30, 200)
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

t.penup()
t.goto(-300, 250)
t.speed(1)
t.pendown()

screen.listen()  # 계속해서 키보드가 눌러지는 것을 방지하고자 키보드 이벤트 감지
screen.mainloop()  # turtle.done() 과 비슷, 키보드가 계속 눌러지더라도 작동하며 화면이 사라지지 않도록
