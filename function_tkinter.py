from tkinter import *


def subscribe():
    print("Subscribed the CHANNEL")


root = Tk()
root.geometry("600x600")

button = Button(root, text="Subscribe Now", command=subscribe)
button.pack()
button2 = Button(root, text="Exit", command=quit)
button2.pack()

root.mainloop()
