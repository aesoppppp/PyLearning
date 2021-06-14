from tkinter import *

root = Tk()

l1 = Label(root, text='화씨')
l2 = Label(root, text='섭씨')
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(root, text='화씨->썹씨')
b2 = Button(root, text='섭씨->화씨')
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)

root.mainloop()
