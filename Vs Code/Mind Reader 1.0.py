import tkinter as tk
from tkinter import *
import random
def color():
    r =random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    return f"#{r:02x}{g:02x}{b:02x}"
root = tk.Tk()
root.geometry("800x600+50+50")
root.configure(bg="black")
def update_text(label,txt,index):
    if index != 9:
        label.config(text=txt[index],fg=color())
        root.after(1000, update_text, label,txt,(index + 1))
    else:   
        label.config(text=""" The results are in \nyou're gay""",fg=color())

def caculate():
    for ele in root.winfo_children():
        ele.destroy()
    txt = ["analyzing data",
           "performing quailty checks",
           "formating inputs",
           "updating algarithim",
           "caculateing",
           "processing",
           "post prosecing",
           "updating final desicon ",
           "comeing to a conclusion"]
    
    spacer = Label(root,bg="black",)
    spacer.grid(row=1,column=1,padx=10)
    la1 = Label(root,bg="black",fg=color(),text="begginig caculations",font=("comic sans",30),justify="center")
    la1.grid(row=3,column=3)
    root.after(1000, update_text, la1, txt,0)

spacer = Label(root,bg="black",)
spacer.grid(row=1,column=1,padx=10)
la1 = Label(root,bg="black",fg="white",text="Think of a number between 1 - 10",font=("comic sans",30))
la1.grid(row=2,column=2,padx=10)
la2 = Entry(root,bg="black",fg="white",font=("comic sans",30),justify="center")
la2.grid(row=3,column=2,padx=10)
la3 = Button(root,bg="black",fg="white",text="submit",command=caculate,font=("comic sans",15))
la3.grid(row=4,column=2,padx=10)







root.mainloop()
