import turtle
t = turtle.Turtle()
t.shape("turtle")

s = turtle.numinput("", "나이를 입력하시오: ")
t.write("당신의 나이는 " + str(s)+"살 이군요!")

for i in range(4):
    t.left(90)
    t.fd(100)

turtle.done()
