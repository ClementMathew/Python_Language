f = open("integers.txt","r")
theSum = 0

for line in f:
    line = line.strip()
    number = int(line)
    theSum += number

print("The sum is",theSum)