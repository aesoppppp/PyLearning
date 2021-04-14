import time
 
fseconds = time.time() // 60 #전체 분
minute = fseconds % 60 #현재 분
hour = fseconds // 60 % 24 #현재 시

print("현재 시간(영국 그리니치 시각):", int(hour), "시", int(minute), "분")
