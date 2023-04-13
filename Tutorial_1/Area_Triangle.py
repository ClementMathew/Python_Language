import math

a = int(input("Enter the side a : "))
b = int(input("Enter the side b : "))
c = int(input("Enter the side c : "))

s= (a+b+c)/2
f = s*(s-a)*(s-b)*(s-c)
Area = math.sqrt(f)
print("Area = ",Area)
