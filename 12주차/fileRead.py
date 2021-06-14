"""
infile = open("phones.txt", "rt", encoding='UTF8')  # r은 읽기 모드, w는 쓰기 모드, a는 추가 모드, r+는 읽기와 쓰기 모드
lines = infile.read()
print(lines)

infile.close()
"""

with open("phones.txt", "rt", encoding='UTF8') as infile:
    lines = infile.read()
    print(lines)
print("============")

# 한줄만
with open("phones.txt", "rt", encoding='UTF8') as infile:
    lines = infile.readline()
    print(lines)
print("============")

# 한줄만 반복문
with open("phones.txt", "rt", encoding='UTF8') as infile:
    while True:
        lines = infile.readline()
        if not lines:
            break
        print(lines)
print("============")

# 전체
with open("phones.txt", "rt", encoding='UTF8') as infile:
    lines = infile.readlines()
    print(lines)
