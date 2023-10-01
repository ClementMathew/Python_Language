
A = input("Enter first matrix : ").split()
B = input("Enter second matrix : ").split()

li1 = []
li2 = []

for i in A:
    li1.append(int(i))
    
for i in B:
    li2.append(int(i))

from itertools import product

mainli = []

mainli.append(li1)
mainli.append(li2)

ans = list(product(*mainli))

for i in ans:
    print(i,end=" ")
