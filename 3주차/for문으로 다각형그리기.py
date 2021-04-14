import turtle
t = turtle.Turtle()
t.shape("turtle")

n = int(input("몇각형을 그리시겠어요? (3-6): "))
a = int(input("당신의 이름을 몇 번 출력할까요: "))

for i in range(n):
    t.fd(100)
    t.lt(360 // n)

for _ in range(a):
    print("이동민")

for _ in range(3):
    print("굿")

