i = 0
sum = 0
print("Enter 10 positive numbers")
while i!=10:
    i+=1
    n = int(input(": "))
    if(n>0):
        sum+=n
    else:
        i-=1
print(sum)