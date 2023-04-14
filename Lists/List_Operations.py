
import math
x= 2
li = [x,math.sqrt(x)]
print(li)

first = list(range(1,5))
print(first)

second = list("Hi there")
print(second)

print(len(second))
print(second[0])
print(second[2:4])

third = first + [5,6]
print(third)
print(first == third)

print([1,2,3,4])
for num in [1,2,3,4] or first:
    print(num,end=" ")

print("\n")
print(3 in first)

first[3] = 10
print(first)

first.append(8)
print(first)

first.extend(third)
print(first)

first.insert(5, 7)
print(first)

first.pop()
print(first)

first.pop(6)
print(first)

first.sort()
print(first)