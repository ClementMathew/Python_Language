n = int(input("Enter the number of rows : "))

for i in range(n):
	s = ""
	num = 1
	for j in range(i+1):
		num = str(num)
		s = s+num+" "
		num = int(num)+1
	print(s)