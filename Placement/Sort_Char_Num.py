# string = list(input("Enter the string with alphabets and digits: "))

string = "clement924"

digi = []
alph = []

for i in string:
    if i.isdigit() == True:
        digi.append(i)
    else:
        alph.append(i)

alph.sort()
digi.sort()

mainli = []

mainli.extend(digi)
mainli.extend(alph)

for i in mainli:
    print(i,end="")
