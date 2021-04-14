import turtle

t = turtle.Turtle()
t.shape("turtle")

t.speed(0)
t.color('red', 'yellow')  # 도형의 선 색상을 red로, 채우기 색상을 yellow로 설정
t.begin_fill()  # 속이 채워진 도형을 그림

while True:
    t.fd(200)
    t.left(170)
    if abs(t.pos()) < 1:  # 터틀이 시작 위치보다 1미만 떨어져 있을 때
        break

t.end_fill()
turtle.done()

# If the turtle position is less than 1 unit away, the while statement terminates and the end_fill() statement
# executes to complete the yellow color fill.
