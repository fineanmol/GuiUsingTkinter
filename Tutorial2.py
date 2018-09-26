# Tutorial 2 for Buttons in GUI

from tkinter import *

root = Tk()
root.minsize(height=233, width=314)
topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack()
button1 = Button(topframe, text="File", fg="blue")
button1.pack(side=LEFT)
button2 = Button(topframe, text="Edit", fg="blue")
button2.pack(side=LEFT)
button3 = Button(topframe, text="View", fg="blue")
button3.pack(side=LEFT)

one = Label(root, text="Welcome to MY GUI", bg="cyan")
one.pack(side=LEFT, fill=Y)

one2 = Label(root, text="Padding", bg="RED")
one2.pack(side=BOTTOM, fill=X, padx=34, pady=35)
root.mainloop()
