import random

x = random.randint(1, 100)
y = random.randint(1, 100)
s = x - y

answr = int(input(str(x) + "-" + str(y) + "="))

if answr == s:
    print("맞았습니다.")
else:
    print("틀렸습니다.")