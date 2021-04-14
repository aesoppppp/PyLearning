kg = int(input("물체의 무게를 입력하시오(킬로그램): "))
speed = int(input("물체의 속도를 입력하시오(미터/초): "))

j = 0.5 * kg * speed**2

print("물체는", j, "(줄)의 에너지를 가지고 있다.")
