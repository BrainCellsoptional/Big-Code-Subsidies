


def select():
    sentance = "man is on a cliff"
    num1 = int(input("range start"))
    num2 = int(input("range end"))
    print(sentance[num1:num2])
    pass



def mathgame():
    num1 = int(input("first number"))
    num2 = int(input("second number"))
    numerator = input("+ for add, - for minus, 8 for times, / for divide")
    if numerator == "+":
        answer = num1 + num2
    elif numerator == "-":
        answer = num1 - num2
    elif numerator == "*":
        answer = num1 * num2
    elif numerator == "/":
        answer = num1 / num2
    print(f"{num1}{numerator}{num2} = {answer}")
    pass


def spell():
    words1 = ["beans","beens", "bens"]
    words2 = ["mulitytasked", "miltitasked","multitasked"]
    words3 = ["sumbmerged", "submargeed","sybmargeed"]
    print("I will give you 3 words you have to select which word fits the sentace.")
    print()
    fil = 0
    while fil == 0:
        print("________________________________________________________________________")
        print("my docter siad i have aids due to",words1,", so he decided i should stop")
        try1 = input("spell the correct word")
        if try1 == "beans":
            print("Correct! Well done you know that beans gives you aids")
            fil = fil + 1
        else:
            print()
            print(try1,"is not correct shithead try agian.(no caps:)")
            print()
    print("________________________________________________________________________")
    print("On to the next one")
    print()
    while fil == 1:
        print("Today I ",words2,"by scratcing my nuts while gamening")
        try1 = input("spell the word.")
        if try1 == "multitasked":
            print("Correct!",try1," was the correct answer.")
            fil = fil + 1
        else:
            print()
            print("Why did you think",try1,"was correct, you couldn't be more wrong. idioty")
            print()
    print("________________________________________________________________________")
    print("On to the last one")
    print()
    while fil == 2:
        print("When my phone got",words3,"it stopped working so i sent it back to the sweetshops")
        try1 = input("select your final word")
        if try1 == "submerged":
            print("well done shit head it seems my tricks didnt confuse you :) you have my respect")
            fil = fil + 1
        else:
            print()
            print("well done",try1," was NOT correct.  Try agian")
            print()
    print("congrats you completed my horrible spelling test you get one big Phat gold star")
    pass



    


game = int(input("press 1 for cliff man, 2 for math and 3 for spelling"))
if game == 1:
    print(" uuuuhhh select some numbers I guess")
    print()
    select()
    
elif game == 2:
    print("lets do some math cunt")
    print()
    mathgame()
    
elif game == 3:
    print("time to spell, dickhead")
    print()
    spell()
    






