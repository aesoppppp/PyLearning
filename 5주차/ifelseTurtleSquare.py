import turtle
t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("", "도형을 입력하시오: ")
if s == "사각형":
    w = turtle.numinput("", "가로: ")
    h = turtle.numinput("", "세로: ")
    t.fd(w)
    t.left(90)
    t.fd(h)
    t.left(90)
    t.fd(w)
    t.left(90)
    t.fd(h)
    
