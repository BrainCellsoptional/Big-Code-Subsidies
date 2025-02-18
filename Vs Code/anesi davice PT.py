# Print out the value of your variable
var1 = 1
print(var1)
# Change the value of your variable to 8
va1 = 8
# Print it out
print(var1)
# Create another variable called var2 set the value to 16
var2 = 16
# Print it out
print(var2)
# Create a third variable called var3, set the value to var1 + var2
var3 = 3
# Print out var3
print(var3)
# Use any of these maths operators with any of your varibales + , - , * , / , %, //
var4 = var1 * var3

# Print out thee results - do notice anything interesting ( / returns a float)
print(var4)
# Create a string variable called str1 set the value to "Hello "
str1 = "hello "
# Create a string variable called str2 set the value to "World"
str2 = "world"
# Print out str1 and str2
print(str1 + str2)
# Declare a str3 variable and set the value to str1 + str2 
str3 = str1 + str2
# Print out the value of str3
print(str3)
# What happens if you try str1 * str2 ?
#error

# declare a  variable called myname set its value to your name ( use quotes to make it a string)
myname = "oliver"
# declare a variable called age  set  it to your age
age = 21
# Use an f string to print out f"Hello my name is {myname}, I am {age} years old"
print(f"hello my name is {myname}, i am {age} years old")
# Declare more variables and use an f string 3 more times. Use an f string everyday for a week.
height = 12 
weight = 1000
hair_lenght = 10
print(f"im {height}feet, {weight}kgs and have {hair_lenght}cm long")


# ****** DATA TYPES ********

# There four types we need to know int, float, string, boolean

# Which data type?

#   4       5.89  'Hello Andrew'    True     67.89  'muppet'   3    False
    #int            str             boolian   float    str      int     boolian
#  a = 4
#  b = 6
#  print(a + b)     // 10
#  
#  a = '4'
#  b = '6'
#  print(a + b)     // 46     Why?

# Declare a var called mofonui. set the value to 5
# Check the type of mofonui type(mofonui)
# Convert mofonui to a float, a string and a boolean
# Print out the results in an fstring

mofunui = 5
type(mofunui)
float(mofunui)
print(f"{mofunui}")




# What is the output of this?
# print(bool(O))    false
# print(bool(1))    true
# print(bool(-1))   true
# print(bool("False"))  true
# print(bool('0'))  true
# print(bool(''))   false

# When we use input to get user input it returns a string
# If we need something else ( like a number), we need to convert it
# declare 2 variables user_input_1 (u1) user_input_2 (u2)
# set the values to 0
# ask the user for a number between 1 and 10 - store it in user_input_1 
# ask the user for a number between 100 and 200 - store it in user_input_2
# Add the inputs and print the result - what do you notice?
# If you didn't convert them to int the addition will be wrong
ui1 = input("num1 plz (between 1 - 10)")
ui2 = input("num2 plz (between 100 - 200)")
print(ui1 + ui2)
ui1 = int(input("num1 plz (between 1 - 10)"))
ui2 = int(input("num2 plz (between 100 - 200)"))
print(ui1 + ui2)





# Python is a "loosely typed" language it deals with changes in data types
# declare a variable called kapai set the value to 78
# check the type of kapai
# change the value of kapai to "kuri nui"
# check the type of kapai
# What did Python do to the variable?
kapai = 78
print(type(kapai))
kapai = "kuri nui"
print(type(kapai))




# That is alot about variables?
# Why do we need them?
# What are you going to do with them?


# ----CONDITIONAL CODE ---
#
# Computers are the most influential technology in human history, discuss.

# Most machines in history can not make decisions
# Computers can

# declare two variables num1  = 78 num2 =15
# if num1 equals num2, print "the numbers are equal"
# Becareful here, what is the difference between = and ==?
# (= assignment operator, == comparison operator)
num1 = 78
num2= 15
if num1 == num2:
    print("sus")
else:
    print("no good")

# nothing happens if the numbers are not equal
# we can add actions for the not true version with an else
# print "the numbers are not equal"

# you can add more outputs by adding more ifs
# you can use elifs
# you can set a default with an else
# Remember guessing game - if bigger say bigger, if smaller say smaller, if equal say equal
# Come up with your own three or four option example: coffee size, milk type, grade, 

# Store your name in a variable. Ask for user input, if the name matches yours say hello,
# if not say go away
# Print a true false question, if the answer is correct say so, if not say so
# Add a score variable, and print score after question feedback
# 
b = 0
name = "oliver"
name2 = input("say my name")
while b != 1:
    if name == name2:
        print("heizenburg")
        b = b + 1
    else:
        name2 = input("SAY MY NAME")

run = 0
star = 0
while run <1 :
    if input("was the yamato the largest battleship in history t/f") == "t":
        star = star + 1
        print(f"that is correct you have {star} gold stars")
        run = run + 1
    else:
        print("no gold stars for you")
        star = star - 1









#
# **** Functions recap  ************
# Why use a function? 
# Define a function called print_4_lines that prints 4 lines of txt
# call print_4_lines
# Define a function called print_6_lines that prints 6 lines of txt
# call print_6_lines
# Define a function called print_all, it call both the functions above to print out 10 lines
# call print_all
# send a value in to a function
# send a value out


def p4():
    print("jeff \n" * 4)

def p6 ():
    print("top text \n" * 6)

def p8(jeff):
    if jeff == 10:
        jeff = 15
        p4()
        p6()
        return jeff

print(p8(10))