num = [2,3,4,5]
print(num)

for index in range(len(num)):
    num[index] = num[index]**2

print(num)