from tkinter import *

root = Tk()
var = StringVar()
label = Message(root, textvariable=var, relief=RAISED, aspect=300)  
var.set("Hey!? How are you doing? aaaaaaaaaaa")
label.pack(expand=True, fill='both')

root.mainloop()
