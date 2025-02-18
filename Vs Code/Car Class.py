class Car(): #classs
    def __init__(self,carbrand,engine,rpm,bsfc):                                            #input arguments
        self.carbrand = carbrand
        self.engine = engine
        self.rpm = rpm
        self.bsfc = bsfc

    
    def hp(self):                                                                           #Horsepower = Torque x RPM / 5,252 or HP=Fl/(AFR*BFC/60)
        fl = self.rpm / 3.25                                                                #air flow in grams/s (this math is worng on so many levels but its close enough)
        ratio = 12                                                                          #12:1 fuel ratio
        hp = (fl * ((ratio * self.bsfc) / 60 ))                                             #caculates engine horsepower at givin rpm 
        torque = (hp * 5252) / self.rpm                                                     #caculates torque at givin rpm using horsepower
        print(f"""        
        {self.carbrand}
        engine model - {self.engine}
        running at {self.rpm}RPM with a BSFC of {self.bsfc}
        produces - {round(hp,2)} HorsePower and - {round(torque,2)}n/m
        """)



                                            
#print statement displays all info about the engine that the class has processed
def brand_cheek():
    brands = {                                                                              #dictonary containing the lists of avalible options
        "N": "Nissan",
        "T": "Toyota",
        "S": "Subaru",
        "L": "Lancia",
        "M": "Mazda",
        }
    brandselect = input(brands)                                                             #sets brandselect to user input
    return brandselect                                                                      #sends usser input out of function in the form of brank_cheek()

a = brand_cheek()                                                                           #sets usser input to variable


# this block cheeks what engine the usser wants to use and send that info to the class for processing
if a == "N":
    car1 = Car("Nissan","RB26DETT",int(input("Set RPM ")),float(0.66))
    car1.hp()
elif a == "T":
    car1 = Car("Toyota","2JZ",int(input("Set RPM ")),float(0.898))
    car1.hp()
elif a == "S":
    car1 = Car("Subaru","EJ20",int(input("Set RPM ")),float(0.6408))
    car1.hp()
elif a == "L":
    car1 = Car("Lancia","Fiat Twin Cam DOHC",int(input("Set RPM ")),float(1.119))
    car1.hp()
elif a == "M":
    car1 = Car("Mazda","13B",int(input("Set RPM ")),float(0.41))
    car1.hp()
