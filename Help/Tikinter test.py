from tkinter import *
from tkinter import ttk




topleft = 0
topmid = 0
topright = 0
middleleft = 0
middle = 0
middleright = 0
bottomleft = 0
bottommid = 0
bottomright = 0



root = Tk()
frm = ttk.Frame(root, padding=400)



frm.grid()
ttk.Label(frm, text="Tic Tac Toe").grid(column=1, row=0)
ttk.Button(frm, text=0, command=root.destroy).grid(column=0, row=1)
ttk.Button(frm, text=0, command=root.destroy).grid(column=0, row=2)
ttk.Button(frm, text=0, command=root.destroy).grid(column=0, row=3)
ttk.Button(frm, text=0, command=root.destroy).grid(column=1, row=1)
ttk.Button(frm, text=0, command=root.destroy).grid(column=1, row=2)
ttk.Button(frm, text=0, command=root.destroy).grid(column=1, row=3)
ttk.Button(frm, text=0, command=root.destroy).grid(column=2, row=1)
ttk.Button(frm, text=0, command=root.destroy).grid(column=2, row=2)
ttk.Button(frm, text=0, command=root.destroy).grid(column=2, row=3)





root.mainloop()