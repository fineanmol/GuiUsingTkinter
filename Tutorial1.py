# Tutorial 1

from tkinter import *

root = Tk()
#Top Frame
topframe = Frame(root)
topframe.pack()

#Bottom Frame
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

root.geometry("344x233")
# root.minsize(width=344, height=233)
# root.maxsize(width=314, height=233)
# Everything will be inside this

label = Label(root, text="My First GUI", fg="blue", bg="cyan")
label.pack()

label2 = Label(root, text="That's my second GUI", fg="red")
label2.pack()
root.mainloop()
