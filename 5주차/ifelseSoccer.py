import random

options = ["왼쪽", "중앙", "오른쪽"]
computer_choice = random.choice(options)
user_choice = input("어디를 수비하시겠어요? (왼쪽, 중앙, 오른쪽): ")

print("공격수가", str(computer_choice) + "으로 공격했습니다!")
if computer_choice == user_choice:
    print("수비에 성공했습니다!")
else:
    print("수비에 실패하셨습니다...")
