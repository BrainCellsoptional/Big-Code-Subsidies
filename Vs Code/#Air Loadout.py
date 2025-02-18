#Air Loadout
import math

def start():

    def f_14B():
        launch = Aircraft("Mighty F-14B Tomcat",2,2,4,us_aam,a)
        launch.select()
    def f_4E():
        launch = Aircraft("Venrable F-4E Phantom",2,4,0,us_aam,a)
        launch.select()
    def mig_23ML():
        launch = Aircraft("Mediocer Mig-23ML Flogger",2,4,0,ru_aam,a)
        launch.select()
    def su_27():
        launch = Aircraft("Snarling Su-27 Flanker",4,2,4,ru_aam,a)
        launch.select()
    air = {1: f_14B,
        2: f_4E,
        3: mig_23ML,
        4: su_27,
        }
    print("""Select Aircraft
            1 - F-14B Tomcat
            2 - F-4E Phantom
            3 - MIG-23ML Flogger
            4 - SU-27 Flanker
            """)
    a = int(input("ENTER        "))
    air[a]()

def aim9m():
    m1 = Missile("AIM-9M","IRCCM",5.23,2.5,45,"9.4 kg WDU-17/B - 3.175 kg PBXN-3 filler ",85.3 )
    m1.output()
    m1.output2()
    return ""
def aim9d():
    m1 = Missile("AIM-9D","IR",5,2.5,18,"11kg MK 48 2.95kg HMX ",88.5 )
    m1.output()
    m1.output2()
    return ""
def r60():
    m1 = Missile("R-60","IR",3,2.7,30,"3.5 kg continuous-rod warhead ",44 )
    m1.output()
    m1.output2()
    return ""
def r60m():
    m1 = Missile("R-60M","IR","3-5",2.5,30,"3.5 kg continuous-rod warhead - 1.6 kg of depleted uranium ",45 )
    m1.output()
    m1.output2()
    return ""
def r73():
    m1 = Missile("R-73","IRCCM","3-5",2.6,50," 7.4 kg expanding rod ",105 )
    m1.output()
    m1.output2()
    return ""
def aim7e2():
    m1 = Missile("AIM 7E-2","SARH",2.8,4,25," 30 kg MK 38 continuous rod with 9kg of PBXN-4 ",194 )
    m1.output()
    m1.output2()
    return ""
def aim7f():
    m1 = Missile("AIM 7F","SARH","4.5s Thruster - 11s Sustainer ",2.9,25," 39 kg MK 71 continuous rod ",230 )
    m1.output()
    m1.output2()
    return ""
def aim54():
    m1 = Missile("AIM 54 Phoenix","ARAH",27,4.3,18,"60.68 kg Mk82 Mod 0 blast fragmentation ",470 )
    m1.output()
    m1.output2()
    return ""
def r27t():
    m1 = Missile("R-27T","IR",10,4.5,30,"39 kg Expanding rod warhead - 15 kg explosive charge ",245 )
    m1.output()
    m1.output2()
    return ""
def r27er():
    m1 = Missile("R-27ER","SARH","6s Thruster - 11s Sustainer ",4.5,35,"39 kg Expanding rod warhead - 15 kg explosive charge ",253 )
    m1.output()
    m1.output2()
    return ""

us_aam = {1:aim9d,
          2:aim9m,
          3:aim7e2,
          4:aim7f,
          5:aim54,
          }
ru_aam = {1:r60,
          2:r60m,
          3:r73,
          4:r27t,
          5:r27er,
          }

