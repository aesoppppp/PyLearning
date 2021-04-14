import random

lotto = random.randrange(100)
myLotto = int(input("복권번호를 입력하시오 (0에서 99사이): "))
print("당첨번호는", lotto, "입니다.")

digit1 = lotto // 10
digit2 = lotto % 10
myDigit1 = myLotto // 10
myDigit2 = myLotto % 10

if digit1 == myDigit1 and digit2 == myDigit2:
    print("상금은 100만원 입니다.")
elif digit1 == myDigit1 or digit2 == myDigit2 or digit1 == myDigit2 or digit2 == myDigit1:
    print("상금은 50만원 입니다.")
else:
    print("복권에 당첨되지 않았습니다.")