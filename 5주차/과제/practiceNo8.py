import turtle
t = turtle.Turtle()
t.shape("turtle")

x1 = int(input("큰 원의 중심좌표 x1: "))
y1 = int(input("큰 원의 중심좌표 y1: "))
r1 = int(input("큰 원의 반지름: "))

x2 = int(input("작은 원의 중심좌표 x2: "))
y2 = int(input("작은 원의 중심좌표 y2: "))
r2 = int(input("작은 원의 반지름: "))

distance = (((x1 - x2) **2) + ((y1 - y2) **2)) ** 0.5

t.penup()
t.goto(x1, y1)
t.pendown()
t.circle(r1)

t.penup()
t.goto(x2, y2)
t.pendown()
t.circle(r2)

if distance + r2 < r1:
    t.write("두번째 원이 첫번째 원의 내부에 있습니다.")
elif distance < (r1 + r2):
    t.write("두번째 원이 첫번째 원에 걸쳐있습니다.")
else:
    t.write("두번째 원이 첫번째 원의 밖에 있습니다.")

turtle.done()