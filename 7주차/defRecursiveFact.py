def fact(n):
    if n == 1:
        return 1
    return fact(n-1) * n

a = int(input("몇 팩토리얼 입니까: "))
print(fact(a))
