numlist = []
for i in range(5):
    numlist.append(int(input('점수를 입력하시오: ')))
avg = sum(numlist) / len(numlist)

print(avg)
print(f'평균 = {avg}')
