import random
counters = [0, 0, 0, 0, 0, 0]

for _ in range(1000):
    value = random.randint(0, 5)
    counters[value] += 1

for i in range(6):
    print(f'주사위가 {i+1}인 경우는 {counters[i]}')
