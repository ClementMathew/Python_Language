if __name__ == '__main__':
    x = int(input("Enter x : "))
    y = int(input("Enter y : "))
    z = int(input("Enter z : "))
    n = int(input("Enter n : "))

from copy import deepcopy
    
li = []
mainli = []

for i in range(x+1):
    li.append(i)
    for j in range(y+1):
        li.append(j)
        for k in range(z+1):
            li.append(k)
            if (sum(li) != n):
                mainli.append(deepcopy(li))
            li.pop()
        li.pop()
    li.pop()
    
print(mainli)
