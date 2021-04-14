import random

a = random.randint(1, 9)
b = random.randint(1, 9)
answer = a * b
guess = 0

while answer != guess:
    guess = int(input(f"{a}*{b}는 "))

print("맞았습니다.")