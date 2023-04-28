from tkinter import *
from tkinter import ttk


root = Tk()
frm = ttk.Frame(root, padding=400)


global counter
counter = 0

def click():
    global counter
    counter += 1
    mButton1.config(text = counter)

mButton1 = Button(text = counter, command = click, fg = "darkgreen", bg = "white")
mButton1.pack()

root.mainloop()
