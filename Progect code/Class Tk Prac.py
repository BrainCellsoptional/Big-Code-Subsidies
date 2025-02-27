from tkinter import *
from PIL import Image ,ImageTk
import csv
import random


class Display():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1200x1000+250+250")
        self.root.configure(bg="black")


        self.bg="black"
        self.fg="white"
        self.font="Times New Roman", 15
        self.wid = Frame(self.root,bg="grey")
        self.wid.pack(expand=1,fill=BOTH)
        self.points(0)
        self.root.mainloop()

    def points(self,num):
        if num < 2:
            self.lab_list = []
            self.p1 = [0,0,0,0]
            self.p2 = [0,0,0,0]
            self.players = [self.p1,self.p2]
            player = ["Player 1 Chose your Abilitys","Player 2 Chose your Abilitys"]
            txt = ["Health","Damage","Defense","Speed"]

            wid_1 = Label(self.wid,bg=self.bg,fg=self.fg,font=self.font,text=player[num])
            wid_1.grid(row=0,column=(num+num+1),columnspan=2,pady=(5,20),padx=(0,20))

            for x in range(4):
                butt = Button(self.wid,bg=self.bg,fg=self.fg,font=self.font,text=txt[x],width=10,height=2,relief=RAISED,command=lambda value=x,num=num:self.increase(value,num))
                butt.grid(row=x+2,column=num+num+1,sticky=W)
                self.lab = Label(self.wid,bg=self.bg,fg=self.fg,font=self.font,text=self.players[num][x],width=10,height=2,relief=SUNKEN)
                self.lab.grid(row=x+2,column=num+num+2,sticky=W,padx=(0,20))
                self.lab_list.append(self.lab)
        else:
            self.wid.destroy()
            self.fight()
        
            

    def increase(self,val,num):
        print(num)
        if sum(self.players[num]) < 19:
            print(self.players[num])
            self.players[num][val] += 1
            self.lab_list[val].configure(text=self.players[num][val])
        else:
            print(self.players[num])
            self.players[num][val] += 1
            self.lab_list[val].configure(text=self.players[num][val])
            print(self.players[num])
            self.points(num+1)
            

    def fight(self):
        pass
            
    

if __name__ == "__main__":
    Display()