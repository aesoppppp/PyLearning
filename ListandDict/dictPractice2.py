diction = {'Name': '홍길동', 'Age': '20', 'Class': '초급'}
print(diction['Name'])
print(diction['Age'])

for key in sorted(diction.keys()):  # sorted 는 정렬을 해주는 함수
    print(key, diction[key])
