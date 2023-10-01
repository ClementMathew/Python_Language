
start = input("Enter the word and number : ").split()

text = start[0]
n = start[1]

litext = list(text)
litext.sort()

for i in litext:
    print(i)

text2 = ""

for i in litext:
    text2 = text2 + i

from itertools import combinations

mainli = []

for i in range(int(n)):
    if i != 0:
        mainli.extend(list(combinations(text2,i+1)))

li = []

for i in mainli:
    word= ""
    for j in i:
        word = word + j
    li.append(word)

for i in li:
    print(i)
    