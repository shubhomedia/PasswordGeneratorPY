import random
from tkinter import *
import string

def generate_password():
    password=[]
    for i in range(12):
        lower = random.choice(string.ascii_lowercase)
        symbol = random.choice(string.punctuation)
        upper = random.choice(string.ascii_uppercase)
        numbers = random.choice(string.digits)
        password.append(lower)
        password.append(symbol)
        password.append(upper)
        password.append(numbers)





root = Tk()
root.geometry("300x300");
btn = Button(root,text="Generate Password",command=generate_password)
btn.grid(row=2,colum=2)
lbl = Label(roow,font=("times",15,"bold"))
btn.grid(row=4,colum=2)
root.mainloop()