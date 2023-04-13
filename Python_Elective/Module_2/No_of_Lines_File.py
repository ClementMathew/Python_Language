f = open("myfile.txt","r")
i = 0

while True:
    line = f.readline()
    
    if line == "":
        break
    i = i+1
print(i)