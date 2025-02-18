# missile class Ir and SARH
#arguments - seaker type (incloude IRCCM) ,burn range, potential range, total G/s, explosive capcity

class Missile():
    def __init__(self,name,seaker,burn,speed,glock,exp,weight):
        self.name = name
        self.seaker = seaker
        self.burn = burn
        self.speed = speed
        self.glock = glock
        self.exp = exp
        self.weight = weight

#sets the input varibles in a readale output
    def output(self):
        

        print(f"""

            {self.name}
            type - {self.seaker}
            moter - {self.burn}s moter burn time
            speed - MACH {self.speed}+ launch velocity
            turn rate - {self.glock}G Overload
            explosive mass - {self.exp}
            weight - {self.weight} KG
            
            """)
            
#displays options for usser and recives the input



#takes usser input and sorts it to output the relevent data

def aim_9m():
    m1 = Missile("AIM-9M","IRCCM",5.23,2.5,45,"9.4 kg WDU-17/B - 3.175 kg PBXN-3 filler ",85.3 )
    m1.output()

def aim_9d():
    m1 = Missile("AIM-9D","IR",5,2.5,18,"11kg MK 48 2.95kg HMX ",88.5 )
    m1.output()

def r_60():
    m1 = Missile("R-60","IR",3,2.7,30,"3.5 kg continuous-rod warhead ",44 )
    m1.output()

def r_60m():
    m1 = Missile("R-60M","IR","3-5",2.5,30,"3.5 kg continuous-rod warhead - 1.6 kg of depleted uranium ",45 )
    m1.output()

def r_73():
    m1 = Missile("R-73","IRCCM","3-5",2.6,50," 7.4 kg expanding rod ",105 )
    m1.output()

def aim_7e_2():
    m1 = Missile("AIM 7E-2","SARH",2.8,4,25," 30 kg MK 38 continuous rod with 9kg of PBXN-4 ",194 )
    m1.output()

def aim_7f():
    m1 = Missile("AIM 7F","SARH","4.5s Thruster - 11s Sustainer ",2.9,25," 39 kg MK 71 continuous rod ",230 )
    m1.output()

def aim_54():
    m1 = Missile("AIM 54 Phoenix","ARAH",27,4.3,18,"60.68 kg Mk82 Mod 0 blast fragmentation ",470 )
    m1.output()

def r_27t():
    m1 = Missile("R-27T","IR",10,4.5,30,"39 kg Expanding rod warhead - 15 kg explosive charge ",245 )
    m1.output()

def r_27er():
    m1 = Missile("R-27ER","SARH","6s Thruster - 11s Sustainer ",4.5,35,"39 kg Expanding rod warhead - 15 kg explosive charge ",253 )
    m1.output()



dicA = {"1": aim_9d,
        "2": aim_9m,
        "3": aim_7e_2,
        "4": aim_7f,
        "5": aim_54,

        }
dicR = {
        "1": r_60,
        "2": r_60m,
        "3": r_73,
        "4": r_27t,
        "5": r_27er,
        }





class Jet():
    def __init__(self,aircraft,):
        self.aircraft = aircraft 



    def f_14(self):
        print("""        you have selected the Mighty F-14B Tomcat
        Please select your sortie Loadout""")
        pilon1 = str(input(f"""outside pilons
                        1 - {aim_9d()}
                        2 - Aim 9M 
                        """))
        pilon2 = str(input("""fwing pilons
                        1 - Aim 9D
                        2 - Aim 9M
                        4 - Aim 7F
                        5 - Aim 54  
                        """))
        pilon3 = str(input(f"""Center pilons
                        4 - Aim 7F
                        5 - Aim 54  
                        """))
        
        dicA[pilon1]()
        dicA[pilon2]()
        dicA[pilon3]()
        payload_weight = 
        print(f""" """)


    def loadout(self):
        b = 0
        while  b == 0:
            if int(self.aircraft) == 1:
                self.f_14()
                b = b+1
            elif self.aircraft == 2:
                self.f_4()
                b = b+1
            elif self.aircraft == 3:
                self.su_27()
                b = b+1
            else:
                self.aircraft = input("please enter valid Aircraft")






def select():
    print("""Select Aircraft
            1 - F-14B Tomcat
            2 - F-4E Phantom
            3 - SU-27SMT Flanker
            """)
    
    launch = Jet(int(input("Enter   ")),)
    launch.loadout()

payload_weight = []
select()