from tkinter import *

root = Tk()

l1 = Label(root, text='화씨')
l2 = Label(root, text='섭씨')
l1.pack()
l2.pack()

e1 = Entry(root)
e2 = Entry(root)
e1.pack()
e2.pack()

b1 = Button(root, text='화씨->썹씨')
b2 = Button(root, text='섭씨->화씨')
b1.pack()
b2.pack()

root.mainloop()
