n = int(input("Enter the number of rows : "))

for i in range(n):
	num =1
	for j in range(i+1):
		print(num,end=" ")
		num+=1
	print("\r")