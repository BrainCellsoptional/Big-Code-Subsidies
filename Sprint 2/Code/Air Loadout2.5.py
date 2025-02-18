#Air Loadout
import math
from tkinter import *
from PIL import Image ,ImageTk


class Display():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1100x850+50+50")
        self.root.configure(bg="white")

        #Aircraft Images
        self.imgf14 = Image.open("images/F-14B.jpeg")
        self.imgf4 = Image.open("images/F-4E.jpeg")
        self.imgmig = Image.open("images/MIG-23ML.jpeg")
        self.imgsu = Image.open("images/SU-27.jpeg")
        self.imglist = [self.imgf14,self.imgf4,self.imgmig,self.imgsu]

        #Missile images
        self.imgaim9d = Image.open("images/aim9d.jpeg")
        self.imgaim9m = Image.open("images/aim9m.jpeg")
        self.imgaim7e2 = Image.open("images/aim7e2.jpeg")
        self.imgaim7f = Image.open("images/aim7f.jpeg")
        self.imgaim54 = Image.open("images/aim54.jpeg")
        
        self.imgr60 = Image.open("images/r60.jpeg")
        self.imgr60m = Image.open("images/r60m.jpeg")
        self.imgr73 = Image.open("images/r73.jpeg")
        self.imgr27t = Image.open("images/r27t.jpeg")
        self.imgr27er = Image.open("images/r27er.jpeg")

        self.missile_image_list = []

        #Starts the Process and dosnt allow for resizing of display
        self.root.resizable(width=False, height=False)
        self.page1()
        self.root.mainloop()

    def create(self):
        #Creates a blank Frame that fills the root
        #Column is configured to start for 0
        #Row is configure to start from 1(for simplicity)
        self.frame = Frame(self.root,width="800",height="600",bg="black")
        self.frame.pack(expand=1,fill=BOTH)

        self.frame.columnconfigure(0)
        self.frame.rowconfigure(1)

    def destroy(self):
        #Destroys the frame containing all widgits
        self.frame.destroy()

    def previos_page(self,selected_aircraft,air_name,page_num):
        #This Function takes the usser back one page
        #It imports all the information the missile_display function needs updates the page_num and then outputs them  
        self.destroy()
        if page_num == 1:
            self.page1()
        elif int(selected_aircraft) in (1,2) and page_num == 2:
            self.page1()
        else:
            page_num = page_num - 1
            self.missile_pages(selected_aircraft,air_name,page_num)
            self.missile_image_list.pop()

        
        

    def clicked(self,image):
        self.missile_image_list.append(image)

    def hover(self,event,missille_info):
        #This Function configures the info label with information when mouse hovers over missile buttons
        #Incomplete
        #The "Event" argument isnt used in this function but it is needed as an output when the function is called
        #The "Event" argument holds the coordinates of the buttons borders 
        info_list = ["when you hover","over the buttons","this text","will change"]
        self.hover_info.config(text=info_list[missille_info])

    def page1(self):
        self.create()
        #Title
        title_home = Label(self.frame,bg="black",fg="white",text="Multi Nation Fighter jet Loadout",font=("Times New Roman", 25, "bold"),justify="center")
        title_home.grid(row=1,column=1,pady=(100,50),padx=(300,300))
        
        #Text undderneath Title 
        instructions = Label(self.frame,bg="black",fg="white",text="Select An Aircraft for Your Mission ",font=("Times New Roman", 15),justify="center")
        instructions.grid(row=2,column=1,pady=(5,100))

        #Empty space 
        spacer1 = Label(self.frame,bg="black",height=10)
        spacer1.grid(row=3,column=0)


        #----------------------------------------
        #Container holds all the aircraft buttons to help format the buttons in the correct place
        container = Frame(self.frame,bg="black",width=700,height=250)
        container.grid(row=3,column=1,padx=30,pady=100)

        #----------------------------------------
        #Image of Mission 
        self.img = Image.open("images/Mission.gif")

        #Resizes Image
        self.img = self.img.resize((550, 340))  
        self.tk_image = ImageTk.PhotoImage(self.img)

        #Displays Image
        self.image_button = Button(container, image=self.tk_image)
        self.image_button.grid(row=0,column=0,pady=0,padx=10,rowspan=4)

        #----------------------------------------Image 1
        #Button Image of F-14B 
        #Opens image and saves to a variable
        self.img1 = Image.open("images/F-14B.gif") 

        #Resizes image
        self.img1 = self.img1.resize((200, 150))  
        self.tk_image1 = ImageTk.PhotoImage(self.img1)

        #Displays Image and Button
        self.image_button1 = Button(container, image=self.tk_image1,command=lambda:(self.destroy(),self.missile_pages(0,"F-14B TomCat",1)))
        self.image_button1.grid(row=0,column=2,pady=0,padx=5,sticky=N)

        #----------------------------------------Image 2=
        #Button Image of F-4E 
        #Opens image and saves to a variable
        self.img2 = Image.open("images/F-4E.gif")

        #Resizes image
        self.img2 = self.img2.resize((200, 150))  
        self.tk_image2 = ImageTk.PhotoImage(self.img2)

        #Displays Image and Button
        self.image_button2 = Button(container, image=self.tk_image2,command=lambda:(self.destroy(),self.missile_pages(1,"F-4E Phantom",2)))
        self.image_button2.grid(row=0,column=3,pady=0,padx=5,sticky=N)

        #----------------------------------------Image 3
        #Button Image of Mig-23ML 
        #Opens image and saves to a variable
        self.img3 = Image.open("images/MIG-23ML.gif")

        #Resizes image
        self.img3 = self.img3.resize((200, 150))  
        self.tk_image3 = ImageTk.PhotoImage(self.img3)

        #Displays Image and Button
        self.image_button3 = Button(container, image=self.tk_image3,command=lambda:(self.destroy(),self.missile_pages(2,"MIG-23ML Flogger",2)))
        self.image_button3.grid(row=3,column=2,pady=0,padx=5,sticky=N)
        #----------------------------------------Image 4
        #Button Image of SU-27 
        #Opens image and saves to a variable
        self.img4 = Image.open("images/SU-27.gif")  

        #Resizes image 
        self.img4 = self.img4.resize((200, 150))  
        self.tk_image4 = ImageTk.PhotoImage(self.img4)

        #Displays Image and Button
        self.image_button4 = Button(container, image=self.tk_image4,command=lambda:(self.destroy(),self.missile_pages(3,"SU-27 Flanker",1)))
        self.image_button4.grid(row=3,column=3,pady=0,padx=5,sticky=N)

        #----------------------------------------
        #Text underneath F-14B image
        f_14B = Label(container,fg="white",bg="black",text="F-14B",font=("Times New Roman", 15),justify="center")
        f_14B.grid(row=1,column=2,sticky=N)

        #Text underneath F-4E image
        f4_E = Label(container,fg="white",bg="black",text="F-4E",font=("Times New Roman", 15),justify="center")
        f4_E.grid(row=1,column=3,sticky=N)

        #Text underneath Mig-23ML image
        mig_23ML = Label(container,fg="white",bg="black",text="MIG-23ML",font=("Times New Roman", 15),justify="center")
        mig_23ML.grid(row=4,column=2,sticky=N)

        #Text underneath SU-27 image
        su_27 = Label(container,fg="white",bg="black",text="SU-27",font=("Times New Roman", 15),justify="center")
        su_27.grid(row=4,column=3,sticky=N)

        #----------------------------------------

    def missile_pages(self,selected_aircraft,air_name,page_num):
        #Missile slection screen only runs if there is an avalible pilon
        if page_num <=3:
            #Text dictonary for the different Titles 
            self.title = {1:"Outer Wing Pillon Selection",
                          2:"Inner Wing Pillon Selection",
                          3:"Body Pillon Selection",}
            
            self.create()
            #----------------------------------------
            #Main Title for missile selection screen
            #Text changes depending on which pilon the user is selecting for  
            title_missile = Label(self.frame,bg="black",fg="white",text=self.title[page_num],font=("Times New Roman", 25, "bold"),justify="center")
            title_missile.grid(row=0,column=0,columnspan=3,pady=(50,5))

            selected = Label(self.frame,bg="black",fg="white",text=air_name,font=("Times New Roman", 25),justify="center")
            selected.grid(row=1,column=0,columnspan=3,pady=(0,25))

            #----------------------------------------
            #Displays an image of the selected Aircraft
            self.img_display = self.imglist[selected_aircraft].resize((500,300))
            self.tk_image_display = ImageTk.PhotoImage(self.img_display)

            img_box = Label(self.frame,image=self.tk_image_display,bd=10,relief=RAISED)
            img_box.grid(row=2,column=0,padx=25,pady=25)
            #----------------------------------------
            #Container that stores missile buttons   
            container2 = Frame(self.frame,bg="black",width=500,height=300)
            container2.grid(row=2,column=2,padx=25,pady=25)

            #----------------------------------------
            #Asigns missile images into a list in a dictonary with a key value to be called later
            #Each aircraft has its own sellection of missiles avalible for each pilon
            #Some aircraft only have 2 pilons, so the outer pilon is empty
            img_f_14b = {1:[self.imgaim9d,self.imgaim9m],
                         2:[self.imgaim9d,self.imgaim9m,self.imgaim7f,self.imgaim54],
                         3:[self.imgaim7f,self.imgaim54]}

            img_f_4e = {1:[],
                        2:[self.imgaim9d],
                        3:[self.imgaim7e2],}

            img_mig_23ml = {1:[],
                            2:[self.imgr27t],
                            3:[self.imgr60,self.imgr60m]}

            img_su_27 = {1:[self.imgr60,self.imgr60m,self.imgr73],
                         2:[self.imgr73,self.imgr27t,self.imgr27er],
                         3:[self.imgr27t,self.imgr27er]}

            selected_list = [img_f_14b[page_num],img_f_4e[page_num],img_mig_23ml[page_num],img_su_27[page_num]]
            #----------------------------------------

            row = [0,0,1,1]
            col = [0,1,0,1]
            for num in range(4):
                if num < len(selected_list[selected_aircraft]):
                    #Asigns the correct Image to the button
                    self.img_display_missile = selected_list[selected_aircraft][num].resize((225,150))
                    self.tk_image_display_missile = ImageTk.PhotoImage(self.img_display_missile)

                    #Button Creation  
                    missile = Button(container2,image=self.tk_image_display_missile,bd=1,relief=RAISED,bg="black",command=lambda image=self.tk_image_display_missile:(self.destroy(),self.clicked(image),self.missile_pages(selected_aircraft,air_name,page_num + 1)))
                    missile.grid(row=row[num],column=col[num],padx=10,pady=5)

                    #Sends information to hover function and defines which buttons have the hover function applyed  
                    missile.bind("<Enter>", lambda event ,button_num=num: self.hover(event,button_num))
                    missile.image = self.tk_image_display_missile
                    
                else:
                    #Fills container with empty labels so the visable buttons dont shift 
                    place_holder = Label(container2,bg="black",width=30,height=10)
                    place_holder.grid(row=row[num],column=col[num],padx=10,pady=5)
                    
            #Label that updates with information when mouse hovers over buttons
            self.hover_info = Label(self.frame,bg="black",fg="white",width=60,height=7,text="The missiles Information will go here",font=("Times New Roman", 20),justify="left")
            self.hover_info.grid(row=4,column=0,columnspan=3)
            #Back button
            back = Button(self.frame,bg="black",fg="white",text="Back",font=("Times New Roman", 20),justify="center",command=lambda:self.previos_page(selected_aircraft,air_name,page_num))
            back.grid(row=5,column=0,padx=10,pady=10,sticky=SW)
        #Calls the output page 
        else:
            self.output_display(selected_aircraft,air_name,page_num)

    def output_display(self,selected_aircraft,air_name,page_num):
        self.create()
        title_output = Label(self.frame,bg="black",fg="white",text="Your Curently Selected Loadout",font=("Times New Roman", 25, "bold"),justify="center")
        title_output.grid(row=0,column=0,padx=25,pady=25)

        container3 = Frame(self.frame,bg="black",width=400,height=250)
        container3.grid(row=1,column=1,padx=(0,25),pady=(0,10),sticky=NW)

        self.resized = self.imglist[selected_aircraft].resize((400,250))
        self.aircraft_img = ImageTk.PhotoImage(self.resized)

        aircraft = Label(container3,bg="black",fg="black",image=self.aircraft_img,bd=5,relief=RIDGE)
        aircraft.grid(row=0,column=0,sticky=N)

        aircraft_info = Label(container3,width=20,height=6,bd=1,relief=RIDGE,bg="black",fg="white",text="Aircraft info will go here",font=("Times New Roman", 25, "bold"),justify="center")
        aircraft_info.grid(row=1,column=0,pady=(15,0),sticky=S)
        
        container4 = Frame(self.frame,bg="black",width=500,height=500)
        container4.grid(row=1,column=0,padx=(15,0),pady=(0,35),sticky=W)

        for value in range(3):
            if value < len(self.missile_image_list):
                missile_image = Label(container4,image=self.missile_image_list[value],bg="black",bd=5,relief=SUNKEN)
                missile_image.grid(row=value,column=0,pady=(0,10))

                text_box = Label(container4,bg="black",fg="white",bd=10,text="missile text",relief=GROOVE,width=55,height=9)
                text_box.grid(row=value,column=1,padx=5,pady=(0,10),sticky=W)
            else:
                place_holder = Label(container4,bg="black",width=32,height=10)
                place_holder.grid(row=value,column=0,pady=(0,10))

        container5 = Frame(self.frame,width=70,height=5,bg="black")
        container5.grid(row=2,column=0,columnspan=3,padx=55,sticky=N)

        loadout = Label(container5,bd=5,relief=RIDGE,bg="black",fg="white",text="Loadout Information will go here",font=("Times New Roman", 25, "bold"),justify="center",width=44,height=5)
        loadout.grid(row=0,column=0,columnspan=3,rowspan=2,padx=(0,40),pady=(0,10),sticky=W)
        
        #Back button
        back = Button(container5,width=8,height=2,bg="black",fg="white",text="Back",font=("Times New Roman", 20),justify="center",command=lambda:(self.destroy(),self.missile_image_list.pop(),self.missile_pages(selected_aircraft,air_name,(page_num - 1))))
        back.grid(row=0,column=2,padx=(900,0),pady=(0,15),sticky=NW)

        submit = Button(container5,width=8,height=2,bg="black",fg="white",text="Sumbit",font=("Times New Roman", 20),justify="center",command=self.root.destroy)
        submit.grid(row=1,column=2,padx=(900,0),sticky=NW)

if __name__ == "__main__":
    Display()