import random
from tkinter import *
import string





root = Tk()
root.geometry("300x300");
btn = Button(root,text="Generate Password",command=generate_password)
btn.grid(row=2,colum=2)
lbl = Label(roow,font=("times",15,"bold"))
btn.grid(row=4,colum=2)
root.mainloop()