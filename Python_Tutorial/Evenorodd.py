even = 0
odd = 0

print("Enter the number or just enter to quit : ")
while(True):
	num = input(": ")
	if num =="":
		break
	num = int(num)
	if(num%2 == 0):
		even+=1
	else:
		odd+=1
print("No of even numbers : ",even)
print("No of odd numbers : ",odd)

