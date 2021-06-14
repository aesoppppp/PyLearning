from tkinter import *


def btnclick():
    print("Hello World!")


root = Tk()
btn = Button(root, text='Click!', command=btnclick)
btn.pack()
root.mainloop()
