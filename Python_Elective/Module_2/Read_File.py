f = open("myfile.txt","r")

s= f.read()
print(s)

f= open("myfile.txt","r")

for line in f:
    print(line)

# Readline

f = open("myfile.txt","r")

while True:
    line = f.readline()
    if line == "":
        break
    print(line)