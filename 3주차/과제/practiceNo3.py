number = int(input("정수를 입력하시오: "))

first = number % 10
second = number // 10 % 10
third = number // 10 // 10 % 10
forth = number // 10 // 10 // 10 % 10

"""print(first)
print(second)
print(third)
print(forth)"""


sum = first + second + third + forth
print("자리수의 합:", sum)
