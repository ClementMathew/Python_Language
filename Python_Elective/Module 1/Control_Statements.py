#Python Exponentiation

number =2
exponent = 3
product = 1

for eachPass in range(exponent):
    product = product*number
    print(product,end=" ")


#Count controlled Loops

print("\n")
for count in range(4):
    print(count,end=" ")

# Range(x,y)

print("\n")
product = 1

for count in range(1,5):
    product = product*count

print(product)

# Range(var1,var2)

print("\n")
lower = int(input("Enter the lower bound : "))
upper = int(input("Enter the upper bound : "))

theSum = 0
for number in range(lower,upper+1):
    theSum = theSum+number

print(theSum)

# Loop That Counts Down

print("\n")
for count in range(10,0,-1):
    print(count,end=" ")