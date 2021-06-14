from tkinter import *
from tkinter import messagebox


def btnclick():
    messagebox.showinfo(title='info', message='Hello world!\nWelcome to Python!')


root = Tk()
root.geometry('300x200+50+50')

btn = Button(root, text='Click!', command=btnclick)
btn.pack()

root.mainloop()
