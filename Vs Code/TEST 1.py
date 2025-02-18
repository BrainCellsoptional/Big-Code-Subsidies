correct_number = 7
guess = int(input("chose a number between 1 and 10"))

if  guess > correct_number:
    print(f"{guess} is greater than 7 ")
elif guess < correct_number:
    print(f"{guess} is less than than 7 ")
else:
    print("you guessed it")
