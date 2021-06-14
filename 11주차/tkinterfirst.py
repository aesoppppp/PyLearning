from tkinter import *

root = Tk()  # 윈도우(컨테이너) 생성
root.geometry('300x200+50+50')  # 너비x높이+x+y
btn = Button(root, text="Click!")
btn.pack()  # 붙여넣기

root.mainloop()  # 무한루프가 돌며 사용자의 이벤트(마우스 클릭, 키보드 클릭)처리
