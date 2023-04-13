
theSum = 0.0
data = input("Enter a number or just enter to quit : ")

while data!="":
    number = float(data)
    theSum += number
    data = input("Enter a number or just enter to quit : ")
    
print("The sum is = ",theSum)

# Another Method

theSum =0.0

while True:
    data = input("Enter a number or just enter to quit : ")
    if data =="":
        break
    number = float(data)
    theSum += number
    
print("The sum is = ",theSum)