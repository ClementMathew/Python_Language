import math

x1 = int(input("Enter the value of x1 : "))
y1 = int(input("Enter the value of y1 : "))
x2 = int(input("Enter the value of x2 : "))
y2 = int(input("Enter the value of y2 : "))

dx = (x2-x1)**2
dy = (y2-y1)**2

dist = math.sqrt(dx+dy)
print("The distance between points is : ",dist)