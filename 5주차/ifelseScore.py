x = int(input("성적을 입력하세요: "))
y = int(input("기준 성적을 입력하세요: "))
if(x>=y):
    print("성적이", str(y), "점을 넘기므로 합격입니다.")
else:
    print("성적이", str(y), "점을 넘기지 못하므로 불합격입니다.")
