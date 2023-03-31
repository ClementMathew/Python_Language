
# Area of the triangle

A= int(input("Enter the first side: "))
B= int(input("Enter the second side:"))
C= int(input("Enter the third side:"))
S = (A+B+C)/2
Area =(S*(S-A)*(S-B)*(S-B))**0.5

# round method

limit=round(Area,3)
print("The area is",limit)

# format method

print("The area is {:.2f}".format(Area))