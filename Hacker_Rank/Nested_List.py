'''

from copy import deepcopy

mainli=[]

if __name__ == '__main__':
    for _ in range(int(input())):
        li = []
        name = input()
        score = float(input())
        li.append(name)
        li.append(score)
        mainli.append(deepcopy(li))


print(mainli)

'''


di={}
li2 = []

if __name__ == '__main__':
    for _ in range(int(input("Enter number of inputs : "))):
        name = input("Enter name : ")
        score = float(input("Enter score : "))
        
        di[name] = score

li = list(di.values())

li.sort()

for i in li:
    if (min(li) != i):
        li2.append(i)

themin = min(li2)

names = []

for i in di:
    if(di[i] == themin):
        names.append(i)

names.sort()

for i in names:
    print(i)
