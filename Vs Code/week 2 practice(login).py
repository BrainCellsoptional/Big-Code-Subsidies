
print("Welcome to hell please enter your user name and pasword to sign up")
print()
#user enters password and username 
username = input("enter Username ")
password = input("enter pasword ")
#cheeks password to see if its longer than 5, if not makes user reset
if len(password) <= 5:
    print("password not long enough ")
    password = input("please enter a longer password")
#user re-enters pasword
password2 = input("please re-enter ")
#py cheeks if passwords match
while password != password2:
    print("the paswords do not match ")
    password2 = input("please re-enter password ")
else:
    print("sign up scucse")
#make password sucure


#
def login():
    print("_________________________________________________")
    print("welcome to login")
    uname1 = input("please enter username ")
    password1 = input("please enter pasword ")
    
    while username != uname1:
        print("username was incorrect ")
        uname1 = input("please re-enter ")
    else:
        print(uname1+" is correct ")
    while password1 != password:
        print("password try agian ")
        password1 = input("try agian ")
    else:
        print(password1 + " Correct ")
    print("login succsefull")


login()


