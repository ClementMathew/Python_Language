
task = input("Enter the string and number : ").split()

string = task[0]
n = task[1]

from itertools import permutations

li = list(permutations(string,int(n)))

li2 = []

for i in li:
    word = ""
    for j in i:
        word = word + j
    li2.append(word)

li2.sort()

for i in li2:
    print(i)
