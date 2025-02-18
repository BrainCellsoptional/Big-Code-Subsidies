from tkinter import *
num = [0,5,-3,3000,-40000]

ans = [3,8,0,30003,-39997]



def big(num):
    for x in range(5):
        value = (num[x])+3
        if value == ans[x]:
            print(f"{value} Passed")
        else:
            print(f"{value} Failed")

big(num)

root = Tk()
root.geometry('500x500')


def dis():
    lab.config(text=ent.get())

def cheek():
    ent.delete(0, END)
    ent.insert(0,"beans")
    but.invoke()



var = StringVar
ent = Entry(root)
ent.grid(row=0,column=0)

but = Button(root,text="press",command=dis)
but.grid(row=1,column=0)

lab = Label(root)
lab.grid(row=2,column=0)

but2 = Button(root,text="press to check",command=cheek)
but2.grid(row=0,column=1)



root.mainloop()