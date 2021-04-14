b = 0

while True:
    a = int(input("정수를 입력하시오: "))
    b += a
    if a == 0:
        print(f"합은 {b} 입니다.")
        break
