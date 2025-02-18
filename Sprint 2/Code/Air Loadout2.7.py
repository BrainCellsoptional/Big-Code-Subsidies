#Air Loadout
from tkinter import *
from PIL import Image ,ImageTk
import csv
#This code will not run unless Pillow is installed through the console
#To Intsall Pillow open the console, press ctrl + `
#Then type pip install pillow and wait for the download to complete
#If there are errors try sudo pip install pillow 

class Display():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1100x850+50+50")
        self.root.configure(bg="white")
                
        #Aircraft Images
        self.imgf14 = [Image.open("images/F-14B.jpeg"),2,2,4]
        self.imgf4 = [Image.open("images/F-4E.jpeg"),4,4,0]
        self.imgmig = [Image.open("images/MIG-23ML.jpeg"),2,4,0]
        self.imgsu = [Image.open("images/SU-27.jpeg"),4,2,4]

        self.imglist = [self.imgf14,self.imgf4,self.imgmig,self.imgsu]

        self.aircraft_stats = {
            0: {
            "dry": 19838,
            "fuel": 7348,
            "lift": 0.0174,
            "drag": 0.022,
            "sfc": 0.0007,
            "name": "F-14B Tomcat",
            "speed": 2.34,
            "height": 16,
            "g": 6.5,
            "crew": 2,},
            1: {
            "dry": 13757,
            "fuel": 7548,
            "lift": 0.011,
            "drag": 0.033,
            "sfc": 0.0006,
            "name": "F-4E Phantom II",
            "speed": 2.23,
            "height": 18,
            "g": 5,
            "crew": 2,},
            2: {
            "dry": 10400,
            "fuel": 4672,
            "lift": 0.016,
            "drag": 0.015,
            "sfc": 0.00054,
            "name": "Mig 23 ML Flogger",
            "speed": 2.35,
            "height": 18.5,
            "g": 8.5,
            "crew": 1,},
            3: {
            "dry": 16380,
            "fuel": 9400,
            "lift": 0.0172,
            "drag": 0.025,
            "sfc": 0.0008,
            "name": "SU-27 Flanker",
            "speed": 2.35,
            "height": 19,
            "g": 9,
            "crew": 1,},
            }
                            
        #Missile images
        self.imgaim9d = [Image.open("images/aim9d.jpeg"),"aim9d","images/aim9d.jpeg"]
        self.imgaim9m = [Image.open("images/aim9m.jpeg"),"aim9m","images/aim9m.jpeg"]
        self.imgaim7e2 = [Image.open("images/aim7e2.jpeg"),"aim7e2","images/aim7e2.jpeg"]
        self.imgaim7f = [Image.open("images/aim7f.jpeg"),"aim7f","images/aim7f.jpeg"]
        self.imgaim54 = [Image.open("images/aim54.jpeg"),"aim54","images/aim54.jpeg"]
        
        self.imgr60 = [Image.open("images/r60.jpeg"),"r60","images/r60.jpeg"]
        self.imgr60m = [Image.open("images/r60m.jpeg"),"r60m","images/r60m.jpeg"]
        self.imgr73 = [Image.open("images/r73.jpeg"),"r73","images/r73.jpeg"]
        self.imgr27t = [Image.open("images/r27t.jpeg"),"r27t","images/r27t.jpeg"]
        self.imgr27er = [Image.open("images/r27er.jpeg"),"r27er","images/r27er.jpeg"]

        self.missile_image_list = []
        self.missile_keys_list = []
        self.missile_path_list = []

        self.missile_info = {
            "aim9m":["AIM-9M","IRCCM",5.23,2.5,45,"9.4 kg WDU-17/B - 3.175 kg PBXN-3 filler ",85.3],
            "aim9d":["AIM-9D","IR",5,2.5,18,"11kg MK 48 2.95kg HMX ",88.5],
            "aim7e2":["AIM 7E-2","SARH",2.8,4,25,"30 kg MK 38 continuous rod with 9kg of PBXN-4 ",194.0],
            "aim7f":["AIM 7F","SARH","4.5s Thruster - 11s Sustainer ",2.9,25,"39 kg MK 71 continuous rod ",230.0],
            "aim54":["AIM 54 Phoenix","ARAH",27,4.3,18,"60.68 kg Mk82 Mod 0 blast fragmentation ",470.0],
            "r60":["R-60","IR",3,2.7,30,"3.5 kg continuous-rod warhead ",44.0],
            "r60m":["R-60M","IR","3-5",2.5,30,"3.5 kg continuous-rod warhead - 1.6 kg of depleted uranium ",45.0],
            "r73":["R-73","IRCCM","3-5",2.6,50,"7.4 kg expanding rod ",105.0],
            "r27t":["R-27T","IR",10,4.5,30,"39 kg Expanding rod warhead - 15 kg explosive charge ",245.0],
            "r27er":["R-27ER","SARH","6s Thruster - 11s Sustainer ",4.5,35,"39 kg Expanding rod warhead - 15 kg explosive charge ",253.0],
        }

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
            self.missile_keys_list.pop()
            self.missile_path_list.pop()

    #This Function stores the users selected missiles
    def clicked(self,image,key,path):
        self.missile_image_list.append(image)
        self.missile_keys_list.append(key)
        self.missile_path_list.append(path)




    def hover(self,event,key):
        #This Function configures the info label with information when mouse hovers over missile buttons
        #Incomplete
        #The "Event" argument isnt used in this function but it is needed as an output when the function is called
        #The "Event" argument holds the coordinates of the buttons borders
        info_list = self.missile_info[key]
        self.hover_info.config(text=f"""Missile:  {info_list[0]}
                                Gudince type:       {info_list[1]}
                                Rocket Duration:  {info_list[2]}
                                Mach Number:     {info_list[3]}+ launch Velocity
                                Max G Load:        {info_list[4]}G/s
                                Weight:                {info_list[6]}KG
                                Payload:    {info_list[5]}""")
    def payload_calculator(self,selected_air):
        payload_weight = 0
        for x in range(3):
            if x < len(self.missile_keys_list):
                payload_weight += (self.missile_info[self.missile_keys_list[x]][6]) * (self.imglist[selected_air][x+1])

        air_display = (f"""{self.aircraft_stats[selected_air]["name"]}
        Crew: {self.aircraft_stats[selected_air]["crew"]}
        G Limit: +{self.aircraft_stats[selected_air]["g"]}G
        Max Speed: {self.aircraft_stats[selected_air]["speed"]} Mach
        Service Celling: {self.aircraft_stats[selected_air]["height"]} Km""")
        
        return payload_weight,air_display
    
    def fuel_display(self,fuel_num,key,payload_weight):
        #Calculates Total takeoff weight
        #dry weight + fuel weight + payload weight
        total_weight = self.aircraft_stats[key]["dry"] + int(fuel_num) + payload_weight
        
        #Calculate the lift-to-drag ratio 
        #lift drag ratio = lift coefficient / drag coefficient
        ratio = self.aircraft_stats[key]["lift"]/self.aircraft_stats[key]["drag"]

        #Calculate the range using the Breguet range equation
        #range = ((lift drag ratio / sfc) * (weight total / (dry weight + missile weight) ) * (fuel weight / gravity)) /1000 to make into km instaed of meters
        range = ((ratio / self.aircraft_stats[key]["sfc"]) * (total_weight / (self.aircraft_stats[key]["dry"] + payload_weight)) * (float(fuel_num) / 9.81)) / 1000

        self.display.config(text=f"Range:{round(range,2)} Km\nFuel: {fuel_num} Kg \nTakeoff Weight:{total_weight} Kg")



    def read(self):
        with open('Files/History.csv', 'r') as reader:
            history = csv.reader(reader)
            rows = list(history)
            last_row = rows[-1]
            self.keys = []
            self.paths = []

            self.page = int(last_row.pop())
            self.name = last_row.pop()
            self.selected = int(last_row.pop())
            
            for x in range(3):
                if x <= len(last_row):
                    self.keys.append(last_row.pop(0))
                    self.paths.insert(0,last_row.pop())
            try:
                self.previous = f"{self.name} - {self.keys[0]} {self.keys[1]} {self.keys[2]}"
            except:
                self.previous = f"{self.name} - {self.keys[0]} {self.keys[1]}"



    def save(self,selected_aircraft,air_name,page_num,missile_keys_list,missile_path_list):
        with open('Files/History.csv', 'a') as writer:
            missile_keys = ",".join(missile_keys_list)
            missile_paths = ",".join(missile_path_list)
            writer.write(f"{missile_keys},{missile_paths},{selected_aircraft},{air_name},{page_num}\n")

    def skip(self):
        for x in range(3):
            if x < len(self.keys):
                self.missile_keys_list.append(self.keys[x])
                self.missile_path_list.append(self.paths[x])

                image = Image.open(self.paths[x])
                rs_image = image.resize((200, 150))  
                tk_image = ImageTk.PhotoImage(rs_image)
                self.missile_image_list.append(tk_image)

        self.output_display(self.selected,self.name,self.page)


    def page1(self):
        self.read()
        self.create()
        #Title
        title_home = Label(self.frame,bg="black",fg="white",text="Multi Nation Fighter jet Loadout",font=("Times New Roman", 25, "bold"))
        title_home.grid(row=1,column=1,pady=(100,50),padx=(300,300))
        
        #Text undderneath Title 
        instructions = Label(self.frame,bg="black",fg="white",text="Select An Aircraft for Your Mission ",font=("Times New Roman", 15))
        instructions.grid(row=2,column=1,pady=(5,50))

        
        history = Button(self.frame,bg="black",fg="white",font=("Times New Roman", 15),justify=LEFT,text=f"Previously Selected:\n{self.previous}",command=lambda:(self.destroy(),self.skip()))
        history.grid(row=3,column=1,pady=(5,25))

        #----------------------------------------
        #Container holds all the aircraft buttons to help format the buttons in the correct place
        container = Frame(self.frame,bg="black",width=700,height=250)
        container.grid(row=4,column=1,padx=35,pady=100)

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
        f_14B = Label(container,fg="white",bg="black",text="F-14B",font=("Times New Roman", 15))
        f_14B.grid(row=1,column=2,sticky=N)

        #Text underneath F-4E image
        f4_E = Label(container,fg="white",bg="black",text="F-4E",font=("Times New Roman", 15))
        f4_E.grid(row=1,column=3,sticky=N)

        #Text underneath Mig-23ML image
        mig_23ML = Label(container,fg="white",bg="black",text="MIG-23ML",font=("Times New Roman", 15))
        mig_23ML.grid(row=4,column=2,sticky=N)

        #Text underneath SU-27 image
        su_27 = Label(container,fg="white",bg="black",text="SU-27",font=("Times New Roman", 15))
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
            title_missile = Label(self.frame,bg="black",fg="white",text=self.title[page_num],font=("Times New Roman", 25, "bold"))
            title_missile.grid(row=0,column=0,columnspan=3,pady=(50,5))

            selected = Label(self.frame,bg="black",fg="white",text=air_name,font=("Times New Roman", 25))
            selected.grid(row=1,column=0,columnspan=3,pady=(0,25))

            #----------------------------------------
            #Displays an image of the selected Aircraft
            self.img_display = self.imglist[selected_aircraft][0].resize((500,300))
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
                    self.img_display_missile = selected_list[selected_aircraft][num][0].resize((225,150))
                    self.tk_image_display_missile = ImageTk.PhotoImage(self.img_display_missile)

                    #Button Creation  
                    missile = Button(container2,image=self.tk_image_display_missile,bd=1,relief=RAISED,bg="black",command=lambda image=self.tk_image_display_missile,missile_key=selected_list[selected_aircraft][num][1],missile_path=selected_list[selected_aircraft][num][2]:(self.destroy(),self.clicked(image,missile_key,missile_path),self.missile_pages(selected_aircraft,air_name,page_num + 1)))
                    missile.grid(row=row[num],column=col[num],padx=10,pady=5)

                    #Sends information to hover function and defines which buttons have the hover function applyed  
                    missile.bind("<Enter>", lambda event, missile_key=selected_list[selected_aircraft][num][1]: self.hover(event,missile_key))
                    missile.image = self.tk_image_display_missile
                    
                else:
                    #Fills container with empty labels so the visable buttons dont shift 
                    place_holder = Label(container2,bg="black",width=30,height=10)
                    place_holder.grid(row=row[num],column=col[num],padx=10,pady=5)
                    
            #Label that updates with information when mouse hovers over buttons
            self.hover_info = Label(self.frame,bg="black",fg="white",width=70,height=7,font=("Times New Roman", 20),justify=LEFT,anchor="w",
                                    text=f"""Missile: 
                                Gudince type: 
                                Rocket Duration: 
                                Mach Number: 
                                Max G Load: 
                                Weight: 
                                Payload: """,)
            self.hover_info.grid(row=4,column=0,columnspan=3,sticky=E)
            #Back button
            back = Button(self.frame,bg="black",fg="white",text="Back",font=("Times New Roman", 20),command=lambda:self.previos_page(selected_aircraft,air_name,page_num))
            back.grid(row=5,column=0,padx=40,pady=10,sticky=SW)
        #Calls the output page 
        else:
            self.output_display(selected_aircraft,air_name,page_num)

    def output_display(self,selected_aircraft,air_name,page_num):
        air_info = (self.payload_calculator(selected_aircraft))
        self.create()
        title_output = Label(self.frame,bg="black",fg="white",text="Your Curently Selected Loadout",font=("Times New Roman", 25, "bold"))
        title_output.grid(row=0,column=0,padx=25,pady=25)

        container3 = Frame(self.frame,bg="black",width=400,height=250)
        container3.grid(row=1,column=1,padx=(0,25),pady=(0,10),sticky=NW)

        self.resized = self.imglist[selected_aircraft][0].resize((400,250))
        self.aircraft_img = ImageTk.PhotoImage(self.resized)

        aircraft = Label(container3,bg="black",fg="black",image=self.aircraft_img,bd=5,relief=RIDGE)
        aircraft.grid(row=0,column=0,sticky=N)

        aircraft_info = Label(container3,wraplength=600,width=27,height=6,bd=1,relief=RIDGE,bg="black",fg="white",text=air_info[1],font=("Times New Roman", 20),justify=LEFT)
        aircraft_info.grid(row=1,column=0,pady=(15,0),sticky=S)
        
        container4 = Frame(self.frame,bg="black",width=500,height=500)
        container4.grid(row=1,column=0,padx=(15,0),pady=(0,35),sticky=W)

        for value in range(3):
            if value < len(self.missile_image_list):
                missile_image = Label(container4,image=self.missile_image_list[value],bg="black",bd=5,relief=SUNKEN)
                missile_image.grid(row=value,column=0,pady=(0,10))

                text_output = self.missile_info[self.missile_keys_list[value]]

                text_box = Label(container4,bg="black",fg="white",bd=10,relief=GROOVE,width=35,height=6,justify=LEFT,anchor="w",font=("Times New Roman", 15),
                text=f"""{self.imglist[selected_aircraft][value+1]}x {text_output[0]}\nGuidence Type: {text_output[1]}\nMax G Load: {text_output[4]}G/s\nWeight: {text_output[6]}KG """,
                )
                text_box.grid(row=value,column=1,padx=5,pady=(0,10),sticky=W)
            else:
                place_holder = Label(container4,bg="black",width=32,height=10)
                place_holder.grid(row=value,column=0,pady=(0,10))

        container5 = Frame(self.frame,width=70,height=5,bg="black")
        container5.grid(row=2,column=0,columnspan=3,padx=55,sticky=N)

        loadout = Label(container5,bd=5,relief=RIDGE,bg="black",fg="white",width=44,height=5)
        loadout.grid(row=0,column=0,columnspan=3,rowspan=2,padx=(0,40),pady=(0,10),sticky=W)

        fuel_num = IntVar()
        fuel_slider = Scale(loadout,label="Fuel Weight In Kg",variable=fuel_num,to_=0,from_=self.aircraft_stats[selected_aircraft]["fuel"],bg="black",fg="white",font=20,orient=VERTICAL,length=130,command=lambda fuel_num:self.fuel_display(fuel_num,selected_aircraft,air_info[0]))
        fuel_slider.grid(row=0,column=0,sticky=SW)


        self.display = Label(loadout,wraplength=250,bg="black",fg="white",text=f"Range: 0 Km\nFuel: 0 Kg \nTakeoff Wight:{self.aircraft_stats[selected_aircraft]["dry"] + air_info[0]} Kg",font=("Times New Roman", 20),justify=LEFT)
        self.display.grid(row=0,column=1,padx=(50,20),sticky=N)

        display2 = Label(loadout,bg="black",fg="white",text=f"Total Payload Weight: \n{air_info[0]} Kg",font=("Times New Roman", 20),justify=LEFT)
        display2.grid(row=0,column=3,sticky=N)

        #Back button
        back = Button(container5,width=10,height=2,bg="black",fg="white",text="Back",font=("Times New Roman", 20),command=lambda:(self.destroy(),self.missile_image_list.pop(),self.missile_keys_list.pop(),self.missile_path_list.pop(),self.missile_pages(selected_aircraft,air_name,(page_num - 1))))
        back.grid(row=0,column=2,padx=(850,0),pady=(0,15),sticky=NW)

        submit = Button(container5,width=10,height=2,bg="black",fg="white",text="Save & Exit",font=("Times New Roman", 20),command=lambda:(self.save(selected_aircraft,air_name,page_num,self.missile_keys_list,self.missile_path_list),self.root.destroy()))
        submit.grid(row=1,column=2,padx=(850,0),sticky=NW)


if __name__ == "__main__":
    Display()