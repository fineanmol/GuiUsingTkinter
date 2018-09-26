from tkinter import *

root = Tk()
root.geometry("333x344")

label1 = Label(root, text="Email")
label1.grid(rows=1, sticky="w")
label2 = Label(root, text="Password")
label2.grid(rows=1)

entry1=Entry(root)
entry2=Entry(root)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
checkbutton=Checkbutton(root,text="Remember me on this computer")
button=Button(root,text="Submit")

checkbutton.grid(row=3,column=1)
button.grid(column=0)
root.mainloop()
