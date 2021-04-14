import turtle
t = turtle.Turtle()
t.shape("turtle")

n = int(input("얼마나 그릴까요: "))

for i in range(n):
    t.speed(10)
    t.circle(100)
    t.left(360/n)
