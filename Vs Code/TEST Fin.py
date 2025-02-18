import random

answer = []
score = 0
class Test():
    def __init__(self,q,a,r1,r2,r3):
        self.q = q
        self.a = a
        self.r1 = r1 
        self.r2 = r2
        self.r3 = r3

    def ques(self):
        global score
        rand = [self.a,self.r1,self.r2,self.r3]
        random.shuffle(rand)
        g = rand.index(self.a) + 1

        response = {"Q": (self.q),
                    "1":(rand[0]), 
                    "2":(rand[1]),
                    "3":(rand[2]),
                    "4":(rand[3]),
                    }
        print(f"""Q - {response["Q"]}
        1 - {response["1"]}    
        2 - {response["2"]}   
        3 - {response["3"]}   
        4 - {response["4"]}
                """)
        
        t = int(input("Answer Here  "))
        j = rand[t-1]
    
        if t == g:
            print("Correct")
            print()
            score = score + 1
            return j
        else:
            print("Incorrect")
            print()
            return j




def results():
    global answer
    global score
    k = 1
    for x in answer:
        print(f"q{k} answered {x}")
        k = k+1
    if score >= 2:
        print(f"congrates you scored {score} points")
    elif score == 1:
        print(f"well I guess {score} points is ok try better next time")
    else:
        print(f"""ive seen labotomy patients with higher IQ,s than you
               you scored {score} points""")
    




quslist = [["what is the capitol of dezz","nuts","balls","tiwan","canses"],
           ["who is ligma","balls", "nuts", "face","hairy ass"],
           ["what is 9 plus 10", 21,19,20,18]]


qus2 = Test(quslist[0][0],quslist[0][1],quslist[0][2],quslist[0][3],quslist[0][4])
answer.append(qus2.ques())
qus2 = Test(quslist[1][0],quslist[1][1],quslist[1][2],quslist[1][3],quslist[1][4])
answer.append(qus2.ques())
qus2 = Test(quslist[2][0],quslist[2][1],quslist[2][2],quslist[2][3],quslist[2][4])
answer.append(qus2.ques())
results()