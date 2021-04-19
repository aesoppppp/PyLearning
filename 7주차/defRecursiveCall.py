def power2(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    return power2(n-1) * 2

a = int(input("2의 몇 제곱 입니까: "))
print(power2(a))