class Aircraft():
    def __init__(self,aircraft,p1,p2,p3,dic,a):
        self.aircraft = aircraft
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.dic = dic
        self.a = a

    def f_14B_(self):
        print(f""" you have selected the {self.aircraft}
        Please select your Air - Air Loadout
        """)
        wt = []
        print(f"""Select Outer Pilon
            {(self.dic[1]())} 1 - {mod}
            {(self.dic[2]())} 2 - {mod}
            """)
        wt.append(input("ENTER       "))
        print(f"""Please select middle pilon
            {(self.dic[1]())} 1 - {mod}
            {(self.dic[2]())} 2 - {mod}
            {(self.dic[4]())} 4 - {mod}
            {(self.dic[5]())} 5 - {mod}
            """)
        wt.append(input("ENTER       "))
        print(f"""Please select ceter pilon
            {(self.dic[4]())} 4 - {mod}
            {(self.dic[5]())} 5 - {mod}
            """)
        wt.append(input("ENTER       "))
        Missile.payload_weight(self,wt,self.dic,self.aircraft,self.p1,self.p2,self.p3)

    def f_4E_(self):
        print(f""" you have selected the {self.aircraft}
        Please select your Air - Air Loadout
        """)
        wt = []
        print(f"""Please select outer pilon
            {(self.dic[1]())} 1 - {mod}
            """)
        wt.append(input("ENTER       "))
        print(f"""Please select ceter pilon
            {(self.dic[3]())} 3 - {mod}
            """)
        wt.append(input("ENTER       "))
        Missile.payload_weight(self,wt,self.dic,self.aircraft,self.p1,self.p2,self.p3) 

    def mig_23ML_(self):
        print(f""" you have selected the {self.aircraft}
        Please select your Air - Air Loadout
        """)
        wt = []
        print(f"""Select Outer Pilon
            {(self.dic[4]())} 4 - {mod}
        """)
        wt.append(input("ENTER       "))
        print(f"""Please select ceter pilon
            {(self.dic[1]())} 1 - {mod}
            {(self.dic[2]())} 2 - {mod}
            """)
        wt.append(input("ENTER       "))
        Missile.payload_weight(self,wt,self.dic,self.aircraft,self.p1,self.p2,self.p3)

    def su_27_(self):
        print(f"""you have selected the {self.aircraft}
Please select your Air - Air Loadout
        """)
        wt = []
        print(f"""Select Outer Pilon
            {(self.dic[1]())} 1 - {mod}
            {(self.dic[2]())} 2 - {mod}
            {(self.dic[3]())} 3 - {mod}
            """)
        wt.append(input("ENTER       "))
        print(f"""Please select middle pilon
            {(self.dic[3]())} 3 - {mod}
            {(self.dic[4]())} 4 - {mod}
            {(self.dic[5]())} 5 - {mod}
            """)
        wt.append(input("ENTER       "))
        print(f"""Please select ceter pilon
            {(self.dic[4]())} 4 - {mod}
            {(self.dic[5]())} 5 - {mod}
            """)
        wt.append(input("ENTER       "))
        Missile.payload_weight(self,wt,self.dic,self.aircraft,self.p1,self.p2,self.p3)
        
    def select(self):
        des = {1: self.f_14B_,
                 2: self.f_4E_,
                 3: self.mig_23ML_,
                 4: self.su_27_,
            }
        des[self.a]()
        
    def output(self,output_weight,a,wt,dic):
        self.output_weight = output_weight
        self.a = a
        self.wt = wt
        self.dic = dic
        weplist = []
        for x in self.wt:
            self.dic[int(x)]()
            weplist.append(mod1)
        weplist.append("")
        print(f"""Selected 
            Aircraft - {self.aircraft}

            AAM Selected 

            {weplist[0]}
            {weplist[1]}
            {weplist[2]}

            Total Payload Weight
            {self.output_weight}KG
            
            """)

class Missile():
    def __init__(self,name,seaker,burn,speed,glock,exp,weight):
        self.name = name
        self.seaker = seaker
        self.burn = burn
        self.speed = speed
        self.glock = glock
        self.exp = exp
        self.weight = weight
        global w 
        w = weight

    def output(self):
        global mod
        mod = (f"{self.name} {self.glock}G {self.weight}KG")
    def output2(self):
        global mod1
        mod1 = (f"{self.name} - {self.seaker}  {self.burn}s - {self.speed}+ Launch Velocity - {self.glock}G/s  {self.weight}KG - {self.exp}")
        

    def payload_weight(self,wt,dic,aircraft,p1,p2,p3):
        self.wt = wt
        self.dic = dic
        self.aircraft = aircraft
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        pilons = [self.p1,self.p2,self.p3]
        loop = 0
        output_weight = 0
        for x in self.wt:
            self.dic[int(x)]()
            output_weight = output_weight +(float(w) * float(pilons[loop]))
            loop = loop + 1 
        Aircraft.output(self,output_weight,self.aircraft,self.wt,self.dic)

start()