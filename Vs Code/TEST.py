class Test():
    def __init__(self,q,a,r1,r2,r3):
        self.q = q
        self.a = a
        self.r1 = r1 
        self.r2 = r2
        self.r3 = r3


    def ques(self):
        print(f"Q({self.q}\n A({self.a}\n B({self.r1}\n C({self.r2}\n D({self.r3}")
       #




quslist = [["what is the capitol of dezz","nuts","balls","tiwan","canses"],
           ["who is ligma","balls", "nuts", "face","hairy ass"],
           ["what is 9 plus 10", 21,19,20,18]]


qus2 = Test(quslist[0][0],quslist[0][1],quslist[0][2],quslist[0][3],quslist[0][4])
qus2.ques()
qus2 = Test(quslist[1][0],quslist[1][1],quslist[1][2],quslist[1][3],quslist[1][4])
qus2.ques()
qus2 = Test(quslist[2][0],quslist[2][1],quslist[2][2],quslist[2][3],quslist[2][4])
qus2.ques()
