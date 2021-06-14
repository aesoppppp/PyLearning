class Car:
    def drive(self):  # 함수 정의
        self.speed = 10


myCar = Car()  # 객체 생성
myCar.color = "blue"  # 변수 생성
myCar.model = "E-Class"

myCar.drive()
print(myCar.speed)
