#Function practice
# 1. Write a function called hello_world_print that prints "Hello World"
def hello():
    print("hello world")

# 2. Write a function called hello_world_return that returns "Hello World"
def hello1():
    return "hellow world1"

# 3. Write a function called hello_world_both that prints "Hello World" and then returns it
def hello2():
    print("hello world2")
    return "hello world 2"

# 4. Write a function called send_me_in_print that takes one string argument and prints "You sent me _ (argument)"
def str(a):
    print(a)


# 5. Write a function called send_me_in_return that takes one string argument and returns "You sent me _ (argument)"
def str2(a):
    return a

# 6. Write a function called send_me_in_both that takes one string argument and prints and then returns 'You sent me {argument}"
def str3(a):
    print(a)
    return a

# 7. Write a function called chop_join_upper that takes two string arguments, and returns the first 2 letters of the first with the first 3 letters of the second and 
# returns them as an uppercase string. (Don't bother error checking for now! eg what if the first string is only one char long)
    #input: chop_join_upper("Hone", "Heke") 
    #output: HOHEK
def letter(a,b):
    return a[0:2] + b[0:3]
    #return a[0:2] , b[0:3]
    

hello()
print(hello1())
print(hello2())
str("hello world 3")
print(str2("hello world 4 "))
print(str("hello world 5"))
print(letter("hone","heke"))
print(int("1110",2))