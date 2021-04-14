x = int(input("첫 번째 정수를 입력하세요: "))
y = int(input("두 번째 정수를 입력하세요: "))

# y= input("y = ") 이라 입력했다면 y = int(y) 라 하면 된다.
# int() 함수에 실수를 입력한다면 ValueError 이 발생한다.
# 이를 해결하기 위해서는 eval() 함수를 이용한다.

sum = x+y
print(x, "과", y, "의 합은", sum, "입니다.")
