import math

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

check = (b*b)-(4*a*c)

if(check>0):
	root = math.sqrt((check))
	sol1 = ((-b)+root)/(2*a)
	sol2 = ((-b)-root)/(2*a)
	print("The solutions of x are ",sol1,",",sol2)
	
elif (check==0):
	sol = (-b)/(2*a)
	print("The solution is ",sol)

else:
	z= -1*(check)
	root = math.sqrt(z)
	sol1 = ((-b)/(2*a))
	sol2 = (root)/(2*a)
	sol3 = ((-b)/(2*a))
	sol4 = (root)/(2*a)
	print("The solutions of x are ",sol1,"+",sol2,"i",",",sol3,"-",sol4,"i")