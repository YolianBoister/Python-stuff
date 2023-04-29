from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=400)

global topleft
topleft = 0

global topmid
topmid = 0


def midtoptoe():
    global topmid
    topmid += 1
    topmidclick.config(text = topmid)

def lefttoptoe():
    global topleft
    topleft += 1
    topleftclick.config(text = topleft)

topleftclick = Button(text = topleft, command= lefttoptoe, fg= "black", bg= "yellow")
topmidclick = Button(text = topmid, commmand= midtoptoe, fg = "black", bg = "red")
topleftclick.pack()
topmidclick.pack()



root.mainloop()