# Function Practice - Modular Code

# 1. Write a function called my_function that prints ("You called me") to the screen
def my_function():
    print("you called me")



# 2. Write a function called advantages_functions that prints
 	#"1. Group several lines of code under one name
	#2. Code can be changed in one place and used everywhere
	#3. Arguments can be sent in to change the function output"
def advantages_function(num1,num2):
    print("test 1")
    num3 = num1*num2
    return num3









# 3. Write a function called multiply that takes two numbers and prints out 
      #" num1 * num2 = {answer}"
def multiply(num4,num5):
    print(num4 * num5)



# 4. Write a function called miles to km that takes in one argument ( dist in miles ) 1.609344
	#and prints out " -- miles equals --- kms"
def change(miles):
    kms = miles * 1.609344
    print(kms)


# 5. Write a function that returns a string - store the returned value then print it. '

def string():
    myname = "oliver"
    return myname



# 6. Write a function called print_this_letter that takes a string and a number and prints out that letter of the string
def printnum(melon,num10):

    melon = [num10]
    print()




# 7. Write a function called quiz_question_1.
    #The function prints the following to the screen, checks the user answer and prints feedback
    #"Variables passed into functions are called arguments"
      #t) True			f) False
def quiz_1():
    a = input("""Variables passed into functions are called arguments 
              t) True           f) False
              """)
    b = 0
    while b != 1:
        if a == "t":
            print("correct")
            b = b + 1
        else:
            a = input("""your answer was incorrect please try agian
                    t) True           f)false
                    """)
    print("variables in function brakets are called arguments")

    


 

# 8. Write a function called quiz_question_2
	#The function prints the following to the screen, checks the user answer and prints feedback

 #"You can only pass one argument into a function"
      #t) True			f) False
def quiz_2():
    a = input("""You can only pass one argument into a function 
              t) True           f) False
              """)
    b = 0
    while b != 1:
        if a == "f":
            print("correct")
            b = b + 1
        else:
            a = input("""your answer was incorrect please try agian
                    t) True           f)false
                    """)
    print("you can use more than one argument in a function")



# 9. Write a function called quiz_question_3.
    #The function prints the following to the screen, checks the user answer and prints feedback

 #"Variables defined inside functions can only be seen inside them, this is called scope"
     #t) True			f) False
def quiz_3():
    a = input("""Variables defined inside functions can only be seen inside them, this is called scope
              t) True           f) False
              """)
    b = 0
    while b != 1:
        if a == "t":
            print("correct")
            b = b + 1
        else:
            a = input("""your answer was incorrect please try agian
                    t) True           f)false
                    """)
    print("scope is another name for a local variable (they can be used outside of a function using the return comand)")


# 10. Write a function called quiz_question_3

 #"If you want to use a variable inside a function that was defined outside of it,
  #you should use the global keyword"
      #t) True			f) False
def quiz_4():
    a = input("""If you want to use a variable inside a function that was defined outside of it,
                 you should use the global keyword
              t) True           f) False
              """)
    b = 0
    while b != 1:
        if a == "t":
            print("correct")
            b = b + 1
        else:
            a = input("""your answer was incorrect please try agian
                    t) True           f)false
                    """)
    print("that is true you need to use the global command to accsess variabbles defined outside a function ")


# 11 Write a function called mcq that takes in two strings, the first is the question string, the second is the answer
    #The function prints the questions, gets the user response, checks the answer and prints feedback

   #eg In Python which keyword is used to send a value out of a function
		#a) send
		#b) value out
		#c) arg
		#d) return
def mcq():
    c = input("""eg In Python which keyword is used to send a value out of a function
		#a) send
		#b) value out
		#c) arg
		#d) return""")
    v = 0
    while v != 1: 
        if c == "d":
            print("correct ")
        else:
            c = input("""your answer was incorrect please re-try
                      eg In Python which keyword is used to send a value out of a function
		    #a) send
		    #b) value out
		    #c) arg
		    #d) return""")
    print("well done you have completed my weird ass test")

my_function()
advantages_function(4,5)
multiply(6,9)
change(69)
print(string())
printnum('my_big_long_string', 5)#output g
quiz_1()
quiz_2()
quiz_3()
quiz_4()
mcq()


