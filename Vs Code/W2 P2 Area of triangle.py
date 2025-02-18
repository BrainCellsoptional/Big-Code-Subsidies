print("heloo nerd lets caculate the area of a triangle ")
print()
test = 0
while test == 0:
    try:
        b1 = float(input("base(cm) "))
        h1 = float(input("height(cm) "))
        test = test + 1
    except:
        if test == 0:
            b1 = float(input("base(cm) was not valid please re-enter "))
            h1 = float(input("height(cm) was not valid please re-enter "))

base = float(b1)
height = float(h1)

# caculates area
print(base, "*", height, "=", ((base * height) /2)) #this line isnt working

