myString = input("Enter a word : ")
rev=""

for i in myString:
    rev = i+rev

print(rev)