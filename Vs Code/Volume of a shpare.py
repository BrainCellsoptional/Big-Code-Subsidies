# take in some numbers and caculate volume of a sphare
# caculation V = (3/4) * print (math.pi) * (raduis**3)
# Import math Library
import math

# Print the value of pi
print (math.pi)

print("hello we will calculate the volume of a shapre")
# the while loop makes sure that you dont try any str or wierd inputs
a = 0
while a != 1:
    try:
        r = float(input("please give me the raduis ")) # asigns r the input of the usser at forces it to be a float
        if r == float(r):  # stops the loop if corect
            a = a + 1                           
    except:
        print()

    
        

v = ((r**3)* math.pi)*(4/3)
print(f"the volume of a spahre with the raduis of {r} is {v} ")
print(f"rounded to 2 decimals {round(v,2)}")